import streamlit as st
import pandas as pd

# -----------------------------
# Load the CSV file
# -----------------------------
df = pd.read_csv('bbc_clustered.csv')

# -----------------------------
# Mapping cluster numbers to friendly names
# -----------------------------
cluster_names = {
    0: "Politics",
    1: "War/Ukraine",
    2: "Sports",
    3: "General",
    4: "Crime"
}

# -----------------------------
# Streamlit title and description
# -----------------------------
st.title("📰 BBC News Clustering Web App")
st.write("Explore BBC articles by topic!")

# -----------------------------
# Sidebar dropdown: only one
# -----------------------------
selected_cluster_name = st.sidebar.selectbox(
    "Select Topic",
    [cluster_names[i] for i in df['cluster'].unique()]
)

# Convert selected name back to cluster number
selected_cluster = [k for k, v in cluster_names.items() if v == selected_cluster_name][0]

# -----------------------------
# Display top words per cluster (optional)
# -----------------------------
if 'top_words' in df.columns:
    st.subheader(f"Top words in {selected_cluster_name}")
    top_words_list = df[df['cluster'] == selected_cluster]['top_words'].iloc[0].split(',')  # assuming CSV has 'top_words' column
    st.write(", ".join(top_words_list))

# -----------------------------
# Filter articles by selected cluster
# -----------------------------
filtered_articles = df[df['cluster'] == selected_cluster]

# -----------------------------
# Display articles
# -----------------------------
st.subheader(f"Articles in {selected_cluster_name}")
for idx, row in filtered_articles.iterrows():
    st.markdown(f"### [{row['title']}]({row['link']})")
    st.write(row['description'])
    st.markdown("---")
# Filter articles by selected cluster first
filtered_articles = df[df['cluster'] == selected_cluster]

# Then filter by search term if any
search_term = st.sidebar.text_input("Search articles")
if search_term:
    filtered_articles = filtered_articles[
        filtered_articles['title'].str.contains(search_term, case=False, na=False)
    ]
