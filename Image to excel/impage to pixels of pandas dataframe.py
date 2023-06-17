# Importing Image from PIL package  
from PIL import Image
import pandas as pd
import numpy as np
from numpy import asarray
#import xlsxwriter

# creating a image object 
colourImg = Image.open(r"G:\my works new\Python\Image to excel\Screenshot (246).png")
colourPixels = colourImg.convert("RGB")


colourArray = np.array(colourPixels.getdata()).reshape(colourImg.size + (3,))
indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))

df = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])

px = colourPixels.load()
print(colourPixels.size)
print(colourPixels.mode)

data= asarray(colourPixels)
print(data.shape)



print (df['red'][2])
print (df)


d2Excel = pd.ExcelWriter("G:\my works new\excel\Experiments\Images.xlsx", engine = 'xlsxwriter')
#workbook = xlsxwriter.Workbook("G:\my works new\excel\Experiments\Images.xlsx")
#worksheet = workbook.add_worksheet("Sheet1")


df['red'].to_excel(d2Excel, sheet_name='Sheet1')
d2Excel.save()

#for i in range (0,colourPixels.size[0]):
    #for j in range (0,colourPixels.size[1]):
        #worksheet.write(3*i + 1 , j , df["red"][i])

        


