import streamlit as st

# # optional st.set_page_config() is used to configure the settings for the Streamlit app's page.
# st.set_page_config()

# #st.image('money_tree.jpg')
# st.title('Choose page on sidebar:')
# st.subheader('Examine the training data')
# st.subheader('or')
# st.subheader('Either use and explore the model')


import streamlit as st
from PIL import Image

def main():
    st.title("Streamlit Image ")

    # Upload image through Streamlit UI
    uploaded_image = st.file_uploader("money_tree.jpg", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Additional processing or analysis with the image can be added here

if __name__ == "__main__":
    main()
