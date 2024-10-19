import streamlit as st
import random
import matplotlib.pyplot as plt

def monty_hall_game(switch_choice):
    doors = [0, 1, 2]
    car_door = random.choice(doors)
    contestant_choice = random.choice(doors)

    remaining_doors = [door for door in doors if door != contestant_choice and door != car_door]
    host_opens = random.choice(remaining_doors)

    if switch_choice:
        final_choice = [door for door in doors if door != contestant_choice and door != host_opens][0]
    else:
        final_choice = contestant_choice

    win = final_choice == car_door
    return win

def monty_hall_simulation(num_simulations, switch_choice):
    wins = 0
    for _ in range(num_simulations):
        if monty_hall_game(switch_choice):
            wins += 1
    win_rate = wins / num_simulations
    return win_rate

# Interfejs Streamlit
st.title("Symulacja Zagadki Monty'ego Halla")

st.write("Witaj w symulacji zagadki Monty'ego Halla! Możesz zagrać samodzielnie lub uruchomić symulację wielu gier.")

mode = st.selectbox("Wybierz tryb:", ["Gra", "Symulacja"])

if mode == "Gra":
    st.subheader("Tryb Gry")
    doors = [0, 1, 2]
    st.write("Wybierz drzwi (0, 1 lub 2):")
    contestant_choice = st.selectbox("Twój wybór:", doors)

    car_door = random.choice(doors)
    remaining_doors = [door for door in doors if door != contestant_choice and door != car_door]
    host_opens = random.choice(remaining_doors)
    st.write(f"Prezenter otwiera drzwi numer {host_opens}, za którymi jest koza.")

    switch = st.radio("Czy chcesz zmienić swój wybór?", ("Tak", "Nie"))

    if switch == "Tak":
        final_choice = [door for door in doors if door != contestant_choice and door != host_opens][0]
    else:
        final_choice = contestant_choice

    if st.button("Sprawdź wynik"):
        if final_choice == car_door:
            st.success("Gratulacje! Wygrałeś samochód!")
        else:
            st.error("Niestety, wygrałeś kozę.")

elif mode == "Symulacja":
    st.subheader("Tryb Symulacji")
    num_simulations = st.number_input("Podaj liczbę symulacji:", min_value=1, value=1000)
    switch_choice = st.radio("Czy zmieniać wybór w każdej grze?", ("Tak", "Nie"))

    if st.button("Uruchom symulację"):
        switch = True if switch_choice == "Tak" else False
        win_rate = monty_hall_simulation(int(num_simulations), switch)
        st.write(f"Procent wygranych: {win_rate * 100:.2f}%")

        # Wykres wyników
        labels = ['Wygrane', 'Przegrane']
        sizes = [win_rate, 1 - win_rate]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                startangle=90)
        ax1.axis('equal')  # Równe proporcje osi
        st.pyplot(fig1)
