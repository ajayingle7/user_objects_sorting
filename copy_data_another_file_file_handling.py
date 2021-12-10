fh = open("text1.txt","r")

data = fh.read()
fh.close()

#copy in another file

nf = open("text2.txt","w")

nf.write(data)

nf.close()






