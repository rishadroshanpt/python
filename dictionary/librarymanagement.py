books=[]
print('-----------LIBRARY MANAGEMENT SYSTEM-----------')
while True:
    print('''
1.Add.
2.Display.
3.Update.
4.Delete.
5.Search.
6.Exit''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        id=int(input('Enter ID : '))
        name=input('Enter name of the book : ')
        qty=int(input('Enter quantity of the book : '))
        books.append({'id':id,'name':name,'qty':qty})
    elif ch==2:
        print('{:<5}{:<15}{:<5}'.format('ID',' NAME','QTY'))
        print('-'*25)
        for i in books:
            print('{:<5}{:<15}{:<5}'.format(i['id'],i['name'],i['qty']))
    elif ch==3:
        id=int(input('enter the Id of the book that you want to update : '))
        f=0
        for i in books:
            if id==i['id']:
                f=1
                while True:
                    print('''
1.Update  Id.
2.Update  name.
3.Update quantity.
4.Exit.''')
                    ch=int(input('Enter your choice : '))
                    if ch==1:
                        newId=int(input('Enter new  Id : '))
                        i['id']=newId
                    elif ch==2:
                        newName=input('Enter new product name : ')
                        i['name']=newName
                    elif ch==3:
                        newQty=int(input('Enter new product quantity : '))
                        i['qty']=newQty
                    elif ch==4:
                        break
                    else:
                        print('Invalid choice ! ')
        if f==0:
            print('Product not found ! ')
    elif ch==4:
        id=int(input('enter the Id of the book that you want to delete : '))
        f=0
        for i in books:
            if id==i['id']:
                f=1
                books.remove(i)
        if f==0:
            print('Product not found ! ')
    elif ch==5:
        id=int(input('enter the Id of the book that you want to search : '))
        f=0
        for i in books:
            if id==i['id']:
                f=1
                print('{:<5}{:<15}{:<5}'.format('ID',' NAME','QTY'))
                print('-'*25)
                print('{:<5}{:<15}{:<5}'.format(i['id'],i['name'],i['qty']))
        if f==0:
            print('Product not found ! ')
    elif ch==6:
        break
    else:
        print('Invalid choice !')