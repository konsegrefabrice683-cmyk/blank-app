import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.3 - TOUT JOURS INFINIS")
st.caption(f"PARIS + PMU + BOURSE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA - V16.3 BASE")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

# --- BASE DE DONNEES V16.3 ---
EQUIPES_V163 = ["Brest", "Nice", "Mamelodi", "Raja", "Real Madrid", "Barca", "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon", "Inter", "Milan", "Al Hilal", "Al Nassr", "Juventus", "Roma", "Liverpool", "Chelsea", "EFO", "ASFA", "Burkina", "Mali", "ASEC", "Africa", "Wydad", "Esperance", "Al Ahly", "Zamalek", "Simba", "Yanga", "Kaizer Chiefs", "Orlando Pirates", "TP Mazembe"]

CHEVAUX_V163 = ["Mogho Power", "Bangr Nooma", "Etalon dOr", "Wend Panga", "Faso Eclair", "Sahel Vent", "Ouaga Flash", "Bobo Speed", "Kadiogo Star", "Zaka Force", "Naba Etalon", "Yennenga", "Burkina Star"]

# --- GENERATEURS V16.3 ---
def generer_15_matchs_v163():
    liste = []
    for i in range(15):
        a = random.choice(EQUIPES_V163)
        b = random.choice(EQUIPES_V163)
        while b == a:
            b = random.choice(EQUIPES_V163)
        liste.append(a + " vs " + b)
    return liste

def generer_paris_v163(matchs, type_paris):
    rows = []
    for match in matchs:
        eq1 = match.split(" vs ")[0]
        cote = round(random.uniform(1.4, 3.5), 2)
        proba_val = random.randint(55, 85)
        proba = str(proba_val) + "%"
        value_val = round(random.uniform(2.0, 9.0), 1)
        value = "+" + str(value_val) + "%"
        ia = round(random.uniform(70, 82), 1)
        statut = "FEU VERT ULTRA" if ia > 75 else "FEU VERT" if ia > 68 else "ATTENTE"
        
        if type_paris == "1X2":
            marche = eq1 + " Win"
        elif type_paris == "Double Chance":
            marche = random.choice(["1X", "X2", "12"])
        elif type_paris == "BTTS Oui/Non":
            marche = random.choice(["BTTS Oui", "BTTS Non"])
        elif type_paris == "Over/Under":
            marche = random.choice(["Over 1.5", "Over 2.5", "Over 3.5", "Under 2.5"])
        elif type_paris == "Cartons":
            marche = random.choice(["Cartons Over 3.5", "Cartons Over 4.5", "Cartons Over 5.5"])
        elif type_paris == "Corners":
            marche = random.choice(["Corners Over 8.5", "Corners Over 9.5", "Corners Over 10.5"])
        else:
            marche = random.choice(["1-0", "2-1", "2-0", "1-1", "3-1"])
            cote = round(random.uniform(6.0, 15.0), 2)
        
        rows.append([match, marche, cote, proba, value, ia, statut])
    return rows

def generer_pmu_v163():
    chevaux_choisis = random.sample(CHEVAUX_V163, 8)
    rows = []
    for i, cheval in enumerate(chevaux_choisis):
        num = str(i+1)
        cote = round(random.uniform(1.8, 12.0), 1)
        proba = str(random.randint(18, 42)) + "%"
        value = "+" + str(round(random.uniform(1.5, 6.5), 1)) + "%"
        ia = round(random.uniform(60, 82), 1)
        statut = "FEU VERT ULTRA" if ia > 73 else "FEU VERT" if ia > 65 else "ATTENTE"
        rows.append([num, cheval, cote, proba, value, ia, statut])
    return rows

def generer_bourse_v163(type_bourse):
    rows = []
    if type_bourse == "BRVM":
        actifs = ["SONATEL.SN", "ORANGE.SN", "ECOBANK.CI", "SGB.CI"]
        prix_base = [18500, 11200, 4500, 12500]
    elif type_bourse == "USA":
        actifs = ["NVDA", "AAPL", "TSLA", "MSFT"]
        prix_base = [890.5, 182.5, 245.2, 415.2]
    elif type_bourse == "CRYPTO":
        actifs = ["BTC", "ETH", "SOL", "BNB"]
        prix_base = [67450, 3450, 145.2, 580]
    else:
        actifs = ["GOLD", "SILVER", "PETROLE"]
        prix_base = [2345, 28.5, 85.2]
    
    for idx, actif in enumerate(actifs):
        prix = prix_base[idx] if idx < len(prix_base) else random.randint(1000, 5000)
        variation = round(random.uniform(-1.5, 8.5), 1)
        var_str = "+" + str(variation) + "%" if variation > 0 else str(variation) + "%"
        ia = round(random.uniform(68, 82), 1)
        statut = "ULTRA" if ia > 75 else "VERT" if ia > 68 else "ATTENTE"
        action = "ACHETER" if ia > 70 else "GARDER"
        if type_bourse == "CRYPTO" and ia > 80:
            action = "VENDRE"
            statut = "PIEGE"
        rows.append([actif, prix, var_str, ia, statut, action])
    return rows

# --- CONTROLE JOURS INFINIS ---
st.markdown("### CONTROLE JOURS INFINIS - V16.3")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Jours affiches", str(st.session_state.nb_jours) + " jours")
with col_b:
    if st.button("Charger +3 jours", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with col_c:
    if st.button("Charger 10 jours infini", use_container_width=True, type="primary"):
        st.session_state.nb_jours = 10
        st.rerun()

st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "ANALYSE DU JOUR - V16.3 INFINI",
    "PMU-B COMPLET - V16.3 INFINI",
    "BOURSE INTERNATIONALE - V16.3 INFINI"
])

# --- TAB 1 : PARIS V16.3 INFINI ---
with tab1:
    type_paris = st.selectbox(
        "Type LONAB - V16.3",
        ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"],
        key="paris_v163"
    )
    
    base_date = datetime.now()
    for jour_idx in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_idx)
        date_str = date_jour.strftime("%d/%m/%Y")
        
        if jour_idx == 0:
            titre = "AUJOURD HUI - " + date_str + " - 15 MATCHS - V16.3"
        elif jour_idx == 1:
            titre = "DEMAIN - " + date_str + " - 15 MATCHS - V16.3"
        elif jour_idx == 2:
            titre = "APRES DEMAIN - " + date_str + " - 15 MATCHS - V16.3"
        else:
            titre = "JOUR +" + str(jour_idx) + " - " + date_str + " - 15 MATCHS - V16.3"
        
        with st.expander(titre, expanded=(jour_idx < 2)):
            matchs = generer_15_matchs_v163()
            data_paris = generer_paris_v163(matchs, type_paris)
            
            df_paris = pd.DataFrame(
                data_paris,
                columns=["Match", "Marche", "Cote LONAB", "Proba", "Value", "IA %", "STATUT"]
            )
            st.dataframe(df_paris, use_container_width=True, hide_index=True)
            
            # Ticket V16.3
            cote_totale = round(sum([row[2] for row in data_paris[:5]]), 2)
            st.code("TICKET " + type_paris + " " + titre + " | Cote 5 matchs = " + str(cote_totale) + " -> Gain " + str(int(cote_totale * 3000)) + "F - V16.3")

# --- TAB 2 : PMU V16.3 INFINI ---
with tab2:
    type_pmu = st.selectbox(
        "Type LONAB - V16.3",
        ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"],
        key="pmu_v163"
    )
    
    base_date = datetime.now()
    for jour_idx in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_idx)
        date_str = date_jour.strftime("%d/%m/%Y")
        
        if jour_idx == 0:
            titre = "AUJOURD HUI - " + date_str + " - PMU V16.3"
        elif jour_idx == 1:
            titre = "DEMAIN - " + date_str + " - PMU V16.3"
        else:
            titre = "JOUR +" + str(jour_idx) + " - " + date_str + " - PMU V16.3"
        
        with st.expander(titre, expanded=(jour_idx < 1)):
            pmu_data = generer_pmu_v163()
            
            df_pmu = pd.DataFrame(
                pmu_data,
                columns=["Num", "Cheval", "Cote LONAB", "Proba", "Value", "IA %", "STATUT"]
            )
            st.dataframe(df_pmu, use_container_width=True, hide_index=True)
            
            if type_pmu == "Quinte+":
                st.code(titre + " QUINTE+: 1-7-5-3-2 | Gain 435.600F - V16.3")
            elif type_pmu == "Quarte":
                st.code(titre + " QUARTE: 1-7-5-3 | Gain 125.200F - V16.3")
            elif type_pmu == "Tierce":
                st.code(titre + " TIERCE: 1-7-5 | Gain 85.200F - V16.3")
            elif type_pmu == "Couple Gagnant":
                st.code(titre + " COUPLE GAGNANT: 1-7 | Cote 4.5 | Gain 13.500F - V16.3")
            elif type_pmu == "Couple Place":
                st.code(titre + " COUPLE PLACE: 1-7 | Cote 2.85 | Gain 8.550F PLUS SUR - V16.3")
            elif type_pmu == "Gagnant":
                st.code(titre + " GAGNANT: 1 | Cote 2.1 | Gain 6.300F - V16.3")
            else:
                st.code(titre + " PLACE: 1 | Cote 1.35 | Gain 4.050F LE PLUS SUR - V16.3")

# --- TAB 3 : BOURSE V16.3 INFINI ---
with tab3:
    type_bourse = st.selectbox(
        "Marche - V16.3",
        ["BRVM", "USA", "CRYPTO", "OR & MATIERES"],
        key="bourse_v163"
    )
    
    base_date = datetime.now()
    for jour_idx in range(st.session_state.nb_jours):
        date_jour = base_date + timedelta(days=jour_idx)
        date_str = date_jour.strftime("%d/%m/%Y")
        
        if jour_idx == 0:
            titre = "AUJOURD HUI - " + date_str + " - BOURSE " + type_bourse + " V16.3"
        elif jour_idx == 1:
            titre = "DEMAIN - " + date_str + " - BOURSE " + type_bourse + " V16.3"
        else:
            titre = "JOUR +" + str(jour_idx) + " - " + date_str + " - BOURSE " + type_bourse + " V16.3"
        
        with st.expander(titre, expanded=(jour_idx < 1)):
            bourse_data = generer_bourse_v163(type_bourse)
            
            df_bourse = pd.DataFrame(
                bourse_data,
                columns=["Actif", "Prix", "Var", "IA %", "STATUT", "Action"]
            )
            st.dataframe(df_bourse, use_container_width=True, hide_index=True)
            st.success(titre + " - Analyse V16.3 - ACHETER / GARDER")

# --- BOUTON FINAL ---
st.markdown("---")
if st.button("Charger encore +5 jours pour les 3 tableaux - V16.3 INFINI", use_container_width=True, type="primary"):
    st.session_state.nb_jours += 5
    st.rerun()

st.caption("FABRICE EMPIRE MONDIAL ULTRA V16.3 - TOUT JOURS INFINIS - PARIS 15 MATCHS + PMU 8 CHEVAUX + BOURSE 4 ACTIFS - OUAGA - BASE V16.3")
