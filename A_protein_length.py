import matplotlib.pyplot as plt
import numpy as np

def average_std_calculator(filename):
    # return average protein length and their standard deviation from data in filename
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

    av, std = np.average(lengths), np.std(lengths)

    return av, std

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']
true_labels = {'ecoli' : 'E. coli', 'elegans' : 'C. elegans', 'human' : 'H. sapiens',
               'melanogaster' : 'D. melanogaster', 'mouse' : 'M. musculus',
               'subtilis' : 'B. subtilis', 'thaliana' : 'A. thaliana', 'yeast' : 'S. cerevisiae',
               'zebrafish' : 'D. rerio'}
avs = []
stds = []

for i in range(len(labels)):
    av, std = average_std_calculator('hw2/data_' + labels[i] + '.fasta')
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
    plt.savefig('plots/' + 'A_protein_length' + '.png')
    plt.close(fig)

plot(sorted_avs, sorted_labels, sorted_std)
