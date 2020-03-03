import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

amino_acids = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T','X','Z','B','U','O']

labels = ['ecoli', 'human', 'yeast']

contents = []

for label in labels:
    contents.append(amino_acid_content('hw2/data_' + label + '.fasta'))


def plot(amino_acids, contents):
    labels = amino_acids
    ecoli_content = contents[0]
    human_content = contents[1]
    yeast_content = contents[2]

    x = np.arange(len(labels))  # the label locations
    x = x*1.5
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, ecoli_content, width, label='ecoli')
    rects2 = ax.bar(x, human_content, width, label='human')
    rects3 = ax.bar(x + width, yeast_content, width, label='yeast')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.locator_params(nbins=10, axis='y')
    ax.set_ylabel('% of amino acid content in given proteins')
    ax.set_title('Amino acid percentage content')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    #def autolabel(rects):
    #    """Attach a text label above each bar in *rects*, displaying its height."""
    #    for rect in rects:
    #        height = rect.get_height()
    #        ax.annotate('{}'.format(height),
    #                    xy=(rect.get_x() + rect.get_width(), height),
    #                    xytext=(0, 3),  # 3 points vertical offset
    #                    textcoords="offset points",
    #                    ha='center', va='bottom')


    #autolabel(rects1)
    #autolabel(rects2)
    #autolabel(rects3)

    plt.tight_layout()
    plt.grid(c='black', which='major' , axis='y', linewidth=0.2)
    plt.savefig('plots/' + 'lab23' + '.png')
    plt.close(fig)

cut_contents = []
for i in range(len(contents)):
    cut_contents.append(contents[i][:20])

cut_amino_acids = amino_acids[:20]


plot(cut_amino_acids, cut_contents)