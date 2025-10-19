from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_pdf_report(query, text):
    os.makedirs("reports", exist_ok=True)
    file_path = f"reports/{query.replace(' ', '_')}_report.pdf"

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [Paragraph(f"<b>Product Story for:</b> {query}", styles['Title']), Spacer(1, 20)]
    story.append(Paragraph(text.replace("\n", "<br/>"), styles['Normal']))
    doc.build(story)

    return file_path
