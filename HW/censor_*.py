import re


def repl(m):
    return '*' * len(m.group())

text = """Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"""

spam_words = ['began', 'Python']

spam_case = re.findall(('|'.join(spam_words)), text, flags=re.IGNORECASE)

s = re.sub('|'.join(spam_case), repl, text)

print(s)