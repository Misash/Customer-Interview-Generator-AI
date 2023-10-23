
import langChain_helper as lch
import streamlit as st


st.title("Customer Interview Generator")



st.sidebar.markdown("## Customer Information 👥🛍️")

user_name = st.sidebar.text_input(label=f"Name: ",max_chars=7).strip()
user_age = st.sidebar.selectbox(f"Age: ",("18",'19','20','21','22','23','24','25','26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'))
user_gender_pronouns = st.sidebar.selectbox(f"Gender Pronouns: ",("she/her",'he/him','they/them'))
user_place_origin = st.sidebar.text_input(label=f"Country: ",max_chars=15).strip()
user_occupation = st.sidebar.text_input(label=f'Occupation:', max_chars=50).strip()
user_maritalStatus = st.sidebar.selectbox('MaritalStatus:', ('Single','Married','Divorced','Separated','Widowed','Engaged'))
user_education_level = st.sidebar.selectbox('Education Level:', (('No Education','High School', 'Bachelor’s Degree', 'Master’s Degree', 'Doctoral Degree')))

user_interests = st.sidebar.text_input(label=f"Interests:",max_chars=100).strip()



user_habits = st.text_area(label=f"What behaviours/habits does your customer have?",max_chars=300).strip()

user_needs = st.text_area(label=f"What Needs/Goals does your customer have?",max_chars=300).strip()

user_hypothesis = st.text_area(label=f"Type your hypothesis about your customer ",max_chars=500).strip()



st.markdown("## Interview 📝 ")




# Create a button to generate the interview
if st.button("Generate Interview"):
    # Validate if all fields are filled
    if (
        user_name and user_age and user_gender_pronouns and user_place_origin and user_occupation and
        user_maritalStatus and user_education_level and user_interests and user_habits and user_needs and user_hypothesis
    ):
        # Generate the interview
        interview = lch.generateCustomerInterview(name=user_name, 
                                                  age=user_age, 
                                                  pronouns=user_gender_pronouns, 
                                                  originPlace=user_place_origin, 
                                                  occupation=user_occupation, 
                                                  maritalStatus=user_maritalStatus, 
                                                  education_level=user_education_level, 
                                                  interests=user_interests, 
                                                  behaviors_habits=user_habits, 
                                                  needs_goals=user_needs, 
                                                  hypotheses=user_hypothesis)
        
        st.success("Interview Generated Successfully!")
        st.write(interview['interview'])
    else:
        # Show the missing fields
        missing_fields = [field for field, value in {
            "Name": user_name, "Age": user_age, "Gender Pronouns": user_gender_pronouns,
            "Country": user_place_origin, "Occupation": user_occupation, "Marital Status": user_maritalStatus,
            "Education Level": user_education_level, "Interests": user_interests,
            "Behaviors/Habits": user_habits, "Needs/Goals": user_needs, "Hypothesis": user_hypothesis
        }.items() if not value]
        st.warning(f"Please fill in the following fields: {', '.join(missing_fields)}")

