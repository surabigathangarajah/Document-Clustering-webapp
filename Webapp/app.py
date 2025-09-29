# Webapp/app.py
import streamlit as st
import pandas as pd
import os

# --- Load CSV safely ---
BASE_DIR = os.path.dirname(__file__)  # folder where app.py is located
csv_path = os.path.join(BASE_DIR, 'bbc_clustered.csv')
df = pd.read_csv(csv_path)

# --- Sidebar ---
st.sidebar.title("Select Topic")
topics = df['cluster'].unique()
selected_cluster = st.sidebar.selectbox("Select Cluster", topics)

# --- Main App ---
st.title("BBC News Document Clustering")
st.write(f"Showing articles for cluster: {selected_cluster}")

# Filter articles by cluster
cluster_articles = df[df['cluster'] == selected_cluster]

# Optional search within selected cluster
search_term = st.text_input("Search within cluster (optional)").lower()

if search_term:
    cluster_articles = cluster_articles[cluster_articles.apply(
        lambda row: search_term in str(row).lower(), axis=1
    )]

# Display articles
for idx, row in cluster_articles.iterrows():
    st.subheader(row['title'])
    st.write(row['description'])
    st.markdown(f"[Read more]({row['link']})")
    st.markdown("---")
