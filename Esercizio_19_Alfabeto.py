alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
    for i in alphabet:
        if i not in sentence.lower():
            return False
        continue
    return True
