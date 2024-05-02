def valid_paranthesis(s):
    paranthesis = ["(", ")", "{", "}", "[", "]"]
    bracket = []
    for i in s:
        if i in paranthesis:
            bracket.append(i)
    if not bracket:
        return True
    print(bracket)

    flag = False
    for z in range(0, len(bracket)-1):
        zip_ = (bracket[z], bracket[z+1])
        print(zip_)
        if zip_ == ("(", ")") or zip_ == ("{", "}") or zip_ == ("[", "]") : 
            flag = True
        else:
            return False

    return flag


input = "{[]}"
print(valid_paranthesis(input))