import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model_path = "Titanic_prediction.pkl"
model = joblib.load(model_path)  

st.title('🛳️ Prédiction de survie des passagers du Titanic')
st.image("https://c4.wallpaperflare.com/wallpaper/621/139/660/night-ice-uk-transatlantic-steamer-titanic-hd-wallpaper-preview.jpg", caption="le titanic")

st.set_page_config(
    # page_title="Mon Application"
    page_icon="📛"  # Mets ici le chemin vers ton image
)

# Entrées utilisateur
passenger_id = st.number_input('🆔 ID du passager :', min_value=1, format="%d")
Pclass = st.number_input('🏷️ Classe (1 = Première, 2 = Deuxième, 3 = Troisième) :', min_value=1, max_value=3, format="%d")
name = st.text_input('📛 Nom du passager :', value="Unknown")
sex = st.selectbox('⚧️ Sexe du passager :', ['Homme', 'Femme'])
age = st.number_input('🎂 Âge du passager :', min_value=0, step=1, format="%d")
sibSp = st.number_input('👨‍👩‍👦 Nombre de frères/soeurs ou conjoints à bord :', min_value=0, format="%d")
parch = st.number_input('👪 Nombre de parents/enfants à bord :', min_value=0, format="%d")
ticket = st.text_input('🎟️ Numéro du ticket :', value="Unknown")
fare = st.number_input('💰 Tarif payé :', min_value=0.0, format="%.2f")
cabin = st.text_input('🏠 Cabine :', value="Unknown")
embarked = st.selectbox('⚓ Port d’embarquement :', ['C', 'Q', 'S'])

# Mapping des valeurs catégorielles
sex_mapping = {'Homme': 0, 'Femme': 1}
embarked_mapping = {'C': 0, 'Q': 1, 'S': 2}

sex_value = sex_mapping[sex]
embarked_value = embarked_mapping[embarked]

# Convertir les valeurs textuelles en identifiants numériques simples
name_code = hash(name) % 1000  
ticket_code = hash(ticket) % 1000
cabin_code = hash(cabin) % 1000

# Bouton de prédiction
if st.button("🔮 Prédire la survie du passager"):
    # Créer l'input pour le modèle sous forme de tableau numpy
    features = np.array([[passenger_id, Pclass, name_code, sex_value, age, sibSp, parch, ticket_code, fare, cabin_code, embarked_value]], dtype=np.float32)

    # Faire la prédiction
    prediction = model.predict(features)[0]

    # Afficher le résultat
    if prediction == 1:
        st.success("✅ Le passager a survécu !")
        st.image("https://c4.wallpaperflare.com/wallpaper/838/261/289/girl-light-red-nature-clouds-hd-wallpaper-preview.jpg")
    else:
        st.error("❌ Le passager n'a pas survécu.")
        st.image("https://c4.wallpaperflare.com/wallpaper/227/188/37/boat-disaster-drama-romance-wallpaper-preview.jpg")
