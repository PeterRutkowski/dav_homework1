# download data from UniProt

import os
import random

folder_name = 'Eukaryota' # possible names: Bacteria, Viruses, Archaea, Eukaryota

target_url = 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/'+ folder_name +'/'

import urllib.request  # the lib that handles the url stuff
counter = 0
for line in urllib.request.urlopen(target_url):
    if line.decode('utf-8')[-12] != 'A':
        if line.decode('utf-8')[-10] == 'f':
            counter = counter + 1

l = random.sample(range(counter), 200)
print(len(l))
l.sort()

counter = 0
i = 0
for line in urllib.request.urlopen(target_url):
    if line.decode('utf-8')[-12] != 'A':
        if line.decode('utf-8')[-10] == 'f':
            if l[i] == counter:
                print(str(i+1) +' / 200')
                #print('wget', target_url + str(line.decode('utf-8')[56:-2]))
                os.system('wget '+ target_url + str(line.decode('utf-8')[56:-2]))
                i = i + 1
                if i == 200:
                    break
            counter = counter + 1
