#match case is same as the switch case in other languages

user_input: str = input('command:')
command: list[str] = user_input.split()  #.split() is used to split(saparate the sentance).

print(user_input)
match command:
    case ['find',*images]:
        print(f'finding: {images}') 
    case['download',*images]:
        print(f'downloading: {images}')
    case['cancel' | 'delete',*images]:
        print(f'deleting: {images}')
    case _:
        print('command is not found')
