import streamlit as st


class ChatBot:
    def __init__(self, name):
        self.name = name

        self.knowledge = {
            "services": "We provide Customization, Accidental Repair, Ceramic & Graphene Coating and Paintjob.",
            "location": "Delhi, Hyderabad, Kolkata, Pune and Ahmedabad.",
            "brand partners": "Hogert, Bosch, Norton, Blue-Point.",
            "contact": "6405998213",
            "mail": "moonshinecustoms@example.com"
        }

    def get_reply(self, user_text):
        user_text = user_text.lower().strip()

        if user_text in ["hi", "hello", "hey"]:
            return "Hello! How can I help you?"

        for key in self.knowledge:
            if key in user_text:
                return self.knowledge[key]

        return "Sorry, I didn't understand. Try asking about services, location, brand partners, contact, or mail."


bot = ChatBot("Moonshine Customs Chat Bot")

st.set_page_config(
    page_title="Moonshine Customs Chat Bot",
    page_icon="🤖"
)

st.title("🤖 Moonshine Customs Chat Bot")
st.write("Ask me about our services, locations, brand partners, or contact details.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = bot.get_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
