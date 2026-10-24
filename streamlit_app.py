import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 - TOUT INFINI ♾️")
st.caption(f"OUAGA | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

EQUIPES = ["Brest", "Nice", "Mamelodi", "Raja", "Real", "Barca", "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon", "Inter", "Milan", "Al Hilal", "Al Nassr", "Juventus", "Roma", "Liverpool", "Chelsea", "EFO", "ASFA", "ASEC", "Wydad", "Burkina", "Mali", "Al Ahly", "Zamalek", "Simba", "Yanga", "Kaizer", "Orlando", "TP Mazembe", "Flamengo", "Boca", "Ajax", "PSV", "Benfica", "Porto"]

CHEVAUX = ["Mogho Power", "Bangr Nooma", "Etalon dOr", "Wend Panga", "Faso Eclair", "Sahel Vent", "Ouaga Flash", "Bobo Speed", "Kadiogo Star", "Mogho Rapide", "Zaka Force", "Naba Etalon", "Yennenga", "Burkina Star", "Djibo Vent"]

JOCKEYS = ["OUEDRAOGO A.", "KABORE I.", "TRAORE F.", "SANKARA B.", "ZONGO M.", "COMPAORE J.", "KIEMTORE S.", "OUATTARA L."]

BRVM_ACTIFS = ["SONATEL.SN", "ORANGE.SN", "ECOBANK.CI", "SGB.CI", "ONATEL.BF", "CORIS.BF", "BOA.BF", "SICABLE.CI"]
USA_ACTIFS = ["NVDA", "AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "META", "NFLX"]
CRYPTO_ACTIFS = ["BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "SHIB"]
OR_ACTIFS = ["GOLD", "SILVER", "PETROLE", "GAZ", "CUIVRE", "DIAMANT"]

def gen_15_matchs():
    res = []
    for _ in range(15):
        a = random.choice(EQUIPES)
        b = random.choice([x for x in EQUIPES if x != a])
        res.append(f"{a} vs {b}")
    return res

def gen_pmu_race():
    chevaux = random.sample(CHEVAUX, 8)
    rows = []
    for i, ch in enumerate(chevaux, 1):
        cote = round(random.uniform(1.8, 12.5), 1)
        proba = f"{random.randint(15, 45)}%"
        value = f"+{round(random.uniform(1.5, 7.0),1)}%"
        ia = round(random.uniform(60, 82), 1)
        statut = random.choice(["FEU VERT", "FEU VERT ULTRA", "ATTENTE"])
        jockey = random.choice(JOCKEYS)
        rows.append([str(i), ch, jockey, cote, proba, value, ia, statut])
    return rows

def gen_bourse(marche):
    rows = []
    if marche == "BRVM":
        actifs = random.sample(BRVM_ACTIFS, 4)
    elif marche == "USA":
        actifs = random.sample(USA_ACTIFS, 4)
    elif marche == "CRYPTO":
        actifs = random.sample(CRYPTO_ACTIFS, 4)
    else:
        actifs = random.sample(OR_ACTIFS, 3)
    
    for actif in actifs:
        prix = round(random.uniform(1000, 80000), 1)
        var = f"+{round(random.uniform(0.5, 8.5),1)}%" if random.random() > 0.3 else f"-{round(random.uniform(0.5, 3.5),1)}%"
        ia = round(random.uniform(65, 82), 1)
        statut = random.choice(["ULTRA", "VERT", "ATTENTE"])
        action = "ACHETER" if " +" in f" {var}" or "+" in var else "GARDER"
        if ia > 80:
            action = "ACHETER"
        elif ia < 68:
            action = "GARDER"
        rows.append([actif, prix, var, ia, statut, action])
    return rows

# --- CONTROLE JOURS INFINIS GLOBAL ---
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Jours affiches", f"{st.session_state.nb_jours} jours")
with c2:
    if st.button("➕ Charger +3 jours", use_container_width=True):
        st.session_state.nb_jours += 3
        st.rerun()
with c3:
    if st.button("♾️ Charger 10 jours infinis", use_container_width=True):
        st.session_state.nb_jours = 10
        st.rerun()

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["PARIS - JOURS INFINIS ♾️", "PMU-B - JOURS INFINIS ♾️", "BOURSE - JOURS INFINIS ♾️"])

def get_label(j, date_j):
    if j == 0:
        return f"AUJOURD'HUI - {date_j.strftime('%d/%m/%Y')} - 15 MATCHS"
    elif j == 1:
        return f"DEMAIN - {date_j.strftime('%d/%m/%Y')} - 15 MATCHS"
    elif j == 2:
        return f"APRES-DEMAIN - {date_j.strftime('%d/%m/%Y')} - 15 MATCHS"
    else:
        return f"JOUR +{j} - {date_j.strftime('%d/%m/%Y')} - 15 MATCHS"

with tab1:
    type_p = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS", "Over/Under", "Cartons", "Corners", "Score Exact"], key="paris_type")
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        date_j = today + timedelta(days=j)
        label = get_label(j, date_j)
        with st.expander(label, expanded=(j<2)):
            matchs = gen_15_matchs()
            rows = []
            for m in matchs:
                rows.append([m, "1X", 1.85, "65%", "+5%", 75.0, "FEU VERT ULTRA"])
            df = pd.DataFrame(rows, columns=["Match", "Marche", "Cote", "Proba", "Value", "IA", "STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.code(f"TICKET {label} - {type_p}")

with tab2:
    type_pmu = st.selectbox("Type LONAB", ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"], key="pmu_type")
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        date_j = today + timedelta(days=j)
        if j == 0:
            label = f"AUJOURD'HUI - {date_j.strftime('%d/%m/%Y')} - COURSE PMU"
        elif j == 1:
            label = f"DEMAIN - {date_j.strftime('%d/%m/%Y')} - COURSE PMU"
        elif j == 2:
            label = f"APRES-DEMAIN - {date_j.strftime('%d/%m/%Y')} - COURSE PMU"
        else:
            label = f"JOUR +{j} - {date_j.strftime('%d/%m/%Y')} - COURSE PMU"
        with st.expander(label, expanded=(j<1)):
            race_data = gen_pmu_race()
            df_pmu = pd.DataFrame(race_data, columns=["Num", "Cheval", "Jockey", "Cote", "Proba", "Value", "IA", "STATUT"])
            st.dataframe(df_pmu, use_container_width=True, hide_index=True)
            if type_pmu == "Quinte+":
                st.code(f"{label} QUINTE+: 1-7-5-3-2 | Gain 435.600F")
            elif type_pmu == "Couple Place":
                st.code(f"{label} COUPLE PLACE: 1-7 | Gain 8.550F PLUS SUR")
            else:
                st.code(f"{label} {type_pmu}: 1-7-5 | Gain 85.200F")

with tab3:
    choix = st.selectbox("Marche", ["BRVM", "USA", "CRYPTO", "OR"], key="bourse_type")
    today = datetime.now()
    for j in range(st.session_state.nb_jours):
        date_j = today + timedelta(days=j)
        if j == 0:
            label = f"AUJOURD'HUI - {date_j.strftime('%d/%m/%Y')} - BOURSE {choix}"
        elif j == 1:
            label = f"DEMAIN - {date_j.strftime('%d/%m/%Y')} - BOURSE {choix}"
        elif j == 2:
            label = f"APRES-DEMAIN - {date_j.strftime('%d/%m/%Y')} - BOURSE {choix}"
        else:
            label = f"JOUR +{j} - {date_j.strftime('%d/%m/%Y')} - BOURSE {choix}"
        with st.expander(label, expanded=(j<1)):
            data_b = gen_bourse(choix)
            df_b = pd.DataFrame(data_b, columns=["Actif", "Prix", "Var", "IA", "STATUT", "Action"])
            st.dataframe(df_b, use_container_width=True, hide_index=True)
            st.success(f"{label} - Analyse FABRICE EMPIRE MONDIAL - {choix} - ACHETER")

st.markdown("---")
if st.button("♾️ Charger encore +5 jours pour les 3 tableaux", use_container_width=True, type="primary"):
    st.session_state.nb_jours += 5
    st.rerun()

st.caption("FABRICE EMPIRE MONDIAL ULTRA V16.9 - TOUT JOURS INFINIS - PARIS + PMU + BOURSE - OUAGA")
