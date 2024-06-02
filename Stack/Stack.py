from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    str = "We will conquere COVID-19"
    revStr = ""
    st = Stack()
    for w in range(0,len(str)):
        st.push(str[w])

    while(st.is_empty() == False):
        revStr = revStr +st.pop()

    # print(revStr)

    s= "()"
    stt = deque()
    for ind in range(0, len(s)):
        ch = s[ind]
        if (ch == '(' or ch == '[' or ch == '{'):
            stt.append(ch)
        elif (ch == ')' or ch == ']' or ch == '}'):
            if ch != stt.pop():
                print("F")

    print("T")