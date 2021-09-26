def word_integer(lists):
    integers=[]
    if type(lists) is list:
        for i in lists:
            integers.append(len(i))
        return integers
    else:
        return "Plese enter words inside a list"

