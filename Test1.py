class Test:
    #输入不加self，则该函数是内置函数，不能在类外被引用
    #在类内引用：Test.printh
    def printh():
        print('hhhh')
    
    #输入有self,则函数为类的函数，可以在类外被引用
    #类内引用：self.printu
    def printu(self):
        print('uuuu')
    
    #引用测试
    def printall(self):
        Test.printh()
        self.printu()
        print('all...')
    
    #在类内直接声明变量（相当于在函数内置）需要global
    global a
    a=1
    def ta1():
        global a
        a+=1
    def ta2(self):
        global a
        a+=1
    def p_a(self):
        #这个global a 加/不加都一样（不加：一个特例）
        #global a
        Test.ta1()#可输出a=2
        self.ta2()#可输出a=2
        print(a)#经过两次加为a=3
        

t=Test()
t.printall()#可以输出
t.p_a()
        

