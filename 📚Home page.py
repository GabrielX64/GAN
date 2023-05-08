import streamlit as st
#from PIL import Image as img
from modules.update import *
from yaml.loader import SafeLoader
import yaml 
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import base64
import networkx as nx

 
APP_TITLE = "TRAVELS' CONEXIONS"
APP_SUB_TITLE = 'Aquí encontrarás las mejores rutas para tus próximos viajes'

st.set_page_config(APP_TITLE, initial_sidebar_state="collapsed")

def set_bg(main_bg): 
   main_bg_ext = 'gif'
   st.markdown(
      f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
      )

def download_button(pdf, filename):
    b64 = base64.b64encode(pdf).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Descargar </a>'
    return href

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


with open(r'.\utility\contrasena.yaml') as file:
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
    
    bg = r'.\images\e9fff1104283529.5f5fc55c35765.gif'
    set_bg(bg)

    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    #imagen1 = img.open("C:\StreamLit\\files\Logo.jpeg")
    #st.image(imagen1,width=450)
    
    st.subheader(f'¡Bienvenido, {name}!')

    listaPais = [' ','Peru','Ecuador','Colombia','Venezuela','Cuba','Republica Dominicana',
                 'México','Guatemala','El Salvador','Belice','Honduras','Nicaragua','Costa Rica','Panama']
    
    with st.form(key='form1'):
        pais = st.selectbox('Seleccione su país de procedencia:',options=listaPais)
        submit = st.form_submit_button(label='Submit')
    

    if submit:
        for i in range (len(listaPais)):
            if pais == listaPais[i]:
                u.num = i
                switch_page('Vuelos')
        if pais is not listaPais:
            st.error('No se encuentra ese país')
    
    if st.button('Descargar PDF'):

        with open(r'.\mapa\AVIANCA.pdf','rb') as f:
            pdf=f.read()

        st.markdown(download_button(pdf,'AVIANCA.pdf'),unsafe_allow_html=True)
    
    authenticator.logout('Logout','main')