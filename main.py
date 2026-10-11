import streamlit as st
import random
import time


# Page Config
st.set_page_config(
    page_title="Password Guessing Game",
    page_icon="🔐",
    layout="centered"
)

# CSS
st.markdown("""
<style>


.title{
text-align:center;
font-size:40px;
font-weight:bold;
color:#1565C0;
}

.card{
padding:20px;
border-radius:15px;
background:white;
box-shadow:0px 0px 10px gray;
}

.stButton>button{
width:100%;
border-radius:10px;
font-size:18px;
background:#1565C0;
color:white;
height:45px;
}

</style>
""", unsafe_allow_html=True)


# Word Lists
easy_words = ["apple","train","cat","money","tiger","india","raj","group"]

medium_words = ["python","company","monkey","planet","laptop","pushpa","javascript","numpy"]

hard_words = ["elephant","diamond","umbrella","computer","human","pluto","oneplus","fish"]


# Session State
if "page" not in st.session_state:
    st.session_state.page = "menu"

if "secret" not in st.session_state:
    st.session_state.secret = ""

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = 0


# MENU
if st.session_state.page == "menu":

    st.markdown('<p class="title">🔐 Password Guessing Game</p>', unsafe_allow_html=True)

    st.write("## Welcome Player")

    level = st.selectbox(
        "Choose Difficulty",
        ["easy","medium","hard"]
    )

    if st.button("▶ Start Game"):

        if level=="easy":
            st.session_state.secret=random.choice(easy_words)

        elif level=="medium":
            st.session_state.secret=random.choice(medium_words)

        else:
            st.session_state.secret=random.choice(hard_words)

        st.session_state.level=level
        st.session_state.attempts=0
        st.session_state.start_time=time.time()
        st.session_state.page="game"
        st.rerun()


# GAME
elif st.session_state.page=="game":

    elapsed=int(time.time()-st.session_state.start_time)

    st.title("🎮 Password Guessing Game")

    st.info(f"Difficulty : {st.session_state.level.title()}")

    st.write(f"⏱ Timer : {elapsed} sec")

    st.write(" 👍 You have only Five Attempts to Guess the Word ❤️")

    guess=st.text_input("Enter Your Guess")

    if st.button("Submit Guess"):

        st.session_state.attempts+=1

        st.write(f"❤️ Attempts Left : {5-st.session_state.attempts}")

        if guess.lower()==st.session_state.secret:

            st.balloons()

            st.success(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")

            st.write(f"Time Taken : {elapsed} sec")

        else:

            hint=""

            for i in range(len(st.session_state.secret)):

                if i < len(guess) and guess[i].lower()==st.session_state.secret[i]:

                    hint+=guess[i]

                else:

                    hint+="_"

            st.warning(f"Hint : {hint}")

            if st.session_state.attempts>=5:

                st.error("Game Over!")

                st.write("Correct Password :",st.session_state.secret)

    col1,col2=st.columns(2)

    with col1:

        if st.button("🔄 New Game"):

            st.session_state.page="menu"
            st.rerun()

    with col2:

        if st.button("❌ Exit Game"):

            st.session_state.secret=""
            st.session_state.attempts=0
            st.session_state.page="menu"
            st.rerun()