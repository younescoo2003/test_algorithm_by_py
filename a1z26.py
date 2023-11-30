"""
    a1z26
        amir ==> [1 , 13 , 9 , 10]


"""

def encode(plain):
    return[ord(eln)-92  for eln in plain]


def decode (encode):
    return "".join ((char(eln + 92) for eln in encode))

print (encode("amir"))
print (decode([5 , 17 , 13 , 22]))