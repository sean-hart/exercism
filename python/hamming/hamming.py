def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not the same length')
    if strand_a == strand_b:
        return 0

    distance = 0
    location = 0
    for nucleotide in strand_a:
        if nucleotide != strand_b[location]:
            distance += 1
        location += 1

    return distance

# These are roughly the same speed
def distance2(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not the same length')
    if strand_a == strand_b:
        return 0

    distance = 0
    for (a, b) in zip(strand_a, strand_b):
        if a != b:
            distance += 1

    return distance

def distance3(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strand length mismatch')

    return sum(a != b for a, b in zip(strand_a, strand_b))



if __name__ == '__main__':
    import timeit
    print(timeit.timeit(
        'distance("GGACTGA", "GGACTGC")',
        setup="from __main__ import distance"
        )
    )
    print(timeit.timeit(
        'distance2("GGACTGA", "GGACTGC")',
        setup="from __main__ import distance2"
        )
    )
    print(timeit.timeit(
        'distance3("GGACTGA", "GGACTGC")',
        setup="from __main__ import distance3"
        )
    )
