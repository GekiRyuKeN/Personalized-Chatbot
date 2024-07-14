# Import necessary libraries
from g4f.client import Client
import streamlit as st

# Initialize the G4F client
client = Client()

# Define the function for generating creative writing prompts
def generate_writing_prompt(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

# Apply custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .sidebar .sidebar-content {
        background-color: #eeeeee;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.title("Options")
st.sidebar.write("Adjust the settings below:")

# Add examples in the sidebar
st.sidebar.subheader("Examples")
st.sidebar.write("- A story about a lost civilization discovering technology.")
st.sidebar.write("- Compose a poem about the changing seasons.")
st.sidebar.write("- A suspense thriller set in an abandoned mansion.")

# Main interface
st.title("Diamante Creative Writing Assistant 📝")
st.write("Unleash your creativity! Get inspired with unique story ideas, prompts, and plot twists.")

user_input = st.text_area("Enter a genre, tone, or initial plot point...", height=100)

if st.button("Generate Prompt"):
    if user_input:
        prompt = generate_writing_prompt(user_input)
        st.write("### Your Writing Prompt:")
        st.write(prompt)
    else:
        st.write("Please enter a genre, tone, or initial plot point to generate a prompt.")
