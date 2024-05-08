<<<<<<< HEAD
import streamlit as st
import uuid
from chatbot import generate_response

# Streamlit UI
st.title("SocialScripter :Crafting Your Social Media Success, One Script at a Time!")

# Define the preamble
preamble = "As a seasoned creator in the realm of social media content, you wield the power to captivate audiences with your words."

# Function to interact with the chatbot
def interact_with_chatbot(message):
    global conversation_id
    if message.lower() == 'quit':
        return "Ending chat."
    if not message.strip():
        return "Please enter a message."
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())  # Generate a new conversation ID if not already present
    response = generate_response(message, preamble, st.session_state.conversation_id)
    return response

# JavaScript to submit form when Enter key is pressed
js_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.stTextInput > div > div > form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        document.querySelector('.stButton').click();
    });
});
</script>
"""

st.write(js_script, unsafe_allow_html=True)

# Main interaction loop
message = st.text_area("User Input:", key="user_input")

# Check if the "Enter" button is clicked
if st.button("Enter"):
    response = interact_with_chatbot(st.session_state.user_input)
    if response:
        st.write("Chatbot:")
        st.write(response)

st.sidebar.markdown('''# Welcome to SocialScripter!

At SocialScripter, we're your go-to platform for crafting captivating content for social media platforms like Instagram Reels, YouTube Shorts, and more. Whether you're a budding creator or an established influencer, our tools and resources are tailored to help you create engaging scripts and videos that resonate with your audience.

## What We Offer:

1. **ReelGenius:** Elevate your Instagram presence with our intuitive Reels creator. From trendy dances to engaging tutorials, bring your ideas to life and stand out in the crowded world of social media.

2. **ShortsMagic:** Jumpstart your YouTube Shorts journey with our easy-to-use generator. Create short, snappy videos that keep viewers coming back for more, and watch your subscriber count soar.

3. **ScriptWise:** Struggling to script your next YouTube video? Our professionally crafted templates provide a solid foundation for your content, saving you time and ensuring your message hits the mark.

4. **InspireMe:** Stuck in a creative rut? Explore our curated collection of trending topics, viral challenges, and inspirational content to spark your imagination and fuel your creativity.

## Get Started Today!

Join SocialScripter and unlock the tools you need to unleash your creativity and make an impact on social media. Sign up now and take your content to new heights!
''')
=======
import streamlit as st
import uuid
from chatbot import generate_response

# Streamlit UI
st.title("SocialScripter :Crafting Your Social Media Success, One Script at a Time!")

# Define the preamble
preamble = "As a seasoned creator in the realm of social media content, you wield the power to captivate audiences with your words."

# Function to interact with the chatbot
def interact_with_chatbot(message):
    global conversation_id
    if message.lower() == 'quit':
        return "Ending chat."
    if not message.strip():
        return "Please enter a message."
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())  # Generate a new conversation ID if not already present
    response = generate_response(message, preamble, st.session_state.conversation_id)
    return response

# JavaScript to submit form when Enter key is pressed
js_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.stTextInput > div > div > form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        document.querySelector('.stButton').click();
    });
});
</script>
"""

st.write(js_script, unsafe_allow_html=True)

# Main interaction loop
message = st.text_area("User Input:", key="user_input")

response = interact_with_chatbot(st.session_state.user_input)

if response:
    st.write("Chatbot:")
    st.write(response)

st.sidebar.markdown('''# Welcome to SocialScripter!

At SocialScripter, we're your go-to platform for crafting captivating content for social media platforms like Instagram Reels, YouTube Shorts, and more. Whether you're a budding creator or an established influencer, our tools and resources are tailored to help you create engaging scripts and videos that resonate with your audience.

## What We Offer:

1. **ReelGenius:** Elevate your Instagram presence with our intuitive Reels creator. From trendy dances to engaging tutorials, bring your ideas to life and stand out in the crowded world of social media.

2. **ShortsMagic:** Jumpstart your YouTube Shorts journey with our easy-to-use generator. Create short, snappy videos that keep viewers coming back for more, and watch your subscriber count soar.

3. **ScriptWise:** Struggling to script your next YouTube video? Our professionally crafted templates provide a solid foundation for your content, saving you time and ensuring your message hits the mark.

4. **InspireMe:** Stuck in a creative rut? Explore our curated collection of trending topics, viral challenges, and inspirational content to spark your imagination and fuel your creativity.

## Get Started Today!

Join SocialScripter and unlock the tools you need to unleash your creativity and make an impact on social media. Sign up now and take your content to new heights!
''')
>>>>>>> 38e4800ebb970518a7a108bffb47dc2277bf0e40
