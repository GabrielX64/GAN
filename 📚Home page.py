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
    
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        at1 = st.button('Perú')
    with col2:
        at2 = st.button('Ecuador')
    with col3:
        at3 = st.button('Colombia')
    with col4:
        at4 = st.button('Venezuela')
    with col5:
        at6 = st.button('Cuba')

    col6,col7,col8,col9 = st.columns(4)
    with col6:
        at5 = st.button('República Dominicana')
    with col7:
        at7 = st.button('México')
    with col8:
        at8 = st.button('Guatemala')
    with col9:
        at9 = st.button('El Salvador')
    
    col10,col11,col12,col13,col14 = st.columns(5)
    with col10:
        at10 = st.button('Belice')
    with col11:
        at11 = st.button('Honduras')
    with col12:
        at12 = st.button('Nicaragua')
    with col13:
        at13 = st.button('Costa Rica')
    with col14:
        at14 = st.button('Panamá')
    
    
    if at1:
        u.num = 1
    elif at2:
        u.num = 2
    elif at3:
        u.num = 3
    elif at4:
        u.num = 4
    elif at5:
        u.num = 5
    elif at6:
        u.num = 6
    elif at7:
        u.num = 7
    elif at8:
        u.num = 8
    elif at9:
        u.num = 9
    elif at10:
        u.num = 10
    elif at11:
        u.num = 11
    elif at12:
        u.num = 12
    elif at13:
        u.num = 13
    elif at14:
        u.num = 14
    
    if at1 or at2 or at3 or at4 or at5 or at6 or at7 or at8 or at9 or at10 or at11 or at12 or at13 or at14:
        switch_page('Vuelos')
    
    authenticator.logout('Logout','main')