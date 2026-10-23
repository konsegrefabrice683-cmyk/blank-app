import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 FINAL")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

tab_paris, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR - 15 MATCHS", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

with tab_paris:
    st.subheader("PARIS LONAB - 7 TYPES - 15 MATCHS")
    type_paris = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], key="paris_menu")
    
    if type_paris == "1X2":
        df = pd.DataFrame([
            ["Brest vs Nice", "Brest Win", 2.45, "62%", "+5.5%", 76.2, "FEU VERT"],
            ["Mamelodi vs Wiliete", "Mamelodi Win", 1.85, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "Raja Win", 1.90, "66%", "+6.2%", 75.5, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Al-Ahli Win", 1.65, "70%", "+7.1%", 78.5, "FEU VERT ULTRA"],
            ["Real Madrid vs Barca", "Real Win", 2.10, "58%", "+4.2%", 72.3, "FEU VERT"],
            ["Man City vs Arsenal", "City Win", 1.95, "64%", "+5.8%", 74.1, "FEU VERT"],
            ["Bayern vs Dortmund", "Bayern Win", 1.75, "68%", "+6.5%", 77.2, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "PSG Win", 1.55, "72%", "+5.1%", 75.8, "FEU VERT ULTRA"],
            ["Inter vs Milan", "Inter Win", 2.20, "60%", "+4.8%", 71.5, "FEU VERT"],
            ["Al Hilal vs Al Nassr", "Al Hilal Win", 2.05, "61%", "+5.2%", 73.4, "FEU VERT"],
            ["Juventus vs Roma", "Juventus Win", 1.88, "65%", "+5.5%", 74.5, "FEU VERT"],
            ["Liverpool vs Chelsea", "Liverpool Win", 1.92, "63%", "+4.8%", 73.2, "FEU VERT"],
            ["Atletico vs Sevilla", "Atletico Win", 1.78, "67%", "+5.2%", 74.8, "FEU VERT ULTRA"],
            ["Ajax vs PSV", "Ajax Win", 2.15, "59%", "+4.5%", 72.1, "FEU VERT"],
            ["Boca vs River", "Boca Win", 2.35, "57%", "+5.8%", 73.5, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    elif type_paris == "Double Chance":
        df = pd.DataFrame([
            ["Brest vs Nice", "1X", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
            ["Mamelodi vs Wiliete", "1X", 1.55, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "1X", 1.68, "65%", "+3.1%", 70.1, "ATTENTE"],
            ["Al-Ahli vs Khaleej", "1X", 1.35, "80%", "+6.2%", 78.1, "FEU VERT ULTRA"],
            ["Real Madrid vs Barca", "1X", 1.45, "72%", "+5.5%", 76.5, "FEU VERT ULTRA"],
            ["Man City vs Arsenal", "1X", 1.52, "70%", "+4.8%", 74.2, "FEU VERT"],
            ["Bayern vs Dortmund", "1X", 1.28, "82%", "+5.1%", 77.8, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "1X", 1.22, "85%", "+4.2%", 76.2, "FEU VERT ULTRA"],
            ["Inter vs Milan", "1X", 1.48, "69%", "+4.5%", 72.8, "FEU VERT"],
            ["Al Hilal vs Al Nassr", "1X", 1.55, "67%", "+5.2%", 73.5, "FEU VERT"],
            ["Juventus vs Roma", "1X", 1.38, "74%", "+4.8%", 75.2, "FEU VERT ULTRA"],
            ["Liverpool vs Chelsea", "1X", 1.42, "72%", "+4.5%", 74.5, "FEU VERT"],
            ["Atletico vs Sevilla", "1X", 1.32, "76%", "+5.1%", 76.2, "FEU VERT ULTRA"],
            ["Ajax vs PSV", "1X", 1.50, "70%", "+4.2%", 73.8, "FEU VERT"],
            ["Boca vs River", "1X", 1.58, "68%", "+4.8%", 74.1, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    elif type_paris == "BTTS Oui/Non":
        df = pd.DataFrame([
            ["Brest vs Nice", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
            ["Raja vs El-Kanemi", "BTTS Oui", 1.78, "64%", "+5.1%", 73.4, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "BTTS Oui", 1.72, "68%", "+6.1%", 75.8, "FEU VERT ULTRA"],
            ["Real vs Barca", "BTTS Oui", 1.65, "70%", "+6.5%", 76.2, "FEU VERT ULTRA"],
            ["City vs Arsenal", "BTTS Oui", 1.80, "63%", "+5.2%", 73.1, "FEU VERT"],
            ["Bayern vs Dortmund", "BTTS Oui", 1.58, "72%", "+5.8%", 75.5, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "BTTS Oui", 1.75, "66%", "+4.9%", 72.8, "FEU VERT"],
            ["Inter vs Milan", "BTTS Oui", 1.70, "68%", "+5.1%", 74.2, "FEU VERT ULTRA"],
            ["Al Hilal vs Nassr", "BTTS Oui", 1.62, "71%", "+6.2%", 76.8, "FEU VERT ULTRA"],
            ["Boca vs River", "BTTS Oui", 1.90, "60%", "+4.5%", 71.2, "FEU VERT"],
            ["Juventus vs Roma", "BTTS Oui", 1.82, "64%", "+5.2%", 73.5, "FEU VERT"],
            ["Liverpool vs Chelsea", "BTTS Oui", 1.68, "68%", "+5.8%", 75.2, "FEU VERT ULTRA"],
            ["Atletico vs Sevilla", "BTTS Oui", 1.75, "66%", "+5.1%", 74.1, "FEU VERT"],
            ["Ajax vs PSV", "BTTS Oui", 1.60, "70%", "+6.2%", 76.5, "FEU VERT ULTRA"],
            ["Sevilla vs Betis", "BTTS Oui", 1.78, "65%", "+4.8%", 73.8, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    elif type_paris == "Over/Under":
        df = pd.DataFrame([
            ["Brest vs Nice", "Over 1.5", 1.34, "82%", "+5.2%", 77.2, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
            ["Real vs Barca", "Over 2.5", 1.75, "68%", "+5.5%", 76.2, "FEU VERT ULTRA"],
            ["City vs Arsenal", "Over 2.5", 1.80, "65%", "+5.1%", 74.5, "FEU VERT"],
            ["Bayern vs Dortmund", "Over 2.5", 1.55, "75%", "+6.2%", 78.2, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "Over 2.5", 1.60, "72%", "+5.8%", 76.5, "FEU VERT ULTRA"],
            ["Inter vs Milan", "Over 1.5", 1.32, "83%", "+4.8%", 75.2, "FEU VERT ULTRA"],
            ["Al Hilal vs Nassr", "Over 2.5", 1.68, "70%", "+5.5%", 75.8, "FEU VERT ULTRA"],
            ["Boca vs River", "Over 1.5", 1.42, "78%", "+4.2%", 72.5, "FEU VERT"],
            ["Juventus vs Roma", "Over 2.5", 1.72, "67%", "+5.2%", 74.5, "FEU VERT"],
            ["Liverpool vs Chelsea", "Over 2.5", 1.65, "70%", "+5.5%", 75.8, "FEU VERT ULTRA"],
            ["Atletico vs Sevilla", "Over 1.5", 1.35, "80%", "+4.8%", 76.2, "FEU VERT ULTRA"],
            ["Ajax vs PSV", "Over 2.5", 1.58, "72%", "+5.8%", 76.5, "FEU VERT ULTRA"],
            ["Sevilla vs Betis", "Over 2.5", 1.70, "68%", "+5.1%", 74.2, "FEU VERT"],
            ["Man Utd vs Tottenham", "Over 2.5", 1.75, "67%", "+5.2%", 74.8, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    elif type_paris == "Cartons":
        df = pd.DataFrame([
            ["Brest vs Nice", "Over 3.5", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "Over 4.5", 1.85, "65%", "+5.8%", 74.2, "FEU VERT"],
            ["Real vs Barca", "Over 4.5", 1.90, "66%", "+6.2%", 75.2, "FEU VERT ULTRA"],
            ["City vs Arsenal", "Over 3.5", 1.72, "69%", "+5.5%", 74.8, "FEU VERT"],
            ["Bayern vs Dortmund", "Over 4.5", 1.80, "67%", "+5.9%", 75.5, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "Over 3.5", 1.68, "70%", "+5.1%", 73.5, "FEU VERT"],
            ["Inter vs Milan", "Over 4.5", 1.85, "65%", "+5.2%", 74.2, "FEU VERT ULTRA"],
            ["Al Hilal vs Nassr", "Over 3.5", 1.78, "68%", "+5.5%", 74.8, "FEU VERT"],
            ["Boca vs River", "Over 5.5", 2.10, "58%", "+6.8%", 76.2, "FEU VERT ULTRA"],
            ["Sevilla vs Betis", "Over 4.5", 1.82, "66%", "+5.2%", 73.8, "FEU VERT"],
            ["Juventus vs Roma", "Over 4.5", 1.85, "65%", "+5.2%", 74.1, "FEU VERT"],
            ["Liverpool vs Chelsea", "Over 3.5", 1.78, "67%", "+5.5%", 74.5, "FEU VERT"],
            ["Atletico vs Sevilla", "Over 4.5", 1.80, "66%", "+5.8%", 75.2, "FEU VERT ULTRA"],
            ["Ajax vs PSV", "Over 3.5", 1.75, "68%", "+5.1%", 73.8, "FEU VERT"],
            ["Man Utd vs Tottenham", "Over 3.5", 1.72, "69%", "+4.8%", 73.5, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    elif type_paris == "Corners":
        df = pd.DataFrame([
            ["Mamelodi vs Wiliete", "Over 9.5", 1.90, "62%", "+6.2%", 73.8, "FEU VERT"],
            ["Brest vs Nice", "Over 8.5", 1.75, "68%", "+4.1%", 71.2, "FEU VERT"],
            ["Real vs Barca", "Over 9.5", 1.85, "65%", "+5.5%", 74.5, "FEU VERT ULTRA"],
            ["City vs Arsenal", "Over 9.5", 1.80, "66%", "+5.2%", 73.8, "FEU VERT"],
            ["Bayern vs Dortmund", "Over 10.5", 2.05, "60%", "+6.2%", 75.2, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "Over 8.5", 1.72, "69%", "+4.8%", 72.5, "FEU VERT"],
            ["Inter vs Milan", "Over 9.5", 1.82, "64%", "+5.1%", 73.2, "FEU VERT"],
            ["Al Hilal vs Nassr", "Over 9.5", 1.88, "63%", "+5.5%", 74.1, "FEU VERT ULTRA"],
            ["Boca vs River", "Over 8.5", 1.78, "67%", "+5.2%", 73.5, "FEU VERT"],
            ["Ajax vs PSV", "Over 9.5", 1.85, "64%", "+5.2%", 73.8, "FEU VERT"],
            ["Juventus vs Roma", "Over 9.5", 1.80, "65%", "+5.1%", 73.5, "FEU VERT"],
            ["Liverpool vs Chelsea", "Over 9.5", 1.82, "64%", "+5.2%", 74.2, "FEU VERT"],
            ["Atletico vs Sevilla", "Over 8.5", 1.75, "68%", "+4.8%", 72.8, "FEU VERT"],
            ["Man Utd vs Tottenham", "Over 9.5", 1.88, "63%", "+5.5%", 74.1, "FEU VERT ULTRA"],
            ["Sevilla vs Betis", "Over 8.5", 1.78, "67%", "+5.2%", 73.5, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    else:
        df = pd.DataFrame([
            ["Brest vs Nice", "2-1", 8.50, "12%", "+8.5%", 68.2, "FEU VERT"],
            ["Al-Ahli vs Khaleej", "3-1", 12.00, "9%", "+7.2%", 70.5, "FEU VERT"],
            ["Real vs Barca", "2-1", 9.00, "11%", "+7.8%", 69.2, "FEU VERT"],
            ["City vs Arsenal", "2-0", 7.50, "13%", "+6.5%", 68.8, "FEU VERT"],
            ["Bayern vs Dortmund", "3-1", 10.00, "10%", "+7.1%", 70.2, "FEU VERT ULTRA"],
            ["PSG vs Lyon", "3-0", 8.00, "12%", "+6.8%", 69.5, "FEU VERT"],
            ["Inter vs Milan", "1-0", 6.50, "14%", "+5.8%", 67.5, "FEU VERT"],
            ["Al Hilal vs Nassr", "2-1", 8.50, "12%", "+7.2%", 70.1, "FEU VERT"],
            ["Boca vs River", "1-1", 6.00, "15%", "+5.5%", 68.2, "FEU VERT"],
            ["Ajax vs PSV", "2-2", 11.00, "9%", "+8.2%", 71.5, "FEU VERT ULTRA"],
            ["Juventus vs Roma", "1-0", 7.00, "13%", "+6.2%", 69.8, "FEU VERT"],
            ["Liverpool vs Chelsea", "2-1", 8.00, "12%", "+6.5%", 70.2, "FEU VERT"],
            ["Atletico vs Sevilla", "1-0", 6.50, "14%", "+5.8%", 68.5, "FEU VERT"],
            ["Man Utd vs Tottenham", "2-2", 10.50, "10%", "+7.5%", 71.2, "FEU VERT ULTRA"],
            ["Sevilla vs Betis", "2-1", 9.00, "11%", "+6.8%", 70.1, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    st.dataframe(df, use_container_width=True)

with tab_pmu:
    st.subheader("PMU-B LONAB - 7 TYPES")
    type_pmu = st.selectbox("Type LONAB", ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"], key="pmu_menu")
    df_pmu = pd.DataFrame([
        ["1", "Mogho Power", 2.1, "42%", "+6.2%", 74.2, "FEU VERT ULTRA"],
        ["7", "Bangr Nooma", 3.2, "28%", "+4.1%", 72.8, "FEU VERT ULTRA"],
        ["5", "Etalon dOr", 3.8, "25%", "+2.8%", 68.5, "ATTENTE"],
        ["3", "Wend Panga", 4.5, "18%", "-4.2%", 55.1, "NO VALUE"],
    ], columns=["Num","Cheval","Cote LONAB","Proba","Value","IA %","STATUT"])
    st.dataframe(df_pmu, use_container_width=True)
    if type_pmu == "Quinte+": st.code("QUINTE+: 1-7-5-3-2 | Gain 435.600F")
    elif type_pmu == "Couple Place": st.code("COUPLE PLACE: 1-7 | Cote 2.85 | Gain 8.550F PLUS SUR")
    elif type_pmu == "Gagnant": st.code("GAGNANT: 1 | Cote 2.1 | Gain 6.300F")
    elif type_pmu == "Place": st.code("PLACE: 1 | Cote 1.35 | Gain 4.050F LE PLUS SUR")
    else: st.code(f"{type_pmu}: 1-7-5 | Gain estimé 85.200F")

with tab_bourse:
    st.subheader("BOURSE INTERNATIONALE - FABRICE EMPIRE MONDIAL")
    type_bourse = st.selectbox("Marché", ["BRVM", "USA", "CRYPTO", "OR & MATIERES"], key="bourse_menu")
    if type_bourse == "BRVM":
        df_b = pd.DataFrame([
            ["SONATEL.SN", 18500, "+2.7%", 76.5, "ULTRA", "ACHETER"],
            ["ORANGE.SN", 11200, "+1.8%", 71.2, "VERT", "ACHETER"],
            ["ECOBANK.CI", 4500, "+3.1%", 74.8, "ULTRA", "ACHETER"],
            ["SGB.CI", 12500, "+0.9%", 68.5, "ATTENTE", "GARDER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    elif type_bourse == "USA":
        df_b = pd.DataFrame([
            ["NVDA", 890.5, "+8.5%", 78.5, "ULTRA", "ACHETER"],
            ["AAPL", 182.5, "+4.2%", 73.2, "VERT", "ACHETER"],
            ["TSLA", 245.2, "+6.8%", 75.5, "ULTRA", "ACHETER"],
            ["MSFT", 415.2, "+2.1%", 70.1, "VERT", "ACHETER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    elif type_bourse == "CRYPTO":
        df_b = pd.DataFrame([
            ["BTC", 67450, "+8.7%", 83.2, "PIEGE", "VENDRE"],
            ["ETH", 3450, "+5.2%", 76.8, "VERT", "ACHETER"],
            ["SOL", 145.2, "+11%", 79.5, "ULTRA", "ACHETER"],
            ["BNB", 580, "+3.2%", 72.1, "VERT", "ACHETER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    else:
        df_b = pd.DataFrame([
            ["GOLD", 2345, "+6.5%", 77.8, "ULTRA", "ACHETER"],
            ["SILVER", 28.5, "+4.2%", 71.5, "VERT", "ACHETER"],
            ["PETROLE", 85.2, "+2.8%", 69.8, "ATTENTE", "GARDER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    st.dataframe(df_b, use_container_width=True)
    st.success(f"MARCHE {type_bourse} - Analyse FABRICE EMPIRE MONDIAL")

st.caption("FABRICE EMPIRE MONDIAL ULTRA V16.9 - OUAGA - BOURSE INTERNATIONALE COMPLETE")
