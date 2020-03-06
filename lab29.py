import numpy as np
from prettytable import PrettyTable

def amino_acid_content(filename):
    # returns a dictionary with quantities of amino acids at N-terminus

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
    terminus = 0
    for line in f:
        if line[0] == '>':
            terminus = 1
        else:
            amino_acids[line[0]] = amino_acids[line[0]] + 1
            terminus = 0
    f.close()

    quantities = []
    for amino_acid in amino_acids:
        quantities.append(amino_acids[amino_acid])

    return quantities

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']
true_labels = {'ecoli' : 'E. coli', 'elegans' : 'C. elegans', 'human' : 'H. sapiens',
               'melanogaster' : 'D. melanogaster', 'mouse' : 'M. musculus',
               'subtilis' : 'B. subtilis', 'thaliana' : 'A. thaliana', 'yeast' : 'S. cerevisiae',
               'zebrafish' : 'D. rerio'}
amino_acids = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T','X','Z','B','U','O']

quantities = []

for label in labels:
    quantities.append(amino_acid_content('hw2/data_' + label + '.fasta'))

data = []
for i in range(len(quantities)):
    data.append([true_labels[labels[i]], amino_acids[np.argmax(quantities[i])]])


x = PrettyTable()


x.title = 'Most common amino acid at proteins\' N-Terminus for given proteome'
x.field_names = ['proteome', 'most common amino acid at N-Terminus']
for entry in data:
    x.add_row(entry)

print(x)

