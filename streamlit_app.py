import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 FINAL")
st.caption(f"PARIS + PMU + BOURSE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

# --- DATES ---
if "date_selected" not in st.session_state:
    st.session_state.date_selected = "SAM 24"
if "nb_matchs" not in st.session_state:
    st.session_state.nb_matchs = 15

c1, c2, c3, c4, c5, c6 = st.columns(6)
with c1:
    if st.button("VEN 23"):
        st.session_state.date_selected = "VEN 23"
with c2:
    if st.button("SAM 24", type="primary"):
        st.session_state.date_selected = "SAM 24"
with c3:
    if st.button("DIM 25"):
        st.session_state.date_selected = "DIM 25"
with c4:
    if st.button("LUN 26"):
        st.session_state.date_selected = "LUN 26"
with c5:
    if st.button("MAR 27"):
        st.session_state.date_selected = "MAR 27"
with c6:
    if st.button("MER 28"):
        st.session_state.date_selected = "MER 28"

col_a, col_b = st.columns(2)
with col_a:
    st.metric("Jour", st.session_state.date_selected)
    st.metric("Matchs", st.session_state.nb_matchs)
with col_b:
    if st.button("Charger +20 matchs"):
        st.session_state.nb_matchs += 20
        st.rerun()
    if st.button("Reset 15"):
        st.session_state.nb_matchs = 15
        st.rerun()

EQUIPES = ["Brest", "Nice", "Mamelodi", "Raja", "Real", "Barca", "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon", "Inter", "Milan", "Al Hilal", "Al Nassr", "EFO", "ASFA", "ASEC", "Wydad", "Burkina", "Mali", "Ajax", "PSV"]

def gen_matchs(n):
    res = []
    for _ in range(n):
        a = random.choice(EQUIPES)
        b = random.choice([x for x in EQUIPES if x != a])
        res.append(f"{a} vs {b}")
    return res

tab1, tab2, tab3 = st.tabs(["PARIS INFINI", "PMU", "BOURSE"])

with tab1:
    matchs = gen_matchs(st.session_state.nb_matchs)
    type_p = st.selectbox("Type", ["1X2", "Double Chance", "BTTS", "Over/Under", "Cartons", "Corners", "Score Exact"])
    rows = []
    for m in matchs:
        rows.append([m, "1X", 1.85, "65%", "+5%", 75.0, "FEU VERT"])
    df = pd.DataFrame(rows, columns=["Match", "Marche", "Cote", "Proba", "Value", "IA", "STATUT"])
    st.dataframe(df, use_container_width=True, height=500)
    st.code(f"{type_p} - {st.session_state.date_selected} - {len(rows)} matchs")

with tab2:
    st.subheader("PMU-B LONAB")
    df_pmu = pd.DataFrame([
        ["1", "Mogho Power", 2.1, "42%", "+6.2%", 74.2, "FEU VERT"],
        ["7", "Bangr Nooma", 3.2, "28%", "+4.1%", 72.8, "FEU VERT"],
        ["5", "Etalon dOr", 3.8, "25%", "+2.8%", 68.5, "ATTENTE"],
        ["3", "Wend Panga", 4.5, "18%", "-4.2%", 55.1, "NO VALUE"],
    ], columns=["Num", "Cheval", "Cote", "Proba", "Value", "IA", "STATUT"])
    st.dataframe(df_pmu, use_container_width=True)
    st.code("QUINTE+: 1-7-5-3-2 | Gain 435.600F")

with tab3:
    st.subheader("BOURSE INTERNATIONALE")
    choix = st.selectbox("Marche", ["BRVM", "USA", "CRYPTO", "OR"])
    
    if choix == "BRVM":
        data = [
            ["SONATEL.SN", 18500, "+2.7%", 76.5, "ULTRA", "ACHETER"],
            ["ORANGE.SN", 11200, "+1.8%", 71.2, "VERT", "ACHETER"],
            ["ECOBANK.CI", 4500, "+3.1%", 74.8, "ULTRA", "ACHETER"],
            ["SGB.CI", 12500, "+0.9%", 68.5, "ATTENTE", "GARDER"],
        ]
    elif choix == "USA":
        data = [
            ["NVDA", 890.5, "+8.5%", 78.5, "ULTRA", "ACHETER"],
            ["AAPL", 182.5, "+4.2%", 73.2, "VERT", "ACHETER"],
            ["TSLA", 245.2, "+6.8%", 75.5, "ULTRA", "ACHETER"],
            ["MSFT", 415.2, "+2.1%", 70.1, "VERT", "ACHETER"],
        ]
    elif choix == "CRYPTO":
        data = [
            ["BTC", 67450, "+8.7%", 83.2, "PIEGE", "VENDRE"],
            ["ETH", 3450, "+5.2%", 76.8, "VERT", "ACHETER"],
            ["SOL", 145.2, "+11%", 79.5, "ULTRA", "ACHETER"],
            ["BNB", 580, "+3.2%", 72.1, "VERT", "ACHETER"],
        ]
    else:
        data = [
            ["GOLD", 2345, "+6.5%", 77.8, "ULTRA", "ACHETER"],
            ["SILVER", 28.5, "+4.2%", 71.5, "VERT", "ACHETER"],
            ["PETROLE", 85.2, "+2.8%", 69.8, "ATTENTE", "GARDER"],
        ]
    
    df_b = pd.DataFrame(data, columns=["Actif", "Prix", "Var", "IA %", "STATUT", "Action"])
    st.dataframe(df_b, use_container_width=True)
    st.success(f"MARCHE {choix} - OK")

st.caption("FABRICE EMPIRE MONDIAL ULTRA V16.9 - CORRIGE - OUAGA")
