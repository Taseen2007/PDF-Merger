"""
Allows user to add multiple pdfs and merge them into a single pdf.
"""

from pypdf import PdfWriter

# Get user input for pdf files to merge
pdf_list = []
user_input = input("Enter the files you want to merge (separated by spaces): ")

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

try:
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

# Handle any exceptions during the merging process
except Exception as e:
    print(f"Error merging PDFs: {e}")






