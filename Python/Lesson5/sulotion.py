def expression_matter(a, b, c):
    # Return the largest value from all possible valid expressions
    return max(
        a + b + c,     
        a * b * c,   
        (a + b) * c,   
        a * (b + c),  
        a + b * c,   
        a * b + c      
    )
