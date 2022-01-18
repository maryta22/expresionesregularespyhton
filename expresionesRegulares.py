import re

"""

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

print(re.search(r"z(?=a)", "pizza"))
print(re.search(r"z(?!a)", "pizza"))

exp = 'hello there
I am from
Geeks for Geeks'

print(re.search(r"and", "Sun And Moon", flags=re.IGNORECASE))
print(re.findall(r"^\w", exp, flags=re.MULTILINE))

example = (re.search(r"(?:AB)", "ACABC"))
print(example)
print(example.groups())

result = re.search(r"(\w*), (\w*)", "geeks, best")
print(result.groups())

print(re.search(r"[^abc]","abcde"))
print(re.search(r"[a-p]","xenon"))

print(re.search(r"\s","xenon is a gas"))
print(re.search(r"\D+\d*","123geeks123"))

print(re.search(r"9+","289908"))
print(re.search(r"\d{3}","hello1234"))

print(re.search(r"^x","xenon"))
print(re.search(r"s$","geeks"))


"""

def talk(x, y , z):
    if(y<z):
        return 1 +talk (talk(x-1,y,z),talk(y-1,z,x),talk(z-1,x,y))
    else:
        return z


print(talk(18,12,6))