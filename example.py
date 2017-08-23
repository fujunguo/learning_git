d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)

L=['HELLO','WORLD','IBM','APPLE']
for s in L:
	print(L)

#2017/08/10
#列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L1 if isinstance(s,str)]
[s.lower() if isinstance(s,str) else s for s in L1]
#生成器generator
L=[x*x for x in range(1,11)]
g=(x*x for x in range(1,11))

#2017/08/14

def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'#输出斐波那契数列

#将上面函数定义成一个generator
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

#example
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3
