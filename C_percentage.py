from prettytable import PrettyTable
import os
import numpy as np

def amino_acid_content(directory):
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

    for filename in os.listdir(directory):
        if filename[0] != '.':
            f = open(directory + '/' + filename, 'r')

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

amino_acids = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T','X','Z','B','U','O']

labels = ['archaea', 'bacteria', 'eukaryota', 'viruses', 'full']
true_labels = {'archaea' : 'Archaea', 'bacteria' : 'Bacteria', 'eukaryota' : 'Eukaryota',
               'viruses' : 'Viruses', 'full' : 'SwissProt dataset'}

contents = []

for label in labels:
    print(label)
    contents.append(amino_acid_content('data/uniprot_' + label))

# build the table
x = PrettyTable()

x.title = 'Amino acid percentage content in proteins of given proteomes'
x.field_names = ['amino acid', true_labels['archaea'], true_labels['bacteria'],
                 true_labels['eukaryota'], true_labels['viruses'], true_labels['full']]

# sort table data
sums = []
for i in range(len(amino_acids)):
    sum = 0
    for j in range(len(labels)):
        sum = sum + contents[j][i]
    sums.append(sum)
sorted_ind = np.argsort(sums)
sorted_ind = np.flip(sorted_ind)

for i in range(len(amino_acids)-5):
    row = []
    row.append(amino_acids[sorted_ind[i]])
    for j in range(len(contents)):
        row.append(str(contents[j][sorted_ind[i]]) + '%')
    x.add_row(row)

print(x)
