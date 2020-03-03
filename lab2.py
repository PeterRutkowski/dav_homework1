import matplotlib.pyplot as plt
import numpy as np

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

    av, std = np.average(lengths), np.std(lengths)

    return av, std

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']

avs = []
stds = []

for i in range(len(labels)):
    av, std = average_protein_length('hw2/data_' + labels[i] + '.fasta')
    avs.append(av)
    stds.append(std)

print(avs)
sorted_ind = np.argsort(avs)
print(sorted_ind)
sorted_avs = []
sorted_labels = []
sorted_std =[]
for i in range(len(sorted_ind)):
    sorted_avs.append(avs[sorted_ind[i]])
    sorted_labels.append(labels[sorted_ind[i]])
    sorted_std.append(stds[sorted_ind[i]])

def generate_content_plot(avs, ac_types):
    labels = ac_types

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, avs, width, label='Text ')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Text')
    ax.set_title('Text ')
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

    plt.savefig('plots/' + 'protein_length' + '.png')
    plt.close(fig)

def plot2(avs, label, errors):
    # Build the plot
    x_pos = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.bar(x_pos, avs, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Average protein length')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title('Average protein lengths of various proteomes')
    ax.yaxis.grid(True)

    ax.legend(['protein length'])

    # Save the figure and show
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/' + 'protein_length2' + '.png')
    plt.close(fig)

generate_content_plot(sorted_avs, sorted_labels)
plot2(sorted_avs, sorted_labels, sorted_std)