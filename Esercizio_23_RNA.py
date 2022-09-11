def to_rna(dna_strand):
    dna_strand =  dna_strand.replace('A', 'U').replace('T', 'A')
    rna_strand = ''
    for char in dna_strand:
        if char == 'C':
            rep = 'G'
        elif char == 'G':
            rep = 'C'
        else:
            rep = char
        rna_strand += rep
    return rna_strand