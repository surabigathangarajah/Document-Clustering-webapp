# Webapp/app.py
import streamlit as st
import pandas as pd
import os

# --- Load CSV safely ---
BASE_DIR = os.path.dirname(__file__)  # folder where app.py is located
csv_path = os.path.join(BASE_DIR, 'bbc_clustered.csv')
df = pd.read_csv(csv_path)

# --- Map cluster numbers to meaningful topic names ---
cluster_names = {
    0: 'Politics',
    1: 'War',
    2: 'Sports',
    3: 'General',
    4: 'Crime'
}

# --- Sidebar ---
st.sidebar.title("Select Topic")
# list of topic names for selectbox
topics = [cluster_names[c] for c in sorted(df['cluster'].unique())]
selected_topic = st.sidebar.selectbox("Select Cluster", topics)

# Convert selected topic back to cluster number
selected_cluster = [k for k, v in cluster_names.items() if v == selected_topic][0]

# --- Main App ---
st.title("BBC News Document Clustering")
st.write(f"Showing articles for topic: {selected_topic}")

# Filter articles by cluster number
cluster_articles = df[df['cluster'] == selected_cluster]

# Optional search within selected cluster
search_term = st.text_input("Search within topic (optional)").lower()

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
