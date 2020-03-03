from prettytable import PrettyTable

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

labels = ['ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']

contents = []

for label in labels:
    contents.append(amino_acid_content('hw2/data_' + label + '.fasta'))

x = PrettyTable()

x.field_names = ['amino acid','ecoli', 'elegans', 'human', 'melanogaster', 'mouse', 'subtilis', 'thaliana', 'yeast', 'zebrafish']

for i in range(len(amino_acids)):
    row = []
    row.append(amino_acids[i])
    for j in range(len(contents)):
        row.append(str(contents[j][i]) + ' %')
    x.add_row(row)

print(x)