booklist=[]
print("="*30)
while True:
    book=input("도서명 입력 : ")
    if(book==''):
        break
    booklist.append(book)
print("="*30)
booklist.sort()
for i in range(0,len(booklist)):
    print("{} : {}".format(i+1,booklist[i]))

