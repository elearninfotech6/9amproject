import gc

class SomeObj:
	def __del__(self):
        print('The object is destroyed.')

obj1 = SomeObj()
obj2 = obj1
obj3 = obj1
obj1 = None
obj2 = None
obj3 = None

for i in range(10):
    dic = {}
    dic[0] = dic

print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)