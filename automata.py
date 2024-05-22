import sys
import json
import csv
from collections import defaultdict

def main():
    # Opening the json file
    aut_file = open(sys.argv[1])

    # Creating a dictionary with the json file
    aut_dict = json.load(aut_file)

    # Obtaining the inital and ending states from the json file
    initial_state = aut_dict['initial']

    final_state = aut_dict['final']

    # Creating a multimap for transitions. Format: 0a = 1

    transitions = defaultdict(list)

    for transition in aut_dict['transitions']:
        transitions[transition['from']+transition['read']].append(transition['to'])

    print(transitions)


    input_csv = open(sys.argv[2])
    csv_reader = csv.reader(input_csv, delimiter=';')

    for input in csv_reader:
        q = initial_state
        # input[0] since we are processing the word (Ex: aaabaabbb) and not the expected result.
        for symbol in input[0]:
            key = f'{q}{symbol}'
            if (key in transitions):
                q = transitions[key][0]
            else:
                q = -1
        print(int(q) in final_state)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Error: missing arguments. Execute the program properly by running in your terminal: python automata.py <automata-archive.aut>")
        exit(1)
    
    main()