
with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 5\input.in') as f:
    lines = f.readlines()
    line = [entry for entry in lines]

number_of_crates = len(lines[0])//4 #number of crates = amount of charachter line 0 divided by 4

crate_lines = lines[:lines.index('\n')-1] #crate lines = 0-> lines one before \n 
instruction_lines = lines[lines.index('\n')+1:] #instruction lines = lines one after \n till the end

items = list(line)[1:-1:4] #items = in list line [start: end: amount per "jump"]

amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]
#variable a, b, c = integer entry for entry in strip (remove space), split at space if entry is a digit --> removes character and makes digit an int with first one amount, second source, third target

class CrateStack:
    def __init__(self) -> None:
        self.content = [] 

    def add_item_on_top(self, item): # add one item on top (at the end) of the list during setup
        self.content.append(item)

    def take_x_crate(self, x, move_multiple): # take x crates from the top (either one by one by reversing the end of the list if move_multiple=False in Part 1, or all at once)
        return_crate = self.content[-x:]
        self.content = self.content[:-x]
        if move_multiple:
            return return_crate
        else:
            return reversed(return_crate)

    def add_crates(self, new_crates): # add the chunk of crates from another stack on top during moving
        self.content += new_crates

    def get_top_content(self):  #get info about the top crate as a string for the output for the elves
        return self.content[-1] if len(self.content) > 0 else ""





