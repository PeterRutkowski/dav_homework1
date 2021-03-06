# download data from UniProt

import os
import random

folder_name = 'Archaea' # possible folder names: Archaea, Bacteria, Eukaryota, Viruses
# download each folder one by one and save files in data/uniprot_<foldername in lowercase>/
# for example: data/uniprot_archaea/

target_url = 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/'+ folder_name +'/'

# calculate how many supported fasta files there are
import urllib.request
counter = 0
for line in urllib.request.urlopen(target_url):
    if line.decode('utf-8')[-12] != 'A':
        if line.decode('utf-8')[-10] == 'f':
            counter = counter + 1

# choose random 200 indices
l = random.sample(range(counter), 200)
print(len(l))
l.sort()

# download 200 files with indices generated above
counter = 0
i = 0
for line in urllib.request.urlopen(target_url):
    if line.decode('utf-8')[-12] != 'A':
        if line.decode('utf-8')[-10] == 'f':
            if l[i] == counter:
                os.system('wget '+ target_url + str(line.decode('utf-8')[56:-2]))
                i = i + 1
                if i == 200:
                    break
            counter = counter + 1
