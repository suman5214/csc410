import sys
# used to pretty print the matrix
import numpy as np

def process_line(array):
    # formatted_array = []
    # for char in array.strip().split(' '):
    #     formatted_array.append(char)
    # return formatted_array

    return array.strip().split(' ')

# def declare_variables(array):
#     for student1 in range(0, len(array)):
#         for student2 in range(0, len(array[student1])):
#             print('declare-const s{}_s{}\n').format(student1 + 1, array[student1][student2])
        
def declare_variables(array):
        
    for student1 in range(0, len(array)):
        for student2 in range(0, len(array)):
            if(student1 != student2):
                print('declare-const s{}_s{}\n').format(student1 + 1, student2 + 1)
        
        

# ensures the correct amount of arguments
if (len(sys.argv) > 2 or len(sys.argv) == 1):
    sys.exit('Usage: python grouping_A.py <sample-input-file-name>')

# Input file
input = open(sys.argv[1], "r")

# an 2d array of [student, student partnership preferences]
grouping_pref = []

with open(sys.argv[1]) as file:
    for line in file:
        grouping_pref.append(process_line(line))


print(grouping_pref)
declare_variables(grouping_pref)



