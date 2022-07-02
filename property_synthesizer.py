import subprocess
import os
import random
import time

from util import union_dict
from input_generator import InputGenerator
from output_parser import OutputParser

SKETCH_BINARY_PATH = "sketch-frontend/sketch"
LOG_FILE_PATH = "log/"
TEMP_FILE_PATH = "tmp/"
TEMP_NAME_DEFAULT = "tmp"

def extract_filename_from_path(path):
    basename = os.path.basename(path)
    filename, extension = os.path.splitext(basename)

    return filename

def get_tempfile_name(infile, outfile):
    infile_path = infile.name
    
    if infile_path != '<stdin>':
        return extract_filename_from_path(infile_path)
    
    return TEMP_NAME_DEFAULT

def write_tempfile(path, code):
    if not os.path.isdir(TEMP_FILE_PATH):
        os.mkdir(TEMP_FILE_PATH)

    with open(path, 'w') as f:
        f.write(code)

def neg_to_pos(neg_example):
    lines = neg_example.splitlines()
    lines[-1] = '\tassert out;'
    return '\n'.join(lines)

def open_logfile(filename):
    if not os.path.isdir(LOG_FILE_PATH):
        os.mkdir(LOG_FILE_PATH)
    
    return open(LOG_FILE_PATH + filename, 'w')

class PropertySynthesizer:
    def __init__(self, infile, outfile, verbose, inline_bnd, inline_bnd_sound, num_atom_max, minimize_terms) :       
        # Input/Output file stream
        self.__infile = infile
        self.__outfile = outfile
        
        # Temporary filename for iteration
        self.__tempfile_name = get_tempfile_name(infile, outfile)
        
        # Template for Sketch synthesis
        self.__template = infile.read()
        self.__logfile = open_logfile(self.__tempfile_name)

        # Sketch Input File Generator
        self.__minimize_terms = minimize_terms
        self.__input_generator = InputGenerator(self.__template)
        self.__input_generator.set_num_atom(num_atom_max)

        # Synthesized property
        self.__phi_truth = "out = true;"

        # Options
        self.__verbose = verbose
        self.__move_neg_may = True
        self.__timeout = 300

        # Iterators for descriptive message
        self.__inner_iterator = 0
        self.__outer_iterator = 0

        self.__num_soundness = 0
        self.__num_precision = 0
        self.__num_maxsat = 0
        self.__num_synthesis = 0

        self.__time_soundness = 0
        self.__time_precision = 0
        self.__time_maxsat = 0
        self.__time_synthesis = 0

        self.__max_time_soundness = 0
        self.__max_time_precision = 0
        self.__max_time_maxsat = 0
        self.__max_time_synthesis = 0

        self.__min_time_soundness = self.__timeout
        self.__min_time_precision = self.__timeout
        self.__min_time_maxsat = self.__timeout
        self.__min_time_synthesis = self.__timeout

        self.__time_last_query = 0

        self.__statistics = []     

        self.__num_pos_examples = []
        self.__num_used_neg_examples = []
        self.__num_discarded_neg_examples = []

        self.__inline_bnd = inline_bnd
        self.__inline_bnd_sound = inline_bnd_sound

    def __write_output(self, output):
        self.__outfile.write(output)

    def __get_new_tempfile_path(self):
        path = TEMP_FILE_PATH
        path += self.__tempfile_name
        if self.__verbose:
            path += f'_{self.__outer_iterator}_{self.__inner_iterator}'
        path += ".sk"

        self.__inner_iterator += 1

        return path        

    def __try_synthesis(self, path, check_sound=False):
        inline_bnd = self.__inline_bnd if not check_sound else self.__inline_bnd_sound
        try:
            return subprocess.check_output( \
                [SKETCH_BINARY_PATH, path, \
                    '--bnd-inline-amnt', str(inline_bnd)], \
                stderr=subprocess.PIPE, timeout=self.__timeout)
        except subprocess.CalledProcessError as e:
            return None
        except subprocess.TimeoutExpired as e:
            print("Timeout")
            return None

    def __synthesize(self, pos, neg_must, neg_may, lam_functions):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Try synthesis')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator.generate_synthesis_input(pos, neg_must, neg_may, lam_functions)     

        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        end_time = time.time()

        elapsed_time = end_time - start_time
        
        self.__num_synthesis += 1
        self.__time_synthesis += elapsed_time
        if elapsed_time > self.__max_time_synthesis:
            self.__max_time_synthesis = elapsed_time
        if elapsed_time < self.__min_time_synthesis:
            self.__min_time_synthesis = elapsed_time

        log = [f'{self.__outer_iterator}', f'{self.__inner_iterator}']
        log += ['Y', f'{elapsed_time}']
        log += [f'{len(pos)}', f'{len(neg_must)}', f'{len(neg_may)}']

        self.__logfile.write(','.join(log) + "\n")

        if output != None:
            output_parser = OutputParser(output)
            phi = output_parser.parse_property()
            lam = output_parser.get_lam_functions()
            return (phi, lam)
        else:
            return (None, None)

    def __max_synthesize(self, pos, neg_must, neg_may, lam_functions, phi_init):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Run MaxSat')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator.generate_maxsat_input(pos, neg_must, neg_may, lam_functions)    
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)
        
        end_time = time.time()

        elapsed_time = end_time - start_time

        self.__num_maxsat += 1
        self.__time_maxsat += elapsed_time
        if elapsed_time > self.__max_time_maxsat:
            self.__max_time_maxsat = elapsed_time
        if elapsed_time < self.__min_time_maxsat:
            self.__min_time_maxsat = elapsed_time

        log = [f'{self.__outer_iterator}', f'{self.__inner_iterator}']
        log += ['M', f'{elapsed_time}']
        log += [f'{len(pos)}', f'{len(neg_must)}', f'{len(neg_may)}']

        self.__logfile.write(','.join(log) + "\n")

        if output != None:
            output_parser = OutputParser(output)
            neg_may, delta = output_parser.parse_maxsat(neg_may) 
            phi = output_parser.parse_property()
            lam = output_parser.get_lam_functions()
            return (neg_may, delta, phi, lam)
        else:
            neg_may, delta = [], neg_may
            phi = phi_init
            lam = lam_functions
            return (neg_may, delta, phi, lam)

    def __check_soundness(self, phi, lam_functions):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Check soundness')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator.generate_soundness_input(phi, lam_functions)       
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path, check_sound=True)

        end_time = time.time()

        elapsed_time = end_time - start_time

        self.__num_soundness += 1
        self.__time_soundness += elapsed_time
        if elapsed_time > self.__max_time_soundness:
            self.__max_time_soundness = elapsed_time
        if elapsed_time < self.__min_time_soundness:
            self.__min_time_soundness = elapsed_time

        log = [f'{self.__outer_iterator}', f'{self.__inner_iterator}']
        log += ['S', f'{elapsed_time}']
        log += ['-', '-', '-']

        self.__logfile.write(','.join(log) + "\n")

        if output != None:
            output_parser = OutputParser(output)
            e_pos = output_parser.parse_positive_example()
            lam = output_parser.get_lam_functions()
            return (e_pos, lam, False)
        else:
            return (None, None, elapsed_time >= self.__timeout)

    def __check_precision(self, phi, phi_list, pos, neg_must, neg_may, lam_functions):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} - {self.__inner_iterator}: Check precision')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_precision_input(phi, phi_list, pos, neg_must, neg_may, lam_functions)      
        
        start_time = time.time()

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        end_time = time.time()

        elapsed_time = end_time - start_time

        self.__num_precision += 1
        self.__time_precision += elapsed_time
        if elapsed_time > self.__max_time_precision:
            self.__max_time_precision = elapsed_time
        if elapsed_time < self.__min_time_precision:
            self.__min_time_precision = elapsed_time

        log = [f'{self.__outer_iterator}', f'{self.__inner_iterator}']
        log += ['P', f'{elapsed_time}']
        log += [f'{len(pos)}', f'{len(neg_must)}', f'{len(neg_may)}']

        self.__logfile.write(','.join(log) + "\n")

        if output != None:
            output_parser = OutputParser(output)
            e_neg = output_parser.parse_negative_example_precision() 
            phi = output_parser.parse_property()
            lam = output_parser.get_lam_functions()
            return (e_neg, phi, lam)
        else:
            self.__time_last_query = elapsed_time
            return (None, None, None)

    def __check_improves_predicate(self, phi_list, phi, lam_functions):
        if self.__verbose:
            print(f'Iteration {self.__outer_iterator} : Check termination')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator.generate_improves_predicate_input(phi, phi_list, lam_functions)        
        
        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        if output != None:
            output_parser = OutputParser(output)
            e_neg = output_parser.parse_improves_predicate()
            return e_neg
        else:
            return None

    def __model_check(self, phi, neg_example, lam_functions):
        if self.__verbose:
            print(f'Iteratoin {self.__outer_iterator} : Model check')

        path = self.__get_new_tempfile_path()
        code = self.__input_generator \
            .generate_model_check_input(phi, neg_example, lam_functions)

        write_tempfile(path, code)
        output = self.__try_synthesis(path)

        return output != None

    def __synthesizeProperty(self, phi_list, phi_init, pos, neg_must, neg_may, lam_functions, most_precise):
        # Assume that current phi is sound
        phi_e = phi_init
        phi_last_sound = self.__phi_truth
        neg_delta = []

        while True:
            e_pos, lam, timeout = self.__check_soundness(phi_e, lam_functions)
            if e_pos != None:
                pos.append(e_pos)
                lam_functions = union_dict(lam_functions, lam)
                
                # First try synthesis
                phi, lam = self.__synthesize(pos, neg_must, neg_may, lam_functions)
                
                # If neg_may is a singleton set, it doesn't need to call MaxSynth
                # Revert to the last remembered sound property 
                if phi == None and len(neg_may) == 1:
                    phi = phi_init
                    neg_delta += neg_may
                    neg_may = []
                    lam = {}

                # MaxSynth 
                elif phi == None:
                    neg_may, delta, phi, lam = self.__max_synthesize(pos, neg_must, neg_may, lam_functions, phi_init)
                    neg_delta += delta
                
                    # MaxSynth can't minimize the term size, so call the Synth again
                    if self.__input_generator.minimize_terms_enabled:
                        phi, lam = self.__synthesize(pos, neg_must, neg_may, lam_functions)

                phi_e = phi
                lam_functions = union_dict(lam_functions, lam)
            
            # Return the last sound property found
            elif timeout:
                neg_delta = [e for e in neg_delta if self.__model_check(phi_e, e, lam_functions)]
                return (phi_init, pos, neg_must + neg_may, neg_delta, lam_functions)
            
            # Early termination after finding a sound property with negative example
            elif not most_precise and len(neg_may) > 0:
                neg_delta = [e for e in neg_delta if self.__model_check(phi_e, e, lam_functions)]
                return (phi_e, pos, neg_must + neg_may, neg_delta, lam_functions)
            
            # Check precision after pass soundness check
            else:
                phi_init = phi_e    # Remember the last sound property

                # If phi_e is phi_truth, which is initial candidate of the first call,
                # then phi_e doesn't rejects examples in neg_may. 
                if self.__move_neg_may and phi_e != self.__phi_truth:
                    neg_must += neg_may
                    neg_may = []

                e_neg, phi, lam = self.__check_precision(phi_e, phi_list, pos, neg_must, neg_may, lam_functions)
                if e_neg != None:   # Not precise
                    phi_e = phi
                    neg_may.append(e_neg)
                    lam_functions = lam
                else:               # Sound and Precise
                    neg_delta = [e for e in neg_delta if self.__model_check(phi_e, e, lam_functions)]
                    return (phi_e, pos, neg_must, neg_delta, lam_functions)

    def __remove_redundant(self, phi_list):
        for i in range(len(phi_list)):
            phi = phi_list[i]
            others = phi_list[:i] + phi_list[i:]

            e_neg = self.__check_improves_predicate(others, phi)
            if e_neg == None:
                return (True, others)
        
        return (False, phi_list)

    def __minimize_phi_list(self, phi_list):
        has_redundant = True
        while has_redundant:
            has_redundant, phi_list = self.__remove_redundant(phi_list)
        return phi_list

    def __synthesizeAllProperties(self):
        phi_list = []
        pos = []
        neg_may = []
        lam_functions = {}

        while True:
            # Find a property improves conjunction as much as possible
            self.__input_generator.disable_minimize_terms()
            
            most_precise = self.__minimize_terms
            phi, pos, neg_must, neg_may, lam = \
                self.__synthesizeProperty(phi_list, self.__phi_truth, pos, [], neg_may, lam_functions, most_precise)
            lam_functions = lam

            # Check if most precise candidates improves property. 
            # If neg_must is nonempty, those examples are witness of improvement.
            if len(neg_must) == 0:
                e_neg = self.__check_improves_predicate(phi_list, phi, lam_functions)
                if e_neg != None:
                    neg_must = [e_neg]
                else:
                    stat = self.__statisticsCurrentProperty(pos, neg_must, neg_may, neg_used, neg_delta)
                    self.__statistics.append(stat)
                    return

            if self.__minimize_terms: 
                self.__input_generator.enable_minimize_terms()
                
                # Synthesize a new sound candidate, which is minimized
                # We can always synthesize a sound property since we know phi_e
                # Add more positive examples until the synthesized property is sound
                phi, lam = self.__synthesize(pos, neg_must, [], lam_functions)
                lam_functions = union_dict(lam_functions, lam)
                e_pos, lam, timeout = self.__check_soundness(phi, lam_functions)  
                while e_pos != None:
                    pos.append(e_pos)
                    lam_functions = union_dict(lam_functions, lam)
                    
                    phi, lam = self.__synthesize(pos, neg_must, [], lam_functions)
                    lam_functions = union_dict(lam_functions, lam)
                    e_pos, lam, timeout = self.__check_soundness(phi, lam_functions)

            # Strengthen the found property to be most precise L-property
            phi, pos, neg_used, neg_delta, lam = \
                self.__synthesizeProperty([], phi, pos, neg_must, [], lam_functions, True)
            lam_functions = union_dict(lam_functions, lam)
            
            phi_list.append(phi)

            stat = self.__statisticsCurrentProperty(pos, neg_must, neg_may, neg_used, neg_delta)
            self.__statistics.append(stat)
            self.__resetStatistics()

            if self.__verbose:
                print("Obtained a best L-property")
                print(phi + '\n')

                for function_name, code in lam_functions.items():
                    if function_name in phi:
                        print(value + '\n')

            self.__outer_iterator += 1
            self.__inner_iterator = 0

    def __statisticsCurrentProperty(self, pos, neg_must, neg_may, neg_used, neg_delta):
        statistics = {}

        statistics["num_pos"] = len(pos)
        statistics["num_neg_must"] = len(neg_must)
        statistics["num_neg_may"] = len(neg_may)
        statistics["num_neg_used"] = len(neg_used)
        statistics["num_neg_delta"] = len(neg_delta)

        avg_time_synthesis = self.__time_synthesis / self.__num_synthesis \
            if self.__num_synthesis > 0 else 0

        statistics["num_synthesis"] = self.__num_synthesis
        statistics["time_synthesis"] = self.__time_synthesis
        statistics["avg_time_synthesis"] = avg_time_synthesis
        statistics["max_time_synthesis"] = self.__max_time_synthesis
        statistics["min_time_synthesis"] = self.__min_time_synthesis if self.__num_synthesis > 0 else 0

        avg_time_maxsat = self.__time_maxsat / self.__num_maxsat \
            if self.__num_maxsat > 0 else 0

        statistics["num_maxsat"] = self.__num_maxsat
        statistics["time_maxsat"] = self.__time_maxsat
        statistics["avg_time_maxsat"] = avg_time_maxsat
        statistics["max_time_maxsat"] = self.__max_time_maxsat
        statistics["min_time_maxsat"] = self.__min_time_maxsat if self.__num_maxsat > 0 else 0

        avg_time_soundness = self.__time_soundness / self.__num_soundness \
            if self.__num_soundness > 0 else 0

        statistics["num_soundness"] = self.__num_soundness
        statistics["time_soundness"] = self.__time_soundness
        statistics["avg_time_soundness"] = avg_time_soundness
        statistics["max_time_soundness"] = self.__max_time_soundness
        statistics["min_time_soundness"] = self.__min_time_soundness if self.__num_soundness > 0 else 0

        avg_time_precision = self.__time_precision / self.__num_precision \
            if self.__num_precision > 0 else 0

        statistics["num_precision"] = self.__num_precision
        statistics["time_precision"] = self.__time_precision
        statistics["avg_time_precision"] = avg_time_precision
        statistics["max_time_precision"] = self.__max_time_precision
        statistics["min_time_precision"] = self.__min_time_precision if self.__num_precision > 0 else 0

        statistics["time_conjunct"] = self.__time_synthesis
        statistics["time_conjunct"] += self.__time_maxsat
        statistics["time_conjunct"] += self.__time_soundness
        statistics["time_conjunct"] += self.__time_precision

        statistics["last_call"] = self.__time_last_query

        return statistics

    def __resetStatistics(self):
        self.__num_soundness = 0
        self.__num_precision = 0
        self.__num_maxsat = 0
        self.__num_synthesis = 0

        self.__time_soundness = 0
        self.__time_precision = 0
        self.__time_maxsat = 0
        self.__time_synthesis = 0

        self.__min_time_soundness = self.__timeout
        self.__min_time_precision = self.__timeout
        self.__min_time_maxsat = self.__timeout
        self.__min_time_synthesis = self.__timeout

        self.__max_time_synthesis_query = 0
        self.__max_time_maxsat_query = 0
        self.__max_time_soundness_query = 0
        self.__max_time_precision_query = 0

        self.__time_last_query = 0

    def __statisticsFromList(self, l):
        if len(l) == 0:
            return (0, 0, 0, 0)
        else:
            return (sum(l), sum(l) / len(l), max(l), min(l), )

    def __statisticsList(self):
        statistics = []

        # The last cycle is not used as a clause, since it doesn't change any behavior
        num_conjunct = len(self.__statistics) - 1

        nums_synthesis = []
        nums_maxsat = []
        nums_soundness = []
        nums_precision = []

        times_synthesis = []
        times_maxsat = []
        times_soundness = []
        times_precision = []
        times_conjunct = []

        max_times_synthesis = []
        max_times_maxsat = []
        max_times_soundness = []
        max_times_precision = []

        min_times_synthesis = []
        min_times_maxsat = []
        min_times_soundness = []
        min_times_precision = []

        num_pos = []
        num_neg_must = []
        num_neg_may = []
        num_neg_used = []
        num_neg_delta = []

        last_calls = []

        for conj_statistics in self.__statistics:
            nums_synthesis.append(conj_statistics["num_synthesis"])
            nums_maxsat.append(conj_statistics["num_maxsat"])
            nums_soundness.append(conj_statistics["num_soundness"])
            nums_precision.append(conj_statistics["num_precision"])

            times_synthesis.append(conj_statistics["time_synthesis"])
            times_maxsat.append(conj_statistics["time_maxsat"])
            times_soundness.append(conj_statistics["time_soundness"])
            times_precision.append(conj_statistics["time_precision"])
            times_conjunct.append(conj_statistics["time_conjunct"])

            max_times_synthesis.append(conj_statistics["max_time_synthesis"])
            max_times_maxsat.append(conj_statistics["max_time_maxsat"])
            max_times_soundness.append(conj_statistics["max_time_soundness"])
            max_times_precision.append(conj_statistics["max_time_precision"])

            min_times_synthesis.append(conj_statistics["min_time_synthesis"])
            min_times_maxsat.append(conj_statistics["min_time_maxsat"])
            min_times_soundness.append(conj_statistics["min_time_soundness"])
            min_times_precision.append(conj_statistics["min_time_precision"])

            num_pos.append(conj_statistics["num_pos"])
            num_neg_must.append(conj_statistics["num_neg_must"])
            num_neg_may.append(conj_statistics["num_neg_may"])
            num_neg_used.append(conj_statistics["num_neg_used"])
            num_neg_delta.append(conj_statistics["num_neg_delta"])

            last_calls.append(conj_statistics["last_call"])

        total_num_synth, avg_num_synth, max_num_synth, min_num_synth = self.__statisticsFromList(nums_synthesis)
        total_num_maxsat, avg_num_maxsat, max_num_maxsat, min_num_maxsat = self.__statisticsFromList(nums_maxsat)
        total_num_soundness, avg_num_soundness, max_num_soundness, min_num_soundness = self.__statisticsFromList(nums_soundness)
        total_num_precision, avg_num_precision, max_num_precision, min_num_precision = self.__statisticsFromList(nums_precision)

        num_query = total_num_synth
        num_query += total_num_maxsat
        num_query += total_num_soundness
        num_query += total_num_precision

        statistics.append(f'{num_conjunct}')
        
        total_time, avg_time, max_time, min_time = self.__statisticsFromList(times_conjunct)
        avg_time_per_query = total_time / num_query if num_query > 0 else 0

        statistics.append(f'{num_query}')
        statistics.append(f'{total_time:.2f}')
        statistics.append(f'{avg_time_per_query:.2f}')
        statistics.append(f'{avg_time:.2f}')
        statistics.append(f'{max_time:.2f}')
        statistics.append(f'{min_time:.2f}')

        _, avg_pos, max_pos, min_pos = self.__statisticsFromList(num_pos)
        _, avg_neg_must, max_neg_must, min_neg_must = self.__statisticsFromList(num_neg_must)
        _, avg_neg_may, max_neg_may, min_neg_may = self.__statisticsFromList(num_neg_may)
        _, avg_neg_used, max_neg_used, min_neg_used = self.__statisticsFromList(num_neg_used)
        _, avg_neg_delta, max_neg_delta, min_neg_delta = self.__statisticsFromList(num_neg_delta)

        statistics.append(f'{avg_pos:.2f}')
        statistics.append(f'{min_pos}')
        statistics.append(f'{max_pos}')

        statistics.append(f'{avg_neg_must:.2f}')
        statistics.append(f'{min_neg_must}')
        statistics.append(f'{max_neg_must}')

        statistics.append(f'{avg_neg_may:.2f}')
        statistics.append(f'{min_neg_may}')
        statistics.append(f'{max_neg_may}')

        statistics.append(f'{avg_neg_used:.2f}')
        statistics.append(f'{min_neg_used}')
        statistics.append(f'{max_neg_used}')

        statistics.append(f'{avg_neg_delta:.2f}')
        statistics.append(f'{min_neg_delta}')
        statistics.append(f'{max_neg_delta}')

        total_time_synthesis, avg_time_synthesis_per_clause, total_max_time_synthesis, total_min_time_synthesis = self.__statisticsFromList(times_synthesis)
        avg_time_synthesis = total_time_synthesis / total_num_synth if total_num_synth > 0 else 0
        _, avg_max_synthesis, max_max_synthesis, min_max_synthesis = self.__statisticsFromList(max_times_synthesis)
        _, avg_min_synthesis, max_min_synthesis, min_min_synthesis = self.__statisticsFromList(min_times_synthesis)

        statistics.append(f'{total_num_synth}')
        statistics.append(f'{avg_num_synth:.2f}')
        statistics.append(f'{max_num_synth}')
        statistics.append(f'{min_num_synth}')

        statistics.append(f'{total_time_synthesis:.2f}')
        statistics.append(f'{avg_time_synthesis:.2f}')
        statistics.append(f'{avg_time_synthesis_per_clause:.2f}')
        statistics.append(f'{total_max_time_synthesis:.2f}')
        statistics.append(f'{total_min_time_synthesis:.2f}')
        
        statistics.append(f'{avg_max_synthesis:.2f}')
        statistics.append(f'{max_max_synthesis:.2f}')
        statistics.append(f'{min_max_synthesis:.2f}')
        statistics.append(f'{avg_min_synthesis:.2f}')
        statistics.append(f'{max_min_synthesis:.2f}')
        statistics.append(f'{min_min_synthesis:.2f}')

        total_time_maxsat, avg_time_maxsat_per_clause, total_max_time_maxsat, total_min_time_maxsat = self.__statisticsFromList(times_maxsat)
        avg_time_maxsat = total_time_maxsat / total_num_maxsat if total_num_maxsat > 0 else 0
        _, avg_max_maxsat, max_max_maxsat, min_max_maxsat = self.__statisticsFromList(max_times_maxsat)
        _, avg_min_maxsat, max_min_maxsat, min_min_maxsat = self.__statisticsFromList(min_times_maxsat)

        statistics.append(f'{total_num_maxsat}')
        statistics.append(f'{avg_num_maxsat:.2f}')
        statistics.append(f'{max_num_maxsat}')
        statistics.append(f'{min_num_maxsat}')

        statistics.append(f'{total_time_maxsat:.2f}')
        statistics.append(f'{avg_time_maxsat:.2f}')
        statistics.append(f'{avg_time_maxsat_per_clause:.2f}')
        statistics.append(f'{total_max_time_maxsat:.2f}')
        statistics.append(f'{total_min_time_maxsat:.2f}')

        statistics.append(f'{avg_max_maxsat:.2f}')
        statistics.append(f'{max_max_maxsat:.2f}')
        statistics.append(f'{min_max_maxsat:.2f}')
        statistics.append(f'{avg_min_maxsat:.2f}')
        statistics.append(f'{max_min_maxsat:.2f}')
        statistics.append(f'{min_min_maxsat:.2f}')

        total_time_soundness, avg_time_soundness_per_clause, total_max_time_soundness, total_min_time_soundness= self.__statisticsFromList(times_soundness)
        avg_time_soundness = total_time_soundness / total_num_soundness if total_num_soundness > 0 else 0
        _, avg_max_soundness, max_max_soundness, min_max_soundness = self.__statisticsFromList(max_times_soundness)
        _, avg_min_soundness, max_min_soundness, min_min_soundness = self.__statisticsFromList(min_times_soundness)

        statistics.append(f'{total_num_soundness}')
        statistics.append(f'{avg_num_soundness:.2f}')
        statistics.append(f'{max_num_soundness}')
        statistics.append(f'{min_num_soundness}')

        statistics.append(f'{total_time_soundness:.2f}')
        statistics.append(f'{avg_time_soundness:.2f}')
        statistics.append(f'{avg_time_soundness_per_clause:.2f}')
        statistics.append(f'{total_max_time_soundness:.2f}')
        statistics.append(f'{total_min_time_soundness:.2f}')

        statistics.append(f'{avg_max_soundness:.2f}')
        statistics.append(f'{max_max_soundness:.2f}')
        statistics.append(f'{min_max_soundness:.2f}')
        statistics.append(f'{avg_min_soundness:.2f}')
        statistics.append(f'{max_min_soundness:.2f}')
        statistics.append(f'{min_min_soundness:.2f}')

        total_time_precision, avg_time_precision_per_clause, total_max_time_precision, total_min_time_precision = self.__statisticsFromList(times_precision)
        avg_time_precision = total_time_precision / total_num_precision if total_num_precision > 0 else 0
        _, avg_max_precision, max_max_precision, min_max_precision = self.__statisticsFromList(max_times_precision)
        _, avg_min_precision, max_min_precision, min_min_precision = self.__statisticsFromList(min_times_precision)

        statistics.append(f'{total_num_precision}')
        statistics.append(f'{avg_num_precision:.2f}')
        statistics.append(f'{max_num_precision}')
        statistics.append(f'{min_num_precision}')

        statistics.append(f'{total_time_precision:.2f}')
        statistics.append(f'{avg_time_precision:.2f}')
        statistics.append(f'{avg_time_precision_per_clause:.2f}')
        statistics.append(f'{total_max_time_precision:.2f}')
        statistics.append(f'{total_min_time_precision:.2f}')

        statistics.append(f'{avg_max_precision:.2f}')
        statistics.append(f'{max_max_precision:.2f}')
        statistics.append(f'{min_max_precision:.2f}')
        statistics.append(f'{avg_min_precision:.2f}')
        statistics.append(f'{max_min_precision:.2f}')
        statistics.append(f'{min_min_precision:.2f}')

        total_last, avg_last, max_last, min_last = self.__statisticsFromList(last_calls)

        statistics.append(f'{total_last:.2f}')
        statistics.append(f'{avg_last:.2f}')
        statistics.append(f'{max_last:.2f}')
        statistics.append(f'{min_last:.2f}')

        last = self.__statistics[-1]

        statistics.append(f'{last["num_synthesis"]}')
        statistics.append(f'{last["time_synthesis"]:.2f}')
        statistics.append(f'{last["avg_time_synthesis"]:.2f}')
        statistics.append(f'{last["max_time_synthesis"]:.2f}')
        statistics.append(f'{last["min_time_synthesis"]:.2f}')

        statistics.append(f'{last["num_maxsat"]}')
        statistics.append(f'{last["time_maxsat"]:.2f}')
        statistics.append(f'{last["avg_time_maxsat"]:.2f}') 
        statistics.append(f'{last["max_time_maxsat"]:.2f}')
        statistics.append(f'{last["min_time_maxsat"]:.2f}')

        statistics.append(f'{last["num_soundness"]}')
        statistics.append(f'{last["time_soundness"]:.2f}')
        statistics.append(f'{last["avg_time_soundness"]:.2f}') 
        statistics.append(f'{last["max_time_soundness"]:.2f}') 
        statistics.append(f'{last["min_time_soundness"]:.2f}')

        statistics.append(f'{last["num_precision"]}')
        statistics.append(f'{last["time_precision"]:.2f}')
        statistics.append(f'{last["avg_time_precision"]:.2f}')
        statistics.append(f'{last["max_time_precision"]:.2f}')
        statistics.append(f'{last["min_time_precision"]:.2f}')

        statistics.append(f'{last["time_conjunct"]:.2f}')
        statistics.append(f'{last["last_call"]:.2f}')

        return statistics

    def run(self):
        self.__synthesizeAllProperties()
        statistics = self.__statisticsList()
        statistics = ','.join(statistics)

        self.__write_output(f'{self.__infile.name},{statistics}\n')
        self.__logfile.close()