from fpdf import Align, FPDF, XPos, YPos
import PIL
import sys


def main():
    name = get_name()
    create_pdf(name)


def get_name() -> str:
    name = input("Name: ").strip().title()
    return name


def create_pdf(name: str):
    pdf = FPDF()
    pdf.set_font("helvetica", "B", 40)
    pdf.add_page()
    pdf.cell(200, 30, "CS50 Shirtificate", align="C", new_y=YPos.NEXT, center=True)
    pdf.image("shirtificate.png", Align.C, w=180)
    pdf.set_font_size(20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(80, 90)
    pdf.cell(200, 30, f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
