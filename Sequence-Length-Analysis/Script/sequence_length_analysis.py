#! /usr/bin/env python3

import sys

# Define a usage function to display help information
def usage():
    print("""
          Usage: python3 sequence_length_analysis.py <filename>
          
          Description:
          This script analyzes the lengths of sequences in a FASTA file, identifying the longest 
          and shortest sequences, their lengths, and their identifiers.
          
          Arguments:
          <filename>  The name of the file to process (e.g., a FASTA file).
          
          Example:
          python3 sequence_length_analysis.py dna.example.fasta
    """)

#-----Main program logic-------

# Check command-line arguments
if len(sys.argv) < 2:
    print("Error: Missing filename argument.")
    usage()
    sys.exit()

# The program needs the file name as the first argument
filename = sys.argv[1]

try:
    file = open(filename, 'r')
except FileNotFoundError:
    print("Error: The file %s does not exist." % filename)
    sys.exit()

seqs = {}
seqDetails = ''

# Read the file and process sequences
for line in file:
    line = line.strip()

    if line[0] == '>':
        # If there is an ongoing sequence, calculate its length
        if seqDetails in seqs:
            seqs[seqDetails]['length'] = len(seqs[seqDetails]['sequence'])
        
        # Start a new sequence
        seqDetails = line[1:]  # Extract header without '>'
        seqs[seqDetails] = {'sequence': '', 'length': 0}
    else:
        # Append the sequence line to the current sequence
        seqs[seqDetails]['sequence'] += line

# Ensure the last sequence length is calculated
if seqDetails in seqs:
    seqs[seqDetails]['length'] = len(seqs[seqDetails]['sequence'])

# Analyze sequence lengths
lengths = [seqs[seq]['length'] for seq in seqs]
max_length = max(lengths)
min_length = min(lengths)

# Identify sequences with the longest and shortest lengths
longest = [seq for seq in seqs if seqs[seq]['length'] == max_length]
shortest = [seq for seq in seqs if seqs[seq]['length'] == min_length]

# Output results
print("\nSequence Analysis Results:")
print(f"Longest sequence(s) ({max_length} bp):")
for seq in longest:
    print(f"  Identifier: {seq}")

print(f"\nShortest sequence(s) ({min_length} bp):")
for seq in shortest:
    print(f"  Identifier: {seq}")
