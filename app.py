import streamlit as st

# Page title
st.title("My Simple Autobiography & Portfolio")

# Introduction
st.header("About Me")
st.write("""
Hello! My name is **MJ Bascon Gaviola**. I'm a student at the Cebu Institute of Technology - University, passionate about technology and learning new things. I enjoy exploring different cultures and have a deep fascination with Japan. In my free time, I love traveling and experiencing new adventures.
""")

# Image
st.image("Me.jpg", caption="MJ Bascon Gaviola", width=150)

# Portfolio Section
st.header("My Portfolio")
st.subheader("Project 1: PetPals")
st.write("""
PetPals is a project that uses machine learning to recognize different breeds of pets from uploaded images. It is designed to help pet owners and enthusiasts identify and learn about various pet breeds.
""")


# List skills using bullet points
st.header("My Skills")
st.write("""

- Machine Learning
- Web Development
- Data Analysis
""") 

# Education Section
st.header("Education")
st.write("""
- **Bachelor of Science in Information Technology**  
  Cebu Institute of Technology - University  
  (Expected Graduation: 2025)
""")

# Contact Section
st.header("Contact Me")
st.write("Feel free to reach out to me by leaving a message below:")
contact_form = st.text_area("Enter your message here...")
if st.button("Submit"):
    st.write("Thank you for your message! I'll get back to you soon.")

# Footer
st.write("---")
st.write("© 2024 MJ Bascon Gaviola")
