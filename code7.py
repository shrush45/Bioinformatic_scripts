##Finding motif in a DNA string (input: DNA sequence and motif seq)

import streamlit as st

def motif_finder(seq,motif):
    seq = seq.upper()
    motif = motif.upper()
    n = len(motif)
    motif_pos = []
    for i in range(len(seq)):
        m = seq[i:i+n]
        # print(m)
        if m == motif:
            motif_pos.append(i+1)

    return motif_pos

st.title("MOTIF FINDER")
st.caption("This tool finds the morif in a DNA sequence. ")

seq = st.text_input("Enter DNA Sequence:")
motif = st.text_input("Enter Motif Sequence:")

if st.button("Find Motif"):
    result = motif_finder(seq,motif)
    if isinstance(result,list):
        st.success(f"The motif positions are at: {result}")
    else:
        st.error(result)