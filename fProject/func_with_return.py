def add(a,b):
    c=a+b
    return c
d=add(4,9)
print(d)

def name(fname,lname):
    formatfname=fname.title()
    formatlname=lname.title()
    return f"{formatfname} {formatlname}"

c=name("thamindu","KULASekara")
print(c)