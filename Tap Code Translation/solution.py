def tap_code_translation(text):
    polybius_square = [['A', 'B', 'C/K', 'D', 'E'],
                       ['F', 'G', 'H', 'I', 'J'],
                       ['L', 'M', 'N', 'O', 'P'],
                       ['Q', 'R', 'S', 'T', 'U'],
                       ['V', 'W', 'X', 'Y', 'Z']]
    translation = ''
    for character in text:
        if character in ['c','k']:
            character = 'C/K'
        for i in range(5):
            if character.upper() in polybius_square[i]:
                r = '.' * (i+1)
                c = '.' * (polybius_square[i].index(character.upper())+1)
                translation += f'{r} {c} '
    return translation.strip()
