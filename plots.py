# generates plots of amino acid contents of proteomes

import matplotlib.pyplot as plt
import numpy as np

def import_amino_acid_content(filename):
    with open(filename) as f:
        l = [line.rstrip() for line in f]

    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def import_amino_acid_contents():
    archaea = import_amino_acid_content('uniprot_archaea.txt')
    bacteria = import_amino_acid_content('uniprot_bacteria.txt')
    eukaryota = import_amino_acid_content('uniprot_eukaryota.txt')
    viruses = import_amino_acid_content('uniprot_viruses.txt')
    full = import_amino_acid_content('uniprot_full.txt')

    return archaea, bacteria, eukaryota, viruses, full

def generate_content_plot(l1, l2, l3, l4, l5, ac_types, i):
    labels = ['Archaea', 'Bacteria', 'Eucaryota', 'Viruses', 'Various (SwissProt)']
    aminoacid_content = [l1[i], l2[i], l3[i], l4[i], l5[i]]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, aminoacid_content, width, label='Quantity of amino acid ' + ac_types[i])

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('# of type ' + ac_types[i] + ' amino acids in 200 proteomes of given type')
    ax.set_title('Quantity of amino acid ' + ac_types[i])
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    # ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)

    fig.tight_layout()

    plt.savefig('plots/' + ac_types[i] + '.png')
    plt.close(fig)

archaea, bacteria, eukaryota, viruses, full = import_amino_acid_contents()

amino_acid_labels = ['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T','X','Z','B','U','O']

def generate_plots(l1, l2, l3, l4, l5, ac_types):
    for i in range(len(ac_types)):
        generate_content_plot(l1, l2, l3, l4, l5, ac_types, i)

generate_plots(archaea, bacteria, eukaryota, viruses, full, amino_acid_labels)
