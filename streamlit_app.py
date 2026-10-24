import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA - TOUT INFINI")
st.caption("OUAGA")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

EQUIPES = ["Brest","Nice","Mamelodi","Raja","Real","Barca","Man City","Arsenal","Bayern","Dortmund","PSG","Lyon","Inter","Milan","Al Hilal","Al Nassr","EFO","ASFA","ASEC","Wydad","Burkina","Mali","Al Ahly","Zamalek","Simba","Yanga"]

CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed","Kadiogo Star","Mogho Rapide"]

def gen_matchs():
    res = []
    for _ in range(15):
        a = random.choice(EQUIPES)
        b = random.choice([x for x in EQUIPES if x != a])
        res.append(a + " vs " + b)
    return res

def gen_pmu():
    rows = []
    for i in range(8):
        ch = CHEVAUX[i]
        cote = round(random.uniform(1.8, 12.0), 1)
        rows.append([str(i+1), ch, cote])
    return rows

def gen_bourse():
    rows = []
    actifs = ["SONATEL","ORANGE","ECOBANK","SGB","NVDA","AAPL","BTC","ETH","GOLD","SILVER"]
    for act in random.sample(actifs, 4):
        prix = random.randint(1000, 80000)
        var = "+" + str(round(random.uniform(1,8),1)) + "%"
        rows.append([act, prix, var])
    return rows

c1, c2 = st.columns(2)
with c1:
    st.metric("Jours", st.session_state.nb_jours)
with c2:
    if st.button("Charger +3 jours infini"):
        st.session_state.nb_jours += 3
        st.rerun()

tab1, tab2, tab3 = st.tabs(["PARIS INFINI", "PMU INFINI", "BOURSE INFINI"])

with tab1:
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        d = today + timedelta(days=j)
        if j == 0:
            lab = "AUJOURD HUI " + d.strftime("%d/%m") + " - 15 MATCHS"
        elif j == 1:
            lab = "DEMAIN " + d.strftime("%d/%m") + " - 15 MATCHS"
        else:
            lab = "JOUR +" + str(j) + " " + d.strftime("%d/%m") + " - 15 MATCHS"
        with st.expander(lab, expanded=(j<2)):
            matchs = gen_matchs()
            df = pd.DataFrame(matchs, columns=["Match"])
            df["Marche"] = "1X"
            df["Cote"] = 1.85
            df["IA"] = 75.0
            st.dataframe(df, use_container_width=True)

with tab2:
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        d = today + timedelta(days=j)
        lab = "JOUR " + str(j) + " - " + d.strftime("%d/%m") + " - PMU"
        with st.expander(lab, expanded=(j<1)):
            data = gen_pmu()
            df = pd.DataFrame(data, columns=["Num","Cheval","Cote"])
            st.dataframe(df, use_container_width=True)
            st.code("QUINTE: 1-7-5-3-2")

with tab3:
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        d = today + timedelta(days=j)
        lab = "JOUR " + str(j) + " - " + d.strftime("%d/%m") + " - BOURSE"
        with st.expander(lab, expanded=(j<1)):
            data = gen_bourse()
            df = pd.DataFrame(data, columns=["Actif","Prix","Var"])
            st.dataframe(df, use_container_width=True)

st.caption("FABRICE EMPIRE - TOUT INFINI CORRIGE")
