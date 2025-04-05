import streamlit as st

def run():
    st.title("🚽 Flush the Bad Feels")

    st.write("Write down what's bothering you...")

    if "flushed" not in st.session_state:
        st.session_state["flushed"] = False

    if not st.session_state["flushed"]:
        feeling = st.text_input("Your negative feeling", key="input_feeling")

        if feeling:
            st.markdown(f"""
                <div style='
                    margin-top: 30px;
                    padding: 15px;
                    border-radius: 10px;
                    background-color: #ffdddd;
                    width: fit-content;
                    font-size: 20px;
                    border: 2px solid red;
                '>
                    💭 "{feeling}"
                </div>
                <br>
                <img src='https://i.imgur.com/V7nH1gD.png' width='150'><br>
                """, unsafe_allow_html=True)

            if st.button("🚽 Flush it away!"):
                st.session_state["flushed"] = True
                st.experimental_rerun()

    else:
        st.success("🌈 Your feeling has been flushed away. You're lighter now!")
        st.balloons()
        st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=300)
        if st.button("😌 Start over"):
            st.session_state["flushed"] = False
            st.experimental_rerun()

