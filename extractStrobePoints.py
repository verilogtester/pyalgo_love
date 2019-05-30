#! /usr/local/Python-3.6.2/bin/python

"""
# Auto generation of Fault Sim Test bench
This python code parses the testbench template and updates the user-defined strobe points.
#Python features are used to extract the strobe location.
-- created a dictionary of regular expressions used to extract the strobe locations
-- traversing regular expressions in a dictionary 
-- parsing command line options for ease of use
-- replacing global/generic values with the new user provided values like clock, reset, time to inject faults, etc. 
-- created a class of multiple function definitions 
-- generating multiple test benches per test vector. 

This code is modular and manageable, idea is to change the regular expressions at a location for the variable inputs 
""""

import re, getopt, sys, fileinput, os, glob, shlex, subprocess
from shutil import copyfile

class ExtractStrobePoints():

    def __init__(self, file_path):
        self.file_path = file_path
        self.ipname = None
        self.test_obs_dict = {}
        self.test_diag_dict = {}
        # setup regular expressions
        self.rx_dict = {
            'IP name': re.compile(r'^IP: (.*)\n'),
            'testname': re.compile(r'Krf::typical::(.*)\n'),
            'Observation Signals': re.compile(r'Observation Signals:'),
            'Diagnosis Signals': re.compile(r'Diagnosis Signals:'),
            'Associated Scopes': re.compile(r'Associated Scopes:')
        }

    def _parse_line(self, test_line):
        """
        Do a regex search against all defined regexes and 
        return the key and match result of the first matching regex
        """
        for key, rx in self.rx_dict.items():
            match = rx.search(test_line)
            if match:
                return key,match
        # if there is no match
        return None, None

    def extract(self):
        if self.file_path is None:
            return False
        with open(self.file_path,'r') as file:
            curr_line = file.readline()
            while curr_line:
                key, match = self._parse_line(curr_line)
                if key == 'IP name':
                    self.ipname = match.group(1)
                if key == 'testname':
                    testname = match.group(1)
                if key == 'Observation Signals':
                    self.test_obs_dict[testname] = []
                    curr_line = file.readline()
                    while curr_line:
                        key, match = self._parse_line(curr_line)
                        if key == 'Diagnosis Signals': break
                        self.test_obs_dict[testname].append(curr_line)
                        curr_line = file.readline()
                if key == 'Diagnosis Signals':
                    self.test_diag_dict[testname] = []
                    curr_line = file.readline()
                    while curr_line:
                        key, match = self._parse_line(curr_line)
                        if key == 'testname': 
                            testname = match.group(1)
                            break
                        if key == 'Associated Scopes': 
                            break
                        self.test_diag_dict[testname].append(curr_line)
                        curr_line = file.readline()

                curr_line = file.readline()
        return self.test_obs_dict, self.test_diag_dict

    def petty_print(self):
        if self.ipname == None:
            return
        print("IPname : {0:s}".format(self.ipname))
        for testname in self.test_obs_dict.keys():
            print("Testname : {0:s}".format(testname))
            print("Observation Signals :")
            for obs_signal in self.test_obs_dict[testname]:
                print(" {0:s}".format(obs_signal))
            print("Diagnosis Signals :")
            for diag_signal in self.test_diag_dict[testname]:
                print(" {0:s}".format(diag_signal))

def parse_arg():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:r:d:f:t:h", ["clock=", "reset=", "delay=", "input_file=", "tb_template=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        print ("Usage \
                ./file_parser.py \
                -c user_provided_clk_signal \
                -r user_provided_reset_signal \
                -f ./input.txt \
                -d 1700ps \
                -t testbench_template.v")
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            print ("Usage \
                ./file_parser.py \
                -c user_provided_clock_signal \
                -r user_provided_reset_signal \
                -f ./input.txt \
                -d 1700ps \
                -t testbench_template.v")
            sys.exit()
        elif o in ("-c", "--clock"):
            CLOCK = a
        elif o in ("-r", "--reset"):
            RESET = a
        elif o in ("-d", "--delay"):
            DELAY = a
        elif o in ("-f", "--input_file"):
            FILENAME = a
        elif o in ("-t", "--tb_template"):
            TB_TEMPLATE  = a
        else:
            assert False, "unhandled option"
    return CLOCK, RESET, RESET, DELAY, FILENAME, TB_TEMPLATE
    print ("c =", CLOCK)
    print ("r =", RESET)
    print ("d =", DELAY)
    print ("f =", FILENAME)

if __name__ == '__main__':
    #Specify input file path
    CLOCK, RESET, RESET, DELAY, file_path, tb_template = parse_arg()
    obj = ExtractStrobePoints(file_path)
    test_obs_dict, test_diag_dict = obj.extract()
#    obj.petty_print()

    for testname in test_obs_dict.keys():
        #make testbench template for each tests
        copyfile(tb_template, testname+'_tb.sv')
        USER_PROVIDED_OBSERVATION_LOCATIONS = ','.join(str(x).strip() for x in test_obs_dict[testname])
        USER_PROVIDED_DETECTION_LOCATIONS = ','.join(str(x).strip() for x in test_diag_dict[testname])
        #write contents into file
        with open(testname+'_tb.sv', 'r+') as f:
         content = f.read()
         f.seek(0)
         f.truncate()
         f.write(content.replace('USER_PROVIDED_DELAY', DELAY).replace('USER_PROVIDED_CLOCK', CLOCK).replace('USER_PROVIDED_RESET', RESET).replace('USER_PROVIDED_OBSERVATION_LOCATIONS', USER_PROVIDED_OBSERVATION_LOCATIONS).replace('USER_PROVIDED_DETECTION_LOCATIONS', USER_PROVIDED_DETECTION_LOCATIONS))

