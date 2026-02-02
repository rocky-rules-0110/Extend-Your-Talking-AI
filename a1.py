import pyttsx3
import random

def get_responses():
    """Returns a list of fun new phrases for the AI to say."""
    return [
        "I am powered by artificial intelligence and a little bit of caffeine.",
        "Your command is my sequence of bits!",
        "I'm feeling particularly algorithmic today.",
        "That is an excellent observation, human.",
        "Processing... Just kidding, I'm already done!"
    ]

def get_jokes():
    """Returns a list of random jokes for the custom command."""
    return [
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why was the cell phone wearing glasses? It lost its contacts.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem."
    ]

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150) 
        self.engine.setProperty('volume', 0.8) 

    def speak(self, text):
        print(f"AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def update_rate(self, delta):
        current_rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', current_rate + delta)
        self.speak(f"Speech rate adjusted by {delta}.")

    def update_volume(self, delta):
        current_volume = self.engine.getProperty('volume')
        new_volume = max(0.0, min(1.0, current_volume + delta))
        self.engine.setProperty('volume', new_volume)
        self.speak(f"Volume adjusted to {int(new_volume * 100)} percent.")

    def handle_command(self, command):
        command = command.lower().strip()

        if "speed up" in command:
            self.update_rate(50)
        elif "slow down" in command:
            self.update_rate(-50)
        elif "increase volume" in command:
            self.update_volume(0.2)
        elif "decrease volume" in command:
            self.update_volume(-0.2)

        elif "tell a joke" in command:
            self.speak(random.choice(get_jokes()))

        elif "hello" in command or "chat" in command:
            self.speak(random.choice(get_responses()))

        elif "exit" in command:
            self.speak("Goodbye! Have a productive day.")
            return False

        else:
            self.speak("I didn't quite catch that. Try again!")
        
        return True

def main():
    assistant = VoiceAssistant()
    
    print("="*40)
    print("🎙️ VOICE MASTER+: INTERACTIVE AI")
    print("="*40)
    print("Commands: 'speed up', 'slow down', 'increase volume', 'decrease volume', 'tell a joke', 'exit'")

    is_running = True
    while is_running:
        user_input = input("\nEnter command: ")
        is_running = assistant.handle_command(user_input)

if __name__ == "__main__":
    main()