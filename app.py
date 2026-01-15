import streamlit as st
import os

# Set page title
st.set_page_config(page_title="Coffee Request ☕", page_icon="☕")

# Custom CSS for big, easy-to-tap buttons
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        font-size: 20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'finished' not in st.session_state:
    st.session_state.finished = False

# Your specific message sequence
no_msgs = [
    "No",
    "Think again",
    "I'll be sad",
    "Are u sure",
    "Pakka?"
]

# Bold Heading
st.markdown("<h1 style='text-align: center;'>Agr Mei Apky Ghar Au To Ap Mujhy Coffe Pilaogi?</h1>", unsafe_allow_html=True)

if not st.session_state.finished:
    # If she is still clicking 'No' through the sequence
    if st.session_state.no_count < len(no_msgs):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Yes"):
                st.session_state.finished = True
                st.rerun()
                
        with col2:
            if st.button(no_msgs[st.session_state.no_count]):
                st.session_state.no_count += 1
                st.rerun()
    
    # After the last 'No', show the Monkey and the mandatory 'Yes'
    else:
        st.markdown("<h2 style='color: red; text-align: center;'>Bauni Pilani to pregi</h2>", unsafe_allow_html=True)
        
        # This looks for the file you uploaded to GitHub
        if os.path.exists("monkey.jpg"):
            st.image("monkey.jpg", use_container_width=True)
        elif os.path.exists("monkey.png"):
            st.image("monkey.png", use_container_width=True)
        else:
            st.warning("Upload 'monkey.jpg' to GitHub to see the photo here!")

        if st.button("YES! (Last Option)"):
            st.session_state.finished = True
            st.rerun()

# Success Screen
else:
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: green;'>Good! ❤️</h1>", unsafe_allow_html=True)
