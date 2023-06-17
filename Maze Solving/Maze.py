from PIL import Image
import pandas as pd
import numpy as np

img = Image.open(r"G:\my works new\Python\Coding challenges\mazesolving-master\mazesolving-master\examples\small - Copy.png")
colourPixels = img.convert("RGB")
# blackWhite = img.convert("BW")
colourArray = np.array(colourPixels.getdata()).reshape(img.size + (3,))
indicesArray = np.moveaxis(np.indices(img.size), 0, 2)
allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 3))


#to save all pixel values to DataFrame
# df = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])
df1 = pd.DataFrame(allArray, columns=['y', 'x', 'value'])
print(df1["value"][2])

impixels = img.load()
print(impixels)
