# Exercice 1
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    
    def call(self, other_phone):
        call_string = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_string)
        self.call_history.append(call_string)

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print("Outgoing message:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        print("Incoming message: ")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)
    def show_messages_from(self, number):
        print("Message from: ")
        for msg in self.messages:
            if msg["from"] == number:
                print(msg)

p1 = Phone("0666-111-222")
p2 = Phone("0777-333-444")

p1.send_message(p2, "Hello!")
p1.send_message(p2, "Are you free later?")
p2.send_message(p1, "Yes, what's up?")

print("\n--- OUTGOING P1 ---")
p1.show_outgoing_messages()

print("\n--- INCOMING P1 ---")
p1.show_incoming_messages()

print("\n--- MESSAGES FROM 0777-333-444 ---")
p1.show_messages_from("0777-333-444")
