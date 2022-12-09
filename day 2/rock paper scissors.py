map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}



with open(r'C:\Users\cedri\OneDrive\Documents\advent of code\day 2\input.in') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

def points_per_round(round_string):
    a = 0
    opponent_shape = map_input[round_string[0]] #opponent, first character
    our_shape = map_input[round_string[2]] #me, second character

    if (opponent_shape, our_shape) in [('Paper', 'Paper'), ('Rock', 'Rock'), ('Scissors, Scissors')]:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]
    if (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors, Paper')]:
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    if (opponent_shape, our_shape) in [('Rock', 'Paper'), ('Scissors', 'Rock'), ('Paper', 'Scissors')]:   
        return points_per_outcome['Win'] + points_per_shape[our_shape]
    if (opponent_shape, our_shape) in [('Scissors', 'Paper')]:
        return points_per_outcome['Win'] + points_per_shape['Scissors']
    if (opponent_shape, our_shape) in [('Scissors', 'Scissors')]:
        return points_per_outcome['Draw'] + points_per_shape['Scissors']
    else:
        print(opponent_shape, our_shape)
        print("null")

        

        
        
 
    
total = sum([points_per_round(round_string) for round_string in rounds])
print(total)