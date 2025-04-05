import streamlit as st

# Basic list of negative keywords (you can expand this)
NEGATIVE_FEELINGS = ["sad", "angry", "anxious", "worried", "depressed", "lonely", "tired", "upset", "frustrated"]

def is_negative(feeling: str) -> bool:
    feeling = feeling.lower()
    return any(word in feeling for word in NEGATIVE_FEELINGS)

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

    if "flushed" not in st.session_state:
        st.session_state["flushed"] = False
        st.session_state["celebrated"] = False
        st.session_state["feeling"] = ""

    if not (st.session_state["flushed"] or st.session_state["celebrated"]):
        feeling = st.text_input("😞 Type what you're feeling:")

        if feeling:
            st.session_state["feeling"] = feeling
            st.markdown(f'<div class="feeling-box">💭 "{feeling}"</div>', unsafe_allow_html=True)

            if is_negative(feeling):
                st.image("toilet.png", width=100, caption="Toilet 🚽")
                if st.button("🚽 Flush it away!"):
                    st.session_state["flushed"] = True
            else:
                if st.button("🎉 Celebrate this feeling!"):
                    st.session_state["celebrated"] = True

    elif st.session_state["flushed"]:
        st.success("🎉 Your negative feeling has been flushed away.")
        st.markdown(f"'{st.session_state['feeling']}' is gone. You're stronger now. 💪")
        st.image("toilet.png", width=300)
        st.balloons()
        if st.button("🔄 Start Again"):
            st.session_state["flushed"] = False
            st.session_state["feeling"] = ""

    elif st.session_state["celebrated"]:
        st.success("🌟 Let's cherish this beautiful emotion!")
        st.markdown(f"You're feeling: '{st.session_state['feeling']}' — and that's amazing! 💖")
        st.image("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif", width=300)
        st.balloons()
        if st.button("🔄 Start Again"):
            st.session_state["celebrated"] = False
            st.session_state["feeling"] = ""

if __name__ == "__main__":
    run()
