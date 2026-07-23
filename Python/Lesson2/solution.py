def multiple_of_index(arr):
    result = []
    
    for index, value in enumerate(arr):
        if index == 0:
            if value == 0:
                result.append(value)
            continue
            
        if value % index == 0:
            result.append(value)
            
    return result