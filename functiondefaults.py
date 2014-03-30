# Learning how Python deals with default values of
# function parameters

def f(a, L=[]):
    '''This function appends new values to the list'''
    L.append(a)
    return L

# not specifying a list input
print(f(1))
print(f(2))
print(f(3))

# specifying a list input
print(f(1, []))
print(f(2, []))
print(f(3, []))


def g(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return(L)

# not specifying a list input
print(g(1))
print(g(2))
print(g(3))

# specifying a list input
print(g(1, []))
print(g(2, []))
print(g(3, []))
