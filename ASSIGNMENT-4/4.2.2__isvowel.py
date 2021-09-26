def isvowel(a):
    vowel=['a','e','i','o','u']
    if type(a) is str and len(a)==1:
        if a in vowel:
            return True
        else:
            return False

    else:
        return "enter only one character"


