import streamlit as st
import openai

#Open AI key
openai.api_key = st.secrets['OPEN_API_KEY']


#Give role to AI
def get_gardening_advice(plant_name, location, garden_size, season):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{
            "role": "system",
            "content": "You are a gardening assistant."
        }, {
            "role":
            "user",
            "content":
            f"""
            Provide detailed gardening advice for the following conditions:
            - Plant Name: {plant_name}
            - Location: {location}
            - Garden Size: {garden_size}
            - Season: {season}

            Please include:
            1. Planting instructions
            2. Watering schedule
            3. Seasonal advice
            4. Additional tips
            """
        }],
        max_tokens=1000,  # Increase max_tokens for more detailed responses
    )
    return response.choices[0].message['content']


# Streamlit app
st.title('Gardening Assistant')

# User inputs
plant_name = st.text_input('Plant Name')
location = st.text_input('Plating Area/Location')
garden_size = st.text_input('Your Garden Size / Pot Size')
season = st.selectbox('Current Season', ['Summer', 'Winter', 'Fall', 'Spring'])

# Generate advice
if st.button('Get Gardening Advice'):
    if plant_name and location:
        advice = get_gardening_advice(plant_name, location, garden_size,
                                      season)
        st.write(advice)
    else:
        st.write(
            "Please enter both the plant name and planting area/location.")
