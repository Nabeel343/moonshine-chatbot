import streamlit as st


class ChatBot:
    def __init__(self, name):
        self.name = name

        self.knowledge = {
            "services": "We provide Customization, Accidental Repair, Ceramic & Graphene Coating, and Paintjob.",
            "location": "We are located in Delhi, Hyderabad, Kolkata, Pune, and Ahmedabad.",
            "brand partners": "Our brand partners include Hogert and Bosch.",
            "contact": "You can contact Moonshine Customs for more information about our services and bookings.",
            "mail": "You can contact us through our official communication channels for enquiries and bookings."
        }

    def respond(self, message):
        message = message.lower().strip()

        # Greetings
        if any(word in message for word in [
            "hi", "hello", "hey", "good morning",
            "good afternoon", "good evening"
        ]):
            return "Hello! 👋 Welcome to Moonshine Customs. How can I help you today?"

        # Services
        if any(word in message for word in [
            "service", "services", "offering", "offer",
            "provide", "providing", "what do you do",
            "what can you do", "what can you provide",
            "work do you offer", "available services"
        ]):
            return self.knowledge["services"]

        # Location
        if any(word in message for word in [
            "location", "locations", "located", "branch",
            "branches", "where are you", "where are you located",
            "city", "cities"
        ]):
            return self.knowledge["location"]

        # Brand partners
        if any(word in message for word in [
            "brand", "brands", "partner", "partners",
            "bosch", "hogert"
        ]):
            return self.knowledge["brand partners"]

        # Contact
        if any(word in message for word in [
            "contact", "phone", "number", "call",
            "reach", "booking", "book", "appointment"
        ]):
            return self.knowledge["contact"]

        # Email
        if any(word in message for word in [
            "email", "mail", "e-mail"
        ]):
            return self.knowledge["mail"]

        # Thanks
        if any(word in message for word in [
            "thank", "thanks", "thank you"
        ]):
            return "You're welcome! 😊 Let me know if you need anything else."

        return (
            "I'm sorry, I didn't understand that. "
            "You can ask me about our services, locations, "
            "brand partners, contact details, or bookings."
        )


# Streamlit page
st.set_page_config(
    page_title="Moonshine Customs Chat Bot",
    page_icon="🚗"
)

st.title("🚗 Moonshine Customs Chat Bot")
st.write(
    "Ask me about our services, locations, brand partners, "
    "or contact details."
)

# Create chatbot
bot = ChatBot("Moonshine Customs")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    response = bot.respond(user_input)

    # Show bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
