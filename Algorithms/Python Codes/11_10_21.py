book= {
    'name':'Cerrah',
    'writter':'Tess Geritsen',
    'page':'354',
    'date':'2001'
}    
def showbook():
    print(f' {book["name"]} kitabi {book["date"]}-ci ildə {book["writter"]} tərəfindən yazılmışdır və {book["page"]}  səhifədir')

def changeBookInfo():  
    book["name"]=input("bes hansi kitabi deyrsen: ")

    print(f' {book["name"]} kitabi {book["date"]}-ci ildə {book["writter"]} tərəfindən yazılmışdır və {book["page"]}  səhifədir')


showbook()
changeBookInfo()