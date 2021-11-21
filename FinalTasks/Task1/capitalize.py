def basherflerUpper():
    x=input("Adini soyadini daxil et: ")
    y=x.split(" ")
    for word in y:
        t=word.capitalize()
        
        print(t,end=' ')
        
"""
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s                               ##hackerrankda bu isledi burda baskasin yazdim ama bu biraz ferqlidi
                                            burda alt alta dusur yazi ama hackerrankda yazdigimda ideal isdiyir"""
        



basherflerUpper()