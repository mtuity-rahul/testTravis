import hello
class Test:
	def testFunc1(self):
		obj = hello.Hello()
		assert "HelloWorld" == obj.func1()
        #print(obj.func1())

objTest = Test()
objTest.testFunc1()