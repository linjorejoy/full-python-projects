import pandas as pd
import numpy as np

diff_results = "excelfiles/diff.xlsx"
spread_sheets = ["sheet_0.xlsx", "sheet_1.xlsx"]
sheet_names = ["Sheet1", "Sheet2"]

dataframes = {}
comparison = {}

for spreadsheet in spread_sheets:
    dataframes[spreadsheet] = pd.read_excel(f"excelfiles/{spreadsheet}", engine="openpyxl", sheet_name=sheet_names)
    print(type(dataframes[spreadsheet]["Sheet1"]))

with pd.ExcelWriter(diff_results) as writer:
    for index, sheet in enumerate(sheet_names):
        comparison[sheet] = dataframes[spread_sheets[0]][sheet] == dataframes[spread_sheets[1]][sheet]
        rows, cols = np.where(comparison[sheet] == False)
        for row, col in zip(rows, cols):
            dataframes[spread_sheets[0]][sheet].iloc[row, col] = f'{dataframes[spread_sheets[0]][sheet].iloc[row, col]} -> {dataframes[spread_sheets[1]][sheet].iloc[row, col]} '
            dataframes[spread_sheets[0]][sheet].to_excel(writer,index=False,header=True, sheet_name=sheet)





# print(dataframes["sheet_0.xlsx"]["Sheet1"])
# print(dataframes["sheet_0.xlsx"]["Sheet2"])


# df1 = pd.read_excel("excelfiles/sheet_0.xlsx", engine="openpyxl", sheet_name=sheet_names)
# df2 = pd.read_excel("excelfiles/sheet_1.xlsx", engine="openpyxl", sheet_name=sheet_names)

# print(df1[0])
# print(df1[1])

# Sheet 1 Compare

# compare_values_0 = df1[0].values == df2[0].values
# print(compare_values_0)
