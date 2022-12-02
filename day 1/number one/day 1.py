#getting content
with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 1\number one\list.txt') as f:
    content = [i for i in f.read().strip().split("\n")]
    

#string in data
calories = 0
max1 = 0
max2 = 0
max3 = 0
for item in content:
    if item == '':
        if calories > max1:
            max1 = calories
        elif calories > max2:
            max2 = calories
        elif calories > max3:
            max3 = calories
            

            
            max = calories
        calories = 0
    else:
        num = int(item) #creates an int from sting
        calories+= num

print(max1 + max2 + max3)

print(70613*3)
