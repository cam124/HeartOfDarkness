from flask import Blueprint, render_template, request
import openai
import website.config as configure


API_KEY = configure.openAPI_key

views = Blueprint('views', __name__)
openai.api_key = API_KEY

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/author')
def author():
    return render_template('author.html')

@views.route('/map')
def map():
    return render_template('map.html')

@views.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@views.route('/tabloid')
def tabloid():
    return render_template('tabloid.html')

@views.route('/travelbrochure')
def travelbrochure():
    return render_template('travelbrochure.html')

@views.route('/essay')
def essay():
    return render_template('essay.html')

@views.route('/MarlowBot')
def marlowbot(user_input, context):
    # Generate response using OpenAI GPT-3 model
    prompt = f"{context}Marlow: {user_input}\nYou: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract text from response and return
    marlow_response = response.choices[0].text.strip()
    return marlow_response

def chat():
    # Get user input and context
    user_input = request.args.get('user_input', '')
    context = request.args.get('context', '')

    # If user input is not empty, generate bot response
    if user_input:
        context += f"You: {user_input}\nMarlow: {marlowbot(user_input, context)}\n"

    # Render chat template with context and user input
    return render_template('chat.html', context=context, user_input=user_input)