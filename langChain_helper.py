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
    llm = OpenAI(temperature=0.5)


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

        template = """Based on "The Mom Test" by Rob Fitzpatrick, create a simulated interview with a customer using the provided details. Build a character profile and formulate questions to test the given hypotheses. Ensure the dialogue is realistic and analyze responses according to "The Mom Test."
            Customer Details:
            - Name: {name}
            - Age: {age}
            - Pronouns: {pronouns}
            - Origin: {originPlace}
            - Habits: {behaviors_habits}
            - Occupation: {occupation}
            - Marital Status: {maritalStatus}
            - Education: {education_level}
            - Interests: {interests}
            - Needs/Goals: {needs_goals}

            Hypotheses: {hypotheses}

            Chat Format:
            - Interviewer (I)
            - Customer (C)
            - Analysis

            Construct the conversation to explore each hypothesis, providing analysis after each exchange.
            Focus on natural interaction and insightful questioning.
            """
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


    return response 


# example
if __name__ == "__main__" :
    output = generateCustomerInterview('Alexandra',
                                   '30',
                                   'she/her',
                                   'Spain',
                                   'Passionate about sustainable living and eco-friendly technologies. Regularly participates in community gardening projects. Interested in apps that promote environmental awareness.',
                                   'Environmental consultant',
                                   'Married',
                                   'Master’s degree in Environmental Science',
                                   'Sustainable living, technology for environmental conservation, and community gardening',
                                   'Looking for innovative tech solutions to reduce carbon footprint both personally and in her community. Interested in apps that can help track and improve sustainable habits.',
                                   "1. The customer is actively seeking apps that help reduce waste and promote recycling. 2. Willing to invest in high-quality environmental apps, with a budget up to $50 per app. 3. Prefers user-friendly interfaces with community-sharing features. 4. Is a member of online forums discussing sustainability. 5. Shows interest in integrating technology with daily eco-friendly practices."
                                   )['interview']

    print(output)
  


