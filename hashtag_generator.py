def generate_hashtag(s):
    if s.strip() == '':
        return False
    string = '#'+str(s).title().replace(" ", "").strip()
    if len(string) > 140:
        return False
    else:
        return string
