# Filename: pickling.py
# Simple program to show the pickle package functions

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
pi = 3.14
g = (shoplist, pi)
pickle.dump(g, f) #dump the object to file
f.close()

del g #we erase our list from memory

# Read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # load the object from the file
f.close()

print(storedlist[0], str(storedlist[1]))
