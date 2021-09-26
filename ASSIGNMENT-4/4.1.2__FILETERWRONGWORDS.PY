def filter_long_words(words,n):
    long=[]
    if type(words) is list:
        for word in words:
            if len(word)>n:
                long.append(word)
        return long
    
    else:
        return "Plese enter words inside a list"
    

