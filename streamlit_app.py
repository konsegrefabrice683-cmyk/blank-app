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
            st.dataframe(st.session_state.employees, use_container_width=True)
        with tab2:
            with st.form("add_emp"):
                nom = st.text_input("Nom complet")
                poste = st.text_input("Poste")
                dept = st.selectbox("Département", ["RH", "Finance", "IT", "Marketing", "Ventes"])
                salaire = st.number_input("Salaire FCFA", min_value=0)
                if st.form_submit_button("Ajouter Employé"):
                    new_id = st.session_state.employees['ID'].max()+1 if len(st.session_state.employees)>0 else 1
                    new_row = pd.DataFrame([{"ID": new_id, "Nom": nom, "Poste": poste, "Département": dept, "Salaire": salaire, "Statut": "Actif"}])
                    st.session_state.employees = pd.concat([st.session_state.employees, new_row], ignore_index=True)
                    st.success(f"{nom} ajouté !")

    elif menu == "✅ Présences":
        st.subheader("Pointage Présence")
        emp_list = st.session_state.employees['Nom'].tolist()
        choisi = st.selectbox("Employé", emp_list)
        if st.button("📥 Arrivée"):
            st.session_state.presences.append({"Nom": choisi, "Heure": datetime.now().strftime("%H:%M:%S"), "Type": "Arrivée", "Date": str(date.today())})
            st.success(f"Arrivée {choisi} enregistrée")
        if st.button("📤 Départ"):
            st.session_state.presences.append({"Nom": choisi, "Heure": datetime.now().strftime("%H:%M:%S"), "Type": "Départ", "Date": str(date.today())})
            st.success(f"Départ {choisi} enregistré")
        if st.session_state.presences:
            st.table(pd.DataFrame(st.session_state.presences))

    elif menu == "📝 Congés":
        st.subheader("Demande de Congé")
        with st.form("conge"):
            emp = st.selectbox("Employé", st.session_state.employees['Nom'].tolist())
            type_c = st.selectbox("Type", ["Annuel", "Maladie", "Maternité", "Sans solde"])
            debut = st.date_input("Début")
            fin = st.date_input("Fin")
            motif = st.text_area("Motif")
            if st.form_submit_button("Soumettre Demande"):
                st.success(f"Demande de congé {type_c} pour {emp} soumise !")

    elif menu == "💰 Paie":
        st.subheader("Fiche de Paie")
        st.dataframe(st.session_state.employees[['Nom','Poste','Salaire']], use_container_width=True)
        emp_paie = st.selectbox("Choisir employé", st.session_state.employees['Nom'].tolist())
        if emp_paie:
            sal = st.session_state.employees[st.session_state.employees['Nom']==emp_paie]['Salaire'].values[0]
            st.markdown(f"<div class='card'><h3>Bulletin: {emp_paie}</h3><p>Brut: {sal:,} FCFA</p><p>Net: {int(sal*0.95):,} FCFA</p></div>", unsafe_allow_html=True)
            if st.button("📄 Générer PDF Paie"):
                st.balloons()
                st.success("PDF généré !")

    st.sidebar.success("App prête ✅")
