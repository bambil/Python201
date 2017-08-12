# In The Name Of God
# ========================================
# [] File Name : descriptor.py
#
# [] Creation Date : 13-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================


class RevealAccess:
    '''
    A data descriptor that sets and returns values
    normally and prints a message logging their access.
    '''

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 2


m = MyClass()

print(m.x)
print(m.y)

m.x = 2
