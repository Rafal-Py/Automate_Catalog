#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    #report_info = Paragraph(paragraph, styles["BodyText"])
    report_build = [report_title, empty_line]
    for i, line in enumerate(paragraph.split('\n'), start = 0):
        report_build.append(Paragraph(line, styles["BodyText"]))
        if i > 0 and i % 2 == 0:
            report_build.append(empty_line)
    print(report_build)
    report.build(report_build)
