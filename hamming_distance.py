##Counting point mutations - Hamming distance
from packages.biopackage import valid_seq

def hamming_distance(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    c = 0
    if valid_seq(seq1) == True and valid_seq(seq2) == True:
        for i in range(len(seq1)):
            if seq1[i] == seq2[i]:
                pass
            else:
                c+=1
        return c
    else:
        print("The sequence entered is invalid.")
    
seq1 = input("Enter sequence1:")
seq2 = input("Enter sequence2:")

print("The hamming distance between two sequences is:",hamming_distance(seq1,seq2))