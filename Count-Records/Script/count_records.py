#! /usr/bin/env python3

import sys


# Define a usage function to display help information
def usage():
    print(
        """
    Usage: python3 count_records.py <filename>

    Description:
    This script counts the number of records in a file. A record is
    identified by a header line that starts with the '>' character.

    Arguments:
    <filename>  The name of the file to process (e.g., a FASTA file).

    Example:
    python3 count_records.py dna.example.fasta
    """
    )


def count_seqs(filename):
    """
    Count the number of sequences in a FASTA file.
    """
    try:
        with open(filename, "r") as file:
            record_count = sum(1 for line in file if line[0] == ">")
        return record_count
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        sys.exit(1)


# Main program logic


if len(sys.argv) < 2:
    print("Error: Missing filename argument.")
    usage()
    sys.exit(1)

filename = sys.argv[1]
records = count_seqs(filename)

print(f"There are {records} records in {filename}.")
