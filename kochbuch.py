import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Daten für das virtuelle Kochbuch mit vier Rezepten
kochbuch = pd.DataFrame({
    'Rezept': ['Pasta Carbonara', 'Hähnchenbrust mit Gemüse', 'Apfelkuchen', 'Tomatensuppe'],
    'Zutaten': [
        ['Spaghetti', 'Eier', 'Speck', 'Parmesan', 'Salz', 'Pfeffer'],
        ['Hähnchenbrust', 'Paprika', 'Zucchini', 'Karotten', 'Knoblauch', 'Olivenöl'],
        ['Äpfel', 'Mehl', 'Zucker', 'Butter', 'Zimt', 'Zitrone'],
        ['Tomaten', 'Zwiebeln', 'Knoblauch', 'Gemüsebrühe', 'Olivenöl', 'Basilikum']
    ],
    'Anleitung': [
        '1. Speck anbraten\n2. Eier und geriebenen Parmesan hinzufügen\n3. Mit gekochten Spaghetti vermengen\n4. Mit Salz und Pfeffer würzen',
        '1. Hähnchenbrust anbraten\n2. Gemüse schneiden und hinzufügen\n3. Alles zusammen braten\n4. Mit Knoblauch und Olivenöl würzen',
        '1. Äpfel schälen und schneiden\n2. Teig aus Mehl, Zucker und Butter herstellen\n3. Äpfel auf Teig verteilen\n4. Mit Zimt und Zitronensaft würzen',
        '1. Zwiebeln und Knoblauch anbraten\n2. Tomaten hinzufügen und köcheln lassen\n3. Mit Gemüsebrühe aufgießen und pürieren\n4. Mit Olivenöl und Basilikum garnieren'
    ]
})

# Text elements
st.title('Virtuelles Kochbuch')
st.write('Willkommen zu unserem virtuellen Kochbuch!')

# Data elements
st.header('Rezepte')
st.write(kochbuch)

# Input Widgets
selected_recipe = st.selectbox('Wähle ein Rezept aus', kochbuch['Rezept'])
selected_recipe_index = kochbuch[kochbuch['Rezept'] == selected_recipe].index[0]
st.subheader(selected_recipe)
st.write('Zutaten:', ', '.join(kochbuch.at[selected_recipe_index, 'Zutaten']))

# Widget für Lebensmittel und Menge
st.header('Zutaten und Menge')
checked_ingredients = {}
for ingredient in kochbuch.at[selected_recipe_index, 'Zutaten']:
    checked = st.checkbox(ingredient)
    checked_ingredients[ingredient] = checked
    if checked:
        quantity = st.number_input(f'Menge von {ingredient}', min_value=0, value=0)

# Chart elements
st.header('Zutatenverteilung')
ingredients = kochbuch.at[selected_recipe_index, 'Zutaten']
unique_ingredients = list(set(ingredients))
ingredient_counts = [ingredients.count(ingredient) for ingredient in unique_ingredients]

fig, ax = plt.subplots()
ax.pie(ingredient_counts, labels=unique_ingredients, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Sidebar as example layout
st.sidebar.header('Einstellungen')

# Containers (in diesem Fall nicht relevant für das Kochbuch)