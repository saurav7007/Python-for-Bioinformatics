#! /usr/bin/env python3

import sys

# Define a usage function to display help information
def usage():
    print("""
          Usage: python3 count_records.py <filename>
          
          Description:
          This script counts the number of records in a file. 
          A record is identified by a header line that starts with the '>' character.
          
          Arguments:
          <filename>  The name of the file to process (e.g., a FASTA file).
          
          Example:
          python3 count_records.py dna.example.fasta
    """)

# Main program logic
if len(sys.argv) < 2:
    print("Error: Missing filename argument.")
    usage()
    sys.exit()

# The program need the file name as the first argument
filename = sys.argv[1]

# Opening the file if exisit or print an error message
try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file %s does not exist." %filename)
    sys.exit()

# Create a variable to store the count of the records
recordCount = 0

# Reading each line of a file one by one
# Autoincrement the count if the new records are found

for line in content:
    if line[0] == '>':
        recordCount += 1

# Print the output
print('There are %d records in the %s' % (recordCount, filename)) 