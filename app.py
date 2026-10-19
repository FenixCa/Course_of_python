import streamlit as st

st.title("Sistema de Inventarios")

st.write("Bienvenido Carlos")

nombre = st.text_input("Ingrese su nombre")

if nombre:
    st.success(f"Hola {nombre}")
