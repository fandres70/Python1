# This program test Python's read and write abilities

out_file = open("test.txt", "wt")
out_file.write("This text is going out to the file {0}.\nLook at it.".format(out_file.name))
out_file.close()