import pandas as pd
import plotly.express as px
import recommendation_logic as rl


data_path = "final_dataset.csv"

df = rl.load_data(data_path)

def Caloric_Value_Distribution(page):
    fig = px.histogram(df, x="Caloric Value", nbins=10)
    page.plotly_chart(fig, use_container_width=True)

def Nutrition_Density(page):
    top_foods = df.nlargest(10, 'Nutrition Density')  # Top 10 by Nutrition Density
    fig = px.bar(top_foods, x='food', y='Nutrition Density')
    page.plotly_chart(fig, use_container_width=True)

def fat_composition(page):
    top_foods = df.nlargest(10, 'Fat')
    fig = px.bar(top_foods, x='food', y=['Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats'], labels={'value': 'Fat Content'})
    page.plotly_chart(fig, use_container_width=True)

def Carbohydrates_Sugars(page):
    sample_data = df.sample(100)

    fig = px.scatter(
        sample_data,
        x='Carbohydrates',
        y='Sugars',
        color='food',
        size_max=100
    )
    page.plotly_chart(fig, use_container_width=True)