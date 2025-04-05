import streamlit as st
import time

def run():
    st.title("🫧 Bubble Smash: Let Go of Negativity")

    st.markdown(
        """
        <link rel="stylesheet" href="assets/bubble.css">
        """,
        unsafe_allow_html=True,
    )

    if "smashed" not in st.session_state:
        st.session_state["smashed"] = False

    if not st.session_state["smashed"]:
        st.markdown('<div class="bubble" id="bubble">sadness</div>', unsafe_allow_html=True)
        if st.button("💥 Smash the Bubble"):
            st.session_state["smashed"] = True
            st.experimental_rerun()
    else:
        st.markdown('<div class="bubble drained">happy ness</div>', unsafe_allow_html=True)
        st.markdown("### 🌈 It's okay to feel. You're doing great. Here's a little calm for you:")
        st.image("assets/soothing.gif", width=300)
        st.balloons()
