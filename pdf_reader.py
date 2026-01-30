"""
Module pour lire des documents PDF.
(Module to read PDF documents.)
"""

from pypdf import PdfReader


def read_pdf(pdf_path):
    """
    Lit un document PDF et retourne son contenu texte.
    (Reads a PDF document and returns its text content.)
    
    Args:
        pdf_path (str): Chemin vers le fichier PDF
        
    Returns:
        str: Le texte extrait du PDF
    """
    try:
        # Créer un lecteur PDF
        reader = PdfReader(pdf_path)
        
        # Extraire le texte de toutes les pages
        text = ""
        for page_num, page in enumerate(reader.pages, 1):
            text += f"\n--- Page {page_num} ---\n"
            text += page.extract_text()
        
        return text
    except FileNotFoundError:
        return f"Erreur: Le fichier '{pdf_path}' n'existe pas."
    except Exception as e:
        return f"Erreur lors de la lecture du PDF: {str(e)}"


def get_pdf_info(pdf_path):
    """
    Obtient les informations sur un document PDF.
    (Gets information about a PDF document.)
    
    Args:
        pdf_path (str): Chemin vers le fichier PDF
        
    Returns:
        dict: Dictionnaire contenant les informations du PDF
    """
    try:
        reader = PdfReader(pdf_path)
        
        info = {
            "nombre_de_pages": len(reader.pages),
            "metadata": reader.metadata if reader.metadata else {}
        }
        
        return info
    except FileNotFoundError:
        return {"erreur": f"Le fichier '{pdf_path}' n'existe pas."}
    except Exception as e:
        return {"erreur": f"Erreur lors de la lecture du PDF: {str(e)}"}


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]
        
        print("=== Lecture du PDF ===")
        content = read_pdf(pdf_file)
        print(content)
        
        print("\n=== Informations du PDF ===")
        info = get_pdf_info(pdf_file)
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("Usage: python pdf_reader.py <chemin_vers_pdf>")
        print("Exemple: python pdf_reader.py document.pdf")
