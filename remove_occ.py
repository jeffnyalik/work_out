def removeOccurence(s:str)->str:
    ## Option one
    count = 0
    words = "Geeks"
    n = 2

    for i in range(0, len(s)):
        if s[i] == words:
            count +=1
        if count ==  n:
            del s[i]
    
    return s

    hashSet = set()
    res = []

    for i in range(len(s)):
        if s[i] not in hashSet:
            hashSet.add(s[i])
            res.append(s[i])
    return res
    

s = ["Geeks", "For", "Geeks"]
# s = ["food", "Thought", "For", "Thought", "food"]
print(removeOccurence(s))