#a function or a method is defined with keyword def ,
#a python method or a function may or maynot take and argument 
#a python method may or may not return a value
def nameOfMethodOrFunction(a):
	print "Hello World \n" * a
	#all the codes here will be executed if indetened properly

#all the code outside of indented block is mere a code of main block
#hence doesnot takes part in the defination of a function

nameOfMethodOrFunction(5)

print "..........................."


#this an example of a functiion returning a value c
def nameOfAnotherMethod(a, b):
	c = a + b
	return c

value = nameOfAnotherMethod(67, 54)

#this c variavle is ddifferent from c that was in the function,
# as in c/c++ variable residess in the block of codes and not outside
c = nameOfAnotherMethod(5, 8)


print c

#we can even print the returned function like this
print nameOfAnotherMethod(2,3)

#in python, you can provide arguments with the name of parameter
#like this below:
q = nameOfAnotherMethod(b = 6, a = 89)
#as you can see, the position of argument does not matter,
#if we assign the arguments by there name
