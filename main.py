from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation= "P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

df= pd.read_csv("topics.csv")

for index, item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=24)
    pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="L")

    pdf.line(10, 20, 200, 20)

    pdf.ln(278)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="R")

    for i in range(item["Pages"]-1):
        pdf.add_page()

        pdf.ln(278)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.cell(w=0, h=12, txt=item["Topic"], border=0, ln=0, align="R")

pdf.output("output.pdf")