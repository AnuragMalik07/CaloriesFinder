import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([image[0],prompt])
    return response.text


def input_image_setup(uploade_file):
    if uploade_file is not None:
        bytes_data=uploade_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploade_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    
st.set_page_config(page_title="Calories Finder")

st.header("Ai Calories finder")
#input_text=st.text_input("Input Prompt: ",key="input")
uploade_file=st.file_uploader("choose image....",type=["jpg","jpeg","png"])
#Image=""
if uploade_file is not None:
    image = Image.open(uploade_file)
    st.image(image,caption="The uploaded image",use_column_width=True)
    
submit=st.button("tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

if submit:
        image_data=input_image_setup(uploade_file)
        response=get_gemini_response(image_data,input_prompt)
        st.subheader("the response is")
        st.write(response)
 