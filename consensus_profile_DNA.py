## Consensus and Profile
"""
step1 : reading the fasta file 
step2 : extracating sequence lines into a listt
step3 : frequency of each index position to make the profile for ACGT
"""
import numpy as np

def consensus_profile(filepath):
    seqs = []
    with open(filepath,"r") as f:
        data = f.readlines()
        for line in data:
            if line.startswith('>')==False:
                # print(line)
                seqs.append(line.strip())
    matrix = []
    for seq in seqs:
        print(seq)
        for i in seq:
            matrix.append(i)
    print(matrix)
    M = np.array(matrix).reshape(len(seqs),len(seqs[0]))
    print(M)


    
filepath = "seq.fasta"
print(consensus_profile(filepath))

