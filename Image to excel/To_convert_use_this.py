# Importing Image from PIL package  
from PIL import Image
import pandas as pd
import numpy as np
from numpy import asarray
import xlsxwriter

# creating a image object 
colourImg = Image.open(r"G:\my works new\Python\Image to excel\Screenshot (249).png")
colourPixels = colourImg.convert("RGB")
colourArray = np.array(colourPixels.getdata()).reshape(colourImg.size + (3,))
indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))


#to save all pixel values to DataFrame
df = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])

px = colourPixels.load()
width =colourPixels.size[0]
height =colourPixels.size[1]

#print(colourPixels.size[0])
#print(colourPixels.size[1])

print(colourPixels.mode)

#
data= asarray(colourPixels)
print(data.shape)



#print (df['red'][242])
#print (df['red'][243])
#print (df['red'][244])

#print (df)


#d2Excel = pd.ExcelWriter("G:\my works new\excel\Experiments\Images.xlsx", engine = 'xlsxwriter')
workbook = xlsxwriter.Workbook("G:\my works new\excel\Experiments\Images.xlsx")
worksheet = workbook.add_worksheet("Sheet9")


#df['red'].to_excel(d2Excel, sheet_name='Sheet1')
#d2Excel.save()

print(width)
print(height)


for i in range (0,height):
    for j in range (0,width):
        
        worksheet.write(3*i + 0 , j , df["red"][i*width +j ])
        worksheet.write(3*i + 1 , j , df["green"][i*width +j ])
        worksheet.write(3*i + 2 , j , df["blue"][i*width +j ])
        

        
workbook.close()

