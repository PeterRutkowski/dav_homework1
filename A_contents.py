import matplotlib.pyplot as plt
import numpy as np

def amino_acid_content(filename):
    # returns a list with percentages of amino acid contents

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

labels = ['ecoli', 'human', 'yeast']
true_labels = {'ecoli' : 'E. coli', 'human' : 'H. sapiens', 'yeast' : 'S. cerevisiae'}
contents = []

for label in labels:
    contents.append(amino_acid_content('hw2/data_' + label + '.fasta'))

sums = np.sum(contents, axis=0)

# indices of sorted data
sorted_ind = np.argsort(sums)

def plot(amino_acids, contents, indexes):
    # builds plot
    ecoli_content = contents[0]
    human_content = contents[1]
    yeast_content = contents[2]

    ecoli_sorted = []
    human_sorted = []
    yeast_sorted = []
    amino_acids_sorted = []

    for i in range(5,len(indexes)):
        ecoli_sorted.append(ecoli_content[indexes[i]])
        human_sorted.append(human_content[indexes[i]])
        yeast_sorted.append(yeast_content[indexes[i]])
        amino_acids_sorted.append(amino_acids[indexes[i]])

    labels = amino_acids_sorted

    x = np.arange(len(labels))  # the label locations
    x = x*1.5
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width, ecoli_sorted, width, label=true_labels['ecoli'])
    ax.bar(x, human_sorted, width, label=true_labels['human'])
    ax.bar(x + width, yeast_sorted, width, label=true_labels['yeast'])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.locator_params(nbins=10, axis='y')
    ax.set_ylabel('% of amino acid in proteins of given proteomes')
    ax.set_title('Amino acid percentage content in proteins of given proteomes')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.tight_layout()
    plt.grid(c='black', which='major' , axis='y', linewidth=0.2)
    plt.savefig('plots/' + 'A_contents' + '.png')
    plt.close(fig)

plot(amino_acids, contents, sorted_ind)
