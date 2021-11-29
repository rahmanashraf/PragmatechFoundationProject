class change:
    def __init__(self,x,y,z):
        self.a=x+y+z
x=change(1,2,3)
y=getattr(x,'a')
setattr(x,'a',y+1)
print(x.a)


#bunun aciglamasi budr ki get attr i ile biz x deyisenmizi cagirib onun
##self a sini hansiki deyisendir ona set attr i ile (y+1) yedirdiriy
### sonra artiq cemi 6 elemli olan sey 7 edir