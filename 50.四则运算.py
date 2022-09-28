"""
    中缀表达式转后缀表达式：
    对于普通中缀表达式的计算，我们可以将其转化为后缀表达式再进行计算。转换方法也十分简单。只要建立一个用于存放运算符的栈，扫描该中缀表达式：
    如果遇到数字，直接将该数字输出到后缀表达式（以下部分用「输出」表示输出到后缀表达式）；
    如果遇到左括号，入栈；
    如果遇到右括号，不断输出栈顶元素，直至遇到左括号（左括号出栈，但不输出）；
    如果遇到其他运算符，不断去除所有运算优先级大于等于当前运算符的运算符，输出到后缀表达式。最后，新的符号入栈；
    把栈中剩下的符号依次弹出到后缀表达式，表达式转换结束
"""
"""
    如何处理负数：
    如果中缀表达式第一个符号是”-“，则这个符号是负号，在表达式最前面加一个0将其转化为减号
    如果左括号（后是”-“，则这个符号是负号，在”（“后面加一个0，将负号转化为减号，此时并不需要真的在中缀表达式中加一个0，只需要在将”（“入栈后在后缀表达式中加一个0
    除以上两种情况外”-“均为减号
"""
"""
    后缀表达式的计算：
    后缀表达式的计算就是从左到右扫描表达式，遇到数字就将其压入栈，遇到操作符表示可以计算，这时取出栈顶的两个元素进行操作，然后再次将结果压入栈，
    最后栈里会留下一个元素，该元素就是运行结果
"""


class Solution:

    suffix_exp = []
    operator_stack = []
    num_stack = []

    def calculate(self, medial_exp):
        medial_exp = medial_exp.replace(" ", "")
        medial_exp = medial_exp.replace("{", "(")
        medial_exp = medial_exp.replace("}", ")")
        medial_exp = medial_exp.replace("[", "(")
        medial_exp = medial_exp.replace("]", ")")
        # print(medial_exp)
        if medial_exp[0] == "-":
            medial_exp = "0" + medial_exp

        lens = len(medial_exp)
        i = 0
        while i < lens:
            if medial_exp[i].isdigit() is True:     # 是数字
                j = 1
                x = i
                num = medial_exp[i]
                while j < lens - x:
                    if medial_exp[x+j].isdigit() is True:
                        num = num + medial_exp[x+j]
                        i += 1
                        j += 1
                    else:
                        break

                self.suffix_exp.append(int(num))

                i += 1
            else:   # 是运算符或括号
                if medial_exp[i] == "(":
                    self.operator_stack.append(medial_exp[i])
                    if medial_exp[i+1] == "-":
                        self.suffix_exp.append(0)
                elif medial_exp[i] == ")":
                    while self.operator_stack[len(self.operator_stack)-1] != "(":
                        self.suffix_exp.append(self.operator_stack.pop())
                    self.operator_stack.pop()
                else:   # 中缀表达式此时的运算符是+-*/
                    if len(self.operator_stack) == 0:   # 符号栈为空
                        self.operator_stack.append(medial_exp[i])
                    else:   # 符号栈非空

                        if medial_exp[i] == "*" or medial_exp[i] == "/":   # 中缀表达式中此时运算符是*或/
                            while self.operator_stack:
                                cur_operator = self.operator_stack.pop()
                                self.operator_stack.append(cur_operator)
                                if cur_operator in ("*", "/"):
                                    self.suffix_exp.append(self.operator_stack.pop())
                                else:
                                    break
                            self.operator_stack.append(medial_exp[i])
                        else:   # 中缀表达式中此时运算符是+或-
                            while self.operator_stack:
                                cur_operator = self.operator_stack.pop()
                                self.operator_stack.append(cur_operator)
                                if cur_operator in ("+", "-", "*", "/"):
                                    self.suffix_exp.append(self.operator_stack.pop())
                                else:
                                    break
                            self.operator_stack.append(medial_exp[i])
                i += 1
        while self.operator_stack:
            self.suffix_exp.append(self.operator_stack.pop())
        # print(self.suffix_exp)

        for item in self.suffix_exp:
            if type(item) is int:
                self.num_stack.append(item)
            else:
                b = self.num_stack.pop()
                a = self.num_stack.pop()
                if item == "+":
                    self.num_stack.append(a+b)
                elif item == "-":
                    self.num_stack.append(a-b)
                elif item == "*":
                    self.num_stack.append(a*b)
                else:
                    self.num_stack.append(a//b)
        return self.num_stack.pop()


s = Solution()
print(s.calculate("3*5+8-0*3-6+0+0"))
