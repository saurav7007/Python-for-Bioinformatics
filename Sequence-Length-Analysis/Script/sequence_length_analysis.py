#! /usr/bin/env python3

import sys


# Define a usage function to display help information
def usage():
    print(
        """
          Usage: python3 sequence_length_analysis.py <filename>

          Description:
          This script analyzes the lengths of sequences in a FASTA file,
          identifying the longest and shortest sequences, their lengths,
          and their identifiers.

          Arguments:
          <filename>  The name of the file to process (e.g., a FASTA file).

          Example:
          python3 sequence_length_analysis.py dna.example.fasta
        """
        )


def seq_len(filename):
    """
    Reads a FASTA file and returns a dictionary with sequence lengths.
    """
    try:
        seqs = {}
        seq_id = None

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line[0] == ">":
                    seq_id = line[1:]
                    seqs[seq_id] = 0  # Initialize sequence length
                elif seq_id:
                    seqs[seq_id] += len(line)  # Add sequence length

        return seqs

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")

        return None


def long_seq(seq_len):
    """
    Calculates the longest sequence from the dictionary with sequence lengths
    """
    max_len = max(seq_len.values())
    longest_seqs = [seq for seq in seq_len.items() if seq[1] == max_len]

    return longest_seqs


def short_seq(seq_len):
    """
    Calculates the shortest sequence from the dictionary with sequence lengths
    """
    max_len = max(seq_len.values())
    shortest_seqs = [seq for seq in seq_len.items() if seq[1] == max_len]

    return shortest_seqs

# -----Main program logic-------


# Check Arguments
if len(sys.argv) < 2:
    print("Error: Missing filename argument.")
    usage()
    sys.exit()

filename = sys.argv[1]

# Read sequences length from the fasta file
seq_details = seq_len(filename)

# Identify sequences with the longest and shortest lengths
longest = long_seq(seq_details)
shortest = long_seq(seq_details)

print(longest)

# Output results
print("\nSequence Analysis Results:")
print(f"Longest sequence(s) of ({longest[0][1]} bp):")
for seq_id in longest:
    print(f" Idenfier: {seq_id[0]}")

print(f"\nShortest sequence(s) of ({shortest[0][1]} bp):")
for seq_id in shortest:
    print(f"  Identifier: {seq_id[0]}")
