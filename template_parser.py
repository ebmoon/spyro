import lexer
import generator_rule_parser
import example_rule_parser

class TemplateParser():
    def __init__(self, template):
        # Split input code into three parts
        template, variable_section = self.__split_section_from_code(template, 'var')
        template, relation_section = self.__split_section_from_code(template, 'relation')
        template, generator_section = self.__split_section_from_code(template, 'generator')
        template, example_section = self.__split_section_from_code(template, 'example')

        self.__implenetation = template
        self.__var_decls = self.__split_var_section(variable_section)
        self.__int_decls = [(typ, symbol) for typ, symbol in self.__var_decls if typ == 'int']
        self.__relations = self.__split_relation_section(relation_section)
        self.__generators = self.__split_generator_section(generator_section)
        self.__example_generators = self.__split_example_section(example_section)
        self.__structs = self.__split_struct_definitions(template)

    def __split_section_from_code(self, code, section_name):
        target = section_name
        section_symbol_loc = code.find(target)
        start = code.find('{', section_symbol_loc)
        end = code.find('}', start)

        section_content = code[start+1:end]
        remainder = code[:section_symbol_loc] + code[end + 1:]

        return (remainder.strip(), section_content.strip())

    def __split_var_section(self, section_content):
        decls = [decl.strip().split() for decl in section_content.split(';')]
        return [(decl[0], decl[1]) for decl in decls[:-1]]

    def __split_relation_section(self, section_content):
        return [rel.strip() for rel in section_content.split(';')[:-1]]

    def __split_generator_section(self, section_content):
        return generator_rule_parser.parser.parse(section_content)

    def __split_example_section(self, section_content):
        return example_rule_parser.parser.parse(section_content)

    def __parse_struct(self, code):
        start = code.find('{')
        end = code.find('}', start)

        symbol = code[:start].strip().split()[1]
        content = code[start+1:end]
        decls = [line.strip().split() for line in content.split(';')[:-1]]
        decl_pairs = [(decl[0], decl[1]) for decl in decls]

        return (symbol, decl_pairs)

    def __split_struct_definitions(self, code):
        struct_list = []
        while True:
            target = 'struct'
            struct_loc = code.find(target)
            start = code.find('{', struct_loc)
            end = code.find('}', start)
            
            if (struct_loc < 0):
                break

            struct_code = code[struct_loc:end+1]
            code = code[:struct_loc] + code[end + 1:]
            struct_list.append(struct_code.strip())

        return [self.__parse_struct(code) for code in struct_list]

    def get_int_symbols(self):
        return self.__int_decls

    def get_context(self):
        return {rule[1]:rule[0] for rule in self.__generators}

    def get_generator_rules(self):
        return self.__generators

    def get_example_rules(self):
        return self.__example_generators

    def get_implementation(self):
        return self.__implenetation + '\n\n'

    def get_arguments_defn(self):
        return ','.join([typ + ' ' + symbol for typ, symbol in self.__var_decls])

    def get_integer_arguments_defn(self):
        return ','.join([typ + ' ' + symbol for typ, symbol in self.__int_decls])

    def get_copied_arguments_defn(self):
        return ','.join([typ + ' ' + symbol + '_copy' for typ, symbol in self.__int_decls])

    def get_arguments_call(self):
        return ','.join([symbol for _, symbol in self.__var_decls])

    def get_integer_arguments_call(self):
        return ','.join([symbol for _, symbol in self.__int_decls])

    def get_copied_arguments_call(self):
        return ','.join([symbol + "_copy" for _, symbol in self.__var_decls])

    def get_int_copied_arguments_call(self):
        return ','.join([symbol + "_copy" for _, symbol in self.__int_decls])

    def get_variables_with_hole(self):
        def decl(typ, symbol):
            hole = f'{typ}_gen()'
            return f'\t{typ} {symbol} = {hole};'

        return '\n'.join([decl(typ, symbol) for typ, symbol in self.__var_decls])

    def get_copied_variables_with_hole(self):
        def decl(typ, symbol):
            hole = f'{typ}_gen()'
            return f'\t{typ} {symbol}_copy = {hole};'

        return '\n'.join([decl(typ, symbol) for typ, symbol in self.__var_decls])

    def get_relations(self):
        return '\n'.join(['\t' + rel + ';' for rel in self.__relations])

    def get_structs(self):
        return self.__structs