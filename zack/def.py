num = 1

def fun1():
    global num #当内部区域想改变外部区域的值时，需要使用global声明
    num2 = 10
    num += 1
    print(num)
    def fun2():
        # 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
        nonlocal num2
        num2 = 100
        print(num2)
    fun2()
    print(num2)


fun1()