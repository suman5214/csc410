import sys
# used to pretty print the matrix
import numpy as np

# process line of student pair into an array
def process_line(array):
    return array.strip().split(' ')

# declares all possible variables of student pairs
def declare_variables(array):
    all_pairs = []
    for student1 in range(0, len(array)):
        for student2 in range(0, len(array)):
            if(student1 != student2):
                formatted_line = 'declare-const s{}_s{}\n'.format(student1 + 1, student2 + 1)
                all_pairs.append(formatted_line)
    return all_pairs

def is_priority(student1, student2, student_prefs):
    if student2 in student_prefs[student1]:
        return True
    else:
        return False
        

# ensures the correct amount of arguments
if (len(sys.argv) > 2 or len(sys.argv) == 1):
    sys.exit('Usage: python grouping_A.py <sample-input-file-name>')
# Input file
input = open(sys.argv[1], "r")

# an 2d array of [student, student partnership preferences]
grouping_pref = []
# all possible pairing boolean variables in the domain.
all_pairs = []

with open(sys.argv[1]) as file:
    for line in file:
        grouping_pref.append(process_line(line))
all_pairs = declare_variables(grouping_pref)


print(grouping_pref)
print(all_pairs)




