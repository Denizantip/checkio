def verify_anagrams(first_word, second_word):
    
    def texted(text):
        return sorted(list(text.replace(' ','').lower()))
        
    if texted(first_word) == texted(second_word):
        return True
    else:
        return False

