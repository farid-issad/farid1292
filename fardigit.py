import PyPDF2
import os

def lire_pdf(chemin_fichier):
    """
    Lit un document PDF et retourne son contenu texte.
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier PDF
        
    Returns:
        str: Le contenu texte du PDF
    """
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(chemin_fichier):
            return f"Erreur: Le fichier {chemin_fichier} n'existe pas."
        
        # Ouvrir le fichier PDF
        with open(chemin_fichier, 'rb') as fichier:
            lecteur_pdf = PyPDF2.PdfReader(fichier)
            
            # Obtenir le nombre de pages
            nombre_pages = len(lecteur_pdf.pages)
            print(f"Le PDF contient {nombre_pages} page(s)")
            
            # Extraire le texte de toutes les pages
            texte_complet = ""
            for numero_page in range(nombre_pages):
                page = lecteur_pdf.pages[numero_page]
                texte_complet += f"\n--- Page {numero_page + 1} ---\n"
                texte_complet += page.extract_text()
            
            return texte_complet
            
    except Exception as e:
        return f"Erreur lors de la lecture du PDF: {str(e)}"

# Exemple d'utilisation
if __name__ == "__main__":
    print("salut")
    print("salut 12")
    print("azul")
    print("\n=== Fonction de lecture PDF ===")
    print("Oui, je peux lire un document PDF!")
    print("Utilisez la fonction lire_pdf('chemin/vers/fichier.pdf') pour lire un PDF.")
    
    # Exemple avec un fichier de test (si disponible)
    fichier_exemple = "exemple.pdf"
    if os.path.exists(fichier_exemple):
        print(f"\nLecture du fichier {fichier_exemple}:")
        contenu = lire_pdf(fichier_exemple)
        print(contenu)
    else:
        print(f"\nPour tester, créez un fichier PDF nommé '{fichier_exemple}' dans ce répertoire.")