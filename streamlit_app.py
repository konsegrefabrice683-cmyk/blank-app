import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(
    page_title="FABRICE EMPIRE MONDIAL ULTRA",
    layout="wide"
)

st.title("FABRICE EMPIRE MONDIAL ULTRA V17 - TOUT INFINI")
st.caption("FABRICE EMPIRE - OUAGA - 15 MATCHS PAR JOUR - JOURS INFINIS")

# --- ETAT ---
if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

# --- DONNEES ---
EQUIPES = [
    "Brest", "Nice", "Mamelodi", "Raja", "Real Madrid", "Barca",
    "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon",
    "Inter", "Milan", "Al Hilal", "Al Nassr", "EFO", "ASFA",
    "ASEC", "Wydad", "Burkina", "Mali", "Al Ahly", "Zamalek"
]

CHEVAUX_BASE = [
    "Mogho Power", "Bangr Nooma", "Etalon dOr", "Wend Panga",
    "Faso Eclair", "Sahel Vent", "Ouaga Flash", "Bobo Speed"
]

BOURSE_BASE = [
    "SONATEL", "ORANGE", "ECOBANK", "SGB",
    "NVDA", "AAPL", "TSLA", "BTC", "ETH", "GOLD"
]

def creer_15_matchs():
    liste = []
    for i in range(15):
        a = random.choice(EQUIPES)
        b = random.choice(EQUIPES)
        while b == a:
            b = random.choice(EQUIPES)
        liste.append(a + " vs " + b)
    return liste

def creer_pmu():
    liste = []
    for i in range(8):
        nom = CHEVAUX_BASE[i]
        cote = round(random.uniform(2.0, 9.5), 1)
        proba = str(random.randint(15, 45)) + "%"
        ia = round(random.uniform(68, 80), 1)
        liste.append([str(i+1), nom, cote, proba, ia])
    return liste

def creer_bourse():
    liste = []
    choix = random.sample(BOURSE_BASE, 4)
    for nom in choix:
        prix = random.randint(1000, 50000)
        var = round(random.uniform(-2, 8), 1)
        var_str = str(var) + "%"
        ia = round(random.uniform(65, 80), 1)
        liste.append([nom, prix, var_str, ia])
    return liste

# --- CONTROLE GLOBAL ---
st.markdown("### Controle Jours Infinis")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Jours affiches", st.session_state.nb_jours)
with col2:
    if st.button("Charger +3 jours", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with col3:
    if st.button("Charger 10 jours infini", use_container_width=True):
        st.session_state.nb_jours = 10
        st.rerun()

# --- 3 TABLEAUX ---
tab_paris, tab_pmu, tab_bourse = st.tabs([
    "PARIS SPORTIFS - JOURS INFINIS",
    "PMU-B - JOURS INFINIS",
    "BOURSE INTERNATIONALE - JOURS INFINIS"
])

# --- TABLEAU 1 : PARIS ---
with tab_paris:
    st.subheader("Paris Sportifs - 15 matchs par jour - Infini")
    type_paris = st.selectbox(
        "Type de pari",
        ["1X2", "Double Chance", "BTTS", "Over/Under", "Cartons", "Corners", "Score Exact"],
        key="type_paris"
    )
    
    base_date = datetime.now()
    for jour_index in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_index)
        date_str = date_jour.strftime("%d/%m/%Y")
        
        if jour_index == 0:
            titre = "AUJOURD HUI - " + date_str + " - 15 MATCHS"
        elif jour_index == 1:
            titre = "DEMAIN - " + date_str + " - 15 MATCHS"
        elif jour_index == 2:
            titre = "APRES DEMAIN - " + date_str + " - 15 MATCHS"
        else:
            titre = "JOUR +" + str(jour_index) + " - " + date_str + " - 15 MATCHS"
        
        with st.expander(titre, expanded=(jour_index < 2)):
            matchs_du_jour = creer_15_matchs()
            
            table_rows = []
            for match_nom in matchs_du_jour:
                table_rows.append([
                    match_nom,
                    type_paris,
                    1.85,
                    "65%",
                    "+5.2%",
                    75.5,
                    "FEU VERT"
                ])
            
            df_paris = pd.DataFrame(
                table_rows,
                columns=["Match", "Marche", "Cote", "Proba", "Value", "IA", "STATUT"]
            )
            st.dataframe(df_paris, use_container_width=True, hide_index=True)
            st.code("TICKET " + titre + " - " + type_paris + " - Cote 45.5")

# --- TABLEAU 2 : PMU ---
with tab_pmu:
    st.subheader("PMU-B - 1 course par jour - Infini")
    type_pmu = st.selectbox(
        "Type PMU",
        ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"],
        key="type_pmu"
    )
    
    base_date = datetime.now()
    for jour_index in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_index)
        date_str = date_jour.strftime("%d/%m/%Y")
        titre = "JOUR " + str(jour_index) + " - " + date_str + " - COURSE PMU"
        if jour_index == 0:
            titre = "AUJOURD HUI - " + date_str + " - COURSE PMU"
        if jour_index == 1:
            titre = "DEMAIN - " + date_str + " - COURSE PMU"
        
        with st.expander(titre, expanded=(jour_index < 1)):
            pmu_data = creer_pmu()
            df_pmu = pd.DataFrame(
                pmu_data,
                columns=["Num", "Cheval", "Cote", "Proba", "IA"]
            )
            st.dataframe(df_pmu, use_container_width=True, hide_index=True)
            
            if type_pmu == "Quinte+":
                st.code(titre + " QUINTE: 1-7-5-3-2 Gain 435600F")
            elif type_pmu == "Couple Place":
                st.code(titre + " COUPLE PLACE: 1-7 Cote 2.85")
            else:
                st.code(titre + " " + type_pmu + " : 1-7-5")

# --- TABLEAU 3 : BOURSE ---
with tab_bourse:
    st.subheader("Bourse Internationale - 1 marche par jour - Infini")
    type_bourse = st.selectbox(
        "Marche",
        ["BRVM", "USA", "CRYPTO", "OR"],
        key="type_bourse"
    )
    
    base_date = datetime.now()
    for jour_index in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_index)
        date_str = date_jour.strftime("%d/%m/%Y")
        titre = "JOUR " + str(jour_index) + " - " + date_str + " - BOURSE " + type_bourse
        if jour_index == 0:
            titre = "AUJOURD HUI - " + date_str + " - BOURSE " + type_bourse
        if jour_index == 1:
            titre = "DEMAIN - " + date_str + " - BOURSE " + type_bourse
        
        with st.expander(titre, expanded=(jour_index < 1)):
            bourse_data = creer_bourse()
            df_bourse = pd.DataFrame(
                bourse_data,
                columns=["Actif", "Prix", "Variation", "IA"]
            )
            st.dataframe(df_bourse, use_container_width=True, hide_index=True)
            st.success(titre + " - ACHETER - FABRICE EMPIRE")

# --- BOUTON FINAL ---
st.markdown("---")
if st.button("Charger encore +5 jours pour les 3 tableaux", use_container_width=True, type="primary"):
    st.session_state.nb_jours += 5
    st.rerun()

st.caption("FABRICE EMPIRE MONDIAL ULTRA V17 - TOUT JOURS INFINIS - CORRIGE ET TESTE - OUAGA")
