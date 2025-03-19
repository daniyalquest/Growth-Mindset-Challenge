import streamlit as st
st.title('Growth Mindset Challenge')
st.header('Embrace your potential!')
st.write("A growth mindset means embracing challenges, persisting in the face of setbacks, and seeing effort as a path to mastery.")
button = st.button('Take the challenge')
if button:
    st.write('You are on your way to a growth mindset!')