import re

txt = r"^1233"
x = re.match(txt, "123434")
y=re.search(r"[1-9]",txt)
print(x)
print(y)