import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE V17", layout="wide")

st.title("FABRICE EMPIRE MONDIAL ULTRA V17 - MOTEUR JOURS INFINIS")
st.caption("PARIS 15 MATCHS + PMU 8 CHEVAUX + BOURSE 4 ACTIFS | JOURS INFINIS | OUAGA")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 5

EQUIPES = ["Real Madrid","Barca","Man City","Arsenal","Bayern","PSG","Inter","Milan","Brest","Nice","Mamelodi","Raja","EFO","ASFA","ASEC","Wydad","Burkina","Al Ahly","Zamalek","Simba","TP Mazembe","Liverpool","Chelsea","Juventus","Dortmund"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed","Kadiogo Star","Zaka Force","Yennenga","Burkina Star"]
ACTIFS = ["SONATEL","ORANGE","ECOBANK","SGB","NVDA","AAPL","TSLA","BTC","ETH","SOL","GOLD","SILVER"]

def get_label_jour(j, date_obj, suffix):
    ds = date_obj.strftime("%d/%m/%Y")
    if j == 0:
        return f"AUJOURD HUI - {ds} - {suffix}"
    elif j == 1:
        return f"DEMAIN - {ds} - {suffix}"
    elif j == 2:
        return f"APRES DEMAIN - {ds} - {suffix}"
    else:
        return f"JOUR +{j} - {ds} - {suffix}"

col1, col2, col3 = st.columns([2,2,2])
with col1:
    st.metric("Moteur V17", f"{st.session_state.nb_jours} JOURS INFINIS")
with col2:
    if st.button("➕ +3 JOURS INFINIS", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with col3:
    if st.button("♾️ +10 JOURS INFINIS", use_container_width=True, type="primary"):
        st.session_state.nb_jours += 10
        st.rerun()

tabs = st.tabs(["PARIS V17 INFINI", "PMU-B V17 INFINI", "BOURSE V17 INFINI"])

with tabs[0]:
    type_paris = st.selectbox("Type LONAB V17", ["1X2","Double Chance","BTTS Oui/Non","Over/Under","Cartons","Corners","Score Exact"], key="v17_p")
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        label = get_label_jour(j, dj, "15 MATCHS V17")
        with st.expander(label, expanded=(j < 2)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice(EQUIPES)
                while b == a:
                    b = random.choice(EQUIPES)
                match = a + " vs " + b
                if type_paris == "1X2":
                    marche = a + " Win"
                    cote = round(random.uniform(1.6, 3.2), 2)
                elif type_paris == "Double Chance":
                    marche = random.choice(["1X","X2","12"])
                    cote = round(random.uniform(1.3, 1.9), 2)
                elif type_paris == "BTTS Oui/Non":
                    marche = random.choice(["BTTS Oui","BTTS Non"])
                    cote = round(random.uniform(1.7, 2.2), 2)
                elif type_paris == "Over/Under":
                    marche = random.choice(["Over 2.5","Under 2.5","Over 1.5"])
                    cote = round(random.uniform(1.8, 2.3), 2)
                elif type_paris == "Cartons":
                    marche = random.choice(["Over 3.5 Cartons","Over 4.5 Cartons"])
                    cote = round(random.uniform(1.7, 2.4), 2)
                elif type_paris == "Corners":
                    marche = random.choice(["Over 8.5 Corners","Over 9.5 Corners"])
                    cote = round(random.uniform(1.8, 2.2), 2)
                else:
                    marche = random.choice(["1-0","2-1","2-0","1-1"])
                    cote = round(random.uniform(6.0, 12.0), 
