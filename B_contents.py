import numpy as np
from prettytable import PrettyTable

def average_protein_length(filename):
    # return the average protein length
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
    # return a list with percentage contents of amino acids

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

contents_b = amino_acid_content('data/pdb_seqres.txt')[:20]

amino_acids = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T']

print('PDB average protein length:')
print(np.round(average_protein_length('data/pdb_seqres.txt'), 2))
print()
print('PDB amino acid percentage contents:')

# sort data for plotting
sorted_ind = np.argsort(contents_b)[:20]

sorted_content = []
sorted_labels = []

for i in range(len(sorted_ind)):
    sorted_content.append(contents_b[sorted_ind[i]])
    sorted_labels.append((amino_acids[sorted_ind[i]]))

for i in range(len(contents_b)):
    sorted_content[i] = str(sorted_content[i]) + '%'

# build the table of percentage contents
x = PrettyTable()
x.field_names = sorted_labels

x.add_row(sorted_content)

print(x)
