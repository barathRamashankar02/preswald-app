from preswald import text, plotly, connect, get_df, table, query, slider, sidebar
import plotly.express as px

# App Header
text("🥘 Indian Food Nutrition Explorer")
text("Explore the calories, proteins, and other nutrition facts of popular Indian dishes!")


# Load Dataset
connect()
df = get_df('food_csv')

# Calorie Threshold Slider
calorie_threshold = slider("Minimum Calories (kcal)", min_val=0, max_val=1200, default=300)

# SQL 
sql = f'SELECT "Dish Name", "Calories (kcal)", "Protein (g)", "Fats (g)", "Carbohydrates (g)" FROM food_csv WHERE "Calories (kcal)" > {calorie_threshold}'
high_calorie_df = query(sql, "food_csv")

table(high_calorie_df, title=f"🥗 Dishes with more than {calorie_threshold} kcal")

# Viz 1: Calories vs Proteins Bubble Chart
fig1 = px.scatter(
    high_calorie_df,
    x="Protein (g)", 
    y="Calories (kcal)",
    size="Fats (g)",
    hover_name="Dish Name",
    title="Protein vs Calories (Bubble size = Fats)",
    labels={"Protein (g)": "Protein (g)", "Calories (kcal)": "Calories (kcal)"},
)

plotly(fig1)

# Viz 2: Top 10 High-Calorie Dishes Bar Chart
top10_df = df.sort_values("Calories (kcal)", ascending=False).head(10)
fig2 = px.bar(
    top10_df,
    x="Dish Name",
    y="Calories (kcal)",
    title="Top 10 High-Calorie Indian Dishes",
    color="Calories (kcal)",
    labels={"Calories (kcal)": "Calories"},
)
fig2.update_layout(xaxis_tickangle=-45)
plotly(fig2)