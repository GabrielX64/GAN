import streamlit as st
from modules.update import *
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import base64

#def set_bg(main_bg): 
#    main_bg_ext = 'gif'
#    st.markdown(
#      f"""
#         <style>
#         .stApp {{
#             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
#             background-size: cover
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#      )

def multiplicar_unaescala(mat: np.ndarray):
    df = pd.read_excel(r'.\utility\MatrizAvianca.xlsx', sheet_name='Matriz Universal', header=None)
    matriz = df.to_numpy()

    A_bool = mat.astype(bool)
    B_bool = matriz.astype(bool)
    C_bool: np.ndarray = np.dot(A_bool,B_bool)
    Ce = C_bool.astype(int)

    return Ce

def MostrarTODO(option,selected,listaP):
    df = pd.read_excel(r'.\utility\MatrizAvianca.xlsx', sheet_name='Matriz Universal', header=None)
    matriz = df.to_numpy()
    a = multiplicar_unaescala(matriz)
    b = multiplicar_unaescala(a)

    c=0

    if option != " ":
        if selected == 'DIRECTA':
            st.text("Conexión directa")
            for i in range(matriz.shape[0]):
                if option == listaP[i]:
                    for k in range(matriz.shape[1]):
                        if matriz[i][k] == 1:
                            st.text(f'Existe vuelo directo con:{listaP[k]} ')
                            c+=1
            if c == 0:
                st.text('No tiene ninguna conexión con otra ciudad')
        elif selected == 'UNA ESCALA':
            st.text("Una escala")
            for i in range(a.shape[0]):
                if option == listaP[i]:
                    for k in range(a.shape[1]):
                        if a[i][k] == 1:
                            st.text(f'Existe vuelo de una escala con:{listaP[k]}')
                            c+=1
            if c == 0:
                st.text('No tiene ninguna conexión de una escala')
        elif selected == 'DOS ESCALAS':
            st.text("Dos escalas")
            for i in range(b.shape[0]):
                if option == listaP[i]:
                    for k in range(b.shape[1]):
                        if b[i][k] == 1:
                            st.text(f'Existe vuelo de dos escalas con:{listaP[k]} ')
                            c+=1
            if c == 0:
                st.text('No tiene ninguna conexión de dos escalas')
       
def main():
    #bg = r'.\images\dc644b107345049.5fa4ae1b8c86e.gif'
    #set_bg(bg)

    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """,
        unsafe_allow_html=True)
    

    st.header('VUELOS')

    listaP = ['Lima', 'Trujillo', 'Chiclayo', 'Piura', 'Iquitos', 'Maldonado', 'Cusco', 'Juliaca', 'Arequipa', 
              'Guayaquil', 'Quito', 'Bogota', 'Leticia', 'Florencia', 'Pasto', 'Tumaco', 'Popayán', 'Cali', 
              'Neiva', 'Villavicencio', 'Ibagué', 'Armenia', 'Pereira', 'Manizales', 'Yopal', 'Medellín', 
              'Montería', 'Cartagena', 'Barranquilla', 'San Andrés', 'Santa Marta', 'Riohacha', 'Valledupar', 
              'Cúcuta', 'Bucaramanga', 'Barrancabermeja', 'Caracas', 'San Juan', 'Punta Cana', 'Santo Domingo', 
              'La Habana', 'Cancún', 'Ciudad de Mexico', 'Flores', 'Ciudad de Guatemala', 'San Salvador', 
              'Belice','San Pedro de Sula', 'Tegucigalpa', 'La Ceiba', 'Roatán', 'Managua', 'Liberia', 
              'San José de Costa Rica', 'Ciudad de Panamá']

    tipo = ['DIRECTA','UNA ESCALA','DOS ESCALAS']
    
    selected = option_menu(
        menu_title=None,
        options=tipo,
        icons=['Arrow up','Arrow up Arrow down','Plane'],
        menu_icon='cast',
        default_index=0,
        orientation='horizontal'
    )

    if selected:
        option = None
        match u.num:
            case 1:#PERU
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Lima', 'Trujillo', 'Chiclayo', 'Piura', 'Iquitos', 'Maldonado', 'Cusco', 'Juliaca', 'Arequipa')
                )
            
            case 2:#ECUADOR
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Quito','Guayaquil')
                )
                
            case 3:#COLOMBIA
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Bogota', 'Leticia', 'Florencia', 'Pasto', 'Tumaco', 'Popayán', 'Cali', 'Neiva', 'Villavicencio', 
                     'Ibagué', 'Armenia', 'Pereira', 'Manizales', 'Yopal', 'Medellín', 'Montería', 'Cartagena', 'Barranquilla', 
                     'San Andrés', 'Santa Marta', 'Riohacha', 'Valledupar', 'Cúcuta', 'Bucaramanga', 'Barrancabermeja')
                )
            case 4:#VENEZUELA
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Caracas')
                )
            case 5:#REPUBLICA DOMINICANA
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','San Juan', 'Punta Cana', 'Santo Domingo')
                )
            case 6:#CUBA
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','La Habana')
                )
            case 7:#MEXICO
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Cancún', 'Ciudad de Mexico')
                )
            case 8:#GUATEMALA
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Flores', 'Ciudad de Guatemala')
                )
            case 9:#EL SALVADOR
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','San Salvador')
                )
            case 10:#BELICE
                option = st.selectbox(
                    'Seleccione su punto origen',
                    (' ','Belice')
                )
            case 11: #HONDURAS
                option = st.selectbox(
                    'Seleccione su punto de origen',
                    (' ','San Pedro de Sula', 'Tegucigalpa', 'La Ceiba', 'Roatán')
                )
            case 12: #NICARAGUA
                option = st.selectbox(
                    'Seleccione su punto de origen',
                    (' ','Managua', 'Liberia')
                )
            case 13: #COSTA RICA
                option = st.selectbox(
                    'Seleccione su punto de origen',
                    (' ','San José de Costa Rica')
                )
            case 14: #PANAMÁ
                option = st.selectbox(
                    'Seleccione su punto de origen',
                    (' ','Ciudad de Panamá')
                )
        #MostrarConexiones(option,selected,listaP)
        MostrarTODO(option,selected,listaP)
    #if option != ' ':
    #   st.write(f"Punto de origen: {option}")
    
    back = st.button('Back')
    if back:
        switch_page('Home page')

if __name__=="__main__":
    main()