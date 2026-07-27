function dnaStrand(dna) {
    const complement = {
        A: "T",
        T: "A",
        C: "G",
        G: "C"
    };

    return dna
        .split("")
        .map(letter => complement[letter])
        .join("");
}