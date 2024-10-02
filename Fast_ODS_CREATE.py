from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P
from odf.style import Style, TextProperties, TableCellProperties

# Create a new ODS document
doc = OpenDocumentSpreadsheet()

# Create a new table
table = Table(name="Monthly Payments")
doc.spreadsheet.addElement(table)

# Define styles for headers and cells
header_style = Style(name="HeaderStyle", family="table-cell")
header_style.addElement(TextProperties(fontweight="bold", fontsize="12pt", color="#FFFFFF"))
header_style.addElement(TableCellProperties(backgroundcolor="#4F81BD"))
doc.styles.addElement(header_style)

cell_style = Style(name="CellStyle", family="table-cell")
cell_style.addElement(TextProperties(fontsize="10pt"))
doc.styles.addElement(cell_style)

# Define the header row
header_row = TableRow()
headers = ["Referente", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
"Novembro", "Dezembro", "Total"]
for header in headers:
    cell = TableCell()
    cell.setAttribute("stylename", "HeaderStyle")  # Set the header style
    cell.addElement(P(text=header))
    header_row.addElement(cell)
table.addElement(header_row)

# Define services and example monthly payments
services = [
    ("CAIXA HAB", []),
    ("RGE", []),
    ("COND/AGUA", []),
    ("INTERNET", []),
    ("OUTRO", []),
]

# Add service rows with monthly payments and total
for service, payments in services:
    row = TableRow()
    cell = TableCell()
    cell.setAttribute("stylename", "CellStyle")  # Set the cell style for service name
    cell.addElement(P(text=service))
    row.addElement(cell)

    total = 0
    for payment in payments:
        cell = TableCell()
        cell.setAttribute("stylename", "CellStyle")  # Set the cell style for payments
        cell.addElement(P(text=str(payment)))
        row.addElement(cell)
        total += payment

    # Add the total cell
    total_cell = TableCell()
    total_cell.setAttribute("stylename", "CellStyle")  # Set the cell style for total
    total_cell.addElement(P(text=str(total)))
    row.addElement(total_cell)

    # Add the row to the table
    table.addElement(row)

# Save the document
doc.save("monthly_payments.ods")
