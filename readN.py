# QUESTION:
# This is an interview question asked by Microsoft.
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads
# n characters. For example, given a file with the content “Hello world”, three read7() returns
# “Hello w”, “orld” and then “”.

# solution with using class:

class fileread:
    def __init__(self):
        self.leftover = ""
    def readN(self, n):
        value = self.leftover
        text = None
        while len(value) < n and (text is None or len(text) == 7):
            text = read7()
            value += text
        self.leftover = value[n:]
        return value[:n]

# solution without using class:

leftover = ""
def readN(n):
    global leftover
    value = leftover
    text = None
    while len(value) < n and (text is None or len(text) == 7):
        text = read7()
        value += text
    leftover = value[n:]
    return value[:n]