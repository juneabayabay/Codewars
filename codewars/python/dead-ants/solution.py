def deadAnts(ants):
    ants = ants.replace("ant", "")
    
    return max(
        ants.count("a"),
        ants.count("n"),
        ants.count("t")
    )