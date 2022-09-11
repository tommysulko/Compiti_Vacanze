def transform(legacy_data):
    legacy_data = legacy_data.upper()
    score = 0
    for char in legacy_data:
        if char in "AEIOULNRST":
            score += 1
        elif char in "DG":
            score += 2
        elif char in "BCMP":
            score += 3
        elif char in "FHVWY":
            score += 4
        elif char == "K":
            score += 5
        elif char in "JX":
            score += 8
        else:
            score += 10
    return score