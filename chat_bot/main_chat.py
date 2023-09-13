import json
import re
import random_response  #importing  another file random_classs

def load_json(file):
    with open(file) as bot_responses:          # in this we are converting the json in to dictonary so the we cam read imnside our program
        print(f'loaded "{file}" sucefully!')
        return json.load(bot_responses)       #load() is used to load arrays or picked objects from the file(ued is json mainly)


response_data: dict = load_json('response.json')



def get_response(input_str: str):
    split_message: list[str] = re.split(r'\s+|[,?!.-]\s*', input_str.lower())  # r' is a raw string
    score_list: list[int] = []     # re.split(r'\s+|[,?!.-]\s*', is sued to split the string and it will not consider the +|[,?!.-]\ in input


    for response in response_data:
        response_score: int = 0
        required_score: int = 0
        required_words: list[int] = response['required_words']


        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response['user_input']:
                    response_score += 1


        score_list.append(response_score)

    best_response: int = max(score_list)
    response_index: int = score_list.index(best_response)

    if input_str == "":
        return "please type something so that we can chat!"

    if best_response != 0:
        return response_data[response_index]['bot_response']  #we can remove this statement

    return random_response.get_random_response()


def main():
    while True:

        user_inpur: str = input('you: ')
        print('bot;', get_response(user_inpur))



if __name__ == '__main__':
    main()