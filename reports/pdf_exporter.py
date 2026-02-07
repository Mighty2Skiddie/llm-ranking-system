

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def create_pdf_report(report_data, output_path="output/assignment.pdf"):
    
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    
    elements = []
    
   
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    
    title = Paragraph("LLM COMPARISON AND RANKING REPORT", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
   
    elements.append(Paragraph("Overall Rankings", heading_style))
    
    ranking_data = [["Rank", "Model", "Score", "Comfort Level"]]
    for rank, model_name, score in report_data["rankings"]:
        comfort = report_data["models"][model_name]["comfort_level"]
        ranking_data.append([f"#{rank}", model_name, f"{score}/10", comfort])
    
    ranking_table = Table(ranking_data, colWidths=[0.8*inch, 2*inch, 1.2*inch, 1.5*inch])
    ranking_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    
    elements.append(ranking_table)
    elements.append(Spacer(1, 0.4*inch))
    
    # Add detailed analysis for each model
    elements.append(Paragraph("Detailed Model Analysis", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    for rank, model_name, score in report_data["rankings"]:
        model_info = report_data["models"][model_name]
        
        # Model header
        model_header = Paragraph(f"<b>#{rank}. {model_name}</b> (Score: {score}/10)", 
                                 styles['Heading3'])
        elements.append(model_header)
        
        # Create table with advantages and disadvantages
        detail_data = [
            ["Category", "Details"],
            ["Advantages", "\n".join([f"• {adv}" for adv in model_info["advantages"]])],
            ["Disadvantages", "\n".join([f"• {dis}" for dis in model_info["disadvantages"]])],
            ["Justification", get_ranking_justification_text(rank, model_name)]
        ]
        
        detail_table = Table(detail_data, colWidths=[1.5*inch, 5.5*inch])
        detail_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#ecf0f1')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        
        elements.append(detail_table)
        elements.append(Spacer(1, 0.3*inch))
    
    
    doc.build(elements)
    
    return output_path


def get_ranking_justification_text(rank, model_name):
   
    from core.ranker import get_ranking_justification
    return get_ranking_justification(rank, model_name)