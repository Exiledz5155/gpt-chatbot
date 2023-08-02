import openai


class Chatbot:
    def __init__(self):
        with open(".env", 'r') as file:
            openai.api_key = file.readline().split("=")[1].strip()
            #print(file.readline().split("=")[1].strip())

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

'''
with open(".env", 'r') as file:
    print(file.readline().split("=")[1])
'''

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me a story about a frog")
    print(response)
