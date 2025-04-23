import re
from collections import OrderedDict

def clean_effects(filename):
    reagents = OrderedDict()  # Use OrderedDict to maintain the original order of reagents

    with open(filename, 'r') as file:
        current_reagent = None

        for line in file:
            line = line.rstrip()  # remove leading/trailing whitespaces

            if line != '':
                if not re.search('^\s', line):
                    # line is a new reagent
                    current_reagent = line
                    reagents[current_reagent] = []  # Use a list to preserve the original order of effects
                else:
                    # line is an effect for the current reagent
                    effect = line.strip()
                    if effect not in reagents[current_reagent]:  # Check if the effect is already in the list
                        reagents[current_reagent].append(effect)  # Add the effect to the list

    return reagents

effects = clean_effects('alchemy_cleaned.txt')

# Write the effects to the new file while maintaining the original order
with open('alchemy_doubles_removed.txt', 'w') as file:
    for reagent, effect_list in effects.items():
        if effect_list:  # Check if the effect list for the reagent is not empty
            file.write(reagent + "\n")
            for effect in effect_list:
                file.write(f"    {effect}\n")
            file.write("\n")  # Add a new line after writing the effects for each reagent