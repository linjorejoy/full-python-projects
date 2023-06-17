#!/usr/bin/env python3
# -*- coding: utf-8 -*-


f = open("MyFile.txt","w")

f.write("Hello")
f.write(" ")
#f.write("1") #str(1) -> "1"
f.close()

f = open("MyFile.txt","a")
f.write("World")
f.write(" Again")
f.write("\n")
f.close()

f = open("MyFile.txt","r")
line = f.readline()
print(line)

print(line.strip("\n"))
print(line.strip("\n").split(" "))
print(line)
print(int("1")) #int("1") -> 1
f.close()

with open("MyFile.txt","r") as f:
    line2 = f.readline()
    print(line2)
    
print(f.readline())
    