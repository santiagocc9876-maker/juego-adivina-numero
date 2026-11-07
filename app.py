import streamlit as st
import random

# título de la página web
st.title("🎮 Juego: Adivina el Número")
st.write("He pensado en un número entre **1 y 100**. ¡Intenta adivinarlo!")

# 1. Inicializamos el estado del juego
if "numero_secreto" not in st.session_state:
  st.session_state.numero_secreto = random.randint(1, 100)
  st.session_state.intentos = 0
  st.session_state.juego_terminado = False

# 2. Formulario para ingresar la suposición
with st.form(key='formulario_juego', clear_on_submit=True):
  intento_usuario = st.number_input(
      "Introduce tu suposición:",
      min_value=1,
      max_value=100,
      step=1
  )
  boton_enviar = st.form_submit_button(label="Adivinar")

# 3. Lógica al enviar el número
if boton_enviar and not st.session_state.juego_terminado:
  st.session_state.intentos += 1

  if intento_usuario < st.session_state.numero_secreto:
    st.warning(f"Tu número ({intento_usuario}) es **demasiado bajo**. ¡Prueba con uno más alto!")
  elif intento_usuario > st.session_state.numero_secreto:
    st.warning(f"Tu número ({intento_usuario}) es **demasiado alto**. ¡Prueba con uno más bajo!")
  else:
    st.session_state.juego_terminado = True
    st.success(f"🎉 ¡Felicidades! Adivinaste el número en **{st.session_state.intentos} intentos**.")

# 4. Botón para reiniciar el juego si terminó
if st.session_state.juego_terminado:
  if st.button("Jugar de nuevo"):
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.intentos = 0
    st.session_state.juego_terminado = False
    st.rerun()

# Mostrar contador de intentos actuales si el juego sigue activo
if not st.session_state.juego_terminado and st.session_state.intentos > 0:
  st.info(f"Intentos actuales: {st.session_state.intentos}")
