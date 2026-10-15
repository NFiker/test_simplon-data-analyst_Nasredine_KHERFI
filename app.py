import plotly.express as px
import pandas as pd

# Chargement des données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


# =============================================
# Graphique 1 (Exemple) - Quantité par région
# =============================================
figure1 = px.pie(données, values='qte', names='region', title='Quantité vendue par région')
figure1.write_html('ventes-par-region.html')
print('ventes-par-region.html généré avec succès !')

# =============================================
# Graphique 2 - Ventes par produit (quantité)
# =============================================
figure2 = px.pie(données, values='qte', names='produit', title='Quantité vendue par produit')
figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# =============================================
# Graphique 3 - Chiffre d'affaires par produit
# =============================================
# Calcul du chiffre d'affaires
données['ca'] = données['prix'] * données['qte']

figure3 = px.pie(données, values='ca', names='produit', title='Chiffre d\'affaires par produit')
figure3.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')