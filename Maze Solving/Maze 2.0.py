from PIL import Image
import numpy as np

im = Image.open(r"G:\my works new\Python\Coding challenges\mazesolving-master\mazesolving-master\examples\small - Copy.png")
maze = np.asarray(im)
width, height = im.size
print(maze)
print (width)
print (height)

for i in range(width):
    if(maze[0][i] == 1):
        start = [0,i]
for i in range(width):
    if(maze[height-1][i] == 1):
        end = [height-1,i]
print (start)
print (end)

currCell = start
mazepath = [start]
print(mazepath)

def possible(maze,dir):
    

while True:
    if currCell == end:
        break


