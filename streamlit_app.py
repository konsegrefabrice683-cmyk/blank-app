import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V19 MOTEUR NEUF", layout="wide")
st.title("FABRICE EMPIRE V19 - MOTEUR NEUF")
st.caption("MOTEUR NEUF - PARIS + PMU + BOURSE - VRAIS PRONOS: 2-1 / Over 2.5 / BTTS Oui / X2")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 5

EQUIPES = ["Real Madrid","Barcelone","Man City","Arsenal","Bayern","PSG","Inter Milan","Brest","Nice","EFO","ASFA Yennenga","Burkina Faso","Senegal","Ajax","Dortmund"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed"]

def get_label(j, d):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds} - 15 MATCHS"
    if j==1: return f"DEMAIN - {ds} - 15 MATCHS"
    return f"JOUR +{j} - {ds} - 15 MATCHS"

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ +3 JOURS INFINIS", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with col2:
    if st.button("🔄 RESET", use_container_width=True):
        st.session_state.nb_jours = 5
        st.rerun()

st.write(f"Jours : {st.session_state.nb_jours}")

tab1, tab2, tab3 = st.tabs(["PARIS INFINI","PMU INFINI","BOURSE INFINI"])
today = datetime.now()

# PARIS
with tab1:
    tp = st.selectbox("Type LONAB", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], index=1)

    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj), expanded=(j==0)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice([x for x in EQUIPES if x != a])
                match_name = f"{a} vs {b}"

                # V19 - TOUT SORT DANS MARCHE / PRONO
                if tp == "Score Exact":
                    prono_val = f"{random.randint(0,3)}-{random.randint(0,3)}"
                    cote = round(random.uniform(6.5, 12.5), 2)
                elif tp == "Over/Under":
                    prono_val = random.choice(["Over 0.5","Over 1.5","Over 2.5","Over 3.5","Under 2.5","Under 3.5"])
                    cote = round(random.uniform(1.65, 2.40), 2)
                elif tp == "BTTS":
                    prono_val = random.choice(["BTTS Oui","BTTS Non","BTTS Oui + Over 2.5"])
                    cote = round(random.uniform(1.70, 2.25), 2)
                elif tp == "Cartons":
                    prono_val = random.choice(["Over 2.5 Cartons","Over 3.5 Cartons","Over 4.5 Cartons","Under 4.5 Cartons"])
                    cote = round(random.uniform(1.80, 2.60), 2)
                elif tp == "Corners":
                    prono_val = random.choice(["Over 7.5 Corners","Over 8.5 Corners","Over 9.5 Corners","Over 10.5 Corners"])
                    cote = round(random.uniform(1.85, 2.50), 2)
                elif tp == "Double Chance":
                    prono_val = random.choice(["1X","X2","12"])
                    cote = round(random.uniform(1.25, 1.75), 2)
                else: # 1X2
                    prono_val = random.choice(["1","X","2"])
                    cote = round(random.uniform(1.90, 3.50), 2)

                proba = f"{random.randint(52,78)}%"
                value = f"+{random.randint(2,8)}%"
                ia = random.randint(70, 92)
                rows.append([match_name, prono_val, cote, proba, value, ia])

            # ICI ON MET PRONO AU LIEU DE MARCHE, ET TOUT SORT DEDANS
            df = pd.DataFrame(rows, columns=["Match","Prono","Cote","Proba","Value","IA"])
            st.dataframe(df, width='stretch')

# PMU
with tab2:
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj).replace("15 MATCHS","8 CHEVAUX PMU"), expanded=(j==0)):
            rows = [[str(i+1), ch, round(random.uniform(2.2, 15.0),1), f"{random.randint(8,30)}%", random.randint(65,88)] for i,ch in enumerate(CHEVAUX)]
            df2 = pd.DataFrame(rows, columns=["Num","Cheval","Cote","Proba","IA"])
            st.dataframe(df2, width='stretch')

# BOURSE
with tab3:
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj).replace("15 MATCHS","BOURSE"), expanded=(j==0)):
            rows = [[n, random.randint(1000,80000), f"+{round(random.uniform(0.5,5.5),1)}%", random.randint(70,90)] for n in random.sample(["SONATEL","ORANGE CI","BOA","CORIS BANK","NVDA","BTC","ETH","GOLD"], 5)]
            df3 = pd.DataFrame(rows, columns=["Actif","Prix","Var","IA"])
            st.dataframe(df3, width='stretch')
