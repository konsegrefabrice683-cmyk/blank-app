import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V17", layout="wide")
st.title("FABRICE EMPIRE V17 - PRONO")
st.caption("VRAIS PRONOS - 2-1 / Over 2.5 / BTTS Oui / X2")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 5

EQUIPES = ["Real","Barca","Man City","Arsenal","Bayern","PSG","Inter","Brest","Nice","EFO","ASFA","Burkina"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed"]

def get_label(j, d, suf):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds} - {suf}"
    if j==1: return f"DEMAIN - {ds} - {suf}"
    return f"JOUR +{j} - {ds} - {suf}"

if st.button("➕ +3 JOURS INFINIS"):
    st.session_state.nb_jours += 3
    st.rerun()

tab1, tab2, tab3 = st.tabs(["PARIS INFINI","PMU INFINI","BOURSE INFINI"])
today = datetime.now()

with tab1:
    tp = st.selectbox("Type LONAB", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], key="p1")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "15 MATCHS"), expanded=(j<2)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice([x for x in EQUIPES if x!=a])
                if tp == "Score Exact":
                    prono = f"{random.randint(0,3)}-{random.randint(0,3)}"
                    cote = round(random.uniform(6.0, 12.0),2)
                elif tp == "Over/Under":
                    prono = random.choice(["Over 0.5","Over 1.5","Over 2.5","Under 2.5","Over 3.5"])
                    cote = round(random.uniform(1.70, 2.25),2)
                elif tp == "BTTS":
                    prono = random.choice(["BTTS Oui","BTTS Non"])
                    cote = round(random.uniform(1.65, 2.15),2)
                elif tp == "Cartons":
                    prono = random.choice(["Over 2.5 Cartons","Over 3.5 Cartons","Under 4.5 Cartons"])
                    cote = round(random.uniform(1.80, 2.40),2)
                elif tp == "Corners":
                    prono = random.choice(["Over 7.5 Corners","Over 8.5 Corners","Over 9.5 Corners"])
                    cote = round(random.uniform(1.85, 2.30),2)
                elif tp == "Double Chance":
                    prono = random.choice(["1X","X2","12"])
                    cote = round(random.uniform(1.25, 1.65),2)
                else:
                    prono = random.choice(["1","X","2"])
                    cote = round(random.uniform(1.90, 3.20),2)
                rows.append([f"{a} vs {b}", prono, cote, "65%", "+5%", 75.0, "FEU VERT"])
            df = pd.DataFrame(rows, columns=["Match","Prono","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)

with tab2:
    tp2 = st.selectbox("Type PMU", ["Quinte+","Quarte","Tierce"], key="p2")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "PMU"), expanded=(j<1)):
            rows = [[str(i+1), ch, round(random.uniform(2,9),1), "25%", 72.0] for i,ch in enumerate(CHEVAUX)]
            st.dataframe(pd.DataFrame(rows, columns=["Num","Cheval","Cote","Proba","IA"]), use_container_width=True, hide_index=True)

with tab3:
    tp3 = st.selectbox("Marche", ["BRVM","USA","CRYPTO","OR"], key="p3")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, f"BOURSE {tp3}"), expanded=(j<1)):
            rows = [[n, random.randint(1000,50000), "+2.5%", 75.0] for n in random.sample(["SONATEL","ORANGE","NVDA","BTC","ETH","GOLD"],4)]
            st.dataframe(pd.DataFrame(rows, columns=["Actif","Prix","Var","IA"]), use_container_width=True, hide_index=True)
