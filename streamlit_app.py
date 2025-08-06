import streamlit as st
import random

st.set_page_config(page_title="Team Divider", layout="centered")

st.title("🎲 Team Divider")
st.markdown("Zadej jména hráčů, každé na nový řádek. Klikni na **Vytvořit**, a rozdělíme je náhodně do dvou týmů.")

# Textové pole
names_input = st.text_area("Zadej jména zde:", height=300, placeholder="Např.:\nAlice\nBob\nCharlie\nDavid")

# Tlačítko pro vytvoření týmů
if st.button("Vytvořit týmy"):
    players = [name.strip() for name in names_input.splitlines() if name.strip()]

    if len(players) < 2:
        st.warning("Zadej alespoň 2 jména!")
    else:
        random.shuffle(players)
        half = len(players) // 2
        team_1 = players[:half]
        team_2 = players[half:]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🏆 Tým 1")
            st.markdown("\n".join(team_1))

        with col2:
            st.subheader("🏆 Tým 2")
            st.markdown("\n".join(team_2))
