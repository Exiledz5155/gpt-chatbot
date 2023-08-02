import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choice[0].text
        return response


