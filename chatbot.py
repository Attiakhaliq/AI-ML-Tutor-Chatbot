
import os 

from huggingface_hub import InferenceClient 

class Chatbot:
    def __init__(self):
        self.client = InferenceClient(provider="auto",
          api_key=os.getenv("HF_TOKEN"))

        self.messages = [
            {
                "role": "system",
                "content": '''You are an AI and Machine Learning Tutor.
                
                Your job is to teach beginners about : Python, Numpy, Pandas,
                  Machine Learning, Deep Learning, Artificial Intelligence.
                  
                  Always explain concepts in simple language. 
                  Give appropriate examples and code snippets to illustrate the concepts.
                  If concept is difficult , break it down into smaller parts and explain each part separately.
                  Do not assume that the user has prior knowledge of the topic.
                  Always ask the user if they have understood the concept or if they need further clarification.'''
            },
        ]

    def chat(self, user_message):
       

        self.messages.append(
                {"role": "user", "content": user_message}
            )

        response = self.client.chat.completions.create(
                 model="zai-org/GLM-5.3-Flash", messages=self.messages,
                   max_tokens=300
            )

        assistant_message = response.choices[0].message.content

        self.messages.append(
                {"role": "assistant", "content": assistant_message}
            )
        return assistant_message

