import sys
# used to pretty print the matrix
import itertools
import math

# process line of student pair into an array
def process_line(array):
    arr = array.strip().split(' ')
    for x in range(0, len(arr)):
        arr[x] = int(arr[x])
    return arr

# declares all possible variables of student pairs
def get_variables(array):
    all_pairs = []
    for student1 in range(0, len(array)):
        for student2 in range(0, len(array)):
            if(student1 != student2):
                all_pairs.append('s{}_s{}'.format(student1 + 1, student2 + 1))
    return all_pairs


# declares all possible variables of student pairs
def declare_variables(array):
    all_pairs = []
    for student1 in range(0, len(array)):
        for student2 in range(0, len(array)):
            if(student1 != student2):
                formatted_line = '(declare-const s{}_s{})\n'.format(student1 + 1, student2 + 1)
                all_pairs.append(formatted_line)
    return all_pairs


def is_priority(student1, student2, student_prefs):
    if student2 in student_prefs[student1]:
        return True
    else:
        return False


def build(op, arg1, arg2):
    return "(" + op + " " + arg1 + " " + arg2 + ")"


def generate_constraint(op, true_args, all_args, weight=1):
    brackets = 0;
    answer = "(assert-soft "
    for i in all_args[:len(all_args) - 1]:
        if (i in true_args):
            answer += " (" + op + " " + i
        else:
            answer += " (" + op + " (not " + i + ")"
        brackets += 1
    if (all_args[-1] in true_args):
        answer += " " + all_args[-1]
    else:
        answer += " (not " + all_args[-1] + ")"
    answer += (")" * brackets) + " :weight " + str(weight) + ")"
    return answer


def s_assert(arg, weight=1, id=None):
    if (id == None):
        return "(assert-soft " + arg + " :weight " + str(weight) + ")"
    else:
        return "(assert-soft " + arg + " :weight " + str(weight) + " :id " + str(id) + ")"


def get_priority(group, grouping_prefs):
    priority = 1

    student1 = int(group.split("_")[0][1:])
    student2 = int(group.split("_")[1][1:])

    if (student1 in grouping_prefs[student2-1]):
        priority += 5
    if (student2 in grouping_prefs[student1-1]):
        priority += 5
    return priority 
            



# ensures the correct amount of arguments
if (len(sys.argv) > 2 or len(sys.argv) == 1):
    sys.exit('Usage: python grouping_A.py <sample-input-file-name>')
# Input file
input = open(sys.argv[1], "r")

# an 2d array of [student, student partnership preferences]
grouping_pref = []
# all possible pairing boolean variables in the domain.
all_pairs = []
student_count = 0

with open(sys.argv[1]) as file:
    for line in file:
        grouping_pref.append(process_line(line))
        student_count += 1
all_pairs = get_variables(grouping_pref)

declarations = declare_variables(grouping_pref)
for k in declarations:
    print k
    
constraints = []
print "//////////"
for i in itertools.combinations(all_pairs, r=int(math.floor(student_count/2))):
    weight = 0
    for pair in i:
        weight += get_priority(pair, grouping_pref)
    constraints.append(generate_constraint("and", i, all_pairs, weight))
    print generate_constraint("and", i, all_pairs)
    print "\n" + str(i)

#assertion = s_assert(generate_constraint("or", constraints, constraints))


print "/////////////////////////////////////"
for a in all_pairs:
    print a
    print "priority: " + str(get_priority(a, grouping_pref))
    
'''
assertions = []
for b in constraints:
    assertions.append(s_assert(b))
    print assertions[-1]
'''
print(grouping_pref)
print(all_pairs)
