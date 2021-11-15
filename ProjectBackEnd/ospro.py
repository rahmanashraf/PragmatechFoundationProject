import os

print(os.getcwd())  ###movcud papkani print elir
os.chdir("/Users/HP/Desktop")  ###papkanin adin yazirsan ora direct elir CHangeDIRect
# print(os.listdir())  ###papkanin icini gosterir

os.mkdir("OsModule")   ###TASK1....OsModule adinda Folder yaradildi..
for document in os.listdir():
    print(document)
