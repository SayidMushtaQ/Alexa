from openai import OpenAI;

client = OpenAI(
    api_key='your-api-key'
)
def chatWithGPT(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a personal assistant named alexa. You help users with various tasks, answer questions, and provide information in a friendly and conversational manner. You are knowledgeable, polite, and always ready to assist. Please provide short ans."},
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content

def generateIMG(command):
    response = client.images.generate( 
        prompt=command,
        n=2,
        size="1024x1024"
    )
    return response.data[0].url