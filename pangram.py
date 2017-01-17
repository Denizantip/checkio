def check_pangram(text):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for ch in text.lower():
        if ch in alpha:
            alpha.remove(ch)
    if not alpha:
        return True
    else:
        return False