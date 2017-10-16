import sys
from subprocess import Popen, PIPE


'''
Returns a list of student pairings based on their preferences
@param student: an integer representing the current student whose
preferences we're reading
@param line: a string holding the line that contains the student's
preferences
'''
def get_pairings(student, line):
    prefs = line.strip().split(' ')
    arr = []
    for i in prefs:
        if (i):
            arr.append((student, int(i)))
    return arr


'''
Returns a list of the groups formed in the model of the z3 output
@param z3_output: a string of the console output from z3
'''
def get_final_groups(z3_output):
	groups = []
	z3_output = z3_output.strip().split()
	# find the start of the model in case of unknown syntax
	for i in range(0, len(z3_output)):
		if (z3_output[i] == '(model'):
			break
	# find the groups of two set to true
	for k in range(i, len(z3_output)):
		if (z3_output[k] == '(define-fun' and \
			z3_output[k+1].count('s') > 1 and \
			z3_output[k+4] == 'true)'):
			two_students = z3_output[k+1].split('s')[1:]
			groups.append((two_students[0], two_students[1]))
	return groups


# argument check
if (len(sys.argv) > 2 or len(sys.argv) == 1):
    sys.exit('Usage: python groupinga.py <sample-input-file-name>')

# open the output file
output_file = open('groupinga-formula.smt2', 'w')

student = []
student_count = 1
pairing = []
with open(sys.argv[1]) as file:
    for line in file:
        pairing = pairing + get_pairings(student_count, line)
        student.append(student_count)
        student_count += 1
# case where last line is empty
with open(sys.argv[1]) as file2:
    if (not file2.readlines()[-1].strip()):
        student_count -= 1
        student.append(student_count)

d = []
asrt = '(assert (not (or'
for i in student:
    for j in student:
        if i != j:
            d.append((i,j))
c = []
# student groups declarations
for i in d:
    output_file.write('(declare-const '+'s'+str(i[0])+'s'+str(i[1])+' Bool)\n')
for i in student:
    output_file.write('(declare-const '+'s'+str(i)+' Bool)\n')
for i in d:
    a = i[0]
    b = i[1]
    s = asrt
    for j in d:
        if i !=j:
            if (a in j) or (b in j):
                temp = ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(j[0])+'s'+str(j[1])+')'
                s+=(temp)
    s += ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(a)+')'
    s += ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(b)+')'
    s += ')))'
    output_file.write(s + '\n')
# constraints
for i in student:
    s = '(assert (not (or'
    for j in d:
        if i in j:
            temp = ' (and '+'s'+str(i)+' '+'s'+str(j[0])+'s'+str(j[1])+')'
            s+=(temp)
    s += ')))'
    output_file.write(s + '\n')

for i in d:
    a = i[0]
    b = i[1]
    s = asrt
    if i in pairing:
        output_file.write('(assert-soft '+'s'+str(a)+'s'+str(b)+' :weight 3 )\n')
    else:
        output_file.write('(assert-soft '+'s'+str(a)+'s'+str(b)+' :weight 2 )\n')

for i in student:
    s = asrt
    output_file.write('(assert-soft '+'s'+str(i)+' :weight 1 )\n')    

output_file.write('(check-sat)\n')
output_file.write('(get-model)')

output_file.close()
# run z3 and get output
p = Popen(['/u/csc410h/fall/pub/z3/bin/z3', 'groupinga-formula.smt2'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

output, err = p.communicate()

final_groups = get_final_groups(output)

solution_file = open('groupinga-output.txt', 'w')

solution_file.write(str(len(final_groups)) + " groups formed:")
for i in final_groups:
	solution_file.write("\n" + str(i[0]) + "," + str(i[1]))