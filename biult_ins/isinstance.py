"""
#isinstance() is used to check wiether it is present in the class or not if present then it will print  true
# if it is not present in the list then it will print false
#it should have item name and clas name(apple,fruits)

"""
class fruits:

    def __init__(self,name:str):
        self.name = name

if __name__=='__main__':
    apple:fruits = fruits('apple')
    banana:fruits = fruits('banana')


    print(isinstance(apple,fruits))
    print(isinstance(banana, fruits))
    print(isinstance(str, fruits))
    print(isinstance(10, fruits))