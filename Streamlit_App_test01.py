# My first streamlit app
# Explore Iris Dataset
#
# Requirements:
# Python, Version 3.10.18
# Streamlit, Version 1.36.0
# plotly, Version: 6.3.1
# matplotlib, Version: 3.10.6
# pandas, Version: 2.3.2
#

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy



# Add title and header
st.title("My first project with Streamlit")
st.header("Iris Data Exploration")


df = px.data.iris()

# Create a checkbox
show_data = st.checkbox("Show Dataset")

# Conditionally display the DataFrame
if show_data:
    st.write("### Iris Dataset Preview")
    st.dataframe(df)
else:
    st.info("✅ Dataset hidden. Check the box above to view it.")


# uniqueness of each column
st.header("Uniqueness of each column")
st.write(df.nunique())

# df.dtypes
#------------------------

st.title("🌸 Explore Iris - based on each 'species' type")

# --- Step 1: Create dropdown options ---
# We'll use the "species" column for filtering
species_list = ["All"] + sorted(df["species"].unique().tolist())

# --- Step 2: Add dropdown (selectbox) ---
selected_species = st.selectbox(
    "Select Iris species:",
    options=species_list
)

# --- Step 3: Filter dataset based on dropdown ---
if selected_species == "All":
    filtered_df = df
else:
    filtered_df = df[df["species"] == selected_species]

# --- Step 4: Show data ---
st.write(f"### Showing data for: {selected_species}")
st.dataframe(filtered_df)

# --- Step 5: Optional — plot a scatter chart ---
fig = px.scatter(
    filtered_df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    title=f"Iris Sepal Dimensions ({selected_species})",
    size="petal_length",
    hover_data=["petal_width"]
)

st.plotly_chart(fig, use_container_width=True)

#---------
# --- Step 1: Add radio button ---
import streamlit as st
import plotly.express as px
import pandas as pd

# Load Iris dataset
df = px.data.iris()

st.title("🌸 Interactive Iris Dataset Visualizer")

# --- Step 1: Add radio button ---
mode = st.radio(
    "Choose view mode:",
    ["Before", "After"],
    horizontal=True
)

# --- Step 2: Transform data depending on mode ---
# (You can simulate a condition — e.g., scaling values or filtering)
if mode == "Before":
    df_display = df.copy()
else:
    # Example: simulate “After” by scaling petal lengths
    df_display = df.copy()
    df_display["petal_length"] = df_display["petal_length"] * 3.5


# --- Step 3: Scatter Plot ---

# mode = st.radio("Choose view mode:", ["Before", "After"], horizontal=True)

df_display = df.copy()
if mode == "After":
    df_display["petal_length"] *= 1.5  # Scale up visibly

# --- Scatter plot ---
size_factor = 5 if mode == "Before" else 10  # make "After" dots bigger

fig = px.scatter(
    df_display,
    x="sepal_length",
    y="sepal_width",
    color="species",
    size="petal_length",
    size_max=size_factor,  # control visible size difference
    title=f"Scatter Plot ({mode})",
    hover_data=["petal_width"]
)
st.plotly_chart(fig, use_container_width=True)


# --- Step 4: Bar Chart ---
st.subheader("Bar Chart: Average Petal Length per Species")
bar_data = df_display.groupby("species", as_index=False)["petal_length"].mean()
fig_bar = px.bar(
    bar_data,
    x="species",
    y="petal_length",
    color="species",
    title=f"Bar Chart ({mode})"
)
st.plotly_chart(fig_bar, use_container_width=True)

st.success(f"✅ Mode: {mode} — Both charts updated together!")

