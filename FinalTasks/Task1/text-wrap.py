
import textwrap

import textwrap as txtw

def text_wrap():
    max_width=int(input("Olculuyu daxil edin: "))
    text=input("texti daxil edin: ")
    lines = txtw.wrap(text, max_width)
    for wrapvers in lines:
        print(wrapvers)
        
    

text_wrap()