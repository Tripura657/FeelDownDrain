import streamlit as st
import streamlit.components.v1 as components

# List of negative feelings
NEGATIVE_FEELINGS = [
    "sad", "angry", "anxious", "worried", "depressed",
    "lonely", "tired", "upset", "frustrated"
]

def is_negative(feeling: str) -> bool:
    feeling = feeling.lower()
    return any(word in feeling for word in NEGATIVE_FEELINGS)

def play_flush_sound():
    flush_sound_html = """
        <audio autoplay>
            <source src="https://www.soundjay.com/toilets/sounds/toilet-flush-1.mp3" type="audio/mpeg">
        </audio>
    """
    components.html(flush_sound_html, height=0)

def run():
    st.set_page_config(page_title="Flush Your Feelings 🚽")
    st.title("🧠 Let It Go: Flush Your Feelings")

    st.markdown("""
    <style>
    .feeling-box {
        margin-top: 20px;
        padding: 15px;
        border-radius: 12px;
        background-color: #ffe6e6;
        width: fit-content;
        font-size: 20px;
        border: 2px dashed #ff4d4d;
        animation: wiggle 1s infinite;
    }

    @keyframes wiggle {
      0% { transform: rotate(-2deg); }
      50% { transform: rotate(2deg); }
      100% { transform: rotate(-2deg); }
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "flushed" not in st.session_state:
        st.session_state["flushed"] = False
        st.session_state["celebrated"] = False
        st.session_state["feeling"] = ""

    # Input stage
    if not (st.session_state["flushed"] or st.session_state["celebrated"]):
        feeling = st.text_input("😞 Type what you're feeling:")

        if feeling:
            st.session_state["feeling"] = feeling
            st.markdown(f'<div class="feeling-box">💭 "{feeling}"</div>', unsafe_allow_html=True)

            if is_negative(feeling):
                st.image("https://cdn-icons-png.flaticon.com/512/5117/5117343.png", width=200, caption="Toilet 🚽")
                if st.button("🚽 Flush it away!"):
                    play_flush_sound()
                    st.session_state["flushed"] = True
                    st.experimental_rerun()
            else:
                if st.button("🎉 Celebrate this feeling!"):
                    st.session_state["celebrated"] = True
                    st.experimental_rerun()

    # Flushed stage
    elif st.session_state["flushed"]:
        st.success("🎉 Your negative feeling has been flushed away.")
        st.markdown(f"'{st.session_state['feeling']}' is gone. You're stronger now. 💪")
        st.balloons()

        if st.button("🔄 Start Again"):
            st.session_state["flushed"] = False
            st.session_state["feeling"] = ""
            st.experimental_rerun()

    # Celebrated stage
    elif st.session_state["celebrated"]:
        st.success("🌟 Let's cherish this beautiful emotion!")
        st.markdown(f"You're feeling: '{st.session_state['feeling']}' — and that's amazing! 💖")
        st.balloons()

        if st.button("🔄 Start Again"):
            st.session_state["celebrated"] = False
            st.session_state["feeling"] = ""
            st.experimental_rerun()

if __name__ == "__main__":
    run()
