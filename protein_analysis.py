import os

def average_protein_length(filename):
    # returns average protein length from data in filename
    f = open(filename, 'r')
    sum = 0
    counter = 0
    for line in f:
        if line[0] == '>':
            counter = counter + 1
        else:
            sum = sum + len(line) - 1
    f.close()

    print('sum:', sum)
    print('counter:', counter)
    return sum/counter

def amino_acid_content(aminoacids, filename):
    # returns a dictionary with quantities of amino acids in proteomes
    f = open(filename, 'r')

    j = 0
    for line in f:
        #print(j)
        j = j + 1
        if line[0] != '>':
            #print(line)
            for i in range(len(line)-1):
                aminoacids[line[i]] = aminoacids[line[i]] + 1
    f.close()

    return aminoacids


aminoacids = {
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

dataset = 'viruses' # possibilities: full, archaea, bacteria, eukaryota, viruses
directory = 'data/uniprot_' + dataset

for filename in os.listdir(directory):
    if filename[0] != '.':
        aminoacids = amino_acid_content(aminoacids, directory + '/' + str(filename))

print(aminoacids)

l = []
for aminoacid in aminoacids:
    l.append(aminoacids[aminoacid])
print(l)

with open('uniprot_' + dataset + '.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)
f.close()
