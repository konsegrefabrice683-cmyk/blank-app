import streamlit as st
import pandas as pd
from datetime import datetime, date
import time

st.set_page_config(page_title="RH Manager - Fabrice", page_icon="👔", layout="wide")

st.markdown("""
<style>
.big-title {font-size:32px; font-weight:bold; color:#1E3A8A;}
.card {background:#F3F4F6; padding:15px; border-radius:10px; margin:10px 0;}
</style>
""", unsafe_allow_html=True)

if 'employees' not in st.session_state:
    st.session_state.employees = pd.DataFrame([
        {"ID": 1, "Nom": "KONÉ Fabrice", "Poste": "Manager RH", "Département": "RH", "Salaire": 500000, "Statut": "Actif"},
        {"ID": 2, "Nom": "OUEDRAOGO Awa", "Poste": "Comptable", "Département": "Finance", "Salaire": 350000, "Statut": "Actif"},
        {"ID": 3, "Nom": "TRAORÉ Moussa", "Poste": "Développeur", "Département": "IT", "Salaire": 400000, "Statut": "Congé"},
    ])

if 'presences' not in st.session_state:
    st.session_state.presences = []

st.sidebar.markdown("### RH Manager")
menu = st.sidebar.radio("Navigation", ["📊 Tableau de bord", "👥 Employés", "✅ Présences", "📝 Congés", "💰 Paie"])

st.markdown('<div class="big-title">👔 Plateforme RH - Gestion Complète</div>', unsafe_allow_html=True)
st.caption(f"Connecté: Fabrice | {date.today().strftime('%d/%m/%Y')} | Ouagadougou")

if menu == "📊 Tableau de bord":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Employés", len(st.session_state.employees))
    col2.metric("Actifs", len(st.session_state.employees[st.session_state.employees['Statut']=='Actif']))
    col3.metric("En Congé", len(st.session_state.employees[st.session_state.employees['Statut']=='Congé']))
    col4.metric("Présents Aujourd'hui", len(st.session_state.presences))
    st.divider()
    st.subheader("Répartition par département")
    st.bar_chart(st.session_state.employees['Département'].value_counts())
    st.dataframe(st.session_state.employees, use_container_width=True)

elif menu == "👥 Employés":
    st.subheader("Gestion des Employés")
    tab1, tab2 = st.tabs(["Liste", "Ajouter"])
    with tab1:
       
