def find_linenum_starts_with(lines, target, start=0):
    for i, line in enumerate(lines[start:]):
        if 0 == line.find(target):
            return start+i

    return -1

def remove_last_argument(text):
    start = text.rfind(",")
    end = text.rfind(")")

    return text[:start] + text[end:]

class OutputParser:
    def __init__(self, text):
        self._text = text

    def check_sat(self):
        # TO-DO: Implement
        return True

    def _get_function_code_lines(self, function_name):
        lines = self._text.splitlines()
        
        target = 'void ' + function_name + ' ('
        start = find_linenum_starts_with(lines, target)
        end = find_linenum_starts_with(lines, '}', start)

        return lines[start+2:end]

    def parse_positive_example(self):       
        soundness_code_lines = self._get_function_code_lines("soundness")
        soundness_code_lines = ['\t' + line.strip() for line in soundness_code_lines]

        property_call = soundness_code_lines[-2].replace("obtained_property", "property")
        property_call = remove_last_argument(property_call)

        positive_example_code = '\n'.join(soundness_code_lines[:-3])
        positive_example_code += '\n\tassert ' + property_call.strip()

        print(positive_example_code)

        return positive_example_code

    def parse_negative_example(self):
        # TO-DO: Implement
        return ""

    def parse_specification(self):
        # TO-DO: Implement
        return ""