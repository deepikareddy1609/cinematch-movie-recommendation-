import streamlit as st

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141126, #24103e, #101827);
    color: white;
}
h1 {
    color: #ff4d9d;
    text-align: center;
}
.movie-card {
    background: #251e3d;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 CineMatch")
st.subheader("✨ Find your next favourite movie!")
st.write("Discover movies in your favourite language and genre.")

movies = [
    {
        "title": "RRR",
        "language": "Telugu",
        "genre": "Action",
        "rating": 8.0,
        "year": 2022,
        "poster": "https://image.tmdb.org/t/p/w500/nEufeZlyAOLqO2brrs0yeF1lgXO.jpg"
    },
    {
        "title": "Baahubali 2",
        "language": "Telugu",
        "genre": "Action",
        "rating": 8.2,
        "year": 2017,
        "poster": "https://image.tmdb.org/t/p/w500/2c2hY8F4W0x9sK1f0z2K9xQ.jpg"
    },
    {
        "title": "3 Idiots",
        "language": "Hindi",
        "genre": "Comedy",
        "rating": 8.4,
        "year": 2009,
        "poster": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCssoloscw79z8Tew.jpg"
    },
    {
        "title": "Jawan",
        "language": "Hindi",
        "genre": "Action",
        "rating": 7.0,
        "year": 2023,
        "poster": "https://image.tmdb.org/t/p/w500/jFt1gS4BGHlK8xt76Y81Alp4dbt.jpg"
    },
    {
        "title": "Vikram",
        "language": "Tamil",
        "genre": "Thriller",
        "rating": 8.3,
        "year": 2022,
        "poster": "https://image.tmdb.org/t/p/w500/774UV1aCUR6AS1W7Z0z6js9S5g.jpg"
    },
    {
        "title": "Premam",
        "language": "Malayalam",
        "genre": "Romance",
        "rating": 8.3,
        "year": 2015,
        "poster": "https://image.tmdb.org/t/p/w500/q7tJx3w8R5Gf8x9z8w1Y.jpg"
    },
    {
        "title": "Interstellar",
        "language": "English",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "year": 2014,
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "title": "The Avengers",
        "language": "English",
        "genre": "Action",
        "rating": 8.0,
        "year": 2012,
        "poster": "https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg"
    },
    {
        "title": "Mahanati",
        "language": "Telugu",
        "genre": "Drama",
        "rating": 8.4,
        "year": 2018,
        "poster": "https://image.tmdb.org/t/p/w500/6fVv9i5Q7J8w2p7n3x9Y.jpg"
    },
    {
        "title": "Inception",
        "language": "English",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "year": 2010,
        "poster": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"
    }
]

search = st.text_input("🔍 Search for a movie")

languages = ["All"] + sorted(set(m["language"] for m in movies))
genres = ["All"] + sorted(set(m["genre"] for m in movies))

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("🌍 Choose language", languages)

with col2:
    genre = st.selectbox("🎭 Choose genre", genres)

filtered = [
    m for m in movies
    if (language == "All" or m["language"] == language)
    and (genre == "All" or m["genre"] == genre)
    and search.lower() in m["title"].lower()
]

st.markdown("---")
st.subheader("🍿 Recommended Movies")

if filtered:
    cols = st.columns(2)

    for i, movie in enumerate(filtered):
        with cols[i % 2]:
            st.image(movie["poster"], use_container_width=True)
            st.markdown(
                f"### {movie['title']}"
            )
            st.write(f"🌐 Language: {movie['language']}")
            st.write(f"🎭 Genre: {movie['genre']}")
            st.write(f"📅 Year: {movie['year']}")
            st.write(f"⭐ Sample rating: {movie['rating']}/10")
            st.markdown("---")
else:
    st.warning("No movies found. Try another search!")

st.caption("🎬 CineMatch | Discover movies you'll love")
