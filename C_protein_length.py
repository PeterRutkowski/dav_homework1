import matplotlib.pyplot as plt
import numpy as np
import os

def average_protein_length(directory):
    # return average protein length and standard deviation
    lengths = []
    line_length = 0
    for filename in os.listdir(directory):
        if filename[0] != '.':
            f = open(directory + '/' + filename, 'r')
            for line in f:
                if line[0] == '>':
                    if line_length > 0:
                        lengths.append(line_length)
                        line_length = 0
                else:
                    line_length = line_length + len(line) - 1
            f.close()

            if line_length > 0:
                lengths.append(line_length)
                line_length = 0

    av, std = np.average(lengths), np.std(lengths)
    return av, std

labels = ['archaea', 'bacteria', 'eukaryota', 'viruses', 'full']
true_labels = {'archaea' : 'Archaea', 'bacteria' : 'Bacteria', 'eukaryota' : 'Eukaryota',
               'viruses' : 'Viruses', 'full' : 'Various (SwissProt)'}

avs = []
stds = []

for i in range(len(labels)):
    av, std = average_protein_length('data/uniprot_' + labels[i])
    avs.append(av)
    stds.append(std)

# sort data for plotting
sorted_ind = np.argsort(avs)
sorted_avs = []
sorted_labels = []
sorted_std =[]

for i in range(len(sorted_ind)):
    sorted_avs.append(avs[sorted_ind[i]])
    sorted_labels.append(true_labels[labels[sorted_ind[i]]])
    sorted_std.append(stds[sorted_ind[i]])

def plot(avs, labels, errors):
    # build the plot
    x_pos = np.arange(len(labels))
    fig, ax = plt.subplots()
    
    ax.bar(x_pos, avs, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Average protein length')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title('Average protein lengths of given proteomes')
    ax.yaxis.grid(True)
    ax.legend(['protein length'])
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/' + 'C_protein_length' + '.png')
    plt.close(fig)

plot(sorted_avs, sorted_labels, sorted_std)
