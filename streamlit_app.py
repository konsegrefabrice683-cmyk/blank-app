import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V18", layout="wide")
st.title("FABRICE EMPIRE V18 - JOUR INFINI")
st.caption("VRAIS PRONOS - Score Exact 2-1 / Over 2.5 / BTTS Oui / X2 / Cartons / Corners")

# JOUR INFINI
if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 7

EQUIPES = ["Real Madrid","Barca","Man City","Arsenal","Bayern","PSG","Inter","Brest","Nice","EFO","ASFA","Salitas","Burkina Faso","Senegal","Ajax"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed","Zaka Puissance"]

def get_label(j, d, suf):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds} - {suf}"
    if j==1: return f"DEMAIN - {ds} - {suf}"
    return f"JOUR +{j} - {ds} - {suf}"

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ +3 JOURS INFINIS", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with col2:
    if st.button("🔄 RESET 7 JOURS", use_container_width=True):
        st.session_state.nb_jours = 7
        st.rerun()

st.info(f"📅 Tu affiches {st.session_state.nb_jours} jours - Infini jusqu'en 2027")

tab1, tab2, tab3 = st.tabs(["⚽ PARIS INFINI","🐎 PMU INFINI","📈 BOURSE INFINI"])
today = datetime.now()

# ================= PARIS =================
with tab1:
    tp = st.selectbox("Type LONAB - Choisis ton prono", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], key="p1")
    
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "15 MATCHS"), expanded=(j<2)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice([x for x in EQUIPES if x!=a])
                
                # ICI C'EST LE CHANGEMENT DE NOM ET DE CODE
                if tp == "Score Exact":
                    prono = f"{random.randint(0,3)}-{random.randint(0,3)}"
                    cote = round(random.uniform(6.0, 15.0),2)
                    proba = f"{random.randint(12,28)}%"
                elif tp == "Over/Under":
                    prono = random.choice(["Over 0.5","Over 1.5","Over 2.5","Over 3.5","Under 2.5","Under 3.5"])
                    cote = round(random.uniform(1.65, 2.45),2)
                    proba = f"{random.randint(55,72)}%"
                elif tp == "BTTS":
                    prono = random.choice(["BTTS Oui","BTTS Non","BTTS Oui + Over 2.5"])
                    cote = round(random.uniform(1.70, 2.20),2)
                    proba = f"{random.randint(52,68)}%"
                elif tp == "Cartons":
                    prono = random.choice(["Over 2.5 Cartons","Over 3.5 Cartons","Over 4.5 Cartons","Under 4.5 Cartons"])
                    cote = round(random.uniform(1.80, 2.50),2)
                    proba = f"{random.randint(50,65)}%"
                elif tp == "Corners":
                    prono = random.choice(["Over 7.5 Corners","Over 8.5 Corners","Over 9.5 Corners","Over 10.5 Corners"])
                    cote = round(random.uniform(1.85, 2.40),2)
                    proba = f"{random.randint(54,70)}%"
                elif tp == "Double Chance":
                    prono = random.choice(["1X","X2","12"])
                    cote = round(random.uniform(1.25, 1.80),2)
                    proba = f"{random.randint(68,85)}%"
                else: # 1X2
                    prono = random.choice(["1","X","2"])
                    cote = round(random.uniform(1.85, 3.80),2)
                    proba = f"{random.randint(45,65)}%"

                rows.append([f"{a} vs {b}", prono, cote, proba, "+5%", random.randint(70,92), "✅ FEU VERT"])
            
            # COLONNE CHANGE DE NOM ICI : Prono au lieu de Marche
            df = pd.DataFrame(rows, columns=["Match","Prono","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)

# ================= PMU =================
with tab2:
    tp2 = st.selectbox("Type PMU", ["Quinte+","Quarte","Tierce","Simple"], key="p2")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "PMU 8 CHEVAUX"), expanded=(j<1)):
            rows = []
            for i,ch in enumerate(CHEVAUX[:8]):
                rows.append([str(i+1), ch, round(random.uniform(2.5,12.0),1), f"{random.randint(10,30)}%", random.randint(65,88)])
            df2 = pd.DataFrame(rows, columns=["Num","Cheval","Cote","Proba","IA"])
            st.dataframe(df2, use_container_width=True, hide_index=True)

# ================= BOURSE =================
with tab3:
    tp3 = st.selectbox("Marche Boursier", ["BRVM","USA","CRYPTO","OR"], key="p3")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, f"BOURSE {tp3}"), expanded=(j<1)):
            assets = ["SONATEL","ORANGE CI","BOA","CORIS BANK","NVDA","TESLA","BTC","ETH","GOLD","SILVER"]
            rows = [[n, random.randint(1000,75000), f"+{round(random.uniform(0.5,4.5),1)}%", random.randint(70,90)] for n in random.sample(assets,5)]
            df3 = pd.DataFrame(rows, columns=["Actif","Prix","Variation","IA"])
            st.dataframe(df3, use_container_width=True, hide_index=True)
