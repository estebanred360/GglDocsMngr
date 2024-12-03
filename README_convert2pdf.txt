1. python-docx
Ce module permet de créer et de manipuler des documents Microsoft Word (.docx).

Installation

pip install python-docx
Exemple d'utilisation

from docx import Document

# Créer un nouveau document
doc = Document()

# Ajouter un titre
doc.add_heading('Titre du Document', level=1)

# Ajouter un paragraphe
doc.add_paragraph('Ceci est un paragraphe de texte.')

# Ajouter une liste à puces
doc.add_paragraph('Élément 1', style='List Bullet')
doc.add_paragraph('Élément 2', style='List Bullet')
doc.add_paragraph('Élément 3', style='List Bullet')

# Ajouter un tableau
table = doc.add_table(rows=2, cols=2)
table.cell(0, 0).text = 'Colonne 1'
table.cell(0, 1).text = 'Colonne 2'
table.cell(1, 0).text = 'Ligne 1, Colonne 1'
table.cell(1, 1).text = 'Ligne 1, Colonne 2'

# Enregistrer le document
doc.save('mon_document.docx')
2. reportlab
Ce module permet de créer des documents PDF.

Installation

pip install reportlab
Exemple d'utilisation

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Créer un nouveau document PDF
c = canvas.Canvas("mon_document.pdf", pagesize=letter)

# Ajouter du texte
c.drawString(100, 750, "Titre du Document")
c.drawString(100, 730, "Ceci est un paragraphe de texte.")

# Enregistrer le document
c.save()
3. pandas et openpyxl
Ces modules permettent de créer et de manipuler des feuilles de calcul Excel (.xlsx).

Installation

pip install pandas openpyxl
Exemple d'utilisation

import pandas as pd

# Créer un DataFrame
data = {
    'Colonne 1': ['Valeur 1', 'Valeur 2'],
    'Colonne 2': ['Valeur 3', 'Valeur 4']
}
df = pd.DataFrame(data)

# Enregistrer le DataFrame dans un fichier Excel
df.to_excel('mon_document.xlsx', index=False)
4. Pypandoc
Ce module permet de convertir des documents entre différents formats (Markdown, HTML, PDF, etc.) en utilisant Pandoc.

Installation

pip install pypandoc
Exemple d'utilisation

import pypandoc

# Convertir un fichier Markdown en PDF
output = pypandoc.convert_file('mon_document.md', 'pdf', outputfile="mon_document.pdf")
assert output == ""
Conclusion
Le choix du module dépend du type de document que vous souhaitez générer. Pour des documents Word, 
python-docx est le choix le plus courant. Pour des PDF, reportlab est très puissant. Pour des feuilles de 
calcul Excel, pandas et openpyxl sont souvent utilisés ensemble. Enfin, pour des conversions entre 
différents formats de documents, pypandoc est une excellente option.