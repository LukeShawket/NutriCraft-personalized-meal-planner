import streamlit as st
import pandas as pd
import recommendation_logic as rl
import plotly.express as px
import visualizations as vs

image1 = "https://images.unsplash.com/photo-1742054292309-d07b8f18b0ef?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
image2 = "https://images.unsplash.com/photo-1603569283847-aa295f0d016a?q=80&w=1972&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
image3 = "https://images.unsplash.com/photo-1606728035253-49e8a23146de?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
image4 = "https://images.unsplash.com/photo-1622621746668-59fb299bc4d7?q=80&w=2133&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"


st.set_page_config(
    layout="wide"   
)
st.markdown("# NutriCraft")
st.markdown("##### :rainbow[NutriCraft] is an innovative, personalized meal planning application designed to empower users in achieving their nutritional goals through smart, data-driven recommendations. By seamlessly integrating user preferences, dietary restrictions, and health goals, NutriCraft delivers tailored meal suggestions that are both nutritious and delicious.")


data_path = "final_dataset.csv"
levels = ["Low", "Moderate", "High"]

df = rl.load_data(data_path)


st.sidebar.title("Filters")

is_main = True

recommends = []

child_selection = st.sidebar.selectbox(
    "Nutrition Flter:", 
    ["Filter by Calorie", "Filter by Fat", "Filter by Sugar", "Filter by Protein", "Filter by Dietary Fiber", "Filter All"]
)

if child_selection == "Filter by Calorie":
    calorie_selection = st.sidebar.selectbox(
    "Calories:", 
    ["Low", "Moderate", "High"]
    )

if child_selection == "Filter by Fat":
    fat_selection = st.sidebar.selectbox(
    "Fat:", 
    ["Low", "Moderate", "High"]
    )
    
if child_selection == "Filter by Sugar":
    sugar_selection = st.sidebar.selectbox(
    "Sugar:", 
    ["Low", "Moderate", "High"]
    )
    
if child_selection == "Filter by Protein":
    protein_selection = st.sidebar.selectbox(
    "Protein:", 
    ["Low", "Moderate", "High"]
    )
    
if child_selection == "Filter by Dietary Fiber":
    fiber_selection = st.sidebar.selectbox(
    "Dietary Fiber:", 
    ["Low", "Moderate", "High"]
    )
    
if child_selection == "Filter All":
    calorie_selection = st.sidebar.selectbox(
    "Calories:", 
    ["Low", "Moderate", "High"]
    )
    fat_selection = st.sidebar.selectbox(
    "Fat:", 
    ["Low", "Moderate", "High"]
    )
    sugar_selection = st.sidebar.selectbox(
    "Sugar:", 
    ["Low", "Moderate", "High"]
    )
    protein_selection = st.sidebar.selectbox(
    "Protein:", 
    ["Low", "Moderate", "High"]
    )
    fiber_selection = st.sidebar.selectbox(
    "Dietary Fiber:", 
    ["Low", "Moderate", "High"]
    )
    

results = st.sidebar.slider(
    "Results", 
    min_value=1, 
    max_value=10, 
    value=5
    )
    
def result_chart(recommends):
    if len(recommends) >= results:
            # Sample results
            sampled_foods = recommends.sample(results)
            _index = 1
            st.balloons()
            # Loop through each food item in the sampled DataFrame
            for _, food_row in sampled_foods.iterrows():  # Loop through rows as Series
                # Display the food name
                st.markdown(f"### {_index}. **:rainbow[{food_row['food'].title()}]**")  # Use the 'food' column to display name
                _index += 1
                # Summarize nutritional columns for the bar chart
                selected_columns = food_row[['Caloric Value', 'Fat', 'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol', 'Iron']]
                selected_columns_pie = food_row[['Vitamin A', 'Vitamin B1', 'Vitamin B11', 'Vitamin B12', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K']]
                selected_columns_pie = selected_columns_pie.reset_index()
                selected_columns_pie.columns = ["Nutrient", "Value"]
                filtered_data = selected_columns_pie[selected_columns_pie["Value"] > 0] 

                
                # Convert data for visualizations
                bar_data = pd.DataFrame({
                    "Nutrient": selected_columns.index,
                    "Value": selected_columns.values
                })
                #pie_data = filtered_data.reset_index()
                #pie_data.columns = ["Nutrient", "Value"]
                pie_data = filtered_data.reset_index(drop=True)


                # Create two columns for side-by-side display
                col1, col2 = st.columns(2)

                # Bar chart in the first column
                with col1:
                    bar_fig = px.bar(bar_data, x="Nutrient", y="Value", title="Nutritional Breakdown")
                    st.plotly_chart(bar_fig, use_container_width=True)

                # Pie chart in the second column
                with col2:
                    pie_fig = px.pie(pie_data, names="Nutrient", values="Value", title="Nutritional Composition")
                    #pie_fig.update_traces(textinfo='none')
                    st.plotly_chart(pie_fig, use_container_width=True, key=f"chart_{_index}")



    else:
        st.text(f"There is no {results} recommendations")

s_col1, s_col2 = st.sidebar.columns(2)
if s_col1.button("Filter"):
    is_main = False
    if child_selection == "Filter by Calorie":

        recommends = rl.filter_recommendations_single(df=df, value=calorie_selection, by="calorie")
        # Check if recommendations meet the required count
        result_chart(recommends)

    if child_selection == "Filter by Fat":
        recommends = rl.filter_recommendations_single(df=df, value=fat_selection, by="fat")
        result_chart(recommends)

    if child_selection == "Filter by Sugar":
        recommends = rl.filter_recommendations_single(df=df, value=sugar_selection, by="sugar")
        result_chart(recommends)
    if child_selection == "Filter by Protein":
        recommends = rl.filter_recommendations_single(df=df, value=protein_selection, by="protein")
        result_chart(recommends)

    if child_selection == "Filter by Dietary Fiber":
        recommends = rl.filter_recommendations_single(df=df, value=fiber_selection, by="fiber")
        result_chart(recommends)

    if child_selection == "Filter All":
        recommends = rl.filter_recommendations_by_all(df=df, calorie=calorie_selection, fat=fat_selection,sugar=sugar_selection,protein=protein_selection, fiber=fiber_selection)
        result_chart(recommends)

main_col1, main_col2 = st.columns(2)
if s_col2.button("Home"):
    st.balloons()
    is_main = True

if is_main:
    main_col1.markdown("### 1. :rainbow[Caloric Value Distribution]\n"
    "* Low-Calorie Foods: Foods that fall into the lower calorie ranges (e.g., under 500 calories) are great for health-conscious users or those focusing on light meals.\n"
    "* High-Calorie Foods: Outliers in the higher calorie ranges (e.g., above 1500 calories) could indicate indulgent or energy-dense meals.\n"
    "* Overall Trends: The distribution reveals whether your dataset leans towards low-calorie foods, has balanced options across ranges, or focuses on richer meals.")
    vs.Caloric_Value_Distribution(main_col1)
    main_col2.markdown("<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col2.image(image1, use_container_width=True)
    main_col2.markdown("<br><br>\n<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col2.markdown("### 2. :rainbow[Nutrition Density Comparison]\n"
    "* The Nutrition Density Comparison chart displays the top 10 foods based on their nutrient-to-calorie ratio, providing insight into the most nutrient-packed items in the dataset. Here's the description tailored to the chart:")
    vs.Nutrition_Density(main_col2)
    main_col1.markdown("<br><br>", unsafe_allow_html=True)
    main_col1.image(image2, use_container_width=True)
    main_col1.markdown("<br><br>\n<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col1.markdown("### 3. :rainbow[Fat Composition Breakdown]\n"
    "* The chart highlights the fat composition of the top 10 high-fat foods, giving a clear view of how each type of fat contributes to the total fat content.\n"
    "* Goose Meat Raw has the highest total fat content, dominated by Monounsaturated Fats.\n"
    "* Foods such as Nutmeg Butter Oil and Menhaden Fish Oil are rich in Polyunsaturated Fats, often considered healthier fats for cardiovascular health.")
    vs.fat_composition(main_col1)
    main_col2.markdown("<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col2.image(image3, use_container_width=True)
    main_col2.markdown("<br><br>\n<br><br>\n<br><br>\n<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col2.markdown("### 4. :rainbow[Carbohydrates vs. Sugars Comparison]\n"
    "* This visualization allows users to identify foods that align with their dietary preferences, such as finding low-sugar or balanced-carb options\n"
    "* It helps users explore how carbohydrates and sugars are distributed across a smaller, randomized subset of foods, providing insights into the nutritional composition without overwhelming the interface with the full dataset.")
    main_col1.markdown("<br><br>\n<br><br>", unsafe_allow_html=True)
    main_col1.image(image4, use_container_width=True)
    vs.Carbohydrates_Sugars(main_col2)

