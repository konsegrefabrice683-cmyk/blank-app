import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V21.1 PRONO", layout="wide")
st.title("FABRICE V21.1 - PRONO + JOUR INFINI")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 5

if st.button("➕ +3 JOURS INFINIS"):
    st.session_state.nb_jours += 3
    st.rerun()

def get_label(j, d):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds}"
    if j==1: return f"DEMAIN - {ds}"
    return f"JOUR +{j} - {ds}"

today = datetime.now()
tab_paris, tab_pmu, tab_bourse = st.tabs(["PARIS INFINI", "PMU-B", "BOURSE"])

with tab_paris:
    type_paris = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], key="paris_menu")
    
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(f"{get_label(j, dj)} - {type_paris}", expanded=(j==0)):
            
            if type_paris == "Double Chance":
                df = pd.DataFrame([
                    ["Brest vs Nice", "1X", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
                    ["Mamelodi vs Wiliete", "1X", 1.55, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
                    ["Real Madrid vs Barca", "X2", 1.45, "72%", "+5.5%", 76.5, "FEU VERT ULTRA"],
                    ["Man City vs Arsenal", "12", 1.52, "70%", "+4.8%", 74.2, "FEU VERT"],
                    ["Bayern vs Dortmund", "1X", 1.28, "82%", "+5.1%", 77.8, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "X2", 1.22, "85%", "+4.2%", 76.2, "FEU VERT ULTRA"],
                    ["Inter vs Milan", "1X", 1.48, "69%", "+4.5%", 72.8, "FEU VERT"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            elif type_paris == "BTTS Oui/Non":
                df = pd.DataFrame([
                    ["Brest vs Nice", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
                    ["Real vs Barca", "BTTS Oui", 1.65, "70%", "+6.5%", 76.2, "FEU VERT ULTRA"],
                    ["City vs Arsenal", "BTTS Non", 1.80, "63%", "+5.2%", 73.1, "FEU VERT"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            elif type_paris == "Over/Under":
                df = pd.DataFrame([
                    ["Brest vs Nice", "Over 1.5", 1.34, "82%", "+5.2%", 77.2, "FEU VERT ULTRA"],
                    ["Al-Ahli vs Khaleej", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
                    ["Real vs Barca", "Under 3.5", 2.85, "38%", "+4.2%", 70.1, "FEU VERT"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            elif type_paris == "Score Exact":
                df = pd.DataFrame([
                    ["Brest vs Nice", "2-1", 8.50, "12%", "+8.5%", 68.2, "FEU VERT"],
                    ["Real vs Barca", "2-1", 9.00, "11%", "+7.8%", 69.2, "FEU VERT"],
                    ["City vs Arsenal", "1-0", 7.50, "13%", "+6.5%", 68.8, "FEU VERT"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            elif type_paris == "Cartons":
                df = pd.DataFrame([
                    ["Brest vs Nice", "Over 3.5 Cartons", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
                    ["Real vs Barca", "Over 4.5 Cartons", 1.90, "66%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            elif type_paris == "Corners":
                df = pd.DataFrame([
                    ["Brest vs Nice", "Over 8.5 Corners", 1.75, "68%", "+4.1%", 71.2, "FEU VERT"],
                    ["Real vs Barca", "Over 9.5 Corners", 1.85, "65%", "+5.5%", 74.5, "FEU VERT ULTRA"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            else:
                df = pd.DataFrame([
                    ["Brest vs Nice", "1", 2.45, "62%", "+5.5%", 76.2, "FEU VERT"],
                ], columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            
            st.dataframe(df, width='stretch')
            st.code(f"TICKET {type_paris}: {get_label(j,dj)}")
