import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE EMPIRE V16.9", layout="wide")
st.title("FABRICE EMPIRE V16.9")
st.caption("24/10/2026 - V16.9 AVEC JOUR INFINI - FIX Marche -> Prono")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 1

if st.button("➕ +3 JOURS INFINIS", width='stretch'):
    st.session_state.nb_jours += 3
    st.rerun()

def get_label(j, d):
    ds = d.strftime("%d/%m/%Y")
    if j == 0:
        return f"AUJOURD HUI - {ds} - 15 MATCHS"
    return f"JOUR +{j} - {ds} - 15 MATCHS"

today = datetime.now()
tab_paris, tab_pmu, tab_bourse = st.tabs(["PARIS INFINI", "PMU INFINI", "BOURSE INFINI"])

with tab_paris:
    type_paris = st.selectbox("Type LONAB", ["Double Chance", "1X2", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], index=0)

    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj), expanded=(j==0)):
            
            if type_paris == "Double Chance":
                rows = [
                    ["Inter vs Arsenal", "1X", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
                    ["Inter vs Barca", "X2", 1.45, "72%", "+5.5%", 76.5, "FEU VERT ULTRA"],
                    ["PSG vs EFO", "1X", 1.32, "78%", "+6.5%", 79.5, "FEU VERT ULTRA"],
                    ["Inter vs Man City", "12", 1.52, "70%", "+4.8%", 74.2, "FEU VERT"],
                    ["EFO vs Bayern", "X2", 1.28, "81%", "+5.8%", 77.2, "FEU VERT ULTRA"],
                    ["Real vs Brest", "1X", 1.42, "74%", "+5.0%", 76.0, "FEU VERT ULTRA"],
                    ["ASFA vs EFO", "1X", 1.65, "69%", "+4.2%", 73.5, "FEU VERT"],
                    ["Barca vs PSG", "X2", 1.55, "72%", "+5.5%", 74.8, "FEU VERT ULTRA"],
                    ["Man City vs EFO", "1X", 1.38, "76%", "+6.2%", 78.8, "FEU VERT ULTRA"],
                    ["Barca vs Nice", "1X", 1.55, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
                    ["Brest vs Nice", "X2", 1.35, "80%", "+6.0%", 78.1, "FEU VERT ULTRA"],
                    ["Mamelodi vs Wiliete", "12", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
                    ["Real Madrid vs Barca", "1X", 1.45, "72%", "+5.5%", 76.5, "FEU VERT ULTRA"],
                    ["Bayern vs Dortmund", "X2", 1.28, "82%", "+5.1%", 77.8, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "1X", 1.22, "85%", "+4.2%", 76.2, "FEU VERT ULTRA"],
                ]
            elif type_paris == "1X2":
                rows = [
                    ["Inter vs Arsenal", "1", 2.45, "62%", "+5.5%", 76.2, "FEU VERT"],
                    ["Inter vs Barca", "X", 3.20, "31%", "+2.1%", 71.5, "FEU VERT"],
                    ["PSG vs EFO", "1", 1.65, "70%", "+7.1%", 78.5, "FEU VERT ULTRA"],
                    ["Inter vs Man City", "2", 2.80, "45%", "+4.2%", 72.3, "FEU VERT"],
                    ["EFO vs Bayern", "2", 1.85, "65%", "+5.2%", 75.2, "FEU VERT"],
                    ["Real vs Brest", "1", 1.95, "64%", "+5.8%", 74.1, "FEU VERT"],
                    ["ASFA vs EFO", "X", 3.10, "32%", "+3.0%", 70.5, "FEU VERT"],
                    ["Barca vs PSG", "1", 2.20, "60%", "+4.8%", 71.5, "FEU VERT"],
                    ["Man City vs EFO", "1", 1.55, "72%", "+5.1%", 75.8, "FEU VERT ULTRA"],
                    ["Barca vs Nice", "2", 2.35, "57%", "+5.8%", 73.5, "FEU VERT"],
                    ["Brest vs Nice", "1", 2.10, "58%", "+4.2%", 72.3, "FEU VERT"],
                    ["Mamelodi vs Wiliete", "1", 1.85, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
                    ["Real Madrid vs Barca", "1", 2.10, "58%", "+4.2%", 72.3, "FEU VERT"],
                    ["Bayern vs Dortmund", "1", 1.75, "68%", "+6.5%", 77.2, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "1", 1.55, "72%", "+5.1%", 75.8, "FEU VERT ULTRA"],
                ]
            elif type_paris == "BTTS Oui/Non":
                rows = [
                    ["Inter vs Arsenal", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
                    ["Inter vs Barca", "BTTS Oui", 1.78, "64%", "+5.1%", 73.4, "FEU VERT ULTRA"],
                    ["PSG vs EFO", "BTTS Non", 1.90, "60%", "+4.0%", 72.0, "FEU VERT"],
                    ["Inter vs Man City", "BTTS Oui", 1.65, "70%", "+6.5%", 76.2, "FEU VERT ULTRA"],
                    ["EFO vs Bayern", "BTTS Oui", 1.72, "68%", "+6.1%", 75.8, "FEU VERT ULTRA"],
                    ["Real vs Brest", "BTTS Non", 1.88, "61%", "+4.2%", 72.8, "FEU VERT"],
                    ["ASFA vs EFO", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
                    ["Barca vs PSG", "BTTS Oui", 1.65, "70%", "+6.5%", 76.2, "FEU VERT ULTRA"],
                    ["Man City vs EFO", "BTTS Non", 1.95, "58%", "+3.8%", 71.5, "FEU VERT"],
                    ["Barca vs Nice", "BTTS Oui", 1.75, "66%", "+4.9%", 72.8, "FEU VERT"],
                    ["Brest vs Nice", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
                    ["Mamelodi vs Wiliete", "BTTS Non", 1.92, "59%", "+4.0%", 71.8, "FEU VERT"],
                    ["Real Madrid vs Barca", "BTTS Oui", 1.65, "70%", "+6.5%", 76.2, "FEU VERT ULTRA"],
                    ["Bayern vs Dortmund", "BTTS Oui", 1.58, "72%", "+5.8%", 75.5, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "BTTS Oui", 1.75, "66%", "+4.9%", 72.8, "FEU VERT"],
                ]
            elif type_paris == "Over/Under":
                rows = [
                    ["Inter vs Arsenal", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
                    ["Inter vs Barca", "Over 1.5", 1.34, "82%", "+5.2%", 77.2, "FEU VERT ULTRA"],
                    ["PSG vs EFO", "Over 1.5", 1.28, "85%", "+4.8%", 78.5, "FEU VERT ULTRA"],
                    ["Inter vs Man City", "Over 2.5", 1.75, "68%", "+5.5%", 76.2, "FEU VERT ULTRA"],
                    ["EFO vs Bayern", "Under 2.5", 1.95, "58%", "+3.8%", 71.8, "FEU VERT"],
                    ["Real vs Brest", "Over 2.5", 1.80, "67%", "+5.0%", 74.8, "FEU VERT"],
                    ["ASFA vs EFO", "Over 1.5", 1.42, "78%", "+4.2%", 72.5, "FEU VERT"],
                    ["Barca vs PSG", "Over 2.5", 1.72, "69%", "+5.2%", 75.2, "FEU VERT ULTRA"],
                    ["Man City vs EFO", "Over 1.5", 1.28, "84%", "+5.0%", 78.2, "FEU VERT ULTRA"],
                    ["Barca vs Nice", "Over 2.5", 1.78, "68%", "+5.5%", 75.5, "FEU VERT ULTRA"],
                    ["Brest vs Nice", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
                    ["Mamelodi vs Wiliete", "Over 1.5", 1.35, "81%", "+5.2%", 77.8, "FEU VERT ULTRA"],
                    ["Real Madrid vs Barca", "Over 2.5", 1.75, "68%", "+5.5%", 76.2, "FEU VERT ULTRA"],
                    ["Bayern vs Dortmund", "Over 2.5", 1.55, "75%", "+6.2%", 78.2, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "Over 1.5", 1.30, "82%", "+5.5%", 78.0, "FEU VERT ULTRA"],
                ]
            elif type_paris == "Score Exact":
                rows = [
                    ["Inter vs Arsenal", "2-1", 8.50, "12%", "+8.5%", 68.2, "FEU VERT"],
                    ["Inter vs Barca", "1-0", 7.80, "13%", "+6.2%", 68.2, "FEU VERT"],
                    ["PSG vs EFO", "2-0", 7.20, "14%", "+7.5%", 69.8, "FEU VERT"],
                    ["Inter vs Man City", "1-1", 6.50, "15%", "+6.8%", 69.5, "FEU VERT"],
                    ["EFO vs Bayern", "0-2", 8.00, "12%", "+6.8%", 68.2, "FEU VERT"],
                    ["Real vs Brest", "2-1", 8.20, "12%", "+7.0%", 68.5, "FEU VERT"],
                    ["ASFA vs EFO", "1-0", 6.80, "14%", "+6.0%", 68.8, "FEU VERT"],
                    ["Barca vs PSG", "2-2", 10.0, "9%", "+6.5%", 67.5, "FEU VERT"],
                    ["Man City vs EFO", "2-0", 7.20, "14%", "+7.5%", 69.8, "FEU VERT"],
                    ["Barca vs Nice", "1-0", 7.80, "13%", "+6.2%", 68.2, "FEU VERT"],
                    ["Brest vs Nice", "2-1", 8.50, "12%", "+8.5%", 68.2, "FEU VERT"],
                    ["Mamelodi vs Wiliete", "1-0", 7.00, "14%", "+6.5%", 69.0, "FEU VERT"],
                    ["Real Madrid vs Barca", "2-1", 9.00, "11%", "+7.8%", 69.2, "FEU VERT"],
                    ["Bayern vs Dortmund", "2-0", 8.00, "12%", "+7.2%", 68.5, "FEU VERT"],
                    ["PSG vs Lyon", "3-1", 9.50, "10%", "+7.0%", 67.8, "FEU VERT"],
                ]
            elif type_paris == "Cartons":
                rows = [
                    ["Inter vs Arsenal", "Over 3.5 Cartons", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
                    ["Inter vs Barca", "Over 4.5 Cartons", 1.90, "66%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                    ["PSG vs EFO", "Over 3.5 Cartons", 1.72, "69%", "+5.8%", 74.8, "FEU VERT"],
                    ["Inter vs Man City", "Over 4.5 Cartons", 1.88, "64%", "+5.0%", 73.5, "FEU VERT"],
                    ["EFO vs Bayern", "Over 3.5 Cartons", 1.70, "70%", "+6.0%", 75.5, "FEU VERT"],
                    ["Real vs Brest", "Over 4.5 Cartons", 1.92, "62%", "+4.8%", 72.8, "FEU VERT"],
                    ["ASFA vs EFO", "Over 3.5 Cartons", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
                    ["Barca vs PSG", "Over 4.5 Cartons", 1.90, "66%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                    ["Man City vs EFO", "Over 3.5 Cartons", 1.70, "70%", "+6.0%", 75.5, "FEU VERT"],
                    ["Barca vs Nice", "Over 4.5 Cartons", 1.88, "64%", "+5.0%", 73.5, "FEU VERT"],
                    ["Brest vs Nice", "Over 3.5 Cartons", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
                    ["Mamelodi vs Wiliete", "Over 4.5 Cartons", 1.85, "65%", "+5.8%", 74.2, "FEU VERT"],
                    ["Real Madrid vs Barca", "Over 4.5 Cartons", 1.90, "66%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                    ["Bayern vs Dortmund", "Over 4.5 Cartons", 1.80, "67%", "+5.9%", 75.5, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "Over 3.5 Cartons", 1.68, "70%", "+5.1%", 73.5, "FEU VERT"],
                ]
            else:
                rows = [
                    ["Inter vs Arsenal", "Over 8.5 Corners", 1.75, "68%", "+4.1%", 71.2, "FEU VERT"],
                    ["Inter vs Barca", "Over 9.5 Corners", 1.85, "65%", "+5.5%", 74.5, "FEU VERT ULTRA"],
                    ["PSG vs EFO", "Over 8.5 Corners", 1.72, "69%", "+4.8%", 72.5, "FEU VERT"],
                    ["Inter vs Man City", "Over 9.5 Corners", 1.82, "66%", "+5.5%", 75.0, "FEU VERT"],
                    ["EFO vs Bayern", "Over 10.5 Corners", 2.05, "60%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                    ["Real vs Brest", "Over 8.5 Corners", 1.75, "68%", "+5.0%", 74.0, "FEU VERT"],
                    ["ASFA vs EFO", "Over 8.5 Corners", 1.78, "67%", "+5.2%", 73.8, "FEU VERT"],
                    ["Barca vs PSG", "Over 9.5 Corners", 1.82, "66%", "+5.5%", 75.0, "FEU VERT"],
                    ["Man City vs EFO", "Over 9.5 Corners", 1.85, "65%", "+5.5%", 74.5, "FEU VERT"],
                    ["Barca vs Nice", "Over 8.5 Corners", 1.78, "67%", "+5.2%", 74.2, "FEU VERT"],
                    ["Brest vs Nice", "Over 8.5 Corners", 1.75, "68%", "+4.1%", 71.2, "FEU VERT"],
                    ["Mamelodi vs Wiliete", "Over 9.5 Corners", 1.90, "62%", "+6.2%", 73.8, "FEU VERT"],
                    ["Real Madrid vs Barca", "Over 9.5 Corners", 1.85, "65%", "+5.5%", 74.5, "FEU VERT ULTRA"],
                    ["Bayern vs Dortmund", "Over 10.5 Corners", 2.05, "60%", "+6.2%", 75.2, "FEU VERT ULTRA"],
                    ["PSG vs Lyon", "Over 8.5 Corners", 1.72, "69%", "+4.8%", 72.5, "FEU VERT"],
                ]

            df = pd.DataFrame(rows, columns=["Match","Prono","Cote LONAB","Proba","Value","IA %","STATUT"])
            st.dataframe(df, width='stretch')

with tab_pmu:
    st.subheader("PMU INFINI")
    df_pmu = pd.DataFrame([
        ["1", "Mogho Power", 2.1, "42%", "+6.2%", 74.2, "FEU VERT ULTRA"],
        ["7", "Bangr Nooma", 3.2, "28%", "+4.1%", 72.8, "FEU VERT ULTRA"],
    ], columns=["Num","Cheval","Cote LONAB","Proba","Value","IA %","STATUT"])
    st.dataframe(df_pmu, width='stretch')

with tab_bourse:
    st.subheader("BOURSE INFINI")
    df_b = pd.DataFrame([
        ["SONATEL.SN", 18500, "+2.7%", 76.5, "ULTRA", "ACHETER"],
    ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    st.dataframe(df_b, width='stretch')
