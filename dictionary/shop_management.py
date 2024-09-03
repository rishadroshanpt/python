prods=[]
while True:
    print('''
1.Add Details of the product.
2.Display Products.
3.Update Product Details.
4.Delete Products.
5.Exit''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        prodId=int(input('Enter product Id : '))
        prodName=input('Enter product name : ')
        prodPrice=int(input('Enter price of the product : '))
        prodQty=int(input('Enter product quantity : '))
        prods.append({'prodId':prodId,'prodName':prodName,'prodPrice':prodPrice,'prodQty':prodQty})
    elif ch==2:
        print('{:<15}{:<15}{:<10}{:<10}'.format('Product Id','Product Name','Price','Qty'))
        print('-'*45)
        for i in prods:
            print('{:<15}{:<15}{:<10}{:<10}'.format(i['prodId'],i['prodName'],i['prodPrice'],i['prodQty']))
    elif ch==3:
        id=int(input('enter the Id of the product that you want to update : '))
        f=0
        for i in prods:
            if id==i['prodId']:
                f=1
                while True:
                    print('''
1.Update product Id.
2.Update Product name.
3.Update price.
4.Update quantity.
5.Exit.''')
                    ch=int(input('Enter your choice : '))
                    if ch==1:
                        newId=int(input('Enter new product Id : '))
                        i['prodId']=newId
                    elif ch==2:
                        newName=input('Enter new product name : ')
                        i['prodName']=newName
                    elif ch==3:
                        newPrice=int(input('Enter new price : '))
                        i['prodPrice']=newPrice
                    elif ch==4:
                        newQty=int(input('Enter new product quantity : '))
                        i['prodQty']=newQty
                    elif ch==5:
                        break
                    else:
                        print('Invalid choice ! ')
        if f==0:
            print('Product not found ! ')
    elif ch==4:
        id=int(input('enter the Id of the product that you want to delete : '))
        f=0
        for i in prods:
            if id==i['prodId']:
                f=1
                prods.remove(i)
        if f==0:
            print('Product not found ! ')
    elif ch==5:
        break
    else:
        print('Invalid choice !')