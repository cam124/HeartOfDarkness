from flask import Blueprint, render_template, request
import openai
import os


API_KEY = os.getenv('API_KEY')

views = Blueprint('views', __name__)
openai.api_key = API_KEY

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/author')
def author():
    return render_template('author.html')

@views.route('/natives-perspective')
def map():
    return render_template('natives.html')

@views.route('/marlow')
def marlow():
    return render_template('marlow.html')

@views.route('/diary')
def tabloid():
    return render_template('diary.html')

@views.route('/travelbrochure')
def travelbrochure():
    return render_template('travelbrochure.html')

@views.route('/essay')
def essay():
    return render_template('essay.html')

def marlowbot(user_input, context):
    # Generate response using OpenAI GPT-3 model
    prompt = f"{context}Marlow: {user_input}\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract text from response and return
    marlow_response = response.choices[0].text.strip()
    return marlow_response

@views.route('/MarlowBot')
def chat():
    # Get user input and context
    user_input = request.args.get('user_input', '')
    context = request.args.get('context', 'you are Charles Marlow ')

    # If user input is not empty, generate bot response
    if user_input:
        context += f"You: {user_input}\nMarlow: {marlowbot(user_input, context)}\n"

    # Render chat template with context and user input
    return render_template('chat.html', context=context, user_input=user_input)