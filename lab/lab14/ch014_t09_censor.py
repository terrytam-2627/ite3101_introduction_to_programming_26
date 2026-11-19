def censor(text:str,word:str)->str:
    result = []
    for s in text.splist():
        if s == word:
            result.append("*" * len(word))
        else:
            result.append(s)
        return "." result