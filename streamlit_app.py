import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 FINAL - INFINI")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

if "date_selected" not in st.session_state:
    st.session_state.date_selected = "SAM 24"
if "nb_matchs" not in st.session_state:
    st.session_state.nb_matchs = 15

st.markdown("### 📅 Dates LONAB - INFINI")
c_cal, c1, c2, c3, c4, c5, c6 = st.columns(7)
with c_cal:
    st.markdown("📅")
with c1:
    if st.button("VEN\n23", key="d23"):
        st.session_state.date_selected = "VEN 23"
with c2:
    if st.button("SAM\n24", key="d24", type="primary"):
        st.session_state.date_selected = "SAM 24"
with c3:
    if st.button("DIM\n25", key="d25"):
        st.session_state.date_selected = "DIM 25"
with c4:
    if st.button("LUN\n26", key="d26"):
        st.session_state.date_selected = "LUN 26"
with c5:
    if st.button("MAR\n27", key="d27"):
        st.session_state.date_selected = "MAR 27"
with c6:
    if st.button("MER\n28", key="d28"):
        st.session_state.date_selected = "MER 28"

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Matchs chargés", f"{st.session_state.nb_matchs} / ∞")
with col_b:
    if st.button("➕ Charger +20 matchs", use_container_width=True):
        st.session_state.nb_matchs += 20
        st.rerun()
with col_c:
    if st.button("🔄 Reset à 15", use_container_width=True):
        st.session_state.nb_matchs = 15
        st.rerun()

st.success(f"📆 {st.session_state.date_selected} - {st.session_state.nb_matchs} matchs infinis")

EQUIPES = ["Brest", "Nice", "Mamelodi", "Raja", "Real Madrid", "Barca", "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon", "Inter", "Milan", "Al Hilal", "Al Nassr", "Juventus", "Roma", "Liverpool", "Chelsea", "EFO", "ASFA", "Burkina", "Mali", "ASEC", "Wydad", "Al Ahly", "Zamalek", "Simba", "Yanga", "Kaizer", "Orlando", "TP Mazembe", "Vita Club", "Flamengo", "Boca", "River", "Ajax", "PSV", "Benfica", "Porto", "SALITAS", "RCK"]

def generer_matchs_infinis(n, jour):
    matchs = []
    for i in range(n):
        eq1 = random.choice(EQUIPES)
        eq2 = random.choice([e for e in EQUIPES if e != eq1])
        matchs.append(f"{eq1} vs {eq2}")
    return matchs

tab_paris, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR - INFINI", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

with tab_paris:
    jour = st.session_state.date_selected
    matchs_in
