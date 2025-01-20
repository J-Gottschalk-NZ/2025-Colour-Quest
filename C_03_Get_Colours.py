import csv
import random

# Retrieve colours from csv file and put them in a list
file = open("00_colour_list_hex_v3.csv", "r")
all_colors = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row
all_colors.pop(0)

print(all_colors)

round_colours = []
colour_scores = []

# loop until we have four colours with different scores...
while len(round_colours) < 4:
    potential_colour = random.choice(all_colors)

    # colour scores are being read as a string,
    # change them to an integer to compare / when adding to score list.
    if int(potential_colour[1]) not in colour_scores:
        round_colours.append(potential_colour[0])

        # make score an integer and add it to the list of scores
        colour_scores.append(int(potential_colour[1]))

print("Round colours", round_colours)
print("Round scores", colour_scores)

# Get median score / target score
colour_scores.sort()
print("Sorted", colour_scores)