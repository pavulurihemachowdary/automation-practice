import pdfplumber
import pandas as pd

with pdfplumber.open('weather.pdf') as pdf:
    for page in pdf.pages:
        table=page.extract_table()
        #extract the table from the pdf page, use page.extract_table()

df=pd.DataFrame(table[1:],columns=table[0],index=None)
#to read the table, which is of list of list in a dataframe use 
#   pd.DataFrame()

df.to_excel('weather.xlsx',index=None)