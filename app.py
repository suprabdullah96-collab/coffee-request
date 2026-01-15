import streamlit as st

# Set page title
st.set_page_config(page_title="Sawal Gandom, Jawab Chana", page_icon="☕")

# Custom CSS for better looking buttons
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for tracking 'No' clicks
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'finished' not in st.session_state:
    st.session_state.finished = False

# The list of messages you requested
no_msgs = [
    "No",
    "Think again",
    "I'll be sad",
    "Are u sure",
    "Pakka?"
]

# Title
st.markdown(f"<h1 style='text-align: center;'>Agr Mei Apky Ghar Au To Ap Mujhy Coffe Pilaogi?</h1>", unsafe_allow_html=True)

# Main Logic
if not st.session_state.finished:
    # Check if we have exhausted all 'No' options
    if st.session_state.no_count < len(no_msgs):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Yes"):
                st.session_state.finished = True
                st.rerun()
                
        with col2:
            # Show the next 'No' message based on count
            if st.button(no_msgs[st.session_state.no_count]):
                st.session_state.no_count += 1
                st.rerun()
    else:
        # The 'No' limit is reached - Show the monkey!
        st.markdown("<h2 style='color: red; text-align: center;'>Bauni Pilani to pregi</h2>", unsafe_allow_html=True)
        # Using a direct link to the middle-finger monkey image
        st.image("https://media.tenor.com/images/3f885e3590089e0004e7609f98f6d7f0/tenor.gif", use_container_width=True)
        
        if st.button("Okay fine, Yes! ☕"):
            st.session_state.finished = True
            st.rerun()

# Success Screen
else:
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: green;'>Good! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Be ready, I'm coming for that coffee!</p>", unsafe_allow_html=True)
