
import langChain_helper as lch
import streamlit as st


st.title("Customer Interview Generator")

st.sidebar.title("Customer Information:")

user_name = st.sidebar.text_area(label=f"Name: ",max_chars=7).strip()
user_age = st.sidebar.text_area(label=f"Age: ",max_chars=2).strip()
user_gender_pronouns = st.sidebar.selectbox(f"Gender Pronouns: ",("she/her",'he/him','they/them'))




# user_pet_color = st.sidebar.text_area(label=f"What color is your {user_animal_type}?",max_chars=10).strip()



# if user_pet_color:
#     response = lch.generate_pet_name(user_animal_type,user_pet_color)
#     st.text(response['pet_names'])