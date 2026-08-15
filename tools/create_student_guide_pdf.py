#!/usr/bin/env python3
"""Create the bilingual student sharing guide for the thesis template.

Install the small Arabic text helpers locally before running:
python3 -m pip install --target tmp/pdfs/vendor -r tools/pdf-requirements.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "tmp" / "pdfs" / "vendor"
sys.path.insert(0, str(VENDOR))

import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUTPUT = ROOT / "output" / "pdf" / "UTS_PhD_Thesis_Template_Student_Guide.pdf"
WIDTH, HEIGHT = A4

NAVY = HexColor("#102A43")
BLUE = HexColor("#1E6F9F")
CYAN = HexColor("#35B5C5")
CORAL = HexColor("#EE765E")
CREAM = HexColor("#F7F4ED")
PALE_BLUE = HexColor("#EAF4F7")
PALE_CORAL = HexColor("#FCEDE8")
INK = HexColor("#243B53")
MUTED = HexColor("#627D98")
LINE = HexColor("#D9E2EC")

REPO_URL = "https://github.com/smaq777/uts-thesis-template-community"
CLONE_COMMAND = "gh repo clone smaq777/uts-thesis-template-community"


def register_fonts() -> None:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    pdfmetrics.registerFont(TTFont("Arial", str(font_dir / "Arial.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(font_dir / "Arial Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Arabic", str(font_dir / "Arial Unicode.ttf")))


def rounded_box(c: canvas.Canvas, x: float, y: float, w: float, h: float,
                fill: Color, radius: float = 12, stroke: Color | None = None) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke or fill)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def wrap_text(text: str, font: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_paragraph(c: canvas.Canvas, text: str, x: float, y: float, width: float,
                   font: str = "Arial", size: float = 10.5,
                   leading: float = 15, color: Color = INK) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def shape_ar(text: str) -> str:
    return get_display(arabic_reshaper.reshape(text))


def wrap_arabic(text: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        shaped = shape_ar(candidate)
        if pdfmetrics.stringWidth(shaped, "Arial-Arabic", size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_arabic(c: canvas.Canvas, text: str, right_x: float, y: float,
                width: float, size: float = 11, leading: float = 18,
                color: Color = INK, bold: bool = False) -> float:
    font = "Arial-Bold" if bold else "Arial-Arabic"
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_arabic(text, size, width):
        c.drawRightString(right_x, y, shape_ar(line))
        y -= leading
    return y


def page_header(c: canvas.Canvas, section: str, page: int, arabic: bool = False) -> None:
    c.setFillColor(NAVY)
    c.rect(0, HEIGHT - 42, WIDTH, 42, fill=1, stroke=0)
    c.setFillColor(white)
    if arabic:
        c.setFont("Arial-Arabic", 9)
        c.drawRightString(WIDTH - 36, HEIGHT - 27, shape_ar(section))
    else:
        c.setFont("Arial-Bold", 9)
        c.drawString(36, HEIGHT - 27, section.upper())
    c.setFont("Arial", 9)
    c.drawRightString(WIDTH - 36, 22, str(page))
    c.setStrokeColor(LINE)
    c.line(36, 34, WIDTH - 36, 34)


def title(c: canvas.Canvas, text: str, y: float, subtitle: str | None = None) -> float:
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 24)
    c.drawString(42, y, text)
    y -= 24
    if subtitle:
        y = draw_paragraph(c, subtitle, 42, y, WIDTH - 84, size=10.5,
                           leading=15, color=MUTED)
    return y


def benefit(c: canvas.Canvas, number: str, heading: str, body: str,
            x: float, y: float, w: float) -> None:
    rounded_box(c, x, y - 67, w, 67, white, 10, LINE)
    c.setFillColor(CYAN)
    c.circle(x + 23, y - 23, 12, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 9)
    c.drawCentredString(x + 23, y - 26, number)
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 10.5)
    c.drawString(x + 44, y - 20, heading)
    draw_paragraph(c, body, x + 44, y - 37, w - 55, size=8.5,
                   leading=11, color=MUTED)


def cover(c: canvas.Canvas) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, HEIGHT - 16, WIDTH, 16, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.circle(WIDTH - 65, HEIGHT - 90, 75, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.circle(WIDTH - 25, HEIGHT - 160, 38, fill=1, stroke=0)

    c.setFillColor(BLUE)
    c.setFont("Arial-Bold", 10)
    c.drawString(48, HEIGHT - 92, "COMMUNITY THESIS WORKFLOW")
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 31)
    c.drawString(48, HEIGHT - 148, "A clearer way to write")
    c.drawString(48, HEIGHT - 186, "and manage your PhD thesis")

    draw_paragraph(
        c,
        "A practical, structured workflow for UTS PhD and HDR students, from the first chapter to supervisor review and examiner corrections.",
        48,
        HEIGHT - 226,
        430,
        size=12,
        leading=18,
        color=INK,
    )

    rounded_box(c, 48, HEIGHT - 390, WIDTH - 96, 92, PALE_BLUE, 14)
    c.setFont("Arial-Arabic", 18)
    c.setFillColor(NAVY)
    c.drawRightString(WIDTH - 70, HEIGHT - 330, shape_ar("طريقة أوضح لكتابة وإدارة رسالة الدكتوراه"))
    draw_arabic(
        c,
        "دليل عملي لتنظيم الرسالة، وتتبع التعديلات، ومراجعة المشرف، ومعالجة ملاحظات الممتحنين.",
        WIDTH - 70,
        HEIGHT - 356,
        WIDTH - 140,
        size=11,
        leading=17,
        color=MUTED,
    )

    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 13)
    c.drawString(48, 205, "UTS Thesis Template Community")
    c.setFillColor(MUTED)
    c.setFont("Arial", 9.5)
    c.drawString(48, 184, "Unofficial, community-maintained, and based on a real thesis workflow")

    rounded_box(c, 48, 80, WIDTH - 96, 70, NAVY, 12)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 10)
    c.drawString(66, 125, "THE GOAL")
    c.setFont("Arial", 12)
    c.drawString(66, 101, "Spend less time managing files. Spend more time improving your research.")
    c.showPage()


def english_story(c: canvas.Canvas) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    page_header(c, "Why this template exists", 2)
    y = title(c, "A large thesis quickly becomes hard to manage", HEIGHT - 88)

    y = draw_paragraph(
        c,
        "Writing a thesis is not difficult only because of the research. The document itself becomes a project. Chapters grow, references move, figures change, feedback arrives, and several versions begin circulating.",
        42,
        y - 12,
        WIDTH - 84,
        size=11,
        leading=17,
    )

    rounded_box(c, 42, y - 178, 242, 146, PALE_CORAL, 12)
    c.setFillColor(CORAL)
    c.setFont("Arial-Bold", 12)
    c.drawString(58, y - 58, "The common problem")
    problems = [
        "One large file becomes fragile",
        "Old and new versions get mixed up",
        "Supervisor feedback is difficult to trace",
        "Examiner corrections become another project",
    ]
    py = y - 82
    for item in problems:
        c.setFillColor(CORAL)
        c.circle(61, py + 3, 3, fill=1, stroke=0)
        draw_paragraph(c, item, 72, py, 194, size=9.2, leading=12, color=INK)
        py -= 25

    rounded_box(c, 310, y - 178, 243, 146, PALE_BLUE, 12)
    c.setFillColor(BLUE)
    c.setFont("Arial-Bold", 12)
    c.drawString(326, y - 58, "The structured alternative")
    solutions = [
        "Separate files for each part of the thesis",
        "Git history for every meaningful revision",
        "Clear review outputs for the supervisor",
        "Stable records for examiner responses",
    ]
    sy = y - 82
    for item in solutions:
        c.setFillColor(CYAN)
        c.circle(329, sy + 3, 3, fill=1, stroke=0)
        draw_paragraph(c, item, 340, sy, 194, size=9.2, leading=12, color=INK)
        sy -= 25

    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 18)
    c.drawString(42, y - 225, "What changes in practice")
    benefit(c, "1", "Organise", "Keep chapters, figures, tables, references, and appendices in clear locations.", 42, y - 250, 248)
    benefit(c, "2", "Track", "Use Git and GitHub to record what changed and return to an earlier state.", 305, y - 250, 248)
    benefit(c, "3", "Review", "Give your supervisor a readable review copy with visible corrections.", 42, y - 332, 248)
    benefit(c, "4", "Respond", "Connect each examiner comment to a clear correction and response.", 305, y - 332, 248)

    rounded_box(c, 42, 76, WIDTH - 84, 56, NAVY, 10)
    c.setFillColor(white)
    c.setFont("Arial-Bold", 11)
    c.drawString(58, 109, "The result")
    c.setFont("Arial", 10)
    c.drawString(58, 89, "A thesis that is easier to write, review, correct, and prepare for submission.")
    c.showPage()


def workflow(c: canvas.Canvas) -> None:
    c.setFillColor(white)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    page_header(c, "The workflow", 3)
    title(c, "One workflow from first draft to final correction", HEIGHT - 88,
          "The template turns thesis management into a sequence of small, clear stages.")

    stages = [
        ("01", "Start with structure", "Set your metadata, front matter, chapters, bibliography, figures, tables, and appendices before the document becomes large."),
        ("02", "Write in manageable files", "Work on one chapter or section at a time. The main thesis file brings everything together when you build the PDF."),
        ("03", "Track meaningful changes", "Use a Git branch for a focused revision. Commit a clear checkpoint after building and checking the result."),
        ("04", "Make supervisor review easier", "Produce a clean reading copy and a review copy with visible corrections. Keep sensitive material in a private repository."),
        ("05", "Address examiner comments", "Give every comment a stable ID. Record the correction, its location, and the response. Then generate all three outputs."),
    ]
    y = HEIGHT - 177
    for number, heading, body in stages:
        c.setFillColor(CYAN if number != "05" else CORAL)
        c.circle(68, y - 7, 20, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Arial-Bold", 10)
        c.drawCentredString(68, y - 11, number)
        c.setFillColor(NAVY)
        c.setFont("Arial-Bold", 12)
        c.drawString(103, y, heading)
        draw_paragraph(c, body, 103, y - 19, 430, size=9.2, leading=13, color=MUTED)
        if number != "05":
            c.setStrokeColor(LINE)
            c.setLineWidth(2)
            c.line(68, y - 29, 68, y - 84)
        y -= 102

    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 14)
    c.drawString(42, 151, "Three useful PDF outputs")
    outputs = [
        ("Thesis_CLEAN.pdf", "Final reading copy"),
        ("Thesis_REVIEW.pdf", "Visible corrections for review"),
        ("Revision_Response.pdf", "Comment-by-comment response"),
    ]
    x = 42
    for filename, label in outputs:
        rounded_box(c, x, 72, 163, 58, PALE_BLUE, 9)
        c.setFillColor(BLUE)
        c.setFont("Arial-Bold", 8.5)
        c.drawString(x + 10, 108, filename)
        c.setFillColor(MUTED)
        c.setFont("Arial", 7.8)
        c.drawString(x + 10, 88, label)
        x += 174
    c.showPage()


def arabic_page(c: canvas.Canvas) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    page_header(c, "لماذا أشارك هذا القالب؟", 4, arabic=True)

    c.setFillColor(NAVY)
    c.setFont("Arial-Arabic", 23)
    c.drawRightString(WIDTH - 42, HEIGHT - 95, shape_ar("الفكرة ببساطة"))
    y = draw_arabic(
        c,
        "عندما تكبر رسالة الدكتوراه، لا تصبح الصعوبة في البحث فقط. يصبح الملف نفسه مشروعاً يحتاج إلى إدارة. تتعدد الفصول والمراجع والأشكال والنسخ، ثم تصل ملاحظات المشرف والممتحنين.",
        WIDTH - 42,
        HEIGHT - 128,
        WIDTH - 84,
        size=11.5,
        leading=19,
    )

    rounded_box(c, 42, y - 130, WIDTH - 84, 110, PALE_BLUE, 12)
    c.setFillColor(BLUE)
    c.setFont("Arial-Arabic", 15)
    c.drawRightString(WIDTH - 60, y - 48, shape_ar("لهذا قررت مشاركة نفس طريقة العمل التي استخدمتها"))
    draw_arabic(
        c,
        "الهدف هو توفير وقت إعداد الرسالة، وتنظيم العمل منذ أول فصل، وتسهيل المراجعة مع المشرف، ثم معالجة ملاحظات الممتحنين بوضوح.",
        WIDTH - 60,
        y - 75,
        WIDTH - 120,
        size=10.5,
        leading=17,
        color=INK,
    )

    c.setFillColor(NAVY)
    c.setFont("Arial-Arabic", 18)
    c.drawRightString(WIDTH - 42, y - 176, shape_ar("كيف يساعدك القالب؟"))

    items = [
        "تقسيم الرسالة إلى فصول وملفات يسهل التعامل معها",
        "تنظيم الأشكال والجداول والمراجع والملاحق",
        "تتبع التعديلات والرجوع إلى النسخ السابقة باستخدام GitHub",
        "إعداد نسخة نظيفة ونسخة واضحة لمراجعة المشرف",
        "توثيق كل ملاحظة من الممتحنين وربطها بالتعديل المناسب",
        "إدارة العمل من بداية الكتابة حتى النسخة النهائية",
    ]
    iy = y - 215
    for index, item in enumerate(items, start=1):
        rounded_box(c, 42, iy - 43, WIDTH - 84, 43, white, 8, LINE)
        c.setFillColor(CYAN if index < 6 else CORAL)
        c.circle(WIDTH - 67, iy - 21, 11, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Arial-Bold", 8)
        c.drawCentredString(WIDTH - 67, iy - 24, str(index))
        draw_arabic(c, item, WIDTH - 90, iy - 17, WIDTH - 150,
                    size=10, leading=15, color=INK)
        iy -= 52

    rounded_box(c, 42, 69, WIDTH - 84, 60, NAVY, 10)
    c.setFillColor(white)
    c.setFont("Arial-Arabic", 12)
    c.drawRightString(WIDTH - 60, 106, shape_ar("النتيجة"))
    draw_arabic(c, "وقت أقل لإدارة الملفات، ووقت أكبر لتحسين البحث والكتابة.",
                WIDTH - 60, 85, WIDTH - 120, size=10, leading=14, color=white)
    c.showPage()


def setup_page(c: canvas.Canvas) -> None:
    c.setFillColor(white)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    page_header(c, "Start here", 5)
    title(c, "Open the guide, then build your first PDF", HEIGHT - 88,
          "The repository contains the template, examples, setup instructions, and the full revision workflow.")

    rounded_box(c, 42, HEIGHT - 277, WIDTH - 84, 112, PALE_CORAL, 12)
    c.setFillColor(CORAL)
    c.setFont("Arial-Bold", 12)
    c.drawString(58, HEIGHT - 193, "Repository access notice")
    draw_paragraph(
        c,
        "The repository is currently private. Students need an invitation from the owner before the link or clone command will work. Update this guide when public access is enabled.",
        58,
        HEIGHT - 217,
        WIDTH - 116,
        size=9.8,
        leading=15,
        color=INK,
    )

    steps = [
        ("1", "Get repository access", "Ask the repository owner for access while the project remains private."),
        ("2", "Read the README", "Choose the local VS Code route or the Overleaf route."),
        ("3", "Replace the example content", "Add your own metadata, chapters, references, figures, tables, and appendices."),
        ("4", "Build and inspect", "Run make all, then read every generated PDF before sharing or submitting it."),
    ]
    y = HEIGHT - 318
    for number, heading, body in steps:
        c.setFillColor(CYAN)
        c.circle(59, y - 5, 13, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Arial-Bold", 8.5)
        c.drawCentredString(59, y - 8, number)
        c.setFillColor(NAVY)
        c.setFont("Arial-Bold", 10.5)
        c.drawString(84, y, heading)
        draw_paragraph(c, body, 84, y - 18, 350, size=8.8, leading=12, color=MUTED)
        y -= 64

    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 11)
    c.drawString(42, 255, "GitHub repository")
    c.setFillColor(BLUE)
    c.setFont("Arial", 9.3)
    c.drawString(42, 234, REPO_URL)
    c.linkURL(REPO_URL, (42, 228, 430, 247), relative=0)

    rounded_box(c, 42, 164, 420, 44, NAVY, 8)
    c.setFillColor(white)
    c.setFont("Arial", 9.3)
    c.drawString(56, 181, CLONE_COMMAND)

    widget = qr.QrCodeWidget(REPO_URL)
    bounds = widget.getBounds()
    size = 78
    drawing = Drawing(size, size, transform=[size / (bounds[2] - bounds[0]), 0, 0,
                                             size / (bounds[3] - bounds[1]), 0, 0])
    drawing.add(widget)
    drawing.drawOn(c, WIDTH - 117, 151)

    rounded_box(c, 42, 67, WIDTH - 84, 70, PALE_BLUE, 10)
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 10)
    c.drawString(58, 115, "Important")
    draw_paragraph(
        c,
        "This is an unofficial community template. Current UTS guidance, your faculty requirements, your examination outcome letter, and your supervisor's advice always take priority.",
        58,
        95,
        WIDTH - 116,
        size=8.8,
        leading=13,
        color=INK,
    )
    c.showPage()


def main() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("UTS PhD Thesis Template Student Guide")
    c.setAuthor("UTS Thesis Template Community")
    c.setSubject("Bilingual student guide for a structured thesis writing workflow")
    cover(c)
    english_story(c)
    workflow(c)
    arabic_page(c)
    setup_page(c)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    main()
