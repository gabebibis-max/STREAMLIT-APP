import streamlit as st
st.title("Minha primeira app")
nome= st.text_input("Qual seu nome?")
idade= st.slider("Sua idade",0,100)
if st.button("Enviar"):
  st.success(f"olá {nome}, voce tem {idade} anos!")
  st.subheader("comentário")
  comentario= st.text_area("escreva algo")
  if cmentario:
    st.write("Voce escreveu:"< comentario)
