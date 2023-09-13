# omm sri sai ram - hare krishna
from flask import Flask, request     # flask is a framework for building web applications
from collections import namedtuple   # nametuples are like data types
from datetime import date
from time import  time

app = Flask(__name__)

@app.route('/')     # every app.route() must coint '/' in it.
def index():
    return {'test': 'this is an example',
            'data': date.today(),              # these are the jsons we are using
            'timestamp': time()}


@app.route('/chat')   # every app.route() must coint '/' in it.
def chat():
    user_input: str = request.args.get('input')
    response: Response = genarate_responses(user_input)

    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }

    return json


Response = namedtuple('Response', 'response accuracy')  # it's is data type

def genarate_responses(user_input: str)->Response:
    lc_case :str = user_input.lower()

    if lc_case == 'hello':
        return Response('hey there!', 1)
    elif lc_case == 'goodbye':
        return Response('see you later', 1)
    else:
        return Response('could not understand!',0)




if __name__ == '__main__':
    app.run()

