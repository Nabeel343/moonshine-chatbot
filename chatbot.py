class ChatBot:
    def __init__(self, name):
        # Bot name
        self.name = name

        # Bot knowledge (memory)
        self.knowledge = {
            "services": "We provide Customization, Accidental Repair, Ceramic & Graphene Coating and Paintjob.",
            "location": "Delhi, Hyderabad, Kolkata, Pune and Ahmedabad.",
            "brand partners": "Hogert, Bosch, Norton, Blue-Point.",
            "contact": "6405998213",
            "mail": "moonshinecustoms@example.com"
        }

    def greet(self):
        print(f"\n{self.name}: Hi! I am {self.name}. Type 'bye' to exit.\n")

    def get_reply(self, user_text):
        # Greeting logic
        if user_text in ["hi", "hello", "hey"]:
            return "Hello! How can I help you?"

        # Keyword matching
        for key in self.knowledge:
            if key in user_text:
                return self.knowledge[key]

        # Default response
        return "Sorry, I didn't understand. Try asking about services, location, brand partners, or contact."

    def run(self):
        self.greet()

        while True:
            user_text = input("You: ").lower().strip()

            if user_text == "bye":
                print(f"{self.name}: Goodbye! Have a great day.")
                break

            reply = self.get_reply(user_text)
            print(f"{self.name}: {reply}")


# Create object and start chatbot
bot = ChatBot("Moonshine Customs Chat Bot")
bot.run()