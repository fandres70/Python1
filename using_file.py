# Filename: using_file.py
# Simple program that writes a text into poem.txt
# and reads it back.

poem='''\
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of someone gently rapping, rapping at my chamber door.
"Tis some visitor," I muttered, "tapping at my chamber door---
        Only this, and nothing more."
'''

f = open('poem.txt', 'w') #open for writing
f.write(poem) # write string to text file
f.close()

f = open('poem.txt', 'r') # the option read can be omitted
for line in f:
    print(line, end='')
f.close() 