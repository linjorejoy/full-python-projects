f= open ("text.txt","w")
f.write("haaaaaaaaaaaa")
f.close()
f= open("text.txt" ,"a")
f.write("\n hooooooooooooo")
f.close()
f= open ("text.txt","r")
a=f.read()
print a
f.close()
