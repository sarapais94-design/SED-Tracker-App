import streamlit as st
import pandas as pd
import os
from datetime import datetime, time
import plotly.graph_objects as go
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="SED Tracker - Suivi Quotidien",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemin du fichier CSV
DATA_FILE = "sed_data.csv"

# Initialiser les colonnes du CSV
COLUMNS = [
    "Date",
    "Heure",
    # Symptômes
    "Douleur (0-10)",
    "Fatigue (0-10)",
    "Vertiges",
    "Nausées",
    # Sommeil
    "Heure coucher",
    "Heure lever",
    "Qualité sommeil (0-10)",
    "Réveils nocturnes",
    # Nourriture
    "Repas",
    "Type aliments",
    "Ressenti après repas",
    # Activités
    "Type activité",
    "Durée activité (min)",
    "Intensité activité (0-10)",
    # Douleur / Énergie
    "Énergie du jour (0-10)",
    # Autres
    "Hydratation (verres/jour)",
    "Météo",
    "Stress (0-10)",
    "Menstruations",
    "Observations"
]

# Charger ou créer le fichier CSV
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Titre principal
st.title("📊 SED Tracker - Suivi Quotidien")
st.markdown("""
Bienvenue dans votre outil de suivi personnalisé pour le Syndrome d'Ehlers-Danlos (SED).
Enregistrez quotidiennement vos symptômes, activités et observations pour identifier les patterns et adapter vos stratégies.
""")

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choisissez une section :",
    ["📝 Saisir données", "📈 Visualiser données", "🌳 Arbre de décision", "📋 Historique"]
)

# ============================================================================
# PAGE 1 : SAISIR LES DONNÉES
# ============================================================================
if page == "📝 Saisir données":
    st.header("Saisir vos données du jour")
    
    with st.form("daily_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📅 Date et Heure")
            date_input = st.date_input("Date", value=datetime.today())
            time_input = st.time_input("Heure", value=datetime.now().time())
        
        with col2:
            st.subheader("💪 Symptômes")
            douleur = st.slider("Douleur (0-10)", 0, 10, 5)
            fatigue = st.slider("Fatigue (0-10)", 0, 10, 5)
            vertiges = st.checkbox("Vertiges")
            nausees = st.checkbox("Nausées")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("😴 Sommeil")
            heure_coucher = st.time_input("Heure coucher", value=time(23, 0))
            heure_lever = st.time_input("Heure lever", value=time(7, 0))
            qualite_sommeil = st.slider("Qualité sommeil (0-10)", 0, 10, 5)
            reveils_nocturnes = st.number_input("Réveils nocturnes", min_value=0, value=0)
        
        with col4:
            st.subheader("🍽️ Nourriture")
            repas = st.text_input("Repas du jour (ex: petit-déj, déj, dîner)")
            type_aliments = st.text_area("Type d'aliments consommés")
            ressenti_repas = st.selectbox("Ressenti après repas", ["Bien", "Neutre", "Mal"])
        
        col5, col6 = st.columns(2)
        
        with col5:
            st.subheader("🏃 Activités")
            type_activite = st.text_input("Type d'activité (ex: marche, repos, écran, travail)")
            duree_activite = st.number_input("Durée activité (minutes)", min_value=0, value=0)
            intensite_activite = st.slider("Intensité activité (0-10)", 0, 10, 5)
        
        with col6:
            st.subheader("⚡ Énergie et Autres")
            energie = st.slider("Énergie du jour (0-10)", 0, 10, 5)
            hydratation = st.number_input("Hydratation (verres/jour)", min_value=0, value=8)
            meteo = st.selectbox("Météo", ["Ensoleillé", "Nuageux", "Pluvieux", "Neigeux", "Orageux"])
            stress = st.slider("Stress (0-10)", 0, 10, 5)
            menstruations = st.selectbox("Menstruations", ["Non", "Avant", "Pendant", "Après"])
        
        observations = st.text_area("Observations supplémentaires")
        
        # Bouton de soumission
        submitted = st.form_submit_button("✅ Enregistrer les données")
        
        if submitted:
            df = load_data()
            new_row = {
                "Date": str(date_input),
                "Heure": str(time_input),
                "Douleur (0-10)": douleur,
                "Fatigue (0-10)": fatigue,
                "Vertiges": "Oui" if vertiges else "Non",
                "Nausées": "Oui" if nausees else "Non",
                "Heure coucher": str(heure_coucher),
                "Heure lever": str(heure_lever),
                "Qualité sommeil (0-10)": qualite_sommeil,
                "Réveils nocturnes": reveils_nocturnes,
                "Repas": repas,
                "Type aliments": type_aliments,
                "Ressenti après repas": ressenti_repas,
                "Type activité": type_activite,
                "Durée activité (min)": duree_activite,
                "Intensité activité (0-10)": intensite_activite,
                "Énergie du jour (0-10)": energie,
                "Hydratation (verres/jour)": hydratation,
                "Météo": meteo,
                "Stress (0-10)": stress,
                "Menstruations": menstruations,
                "Observations": observations
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            save_data(df)
            st.success("✅ Données enregistrées avec succès !")
            st.balloons()

# ============================================================================
# PAGE 2 : VISUALISER LES DONNÉES
# ============================================================================
elif page == "📈 Visualiser données":
    st.header("Visualisation de vos données")
    
    df = load_data()
    
    if len(df) == 0:
        st.warning("⚠️ Aucune donnée enregistrée pour le moment. Commencez par saisir vos données !")
    else:
        st.subheader(f"📊 Nombre de jours enregistrés : {len(df)}")
        
        # Convertir les colonnes numériques
        numeric_cols = ["Douleur (0-10)", "Fatigue (0-10)", "Qualité sommeil (0-10)", 
                       "Intensité activité (0-10)", "Énergie du jour (0-10)", "Stress (0-10)"]
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Graphiques en ligne
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Douleur et Fatigue au fil du temps")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Douleur (0-10)'], mode='lines+markers', name='Douleur'))
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Fatigue (0-10)'], mode='lines+markers', name='Fatigue'))
            fig.update_layout(hovermode='x unified', height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Énergie et Stress au fil du temps")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Énergie du jour (0-10)'], mode='lines+markers', name='Énergie'))
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Stress (0-10)'], mode='lines+markers', name='Stress'))
            fig.update_layout(hovermode='x unified', height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Statistiques moyennes
        col3, col4, col5, col6 = st.columns(4)
        with col3:
            st.metric("Douleur moyenne", f"{df['Douleur (0-10)'].mean():.1f}/10")
        with col4:
            st.metric("Fatigue moyenne", f"{df['Fatigue (0-10)'].mean():.1f}/10")
        with col5:
            st.metric("Énergie moyenne", f"{df['Énergie du jour (0-10)'].mean():.1f}/10")
        with col6:
            st.metric("Stress moyen", f"{df['Stress (0-10)'].mean():.1f}/10")
        
        # Tableau des données
        st.subheader("📋 Tableau complet des données")
        st.dataframe(df, use_container_width=True)

# ============================================================================
# PAGE 3 : ARBRE DE DÉCISION
# ============================================================================
elif page == "🌳 Arbre de décision":
    st.header("Génération d'un arbre de décision")
    
    df = load_data()
    
    if len(df) < 10:
        st.warning(f"⚠️ Vous avez {len(df)} jours de données. Minimum 10 jours recommandés pour générer un arbre significatif.")
    else:
        st.success(f"✅ Vous avez {len(df)} jours de données. Vous pouvez générer un arbre !")
        
        # Convertir les colonnes numériques
        df_model = df.copy()
        numeric_cols = ["Douleur (0-10)", "Fatigue (0-10)", "Qualité sommeil (0-10)", 
                       "Intensité activité (0-10)", "Énergie du jour (0-10)", "Stress (0-10)",
                       "Durée activité (min)", "Hydratation (verres/jour)"]
        
        for col in numeric_cols:
            if col in df_model.columns:
                df_model[col] = pd.to_numeric(df_model[col], errors='coerce')
        
        # Sélection de la variable cible
        st.subheader("Configurer l'arbre de décision")
        
        col1, col2 = st.columns(2)
        
        with col1:
            target_var = st.selectbox(
                "Variable à prédire (cible) :",
                ["Fatigue (0-10)", "Douleur (0-10)", "Énergie du jour (0-10)", "Stress (0-10)"]
            )
        
        with col2:
            max_depth = st.slider("Profondeur maximale de l'arbre", 2, 10, 4)
        
        # Sélection des variables explicatives
        feature_options = [col for col in numeric_cols if col != target_var and col in df_model.columns]
        selected_features = st.multiselect(
            "Variables explicatives (features) :",
            feature_options,
            default=feature_options[:5] if len(feature_options) > 5 else feature_options
        )
        
        if st.button("🌳 Générer l'arbre de décision"):
            if len(selected_features) == 0:
                st.error("❌ Veuillez sélectionner au moins une variable explicative.")
            else:
                # Préparer les données
                df_clean = df_model[selected_features + [target_var]].dropna()
                
                if len(df_clean) < 5:
                    st.error("❌ Pas assez de données complètes pour générer l'arbre.")
                else:
                    X = df_clean[selected_features]
                    y = df_clean[target_var]
                    
                    # Entraîner le modèle
                    clf = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=2, random_state=42)
                    clf.fit(X, y)
                    
                    # Afficher la performance
                    score = clf.score(X, y)
                    st.info(f"📊 Score du modèle : {score:.2%}")
                    
                    # Visualiser l'arbre
                    fig, ax = plt.subplots(figsize=(20, 10))
                    plot_tree(clf, feature_names=selected_features, filled=True, rounded=True, ax=ax)
                    st.pyplot(fig)
                    
                    # Afficher l'importance des variables
                    st.subheader("📊 Importance des variables")
                    importance_df = pd.DataFrame({
                        'Variable': selected_features,
                        'Importance': clf.feature_importances_
                    }).sort_values('Importance', ascending=False)
                    
                    fig = px.bar(importance_df, x='Importance', y='Variable', orientation='h')
                    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 4 : HISTORIQUE
# ============================================================================
elif page == "📋 Historique":
    st.header("Historique complet")
    
    df = load_data()
    
    if len(df) == 0:
        st.warning("⚠️ Aucune donnée enregistrée pour le moment.")
    else:
        # Afficher le tableau complet
        st.subheader(f"📊 Total : {len(df)} jours enregistrés")
        st.dataframe(df, use_container_width=True)
        
        # Télécharger les données
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger les données (CSV)",
            data=csv,
            file_name="sed_data.csv",
            mime="text/csv"
        )
        
        # Statistiques détaillées
        st.subheader("📈 Statistiques détaillées")
        numeric_cols = ["Douleur (0-10)", "Fatigue (0-10)", "Qualité sommeil (0-10)", 
                       "Intensité activité (0-10)", "Énergie du jour (0-10)", "Stress (0-10)"]
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        stats_df = df[numeric_cols].describe().round(2)
        st.dataframe(stats_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    SED Tracker v1.0 | Outil de suivi personnalisé pour le Syndrome d'Ehlers-Danlos
</div>
""", unsafe_allow_html=True)

