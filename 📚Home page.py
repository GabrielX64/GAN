import streamlit as st
from PIL import Image as img
from update import *
from yaml.loader import SafeLoader
import yaml
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

APP_TITLE = "TRAVELS' CONEXIONS"
APP_SUB_TITLE = 'Aquí encontrarás las mejores rutas para tus próximos viajes'

st.set_page_config(APP_TITLE, initial_sidebar_state="collapsed")

st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """,
        unsafe_allow_html=True)

#def imagen(dir):
#    imagen = img.open(dir)
#    st.image(imagen,width=200)

hashed_passwords = stauth.Hasher(['XXXXX']).generate()


with open('.\contrasena.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    #diccionario={"name":['Neera Aranguri','Gabriel Cajas'],"username":['kitty_24','GabrielX_64']}
authenticator = stauth.Authenticate(config['credentials'],
                                    config['cookie']['name'],
                                    config['cookie']['key'],
                                    config['cookie']['expiry_days'],
                                    config['preauthorized'])

name, authentication_status, username = authenticator.login('Login', 'main')

#print(authentication_status)

if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
    
if st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

if st.session_state["authentication_status"]:
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    #imagen1 = img.open("C:\StreamLit\\files\Logo.jpeg")
    #st.image(imagen1,width=450)
    
    st.subheader('¡Bienvenido!')
    st.text('Haz click en el boton para continuar:')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        at1 = st.button('Perú')
    with col2:
        at2 = st.button('Ecuador')
    with col3:
        at3 = st.button('Venezuela')
    
    if at1:
        u.num = 1
    elif at2:
        u.num = 2
    elif at3:
        u.num = 3
    
    if at1 or at2 or at3:
        switch_page('Vuelos')
    
    authenticator.logout('Logout','main')