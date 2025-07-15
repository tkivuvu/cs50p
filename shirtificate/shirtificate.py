from fpdf import FPDF

class PDF(FPDF):
    def header(self):

        self.set_font("Arial", size=50)

        self.cell(80)

        self.cell(30, 50, "CS50 Shirtificate", align="C")

        self.ln(20)

name = input("Name: ")

pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", x=30, y=60, w=150.622, h=150.368, keep_aspect_ratio=True)
pdf.set_font("Arial", size = 20)
pdf.set_text_color(255, 255, 255)
pdf.cell(200, 150, txt = f"{name} took CS50", ln = True, align = 'C')

pdf.output("shirtificate.pdf")
