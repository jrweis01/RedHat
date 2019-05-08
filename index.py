import re
import os
import sys
import copy
import ntpath


def get_file_name_from_path(full_path):
    head, tail = ntpath.split(full_path)
    return tail or ntpath.basename(head)


class GetDataFromFile:
    def __init__(self, search_criteria):
        self.search_criteria = search_criteria

    def run(self, this_file):
        print("searching file: " + this_file + " for regex: " + self.search_criteria)
        try:
            f = open(this_file, 'r')
            file_lines = f.readlines()
            f.close()
            return file_lines
        except Exception as ex:
            print("ERROR (trying to gt data from a file): " + str(ex))

    def search_data_content(self, lines, file_name):
        found_line = {"file_name": file_name, "line_number": -1, "pos": -1, "matched_text": '', "line_text": '',
                      "length_text_found": -1}
        found_lines = []
        found_match = False
        line_number = 0
        for line in lines:
            matches = re.findall(self.search_criteria, line)
            if len(matches) > 0:
                start_pos = 0
                for match in matches:
                    found_match = True
                    found_line["line_number"] = line_number
                    found_line["pos"] = line.index(match, start_pos)
                    found_line["matched_text"] = match
                    found_line["length_text_found"] = len(match)
                    found_line["line_text"] = line.strip('\n')
                    found_lines.append(copy.deepcopy(found_line))
                    start_pos = found_line["pos"] + found_line["length_text_found"] + 1
                    print(found_line["file_name"] + ", line: " + str(found_line["line_number"]) + ": " + line)
            line_number += 1
        return found_match, found_lines


class GetDataFromStdin(GetDataFromFile):
    def __init__(self, search_criteria):
        GetDataFromFile.__init__(self, search_criteria)
        # Get input from Standard input (stdin)
        # ^D will end collection of input
        print("Listening for standard input")

    def run(self):
        try:
            data = sys.stdin.readlines()
            return data
        except Exception as ex:
            print("ERROR (trying to gt data from standard input): " + str(ex))


class SearchInputSources:
    def __init__(self, search_criteria, list_of_files_to_parse):
        self.search_criteria = search_criteria
        self.stdin_sources = list_of_files_to_parse

    def run(self):
        file_name = ''
        data = ''
        results = False
        all_matched_results = []

        for stdin_source in self.stdin_sources:
            get_data = ''
            if stdin_source == '-':
                get_data = GetDataFromStdin(self.search_criteria)
                file_name = 'Standard Input'
            elif os.path.isfile(stdin_source):
                get_data = SearchInputSources(self.search_criteria)
                file_name = get_file_name_from_path(stdin_source)
            else:
                print("ERROR: path is not found: " + stdin_source)

            if get_data != '':
                data = get_data.run()

            if data != '':
                found_re_matches, results = get_data.search_data_content(data, file_name)

            if found_re_matches:
                print(results)
                for result in results:
                    all_matched_results.append(result)
            else: # for debugging
                print("No matches found in file " + file_name + "!!")
        return all_matched_results


class OutPut:
    def __init__(self, underscore, color, machine, data):
        self.underscore = underscore
        self.color = color
        self.machine = machine
        self.data = data

    def format_results(self):
        '''Print the file name and the line number for every match.

        The Script accepts optional parameters which are mutually exclusive:

        -u ( --underscore ) which prints '^' under the matching text

        -c ( --color ) which highlight matching text

        -m ( --machine ) which generates machine readable output

                         format: file_name:no_line:start_pos:matched_text'''
        machine_readable_output = []
        data_index = 0
        finished_ok = False
        try:
            machine_readable_output = []
            while data_index < len(self.data):
                print("File name: %s, Line: %s" % (self.data[data_index]["file_name"],
                                                   self.data[data_index]["line_number"]))
                if self.color:
                    temp_text = self.data[data_index]["line_text"]
                    print(temp_text[:self.data[data_index]["pos"]] + "\033[1;37;42m" + self.data[data_index]["matched_text"] + "\033[0;37;0m" +
                          temp_text[self.data[data_index]["pos"] + self.data[data_index]["length_text_found"] + 1:])
                    # print()
                    # print('\n')

                if self.underscore:
                    if not self.color:
                        print(self.data[data_index]["line_text"] + '\n')
                    header_titles_length = 19
                    header_length = len(self.data[data_index]["file_name"]) + len(str(self.data[data_index]
                                                                                      ["line_number"]))
                    padding = self.data[data_index]["pos"]  # + header_titles_length + header_length
                    padding_counter = 0
                    whitespaces = ''
                    while padding_counter <= padding:
                        whitespaces = whitespaces + ' '
                        padding_counter += 1
                    underscores = 0
                    underscore_text = ''
                    while underscores < len(self.data[data_index]["matched_text"]):
                        underscore_text = underscore_text + '^'
                        underscores += 1
                    print(whitespaces + underscore_text + '\n')

                if self.machine:
                    machine_readable_output.append(self.data[data_index]["file_name"] + ":" +
                                                   str(self.data[data_index]["line_number"]) + ":" +
                                                   str(self.data[data_index]["pos"]) + ":" +
                                                   self.data[data_index]["matched_text"])
                data_index += 1
                finished_ok = True
        except Exception as ex:
            print(ex)
        for machine_output in machine_readable_output:
            print(machine_output)
        return finished_ok


def parse_cmd_line(args):
    input_sources = []
    underscore = False
    color = False
    machine = False
    regex = ''

    '''Validate syntax errors of the regular expression'''
    try:
        re.compile(args[1])
        regex = args[1].strip('\"')
        regex = regex.strip('\'')
    except re.error:
        print("ERROR: First command line parameter must be a valid regular expression")
        return False, regex, input_sources, underscore, color, machine

    '''Set output format flags'''
    cmd_line_param_index = 2
    while cmd_line_param_index < len(args) and args[cmd_line_param_index][:1] == "-":
        if args[cmd_line_param_index].lower() == '-u':
            underscore = True
            cmd_line_param_index += 1
        elif args[cmd_line_param_index].lower() == '-c':
            color = True
            cmd_line_param_index += 1
        elif args[cmd_line_param_index].lower() == '-m':
            machine = True
            cmd_line_param_index += 1
        else:
            break
    '''collect sources of input'''
    while cmd_line_param_index < len(args):
        input_sources.append(args[cmd_line_param_index])
        cmd_line_param_index += 1
    if len(input_sources) == 0:
        input_sources.append("-")

    return True, regex, input_sources, underscore, color, machine


def _get_current_os():
    if 'linux' in sys.platform:
        return 'Linux'
    elif 'win32' in sys.platform:
        return 'Windows'
    elif 'darwin' in sys.platform:
        return 'Mac OS X'
    else:
        return 'OTHER'


def main(args):
    '''	This program requires at least one arguments being a valid regular expression to search for,
    additional optional arguments are:
    output formatting parameters -u = underscore, -c = highlight matched text, -m = machine readable format
    path to files, if no paths are given or the path is '-' the program will collect data from the stndard input until
    'escaped (Ctrl-D) .'''
    if len(args) > 1:
        current_os = _get_current_os
        is_re_valid, regex, input_sources, underscore, color, machine = parse_cmd_line(args)
    else:
        is_re_valid = False

    if is_re_valid:
        find_reg_ex_in_files = SearchInputSources(regex, input_sources)
        results = find_reg_ex_in_files.run()
        # print_results = OutPut(underscore, color, machine, results)
        print_results = OutPut(underscore, color, machine, results)
        print_results.format_results()

    else:
        print(main.__doc__)
        pass


if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
