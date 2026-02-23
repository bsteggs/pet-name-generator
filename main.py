import streamlit as st
import langchain_helper as lch

st.set_page_config(
    page_title="Pet Name Generator",
    page_icon="🐾",
    layout="centered",
)

st.title("🐾 Pet Name Generator")
st.caption("Now with personality-based naming")

# ---------------- Sidebar ----------------

st.sidebar.header("Customize")

animal_type = st.sidebar.selectbox(
    "Pet type",
    ("Dog", "Cat", "Rabbit", "Horse", "Hamster"),
)

pet_color = st.sidebar.text_input(
    "Color",
    max_chars=25,
    placeholder="white, black, golden...",
)

style = st.sidebar.selectbox(
    "Style",
    ("Cute", "Cool", "Funny", "Mythical", "Elegant"),
)

personality = st.sidebar.text_input(
    "Personality traits",
    max_chars=40,
    placeholder="playful, lazy, chaotic...",
)

count = st.sidebar.slider(
    "Number of names",
    min_value=5,
    max_value=20,
    value=5,
)

st.sidebar.caption("Example personality: sleepy, royal, mischievous")

# ---------------- Generator ----------------

st.divider()

if st.button("✨ Generate names", use_container_width=True):

    if not pet_color:

        st.warning("Please enter a color")

    else:

        with st.spinner("Generating..."):

            result = lch.generate_pet_names(

                animal_type=animal_type.lower(),
                pet_color=pet_color.lower(),
                style=style.lower(),
                personality=personality.lower() if personality else "neutral",
                count=count,
            )

        st.subheader("Results")

        st.markdown(result)