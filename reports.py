#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, title, additional):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_table = Paragraph(additional, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_table, empty_line])
