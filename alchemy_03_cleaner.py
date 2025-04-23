import re

with open('alchemy_replaced.txt', 'r') as file:
    with open('alchemy_cleaned.txt', 'w') as output_file:  # Open a new file for writing
    	for line in file:
            if "NAME" not in line and not re.findall('^\s', line):
                line = '    ' + line
            elif "NAME" in line:
            	line = line[:-5] + '\n'
            output_file.write(line)