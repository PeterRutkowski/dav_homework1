import matplotlib.pyplot as plt
import numpy as np
import os

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

    counter = 0
    for filename in os.listdir(directory):
        if filename[0] != '.':
            counter += 1
            if counter == 11:
                break
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
               'viruses' : 'Viruses', 'full' : 'Various (SwissProt)'}

contents = []

for label in labels:
    print(label)
    contents.append(amino_acid_content('data/uniprot_' + label))

def plot(amino_acids, contents):
    # build the plot
    archaea_content = contents[0]
    bacteria_content = contents[1]
    eukaryota_content = contents[2]
    viruses_content = contents[3]
    full_content = contents[4]
    
    # sort data for plotting
    sums = np.sum(contents, axis=0)
    sorted_ind = np.argsort(sums)
    
    labels = []
    archaea_sorted = []
    bacteria_sorted = []
    eukaryota_sorted = []
    viruses_sorted = []
    full_sorted = []

    for i in range(5, len(sorted_ind)):
        labels.append(amino_acids[sorted_ind[i]])
        archaea_sorted.append(archaea_content[sorted_ind[i]])
        bacteria_sorted.append(bacteria_content[sorted_ind[i]])
        eukaryota_sorted.append(eukaryota_content[sorted_ind[i]])
        viruses_sorted.append(viruses_content[sorted_ind[i]])
        full_sorted.append(full_content[sorted_ind[i]])

    x = np.arange(len(labels))  # the label locations
    x = x*7
    width = 1.0  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - 2*width, archaea_sorted, width, label='ecoli')
    ax.bar(x - width, bacteria_sorted, width, label='human')
    ax.bar(x, eukaryota_sorted, width, label='yeast')
    ax.bar(x + width, viruses_sorted, width, label='yeast')
    ax.bar(x + 2*width, full_sorted, width, label='yeast')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.locator_params(nbins=10, axis='y')
    ax.set_ylabel('% of amino acid in proteins of given proteomes')
    ax.set_title('Amino acid percentage content in proteins of given proteomes')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.tight_layout()
    plt.grid(c='black', which='major' , axis='y', linewidth=0.2)
    plt.savefig('plots/' + 'C_contents' + '.png')
    plt.close(fig)

plot(amino_acids, contents)
