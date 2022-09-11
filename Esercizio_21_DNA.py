def distance(strand_a, strand_b):
    cont = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for k, i in zip(strand_a, strand_b) if k != i)