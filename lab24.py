import numpy as np

def average_protein_length(filename):
    # returns average protein length from data in filename
    f = open(filename, 'r')

    lengths = []
    first_digit_index = 0
    last_digit_index = 0
    for line in f:
        if line[0] == '>':
            for i in range(len(line)):
                if line[i:i+7] == 'length:':
                    first_digit_index = i+7 #first digit of protein length
                    break

            for i in range(first_digit_index,len(line)):
                if line[i] == ' ':
                    last_digit_index = i
                    break

            lengths.append(int(line[first_digit_index:last_digit_index]))

    f.close()

    np.asarray(lengths)

    return np.average(lengths)

def amino_acid_content(filename):
    # returns a dictionary with quantities of amino acids

    amino_acids = {
        'G': 0,
        'A': 0,
        'L': 0,
        'M': 0,
        'F': 0,
        'W': 0,
        'K': 0,
        'Q': 0,
        'E': 0,
        'S': 0,
        'P': 0,
        'V': 0,
        'I': 0,
        'C': 0,
        'Y': 0,
        'H': 0,
        'R': 0,
        'N': 0,
        'D': 0,
        'T': 0,
        'X': 0,
        'Z': 0,
        'B': 0,
        'U': 0,
        'O': 0
    }

    f = open(filename, 'r')

    for line in f:
        if line[0] != '>':
            for i in range(len(line)-1):
                amino_acids[line[i]] = amino_acids[line[i]] + 1
    f.close()

    sum = 0

    for amino_acid in amino_acids:
        sum = sum + amino_acids[amino_acid]

    for amino_acid in amino_acids:
        amino_acids[amino_acid] = round((amino_acids[amino_acid]/sum)*100, 2)

    content = []

    for amino_acid in amino_acids:
        content.append(amino_acids[amino_acid])

    return content

# average protein length
print(average_protein_length('data/pdb_seqres.txt'))

# amino acid percentage content
print(amino_acid_content('data/pdb_seqres.txt'))