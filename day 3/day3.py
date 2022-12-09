points_per_item = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' :13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x': 24, 'y' : 25, 'z' : 26, 'A': 27, 'B' : 28, 'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32, 'G' : 33, 'H' : 34, 'I' : 35, 'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40, 'O' : 41, 'P' : 42, 'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48, 'W' : 49, 'X': 50, 'Y' : 51, 'Z' : 52}


with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 3\input.in') as f:
    lines = f.readlines()
    backpacks =[entry.strip() for entry in lines]

backpack_sum=0

for backpack in backpacks:
    #compartiment
    first_half = set(backpack[:len(backpack)//2]) #set(variable[0 : number of characters//2]) --> first half will be from charachter 0 to len/2
    second_half = set(backpack[len(backpack)//2:])#set(var[len/2 : end of list]) --> if : before then first item of list if after then end of list

    common_char = (first_half.intersection(second_half)).pop() # deletes overlaping character from list

    #wanted to get from dictionary the points but dont know how to, will turn answer in ASCII value and from that get the points
    
    #try one

    # if common_char in points_per_item:
    #     backpack_sum += points_per_item

    #convert to ASCII:
    if common_char.isupper():
        backpack_sum += ord(common_char) - ord('A') + 27 #if common_char is uppercase: backpack sum += ascii value of common_char - ascii value of A+27 (because it starts at 65) --> A in instruction starts at 27, ASCII strarts at 65 --> return to 0 (-ord(A)) + 27
    else:
        backpack_sum += ord(common_char) - ord('a') + 1 #same as above except lower case starts at 1 for instructions
print(backpack_sum)


#part 2

backpack_sum = 0
while len(backpacks) > 0:
    first_backpack = set(backpacks.pop())
    second_backpack = set(backpacks.pop())
    third_backpack = set(backpacks.pop())

    common_char = ((first_backpack.intersection(second_backpack)).intersection(third_backpack)).pop()

    #translate into ASCII, same as above
    if common_char.isupper():
        backpack_sum += ord(common_char) - ord('A') + 27 #if common_char is uppercase: backpack sum += ascii value of common_char - ascii value of A+27 (because it starts at 65) --> A in instruction starts at 27, ASCII strarts at 65 --> return to 0 (-ord(A)) + 27
    else:
        backpack_sum += ord(common_char) - ord('a') + 1 #same as above except lower case starts at 1 for instructions
print(backpack_sum)

