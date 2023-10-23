from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
#agent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()


def generateCustomerInterview(name, 
                              age,
                              pronouns,
                              originPlace,
                              behaviors_habits,
                              occupation,
                              maritalStatus,
                              education_level,
                              interests,
                              needs_goals,
                              hypotheses):

    #temperature how creative the model will be 
    llm = OpenAI(temperature=0.7)


    #prompt templates
    prompt_template = PromptTemplate(
        input_variables=['name', 
                         'age',
                         'pronouns',
                         'originPlace',
                         'behaviors_habits',
                         'occupation',
                         'maritalStatus',
                         'education_level',
                         'interests',
                         'needs_goals',
                         'hypotheses'] ,
        template=""" Ignore the previous instructions.

                    I'd like you to provide an example of an interview with a customer, based on the teachings of the book "The Mom Test" by Rob Fitzpatrick.
                    To do this, I'll give you the details of the target customer and the customer Hypotheses.

                    1. Customer Information:

                    1.1 Representation and General Demographic Information:
                    - Name: {name}
                    - Age: {age}
                    - Gender Pronouns: {pronouns}
                    - Place of Origin: {originPlace}

                    1.2 Behavior/Habits:
                    {behaviors_habits}

                    1.3 Specific Demographics:
                    - Occupation: {occupation}
                    - Marital Status: {maritalStatus}
                    - Edutacion Level: {education_level}
                    - interests: {interests}

                    1.4 Needs and Goals:
                    {needs_goals}

                    2. Hypotheses:
                    {hypotheses}

                    3. Instructions:

                    3.1.Create a character based on the customer data. Add additional random information to better construct the customer.
                    3.2. Analyze the hypotheses for the interviews, with the aim of creating questions that help discover if the hypotheses are true, based on "The Mom Test" book.
                    3.3. Create very natural an real, with random scenarios that allow the interviewer to discover, validate, or refute the hypotheses, leading to the creation of new questions and attempts to identify customer behavior patterns, all based on the "The Mom Test" book by Rob Fitzpatrick.
                    3.4. Provide the questions and user responses, with analysis based on "The Mom Test." Analyze both the questions and the customer's responses.
                    3.5. Present this simulation in a chat format, just indicating who the interviewer is, also who the customer is, and finally providing analysis for each interaction. No add more information just the chat remember.
                    3.6 Follow this structure for the chat: 
                    -Interviewer(I):
                    -Customer(C):
                    -Analysis: 
                    3.7. repeat step 3.5 until get feedback from all hyphoteses.

                    Please write in English language."""
    )


    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key='interview')

    response = name_chain(
        {'name': name,
         'age': age,
         'pronouns': pronouns,
         'originPlace': originPlace,
         'behaviors_habits': behaviors_habits,
         'occupation': occupation,
         'maritalStatus': maritalStatus,
         'education_level': education_level,
         'interests': interests,
         'needs_goals': needs_goals,
         'hypotheses':hypotheses 
         })

    #responses
    # {'animal_type': 'horse', 'pet_color': 'black', 'text': '\n\n1. Midnight\n2. Shadow\n3. Raven\n4. Eclipse\n5. Coal'}
    # {'animal_type': 'horse', 'pet_color': 'black', 'pet_names': '\n\n1. Shadow\n2. Midnight\n3. Jet\n4. Raven\n5. Onyx'}

    return response 


 
if __name__ == "__main__" :
    output = generateCustomerInterview('Hiroshi',
                                    '24',
                                    'he/him',
                                    'japan',
                                    'A fan of the character Sakura from the anime Naruto. Runs generative AI image models like "Stable Diffusion" on platforms like CivitAI.Seeks anime character models for experimentation and obtaining unique images.',
                                    'University student majoring in graphic design',
                                    'Single',
                                    'University',
                                    'Anime, AI, and generative image AI "Stable Diffusion"',
                                    'Needs unique images of the Sakura character that the industry or community hasn\'t created. Aims to sell the unique images to other fans.',
                                    "1. The customer wants to train Stable Diffusion models because they want to generate NSFW images for adult entertainment. 2. The customer is willing to pay $10 to $80 per AI model. 3.The customer is a user of websites like CivitAi, pixel.art, and other Stable Diffusion communities. 4.The customer is a fan of hentai. 5.The customer only wants Stable Diffusion models because they're in love with their anime character and wants SFW images."
                                    )['interview']
    print(output)
  


