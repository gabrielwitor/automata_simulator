import sys
import json
import csv

def main():
    # Opening the json file
    aut_file = open(sys.argv[1])

    # Creating a dictionary with the json file
    aut_dict = json.load(aut_file)

    # Obtaining the inital and ending states from the json file
    initial_state = aut_dict['initial']

    final_state = aut_dict['final']

    # Creating a hash map for transitions. Format: 0a = 1

    transitions = {}

    for transition in aut_dict['transitions']:
        transitions[transition['from']+transition['read']] = transition['to']

    input_csv = open(sys.argv[2])
    csv_reader = csv.reader(input_csv, delimiter=';')

    for input in csv_reader:
        q = initial_state
        for symbol in input[0]:
            key = f'{q}{symbol}'
            if (key in transitions):
                q = transitions[key]
            else:
                q = -1
        print(int(q) in final_state)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Error: missing arguments. Execute the program properly by running in your terminal: python automata.py <automata-archive.aut>")
        exit(1)
    
    main()