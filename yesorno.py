# Learning to define functions in Python 3.1

def ask_ok(prompt, retries=4, complaint='Yes or no only please'):
    '''Interactive prompt that asks for a "yes" or "no" answer
and returns True or False'''
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print(complaint)

print(ask_ok("Do you like Python so far?"))
