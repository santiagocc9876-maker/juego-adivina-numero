import streamlit as st
import random

# titulo de la pagina web
st.title("🎮 juego: adivina el numero")
st.write("he pensado en un numero entre **1 y 100**. ¡intenta adivinarlo!")

# 1. inicializamos el estado del juego (variables que se deben recordar entre clics)
if "numero_secreto" not in st.session_state:
  st.session_state.numero_secreto = random.randint (1, 100)
  st.session_state.intentos = 0
  st.session_state.juego_terminado = false 

# 2. caja de texto y boton para que el usuario ingrese su suposicion
# usamos un formulario para que pueda enviar presionando "enter"
with st.form(key='formulario_juego',clear_on_submit=true):
  intento__usuario = st.number_input(
      "introduce tu suposicion:",
      min_value=1
      max_value=100
      step=1
  )
  boton_enviar = st.form_submit_button(label="adivinar")

  # 3. logica cuando el usuario presiona el boton
  if boton_enviar and not st.session_state.juego_terminado:
    st.session_state.intentos +=1

    # comparamos el numero
    if intento_usuario < st.session_state.numero_secreto:
      st.warning(f"tu numero ({intento_usuario}) es **demasiado bajo**. ¡prueba con uno mas alto!")
      elif intento_usuario > st.session_state.numero_secreto:
        st.warning(f"tu numero({intento_usuario}) es **demasiado alto**. ¡prueba con uno mas bajo!")
        else:
          st,session_state:juego_terminado = True
          st.success(f"🎉¡felicidades! adivinaste el numero en **{st.session_state.intentos} intentos**.")

          # 4. boton para reiniciar el juego si termino
          if st.session_state.juego_terminado:
            if st.button("jugar de nuevo"):
              st.session_state.numero_secreto = random.randint(1, 100)
              st.session_state.intentos = 0
              st.session_state.juego_terminado = False
              st.return()

              # mostrarnos un contador visual de cuantos intentos lleva
              st.info(f"intentos actuales: {st.session_state.intentos}")
