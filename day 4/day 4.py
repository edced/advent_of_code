with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 4\input.in') as f:
    lines = f.readlines()
    assignment_paires = [entry.strip() for entry in lines]

def is_range_a_in_range_b(range_a, range_b): #splits function at comma --> x-y , z-a avec x-y range a et z-a range b
    start_a, end_a = map(int, range_a.split('-')) #start a and end a is an integer. start a is start till dash and end is dash till end
    start_b, end_b = map(int, range_b.split('-')) #same
    return start_b <= start_a and end_a <= end_b # is range a in range b if startb is smaller or equal to starta and enda is smaller or equal to end_b


number_of_containers = 0

for assignment_paire in assignment_paires:
    first_range, second_range = assignment_paire.split(',')
    if is_range_a_in_range_b(first_range, second_range) or is_range_a_in_range_b(second_range, first_range):#checks if there is a range included in the other
        number_of_containers += 1

print(number_of_containers)

#part 2
number_of_overlap = 0
for assignment_paire in assignment_paires:
    first_range, second_range = assignment_paire.split(',')
    start_a, end_a = map(int, first_range.split('-'))
    start_b, end_b = map(int, second_range.split('-'))
    if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
        #if start a is in between start b and endb +1 or ...... +1 because range parameter doesnt count end one so range(1,8) will be 1 2 3 4 5 6 7
        number_of_overlap += 1

print(number_of_overlap)