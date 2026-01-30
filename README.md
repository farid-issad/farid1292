# farid1292

## Fonctionnalités

Ce projet inclut un module pour lire des documents PDF.

## Installation

Installez les dépendances nécessaires:

```bash
pip install -r requirements.txt
```

## Utilisation

### Lire un document PDF

Pour lire un document PDF et extraire son texte:

```bash
python pdf_reader.py chemin/vers/document.pdf
```

### Utiliser dans votre code Python

```python
from pdf_reader import read_pdf, get_pdf_info

# Lire le contenu d'un PDF
contenu = read_pdf("document.pdf")
print(contenu)

# Obtenir les informations sur un PDF
info = get_pdf_info("document.pdf")
print(f"Nombre de pages: {info['nombre_de_pages']}")
```

## Exemple

Le module peut extraire le texte de toutes les pages d'un document PDF et afficher les métadonnées du document (auteur, date de création, etc.).