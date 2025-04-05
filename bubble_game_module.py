import streamlit as st

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

    # Initialize session state variables safely
    if "feeling" not in st.session_state:
        st.session_state.feeling = ""
    if "flushed" not in st.session_state:
        st.session_state.flushed = False

    if not st.session_state.flushed:
        feeling = st.text_input("😞 Type what you're feeling:")

        if feeling:
            st.session_state.feeling = feeling
            st.markdown(f'<div class="feeling-box">💭 "{feeling}"</div>', unsafe_allow_html=True)
            st.image("https://cdn-icons-png.flaticon.com/512/5117/5117343.png", width=100, caption="Toilet 🚽")

            flush = st.button("🚽 Flush it away!")
            if flush:
                st.session_state.flushed = True
                # No rerun needed, we check the state on next reload
                st.experimental_rerun()
    else:
        st.success("🎉 Your feeling has been flushed away.")
        st.markdown(f"'{st.session_state.feeling}' is gone. You're stronger now. 💪")
        st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=300)
        st.balloons()

        if st.button("🔄 Start Again"):
            st.session_state.flushed = False
            st.session_state.feeling = ""
            st.experimental_rerun()
if __name__ == "__main__":
    run()
