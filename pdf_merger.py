"""
Allows user to add multiple pdfs and merge them into a single pdf.
"""

from pypdf import PdfWriter

print("Before merging, make sure all PDFs are named without spaces or special characters.\n")
# Get user input for pdf files to merge
pdf_list = []
user_input = input("Enter the files you want to merge (separated by spaces or commas): ")

# Replace commas with spaces if user used commas
if "," in user_input:
    user_input = user_input.replace(",", " ")

# Split the input string into individual file names
for i in user_input.split(" "):
    if ".pdf" not in i:
        i = i + ".pdf"
    pdf_list.append(i)

print("Files you're attempting to merge: ")
print(", ".join(pdf_list))

merger = PdfWriter()

user_choice = input("Do you want to specify page ranges for each PDF? (yes/no): ")

if user_choice.lower() in ['yes', 'y']:
    for pdf in pdf_list:
        start = input(f"Enter the start page for {pdf} (or 'all' for all pages): ")
        if start.lower() == 'all':
            merger.append(pdf)
            continue
        end = input(f"Enter the end page for {pdf}: ")
        merger.append(pdf, pages=(int(start)-1, int(end)))
else:
    # Append each pdf to the merger
    for pdf in pdf_list:
        merger.append(pdf)
    
merged_pdf = input("Enter the name of the merged pdf (with .pdf extension): ")
    
# Replace spaces with hyphens and adds .pdf in the filename if not present
if " " in merged_pdf:
    merged_pdf = merged_pdf.replace(" ", "-")
if not merged_pdf.endswith(".pdf"):
    merged_pdf = merged_pdf + ".pdf"

    
merger.write(merged_pdf)
merger.close()
print("PDFs merged successfully into " + merged_pdf)
