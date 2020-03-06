import numpy as np
import matplotlib as mpl

mpl.use('agg')

import matplotlib.pyplot as plt

def average_protein_length(filename):
    # returns average protein length from data in filename
    f = open(filename, 'r')

    lengths = []
    line_length = 0
    for line in f:
        if line[0] == '>':
            if line_length > 0:
                lengths.append(line_length)
            line_length = 0
        else:
            line_length = line_length + len(line) - 1

    if line_length > 0:
        lengths.append(line_length)
    f.close()

    np.asarray(lengths)

    return lengths

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']
true_labels = {'ecoli' : 'E. coli', 'elegans' : 'C. elegans', 'human' : 'H. sapiens',
               'melanogaster' : 'D. melanogaster', 'mouse' : 'M. musculus',
               'subtilis' : 'B. subtilis', 'thaliana' : 'A. thaliana', 'yeast' : 'S. cerevisiae',
               'zebrafish' : 'D. rerio'}

for label in labels:

    # Create a figure instance
    fig = plt.figure()
    plt.ylim(0, 1500)

    # Create an axes instance
    ax = fig.add_subplot()
    ax.set_ylabel('Protein length')
    ax.set_title('Box plot of protein lengths of ' + true_labels[label])
    ax.set_xticklabels([true_labels[label]])

    # Create the boxplot
    bp = ax.boxplot(average_protein_length('hw2/data_' + label + '.fasta'), 0,  '')

    # Save the figure
    fig.savefig('plots/D_' + label + '.png')
    plt.close(fig)


#pdb
# Create a figure instance
fig = plt.figure()
plt.ylim(0, 1500)

# Create an axes instance
ax = fig.add_subplot()
ax.set_ylabel('Protein length')
ax.set_title('Box plot of protein lengths of PDB dataset')
ax.set_xticklabels(['PDB dataset'])

# Create the boxplot
bp = ax.boxplot(average_protein_length('data/pdb_seqres.txt'), 0, '')

# Save the figure
fig.savefig('plots/D_' + 'PDB' + '.png')
plt.close(fig)