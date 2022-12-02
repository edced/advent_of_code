#getting content
with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 1\number one\list.txt') as f:
    content = [i for i in f.read().strip().split("\n")]
    

#string in data
calories = 0
max = 0
max1 = 0
max2 = 0
max3 = 0
a=0
serie = 1
for item in content:
    if item == '':

       
        if (calories > max1 and calories > max2 and calories > max3):
            max1 = calories
        if (calories < max1 and calories > max2 and calories > max3):
            max2 = calories
        if (calories < max1 and calories < max2 and calories > max3):
            max3 = calories


        calories = 0
    else:
        num = int(item) #creates an int from sting
        calories+= num
        

if max1 + max2 + max3 == 204882:
    print("wrong")

else:
    print("sum of top 3 max = ", max1 + max2 + max3, '\n')

# print("max = ", max, '\n')
# print("max 1, max2, max3: ", max1 , max2, max3)
# print("sum of top 3 max = ", max1 + max2 + max3, '\n')
# print("wrong sum of maxes = ", 204882, '\n')
# print("max*3 = ", 70613*3, '\n')
# print(70613+68330+65939)