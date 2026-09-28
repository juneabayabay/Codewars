from preloaded import codons


def translate_with_frame(dna, frames=[1, 2, 3, -1, -2, -3]):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    results = []

    for frame in frames:

        # Use the original DNA for positive frames
        # and the reverse complement for negative frames
        if frame > 0:
            sequence = dna
        else:
            sequence = "".join(complement[base] for base in dna)[::-1]

        # Convert frame 1, 2, 3 into starting positions 0, 1, 2
        start = abs(frame) - 1

        amino_acids = []

        # Read the DNA three characters at a time
        for i in range(start, len(sequence) - 2, 3):
            triplet = sequence[i:i + 3]

            # Convert the codon into its amino acid
            amino_acids.append(codons[triplet])

        # Turn ['R', '*', 'H'] into 'R*H'
        results.append("".join(amino_acids))

    return results