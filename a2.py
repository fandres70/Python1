def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return len(dna)

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    return len(dna1) > len(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''

    return dna2 in dna1

def is_valid_sequence(dna):
    '''(str) -> bool

    Returns True if dna contains only 'A', 'T', 'C', or 'G'.
    
    >>> is_valid_sequence('ATTCG')
    True
    >>> is_valid_sequence('AGO')
    False
    >>> is_valid_sequence('atCG')
    False
    '''

    is_valid = True
    i = 0
    while is_valid and (i < len(dna)):
        is_valid = (dna[i] in 'ATCG')
        i = i + 1
    return is_valid

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    Return string formed by inserting dna2 into dna1 before position
    indicated by index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('GCTT', 'A', 0)
    'AGCTT'
    >>> insert_sequence('TTTC', 'GAG', 4)
    'TTTCGAG'
    '''
    #Not suse if slicing is a str method. Uncomment for more elegant solution.
    #return dna1[:index] + dna2 + dna1[index:]

    if not (index < len(dna1)):
        return dna1 + dna2

    i = 0
    result_sequence = ''
    
    while (i < len(dna1)):
        if i == index:
            result_sequence = result_sequence + dna2
        result_sequence = result_sequence + dna1[i]
        i = i + 1
    return result_sequence
    
def get_complement(nucleotide):
    '''(str) -> str

    Returns the complement of nucleotide.

    Prerequisite: nucleotide can only be 'A', 'T', 'C', or 'G'.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    '''

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    
def get_complementary_sequence(sequence):
    '''(str) -> str

    Returns the complementary string of nucleotides
    to sequence.

    Prerequisites: sequence only contains 'A', 'T', 'C', or 'G'.
    
    >>> get_complementary_sequence('CCATGG')
    'GGTACC'
    >>> get_complementary_sequence('AGCTT')
    'TCGAA'
    >>> get_complementary_sequence('TTT')
    'AAA'
    '''
    
    complementary_seq = ''

    for nucleotide in sequence:
        complementary_seq = complementary_seq + get_complement(nucleotide)
    return complementary_seq

    
