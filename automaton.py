import sys
import json
import csv
from collections import defaultdict
import time

def main():
    # Opening the json file
    aut_file = open(sys.argv[1])

    # Creating a dictionary with the json file
    aut_dict = json.load(aut_file)

    # Obtaining the inital and ending states from the json file
    initial_state = aut_dict['initial']
    final_states = [str(final_state) for final_state in aut_dict['final']]

    # Creating a multimap for transitions. Format: 0a = 1
    transitions = defaultdict(list)

    for transition in aut_dict['transitions']:
        transitions[transition['from']+transition['read']].append(transition['to'])

    input_csv = open(sys.argv[2])
    csv_reader = csv.reader(input_csv, delimiter=';')

    output_csv = open(sys.argv[3],"w+")
    csv_writer = csv.writer(output_csv,delimiter=';')

    for input in csv_reader:
        q = [initial_state]
        # input[0] since we are processing the word (Ex: aaabaabbb) and not the expected result.
        initial_time = time.perf_counter_ns()
        for symbol in input[0]:
            q = delta(q,symbol,transitions)
        ending_time = time.perf_counter_ns()
        elapsed_time = (ending_time-initial_time) 
        print(f'{input[0]};{input[1]};{detect_if_valid(q,final_states)};{elapsed_time}')
        csv_writer.writerow([f'{input[0]}']+[f'{input[1]}']+[f'{detect_if_valid(q,final_states)}']+[elapsed_time])

def delta(q,symbol,transitions):
    new_q = []
    for state in q:
        key = f'{state}{symbol}'
        if(key in transitions):
            for new_state in transitions[key]:
                print(f'{key}={new_state}')
                new_q.append(new_state)
        # Handle empty movements
        key = f'{state}'
        if(key in transitions): 
            for new_state in transitions[key]:
                print(f'{key}={new_state}')
                new_q.append(new_state)
    return new_q

def detect_if_valid(q, final_states):
    if(set(q).intersection(final_states)):
        return 1
    else:
        return 0

if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print("Error: missing arguments. Execute the program properly by running in your terminal: python automaton.py <automata-archive.aut> <automata-input.in> <automata-output.out>")
        exit(1)
    main()