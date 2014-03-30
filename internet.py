# Downloads the source of a webpage and writes it on test.txt

if __name__ == "__main__":
    from urllib import request
out_file = open("test.txt", 'wb') # the website will return bytes, not text

page = request.urlopen("http://news.bbc.co.uk/")
source = page.read() # if the file was declared as text,
                     # we could add .decode('utf8') at the end.

out_file.write(source)
out_file.close()
page.close
