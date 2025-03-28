import pandas as pd

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function for recommendation logic
def filter_recommendations_by_all(df, calorie, fat, sugar, protein, fiber):
    recommendations = df[
        (df["Caloric Value_Level"] == calorie) &
        (df["Fat_Level"] == sugar) &
        (df["Sugars_Level"] == fat) &
        (df["Protein_Level"] == protein) &
        (df["Dietary Fiber_Level"] == fiber)
    ]
    return recommendations

def filter_recommendations_single(df, value, by):
    if by == "calorie":
        recommendations = df[
            (df["Caloric Value_Level"] == value)
        ]
    if by == "fat":
        recommendations = df[
            (df["Fat_Level"] == value)
        ]
    if by == "sugar":
        recommendations = df[
            (df["Sugars_Level"] == value)
        ]
    if by == "protein":
        recommendations = df[
            (df["Protein_Level"] == value)
        ]
    if by == "fiber":
        recommendations = df[
            (df["Dietary Fiber_Level"] == value)
        ]
    return recommendations