#omm sri sai ram jai sri krishna
from random import choice

def get_random_response()->str:
    random_list: list[str] = [
        "plese try weiting something more descriptive,",
        "oh! it appers you wrote something i don't understand yet",
        "do you mind trying to rephrase that?",
        "i'm terribly sorry, i don't quite catch that.",
        "i can't answer that yet please try asking something else."
    ]

    return choice(random_list)


if __name__ == '__main__':
    for i in range(5):
        print(get_random_response())