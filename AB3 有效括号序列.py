给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s: str) -> bool:
          matching_parentheses = {')': '(', ']': '[', '}': '{'}
          stack=[]

          for char in s:
            if char in matching_parentheses:
                if not stack or stack[-1]!=matching_parentheses[char]:
                    return False
                stack.pop()
            elif char in matching_parentheses.values():
                stack.append(char)
            else:
                continue



          return not stack
        # write code here
matching_parentheses = {')': '(', ']': '[', '}': '{'} 是一个字典，用于存储右括号与左括号之间的匹配关系。这个字典的键是右括号，值是与之匹配的左括号。具体含义如下：

')': '(' 表示右括号 ')' 对应的左括号是 '('。
']': '[' 表示右括号 ']' 对应的左括号是 '['。
'}': '{' 表示右括号 '}' 对应的左括号是 '{'。
这个字典的目的是为了在遍历字符串时，能够方便地通过右括号查找与之匹配的左括号。

详细说明：
在这个括号匹配问题中，我们需要检查每一个右括号是否与前面的某个左括号匹配。为了实现这一点，我们使用栈来跟踪左括号，同时使用这个字典来快速查找右括号对应的左括号。

例如，当我们遇到一个右括号 ) 时，我们可以通过 matching_parentheses[')'] 得到与之匹配的左括号 (。

代码示例中的使用：
在代码中，当遇到右括号时，我们需要检查栈顶的左括号是否与当前的右括号匹配：

python
复制代码
if char in matching_parentheses:
    # 检查栈是否为空，或者栈顶元素是否与当前右括号匹配
    if not stack or stack[-1] != matching_parentheses[char]:
        return False
    stack.pop()
if char in matching_parentheses:：检查当前字符是否是右括号。
if not stack or stack[-1] != matching_parentheses[char]:：检查栈是否为空，或者栈顶元素是否与当前右括号匹配。
not stack：如果栈为空，说明没有匹配的左括号，返回 False。
stack[-1] != matching_parentheses[char]：如果栈顶元素不匹配当前右括号，返回 False。
stack.pop()：如果匹配成功，弹出栈顶元素。
这个匹配字典的作用就是在右括号匹配检查中，快速找到对应的左括号，以便与栈顶元素进行比较。

为什么stack[-1]是负一的意思
ChatGPT
在Python中，列表（或数组）的索引可以为负数，负数索引表示从列表的末尾开始计数。具体来说：

stack[-1] 表示列表 stack 的最后一个元素。
stack[-2] 表示列表 stack 的倒数第二个元素。
依此类推。
这种特性使得我们可以方便地访问列表的末尾元素，而无需知道列表的长度。例如，对于列表 stack = [1, 2, 3]：

stack[0] 返回 1（第一个元素）
stack[1] 返回 2（第二个元素）
stack[2] 返回 3（第三个元素）
stack[-1] 返回 3（最后一个元素）
stack[-2] 返回 2（倒数第二个元素）
stack[-3] 返回 1（倒数第三个元素）
在我们的括号匹配算法中，stack[-1] 用于获取栈的顶部元素（即最近压入栈的左括号）。这是因为栈是后进先出（LIFO, Last In First Out）的数据结构，最后一个压入栈的元素应该是第一个被弹出的元素
        
