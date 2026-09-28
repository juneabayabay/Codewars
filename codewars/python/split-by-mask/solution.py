def split_by_mask(string, mask):
    if sum(mask) != len(string):
        return None

    result = []
    start = 0

    for length in mask:
        result.append(string[start:start + length])
        start += length

    return result