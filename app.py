import streamlit as st

# -----------------------------
# Moonshine Customs Chat Bot
# -----------------------------

class ChatBot:
    def __init__(self, name):
        self.name = name

        self.knowledge = {
            "services": (
                "We provide Customization, Accidental Repair, "
                "Ceramic & Graphene Coating, and Paintjob."
            ),

            "locations": (
                "We are located in Delhi, Hyderabad, Kolkata, Pune, "
                "and Ahmedabad."
            ),

            "brands": (
                "Our brand partners include Hogert and Bosch."
            ),

            "contact": (
                "You can contact Moonshine Customs for more information "
                "about our services and bookings."
            )
        }

    def get_response(self, user_input):
        text = user_input.lower().strip()

        # Greeting
        greetings = [
            "hi", "hello", "hey", "hii", "helo",
            "good morning", "good afternoon", "good evening"
        ]

        if text in greetings:
            return (
                "Hello! 👋 Welcome to Moonshine Customs. "
                "How can I help you today?"
            )

        # Services
        service_keywords = [
            "service", "services",
            "offer", "offering", "offerings",
            "provide", "providing",
            "do you do",
            "what do you do",
        ]

        if any(keyword in text for keyword in service_keywords):
            return self.knowledge["services"]

        # Locations
        location_keywords = [
            "location", "locations",
            "where", "located",
            "branch", "branches",
            "city", "cities"
        ]

        if any(keyword in text for keyword in location_keywords):
            return self.knowledge["locations"]

        # Brand partners
        brand_keywords = [
            "brand", "brands",
            "partner", "partners",
            "brand partner",
            "brand partners",
            "company", "companies"
        ]

        if any(keyword in text for keyword in brand_keywords):
            return self.knowledge["brands"]

        # Booking / contact
        booking_keywords = [
            "book", "booking",
            "appointment",
            "schedule",
            "contact",
            "call",
            "enquiry",
            "inquiry"
        ]

        if any(keyword in text for keyword in booking_keywords):
            return self.knowledge["contact"]

        # Default response
        return (
            "I'm sorry, I didn't understand that. 🤔\n\n"
            "You can ask me about:\n"
            "• Our services\n"
            "• Our locations\n"
            "• Our brand partners\n"
            "• Appointments and bookings"
        )


# -----------------------------
# Streamlit UI
# -----------------------------

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
user_input = st.chat_input("Ask me something...")

if user_input:
    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    response = bot.get_response(user_input)

    # Display bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
