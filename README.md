# SED Tracker - Outil de Suivi Quotidien pour le Syndrome d'Ehlers-Danlos

## 📋 Description

**SED Tracker** est une application web simple et intuitive conçue pour vous aider à suivre quotidiennement vos symptômes, activités et observations liées au Syndrome d'Ehlers-Danlos (SED). L'application vous permet de :

- **Saisir facilement** vos données chaque jour via une interface conviviale
- **Visualiser** vos données sous forme de graphiques et statistiques
- **Générer automatiquement** un arbre de décision pour identifier les patterns entre vos symptômes et vos activités
- **Exporter** vos données en CSV pour analyse ultérieure

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Ouvrez un terminal** dans le dossier du projet

2. **Créez un environnement virtuel** (recommandé) :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancez l'application** :
   ```bash
   streamlit run app.py
   ```

5. **Accédez l'application** : Votre navigateur devrait s'ouvrir automatiquement sur `http://localhost:8501`

## 📊 Fonctionnalités

### 1. 📝 Saisir les données
Enregistrez quotidiennement :
- **Symptômes** : Douleur, Fatigue, Vertiges, Nausées
- **Sommeil** : Heures de coucher/lever, Qualité du sommeil, Réveils nocturnes
- **Nourriture** : Repas, Type d'aliments, Ressenti après repas
- **Activités** : Type, Durée, Intensité
- **Énergie et Autres** : Niveau d'énergie, Hydratation, Météo, Stress, Menstruations
- **Observations** : Notes supplémentaires

### 2. 📈 Visualiser les données
- Graphiques en ligne pour suivre l'évolution de vos symptômes au fil du temps
- Statistiques moyennes (douleur, fatigue, énergie, stress)
- Tableau complet de toutes vos données

### 3. 🌳 Arbre de décision
- Générez automatiquement un arbre de décision une fois que vous avez au moins 10 jours de données
- Choisissez la variable à prédire (fatigue, douleur, énergie, stress)
- Sélectionnez les variables explicatives (activités, sommeil, etc.)
- Visualisez l'importance de chaque variable pour comprendre quels facteurs influencent le plus vos symptômes

### 4. 📋 Historique
- Consultez l'ensemble de vos données enregistrées
- Téléchargez vos données en CSV pour analyse externe
- Consultez les statistiques détaillées

## 💡 Conseils d'utilisation

### Pour des résultats optimaux avec l'arbre de décision :
- **Collectez au moins 20-30 jours de données** pour obtenir des patterns significatifs
- **Soyez cohérent** dans vos saisies quotidiennes
- **Soyez honnête** dans vos évaluations (0-10) pour une meilleure précision
- **Testez différentes combinaisons** de variables explicatives pour découvrir les patterns

### Exemple d'utilisation :
1. Pendant 2-3 semaines, enregistrez quotidiennement vos données
2. Allez dans la section "Visualiser données" pour voir les tendances
3. Une fois que vous avez 10+ jours, allez dans "Arbre de décision"
4. Choisissez "Fatigue" comme variable cible
5. Sélectionnez comme variables explicatives : Douleur, Intensité activité, Qualité sommeil, Stress
6. Générez l'arbre pour voir quels facteurs influencent le plus votre fatigue

## 📁 Structure des fichiers

```
sed_tracker/
├── app.py                 # Application principale Streamlit
├── requirements.txt       # Dépendances Python
├── README.md             # Ce fichier
└── sed_data.csv          # Fichier de données (créé automatiquement)
```

## 🔒 Confidentialité

Vos données sont enregistrées **localement** dans un fichier `sed_data.csv` sur votre ordinateur. Aucune donnée n'est envoyée à des serveurs externes.

## 🐛 Dépannage

### L'application ne démarre pas
- Vérifiez que Python 3.8+ est installé : `python3 --version`
- Vérifiez que les dépendances sont installées : `pip list`
- Réinstallez les dépendances : `pip install -r requirements.txt --force-reinstall`

### Les graphiques ne s'affichent pas
- Vérifiez que vous avez au moins quelques jours de données
- Assurez-vous que les colonnes numériques contiennent des nombres valides

### L'arbre de décision ne se génère pas
- Vous devez avoir au moins 10 jours de données
- Assurez-vous d'avoir sélectionné au moins une variable explicative
- Vérifiez qu'il n'y a pas trop de valeurs manquantes

## 📞 Support

Pour toute question ou suggestion, vous pouvez :
- Consulter la documentation de Streamlit : https://docs.streamlit.io/
- Consulter la documentation de scikit-learn : https://scikit-learn.org/

## 📄 Licence

Cet outil est fourni à titre personnel pour vous aider à mieux comprendre votre condition.

---

**Bonne chance dans votre suivi SED ! 💪**

