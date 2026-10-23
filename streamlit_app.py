import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA V16.9 FINAL")
st.markdown("👤 **Créé par : FABRICE**")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA - Par FABRICE")

tab_paris, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

# --- PARIS AVEC MEME MENU QUE TA CAPTURE ---
with tab_paris:
    st.subheader("PARIS LONAB - 7 TYPES")
    type_paris = st.selectbox("Type LONAB", 
        ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], 
        key="paris_menu"
    )
    
    if type_paris == "1X2":
        df = pd.DataFrame([
            ["Brest vs Nice", "Brest Win", 2.45, "62%", "+5.5%", 76.2, "FEU VERT"],
            ["Mamelodi vs Wiliete", "Mamelodi Win", 1.85, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "Raja Win", 1.90, "66%", "+6.2%", 75.5, "FEU VERT ULTRA"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET 1X2: Brest (2.45) + Mamelodi (1.85) = 4.53 -> 13.590F")

    elif type_paris == "Double Chance":
        df = pd.DataFrame([
            ["Brest vs Nice", "1X", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
            ["Mamelodi vs Wiliete", "1X", 1.55, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "1X", 1.68, "65%", "+3.1%", 70.1, "ATTENTE"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET DC: Brest 1X (1.72) + Mamelodi 1X (1.55) = 2.66 -> 7.980F PLUS SUR")

    elif type_paris == "BTTS Oui/Non":
        df = pd.DataFrame([
            ["Brest vs Nice", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
            ["Raja vs El-Kanemi", "BTTS Oui", 1.78, "64%", "+5.1%", 73.4, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "BTTS Oui", 1.72, "68%", "+6.1%", 75.8, "FEU VERT ULTRA"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET BTTS: 1.85 + 1.78 + 1.72 = 5.66 -> 16.980F")

    elif type_paris == "Over/Under":
        df = pd.DataFrame([
            ["Brest vs Nice", "Over 1.5", 1.34, "82%", "+5.2%", 77.2, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Over 3.5", 2.85, "38%",
