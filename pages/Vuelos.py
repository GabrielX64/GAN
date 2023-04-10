import streamlit as st
from update import *
from streamlit_extras.switch_page_button import switch_page

#def multiplicar_unaescala(mat):
#    m3 =[]
#    
#    for i in range(len(mat)):
#        m3.append([])
#        for j in range(len(mat[0])):
#            m3[i].append(0)
#    
#    for i in range(len(mat)):
#        for j in range(len(mat[0])):
#            for x in range(len(mat)):
#                if mat[i][x] == 1 and mat[x][j] == 1:
#                    m3[i][j]=1
#    
#    #print(f" MATRIZ")
#    #for i in range(len(m3)):
#    #    for j in range(len(m3[0])):
#    #        st.text(f'{m3[i][j]}')
#    #    st.text('\n')
#  
#
#    return m3

def Peru(option,listaP):
    matriz=[[0,1,1,1,1,0,1,1,1],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0],
            [1,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,1,0,0],]

    #st.text(matriz)
    #a = multiplicar_unaescala(matriz)
    #st.text('MATRIZ A')
    #st.text(a)
    for i in range(0,len(listaP)):
        if option == listaP[i]:
            for k in range(len(matriz)):
                if matriz[i][k] == 1:
                    st.text(f'Existe vuelo directo con:{listaP[k]} ')
                                   

def main():
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
    match u.num:
        case 1: 
            listP=['Lima','Trujillo','Chiclayo','Piura','Iquitos','Puerto Maldonado','Cusco','Juliaca','Arequipa']
            option = st.selectbox(
                'Seleccione su punto origen',
                (listP)
            )
            Peru(option,listP)
        case 2:
            option = st.selectbox(
                'Seleccione su punto origen',
                (' ','Quito','Guayaquil')
            )
        case 3:
            option = st.selectbox(
                'Seleccione su punto origen',
                (' ','Caracas')
            )
    #if option != ' ':
    #   st.write(f"Punto de origen: {option}")
    
    back = st.button('Back')
    if back:
        switch_page('Home page')

if __name__=="__main__":
    main()