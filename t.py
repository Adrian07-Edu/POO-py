import dis

def a(lst, el):
    return not el in lst

def b(lst, el):
    return el not in lst

dis.dis(a)
print("\n")
dis.dis(b)