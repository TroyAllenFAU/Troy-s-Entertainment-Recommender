import streamlit as st
import math

# Dataset
dataset = [
    {"name": "The Witcher 3", "features": [1, 0, 10, 9, 9]},
    {"name": "Skyrim", "features": [1, 0, 9, 8, 10]},
    {"name": "Call of Duty", "features": [2, 1, 6, 8, 6]},
    {"name": "Fortnite", "features": [5, 1, 4, 8, 7]},
    {"name": "Minecraft", "features": [3, 1, 5, 7, 10]},
    {"name": "Cyberpunk 2077", "features": [1, 0, 8, 9, 8]},
    {"name": "Resident Evil", "features": [4, 0, 7, 8, 6]},
    {"name": "Dark Souls", "features": [1, 0, 6, 9, 7]},
    {"name": "Stranger Things", "features": [4, 0, 8, 8, 7]},
    {"name": "Breaking Bad", "features": [5, 0, 10, 9, 8]},
    {"name": "The Last of Us", "features": [1, 0, 10, 9, 7]},
    {"name": "Apex Legends", "features": [2, 1, 5, 9, 6]},
    {"name": "Red Dead Redemption 2", "features": [5, 0, 10, 10, 9]},
    {"name": "The Walking Dead", "features": [4, 0, 8, 7, 8]},
    {"name": "Elden Ring", "features": [1, 0, 7, 10, 9]},
]

# Distance function
def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i])**2 for i in range(len(a))))

# Recommendation function
def get_recommendations(selected_item, dataset, k=3):
    target_features = None
    
    for item in dataset:
        if item["name"] == selected_item:
            target_features = item["features"]
            break
    
    distances = []
    
    for item in dataset:
        if item["name"] != selected_item:
            dist = euclidean_distance(target_features, item["features"])
            distances.append((item["name"], dist))
    
    distances.sort(key=lambda x: x[1])
    
    return distances[:k]

# UI
st.title("🎮 Game & Show Recommender")

st.write("Pick something you like and get recommendations!")

names = [item["name"] for item in dataset]

selected = st.selectbox("Choose a game or show:", names)

k = st.slider("How many recommendations?", 1, 5, 3)

if st.button("Recommend"):
    results = get_recommendations(selected, dataset, k)
    
    st.subheader("Recommended for you:")
    
    for name, dist in results:
        st.write(f"**{name}** (similarity score: {round(dist, 2)})")