__author__ = 'Derek'
import copy

class Foo():
    """Blahh"""
    notagoodidea = 'what am I now?'

object1 = Foo()

object1.x = 'who knows'

object2 = object1

object2.notagoodidea = 'whos on first?'

object3 = copy.copy(object1)

object3.notagoodidea = 'im lost'

print('class variable:',Foo.notagoodidea,id(Foo.notagoodidea))
print('instance variable 1:',object1.x,id(object1),id(object1.x))
print('instance variable:',object2.notagoodidea,id(object2.notagoodidea))
print('instance variable:',object3.notagoodidea,id(object3.notagoodidea))



