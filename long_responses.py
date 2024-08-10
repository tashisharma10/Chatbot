import random

R_ABOUT = "I am a chatbot.I am made using python.I can answer only limited questions."
R_EATING = "I can't eat anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_NAME = "My name is bot."
R_WEATHER = "You can check on weather app."


def unknown():
    response = ["Could you please re-phrase that? ",
                "Sounds about right.",
                "What does that mean?",
                "I can't understand.Ask something else",
                "I am not Chatgpt.I can answer only limited questions."][
        random.randrange(7)]
    return response