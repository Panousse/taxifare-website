import streamlit as st
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
pickup_datetime = st.text_input("Pickup datetime (YYYY-MM-DD HH:MM:SS)", "2021-01-01 10:00:00")


#Lieu de départ
st.header("Point de départ")

pickup_longitude = st.number_input("Entrez la longitude de départ", min_value=-180.0, max_value=180.0, step=0.000001, format="%.6f")
pickup_latitude = st.number_input("Entrez la latitude de départ", min_value=-90.0, max_value=90.0, step=0.000001, format="%.6f")
st.header("Point d'arrivée")

#Lieu d'arrivée
dropoff_longitude = st.number_input("Entrez la longitude d'arrivée", min_value=-180.0, max_value=180.0, step=0.000001, format="%.6f")
dropoff_latitude = st.number_input("Entrez la latitude d'arrivée", min_value=-90.0, max_value=90.0, step=0.000001, format="%.6f")

import streamlit as st

#Combien de passager
st.title("Choisissez un chiffre de 1 à 5")

# Utilisation du slider pour choisir un chiffre
passenger_count = st.slider("Sélectionnez un chiffre :", min_value=1, max_value=5, value=1)
st.write("Vous avez sélectionné :", passenger_count)



#Map

def get_map_data():

    return pd.DataFrame({"lat":[pickup_latitude,dropoff_latitude],
                         "lon":[pickup_longitude,dropoff_longitude]})

df = get_map_data()

st.map(df)

#Dictionnaire

params = {
    "pickup_datetime":pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count":passenger_count
}


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

#response = requests.get(url, params=params)

#if url == 'https://taxifare.lewagon.ai/predict':

   # st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if st.button("Appeler l'API"):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Récupération de la prédiction depuis la réponse JSON
        result = response.json()
        result= result["fare"]
        st.success(f"Prédiction : {result}")
    else:
        st.error(f"Erreur lors de l'appel à l'API (code {response.status_code})")
