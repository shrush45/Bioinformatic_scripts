## Transcribed DNA to RNA

def transcribe(seq):
    rna_seq = ''
    for i in seq.upper():
        if i=='T':
            rna_seq+='U'
        else:
            rna_seq+=i
    return rna_seq

seq = input("Enter a DNA sequence: ")
print("The transcribed RNA sequence is:",transcribe(seq))