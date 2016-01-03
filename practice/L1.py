# object
obj=object()

print()
print("hello world")
print(obj)

# list tuple dictionary
list=['a','b',1,2]
tuple=('e','f','3','4')
dictionary={1:"first",'s':"second",'l':"last"}
# assingment
print(list)
list[3]=999
list[3]="string"
print(list[3])

print(tuple)
# tuple[3]=999 //tuple cant be assigned
print(tuple[3])

print(dictionary)
dictionary['l']="the last"
dictionary['l']=1000.0
print(dictionary['l'])

# operator
a=2
b=a**10
print('b = ',b)
print(b)

a1,a2,a3=10,20,30
print(a1,a2,a3)

# condition
if a1>a2:
	print('a1')
elif a1>a3:	
	print('a1')
else:
	print('a2 or a3')	

# loop
i=10
while i>0:
	print('i = ',i)
	i-=2	
print

for x in range(1,10):
	print'x =',x
	x+=1

print
for k in range(10,40,3):
	print'k =',k
	k+=3
print

# function
def isbig(a,b):
	if a>b:
		print'previous is bigger'
	else:
		print'follower is bigger'

isbig(10,20)
isbig(30,True)

# class
class TestClass(object):
#	def __init__(self):
#		super(TestClass, self).__init__()
	def giveA(input):
		self.a=input	
print
d=TestClass()

print 'new obj is ',d						
print
#d.giveA(9)
print d.a