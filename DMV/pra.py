# Data Visualization Project: Indian Retail Sales
# Dataset: india_retail_sales_dataset.csv
# Install once in terminal/Jupyter:
# pip install pandas plotly matplotlib networkx

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx

# 1. Load database (CSV file)
df = pd.read_csv("india_retail_sales_dataset.csv")
print(df.head())
print("Rows and columns:", df.shape)
print(df.isnull().sum())

# Aggregate sales for all visualizations
sales_by_region_category = (
    df.groupby(["Region", "Category"], as_index=False)["Sales"].sum()
)
sales_by_category_segment = (
    df.groupby(["Category", "Segment"], as_index=False)["Sales"].sum()
)

# 2. SANKEY DIAGRAM: Region -> Category -> Segment
links1 = sales_by_region_category.rename(
    columns={"Region": "source_name", "Category": "target_name", "Sales": "value"}
)
links2 = sales_by_category_segment.rename(
    columns={"Category": "source_name", "Segment": "target_name", "Sales": "value"}
)
links = pd.concat([links1, links2], ignore_index=True)
labels = list(pd.unique(pd.concat([links["source_name"], links["target_name"]])))
label_to_id = {label: i for i, label in enumerate(labels)}
fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels, pad=15, thickness=18),
    link=dict(
        source=links["source_name"].map(label_to_id),
        target=links["target_name"].map(label_to_id),
        value=links["value"]
    )
)])
fig.update_layout(title_text="Sales Flow: Region to Category to Segment", font_size=10)
fig.show()

# 3. SUNBURST: Region -> Category -> SubCategory
sun = df.groupby(["Region", "Category", "SubCategory"], as_index=False)["Sales"].sum()
fig = px.sunburst(
    sun, path=["Region", "Category", "SubCategory"], values="Sales",
    title="Sunburst of Sales by Region, Category and Subcategory"
)
fig.show()

# 4. TREEMAP: Region -> Category -> SubCategory
fig = px.treemap(
    sun, path=["Region", "Category", "SubCategory"], values="Sales",
    title="Treemap of Sales by Region, Category and Subcategory"
)
fig.show()

# 5. 3D GEOGRAPHIC SALES VIEW
# Longitude and latitude show city locations; sales are shown on the Z axis.
city_sales = df.groupby(
    ["City", "State", "Region", "Latitude", "Longitude"], as_index=False
)["Sales"].sum()
fig = px.scatter_3d(
    city_sales, x="Longitude", y="Latitude", z="Sales",
    color="Region", size="Sales", hover_name="City",
    hover_data=["State", "Sales"],
    title="3D Geographic View of Sales Across Indian Cities",
    labels={"Longitude": "Longitude", "Latitude": "Latitude", "Sales": "Total Sales"}
)
fig.show()

# 6. NETWORKX GRAPH: Region - Category - Subcategory relationships
G = nx.Graph()
region_category = df.groupby(["Region", "Category"])["Sales"].sum().reset_index()
category_subcat = df.groupby(["Category", "SubCategory"])["Sales"].sum().reset_index()

for _, row in region_category.iterrows():
    G.add_edge(row["Region"], row["Category"], weight=float(row["Sales"]))
for _, row in category_subcat.iterrows():
    G.add_edge(row["Category"], row["SubCategory"], weight=float(row["Sales"]))

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42, k=0.8)
node_colors = []
for node in G.nodes():
    if node in df["Region"].unique():
        node_colors.append("cornflowerblue")
    elif node in df["Category"].unique():
        node_colors.append("orange")
    else:
        node_colors.append("lightgreen")
node_sizes = [500 + 80 * G.degree(n) for n in G.nodes()]
edge_widths = [
    max(0.5, min(5, G[u][v]["weight"] / max(nx.get_edge_attributes(G, "weight").values()) * 5))
    for u, v in G.edges()
]
nx.draw_networkx(
    G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
    font_size=8, width=edge_widths, edge_color="gray"
)
plt.title("NetworkX Relationship Graph: Region, Category and Subcategory")
plt.axis("off")
plt.tight_layout()
plt.show()

# Optional: save charts as HTML files instead of only viewing them:
# fig.write_html("chart_name.html")  # add immediately before each fig.show()
