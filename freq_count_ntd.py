#Counting A,C,G,T/U in a DNA/RNA string
#function to count frequency of each nucleotide
def count(seq):
    freq = {}       #dictionary to store the frequency

    if 'U' in seq.upper():
        print("RNA sequence")
        for i in seq.upper():
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
    else:
        print("DNA sequence")
        for i in seq.upper():
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
    return freq

seq = input("Enter a DNA/RNA string:")
print(count(seq))