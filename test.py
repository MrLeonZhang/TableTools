import pandas as pd

excelFilePath = "sampleData\\ball joint tradeoff table.xlsx"

# Read the Excel file
df = pd.read_excel(excelFilePath)

print(df)
