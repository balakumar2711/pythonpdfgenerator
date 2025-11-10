from fpdf import FPDF
import pandas as pd

#Create the initial layout
pdf = FPDF(orientation= "P", unit="mm", format="A4")

#Set this so that the page break happens and line break works
pdf.set_auto_page_break(auto=False)

#Pandas method to read the csv file
df= pd.read_csv("topics.csv")

#iterate over the CSV file
for index, item in df.iterrows():

    #Defines the header
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=24)
    pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="L")

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    #Set the footer for the first page
    pdf.ln(278)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="R")

    #Iterate over the range of pages on the CSV
    for i in range(item["Pages"]-1):
        #Create the header
        pdf.add_page()

        #Set the footer
        pdf.ln(278)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

#Saves and creates the pdf required
pdf.output("Linedpdf.pdf")