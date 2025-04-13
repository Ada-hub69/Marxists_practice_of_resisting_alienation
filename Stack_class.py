# import time
# def sum_of_n(n):
#     start=time.time
#     the_sum=0
#     for i in range(1,n+1):
#         the_sum = the_sum + i
#         end = time.time()
#         return the_sum,start,end
# # time模块time函数,返回程序运行到该函数的时刻
# a=[]
# a=sum_of_n(100)
# print(a)

# def angram_solutin(s1,s2):
#     c1=[0] * 26
#     c2=[0] * 26
    
#     for i in range(len(s1)):
#         pos = ord(s1[i]) - ord('a')
#         c1[pos] = c1[pos] + 1
#     for i in range(len(s2)):
#         pos = ord(s2[i]) - ord('a')
#         c2[pos] = c2[pos] + 1
#     j = 0
#     still_ok =True
#     while j < 26 and still_ok:
#         if c1[j] == c2[j]:
#             j = j + 1
#         else:
#             still_ok=False
#     return still_ok

# p=ord('a')
# print(p)


class stack:                   #注意事项:类中调用init中的变量时要用self.x的形式进行调用,2定义类时不需要函数那样的括号.3
    def __init__(self): 
        self.container = []    #定义类:栈,有三个方法,一个是增加,一个是删除,一个是判定栈是否为空,在事先确定列表哪里是顶部,对之后的方法代码有影响

    def push(self, element):    #push方法,规定列表中的最右边为底部,遵循栈的先进后出,返回增加元素后的栈
        self.container.append(element)
        return self.container
    
    def delete(self):#delete方法,遵循栈的先进后出,最后返回删除最后一个值的栈,如果想要删除特定位置的元素,需要指定下标
        self.container.pop()
        return self.container  
    
    def is_empty(self):#判定栈是否为空,并且返回对栈是否为空的判定布尔值
        return len(self.container) == 0  

def par_checker(symbol_string):
    s = stack()                 #判定括号是否匹配的函数,调用了栈数据类型,将待判定的括号集合放入字符串,并进行遍历,如果是符合条件的,就加入栈,
                                    #如果是不符合条件的元素,就查看栈是否为空,如果为空,则说明,没有左括号与之匹配,嵌套关系不成立.
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():  
                return False
            else:
                s.delete()
    return s.is_empty()  

a = par_checker("(())")  #使用括号进行测试
print(a)  # 输出 False
