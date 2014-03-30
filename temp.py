def count(word, letter):
    c = 0
    for i in word:
        if i == letter: c = c+1
    
    return c
    
print count("banana", "a")

print count("alabama", "a")

