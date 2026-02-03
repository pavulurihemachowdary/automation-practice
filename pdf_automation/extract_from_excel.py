import pandas as pd
from fpdf import FPDF,XPos,YPos

df=pd.read_excel('Animal.xlsx')
#to read data into a dataframe from excel, use pd.read_excel()

for i,row in df.iterrows():
    #add the pdf for every row, like creating a new instance for each row
    pdf=FPDF(orientation='P',format='A4',unit='pt')
    pdf.add_page()

    #to add the text, call set_font()
    pdf.set_font(family='times',size=24,style='B')
    pdf.cell(w=0,h=50,text=row['name'],align='C',new_x=XPos.LMARGIN,new_y=YPos.NEXT)

    for column in df.columns[1:]:
        pdf.set_font(family='times',size=15,style='B')
        pdf.cell(w=100,h=25,text=str.capitalize(column)+":")

        pdf.set_font(family='times',size=14)
        pdf.cell(w=100,h=25,text=row[column],new_x=XPos.LMARGIN,new_y=YPos.NEXT)
    
    pdf.output(f"{row['name']}.pdf")


