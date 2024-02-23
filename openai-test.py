import openai

# Set your OpenAI API key
openai.api_key = "your-api-key"

# Example prompt for the model
prompt = "Translate the following English text to French:"

# Request completion from the model
response = openai.Completion.create(
    engine="text-davinci-002",  # Use the appropriate engine
    prompt=prompt,
    max_tokens=50,  # Set the desired maximum number of tokens in the response
)

# Print the generated response
print(response.choices[0].text.strip())
