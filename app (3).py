
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(page_title="Candidature Ivan NFINDA – ESCP", layout="centered")

# HEADER
st.title("📊 Ivan NFINDA")
st.subheader("Candidat – Assistant de recherche en analyses quantitatives")
st.markdown("**Projet Sorbonne Alliance | ESCP Business School**")

# À propos de l'entreprise
st.header("🏛️ À propos de l’ESCP et du projet")
st.markdown("""
Fondée en 1819, **ESCP Business School** est une école de management d’envergure européenne.  
Le **projet Sorbonne Alliance** vise à étudier les liens entre **capitaux sociaux, culturels** et **prospérité nationale**, à travers des **données web, enquêtes et bases socio-économiques internationales**.

Le poste proposé implique :
- Collecte de données web & nettoyage
- Enquêtes de terrain
- Analyse statistique et textuelle
- Construction d’indicateurs et visualisation
""")

# À propos de toi
st.header("🙋‍♂️ Présentation")
st.markdown("""
Étudiant en MBA Big Data & IA, je développe des solutions analytiques au service de la prise de décision.  
Grâce à mes expériences chez **Endo Data, Naturalia, Micropole**, j’ai acquis de solides compétences en :
- **Collecte, traitement et visualisation de données**
- **Analyse statistique, textuelle et automatisation**
- **Création d’outils Power BI et reporting automatisé**

Ce poste est une suite logique de mon parcours 💡
""")

# Compétences métiers
st.header("🧠 Compétences métiers")
skills = {
    'Analyse Statistique': 9,
    'Python / SQL': 9,
    'Power BI (DAX / M)': 8,
    'Visualisation de données': 9,
    'Gestion de projet analytique': 8,
    'Collecte web / Scraping': 7,
    'Communication écrite (FR/EN)': 9,
    'R / Stata': 6
}
df_skills = pd.DataFrame.from_dict(skills, orient='index', columns=['Niveau (sur 10)'])

st.dataframe(df_skills.style.highlight_max(axis=0))

# Graphique
st.subheader("📊 Visualisation des compétences")
fig, ax = plt.subplots()
df_skills.plot(kind='barh', ax=ax)
st.pyplot(fig)

# Expériences
st.header("💼 Expériences clés")
st.markdown("""
**Endo Data – Consultant BI (2023-2024)**  
➡️ Automatisation de reporting, tableaux de bord (Power BI), réduction de 40% du temps de production

**Naturalia – Data Analyst (2023)**  
➡️ Analyse de données textuelles et commerciales pour le marketing

**Micropole – Data Analyst Marketing (2022-2023)**  
➡️ Tableaux de bord stratégiques et indicateurs de performance

**Société Générale – Consultant Data (2021-2022)**  
➡️ Structuration de données brutes pour l’analyse métier
""")

# Téléchargement du CV
st.header("📎 Télécharger mon CV")
with open("CV-NFINDA_ESCP.pdf", "rb") as file:
    st.download_button("📄 Télécharger le CV complet (PDF)", data=file, file_name="NFINDA_Ivan_CV.pdf")

# Contact
st.header("📬 Me contacter")
st.markdown("""
📧 **ivannfinda@gmail.com**  
📱 **06 66 51 58 51**  
🏡 Saint-Germain-en-Laye  
""")
