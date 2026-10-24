import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.3 - TOUT JOURS INFINIS")
st.caption("OUAGA - V16.3 BASE - JOURS INFINIS")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

EQUIPES = ["Brest","Nice","Mamelodi","Raja","Real","Barca","Man City","Arsenal","Bayern","Dortmund","PSG","Lyon","Inter","Milan","EFO","ASFA","ASEC","Wydad","Burkina","Mali"]

def gen_matchs():
    res = []
    for _ in range(15):
        a = random.choice(EQUIPES)
        b = random.choice(EQUIPES)
        while b == a:
            b = random.choice(EQUIPES)
        res.append(a + " vs " + b)
    return res

def gen_paris(matchs, type_p):
    rows = []
    for m in matchs:
        rows.append([m, type_p, 1.85, "65%", "+5%", 75.5, "FEU VERT"])
    return rows

def gen_pmu():
    rows = []
    noms = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed"]
    for i, n in enumerate(noms):
        rows.append([str(i+1), n, round(random.uniform(2,9),1), "25%", 72.0, "VERT"])
    return rows

def gen_bourse():
    rows = []
    noms = ["SONATEL","ORANGE","ECOBANK","SGB","NVDA","BTC","ETH","GOLD"]
    for n in random.sample(noms, 4):
        rows.append([n, random.randint(1000,50000), "+2.5%", 75.0, "ACHETER"])
    return rows

c1,c2 = st.columns(2)
with c1:
    st.metric("Jours", st.session_state.nb_jours)
with c2:
    if st.button("Charger +3 jours infini"):
        st.session_state.nb_jours += 3
        st.rerun()

tab1,tab2,tab3 = st.tabs(["PARIS INFINI","PMU INFINI","BOURSE INFINI"])

today = datetime.now()

with tab1:
    tp = st.selectbox("Type LONAB", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], key="p1")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        ds = dj.strftime("%d/%m/%Y")
        if j==0:
            titre = "AUJOURD HUI - " + ds + " - 15 MATCHS"
        elif j==1:
            titre = "DEMAIN - " + ds + " - 15 MATCHS"
        else:
            titre = "JOUR +" + str(j) + " - " + ds + " - 15 MATCHS"
        with st.expander(titre, expanded=(j<2)):
            matchs = gen_matchs()
            data = gen_paris(matchs, tp)
            df = pd.DataFrame(data, columns=["Match","Marche","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)

with tab2:
    tp2 = st.selectbox("Type PMU", ["Quinte+","Quarte","Tierce","Couple Gagnant","Couple Place","Gagnant","Place"], key="p2")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        ds = dj.strftime("%d/%m/%Y")
        titre = "JOUR " + str(j) + " - " + ds + " - PMU"
        if j==0:
            titre = "AUJOURD HUI - " + ds + " - PMU"
        with st.expander(titre, expanded=(j<1)):
            data = gen_pmu()
            df = pd.DataFrame(data, columns=["Num","Cheval","Cote","Proba","IA","STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.code(titre + " " + tp2 + " 1-7-5")

with tab3:
    tp3 = st.selectbox("Marche", ["BRVM","USA","CRYPTO","OR"], key="p3")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        ds = dj.strftime("%d/%m/%Y")
        titre = "JOUR " + str(j) + " - " + ds + " - BOURSE " + tp3
        if j==0:
            titre = "AUJOURD HUI - " + ds + " - BOURSE " + tp3
        with st.expander(titre, expanded=(j<1)):
            data = gen_bourse()
            df = pd.DataFrame(data, columns=["Actif","Prix","Var","IA","Action"])
            st.dataframe(df, use_container_width=True, hide_index=True)

if st.button("Charger +5 jours pour tout"):
    st.session_state.nb_jours += 5
    st.rerun()
