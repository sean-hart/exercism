def to_rna(dna_strand):
    transcription_key = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    rna_strand = ''

    for nucleotide in dna_strand:
        if nucleotide not in (transcription_key.keys()):
            raise ValueError

        rna_strand += transcription_key[nucleotide]

    return rna_strand
