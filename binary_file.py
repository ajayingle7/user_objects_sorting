bf = open("abc.jpg","rb")
data = bf.read()

bf.close()


nbf = open("abcd.jpg","wb")
nbf.write(data)

nbf.close()
