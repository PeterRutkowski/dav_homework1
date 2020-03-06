from prettytable import PrettyTable
import numpy as np

def amino_acid_content(filename):
    # returns a list with percentage content of amino acids

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

amino_acids = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T','X','Z','B','U','O']

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']
true_labels = {'ecoli' : 'E. coli', 'elegans' : 'C. elegans', 'human' : 'H. sapiens',
               'melanogaster' : 'D. melanogaster', 'mouse' : 'M. musculus',
               'subtilis' : 'B. subtilis', 'thaliana' : 'A. thaliana', 'yeast' : 'S. cerevisiae',
               'zebrafish' : 'D. rerio'}

contents = []

for label in labels:
    contents.append(amino_acid_content('hw2/data_' + label + '.fasta'))

    
    
# builds table
x = PrettyTable()
x.title = 'Amino acid percentage content in proteins of given proteomes'
x.field_names = ['amino acid', true_labels['ecoli'], true_labels['elegans'], true_labels['human'],
                 true_labels['melanogaster'], true_labels['mouse'], true_labels['subtilis'],
                 true_labels['thaliana'], true_labels['yeast'], true_labels['zebrafish']]

# sorts plot data
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
