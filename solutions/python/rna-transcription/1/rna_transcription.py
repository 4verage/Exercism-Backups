def to_rna(dna_strand):
    # Prepare a new RNA Strand
    rna = ""

    # Dict for complements
    complements = { "G": "C", "C": "G", "T": "A", "A": "U" }

    # Generate sequence
    for nt in dna_strand:
        rna += complements[nt]

    # Return completed RNA Sequence
    return rna
    