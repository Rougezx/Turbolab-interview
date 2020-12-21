#first part

def split_sum(inputs):
    inputs = inputs.lower()
    output1 = []
    output2= []
    res_first = inputs[0:len(inputs)//2]
    res_second = inputs[len(inputs)//2 if len(inputs)%2 == 0
                                     else ((len(inputs)//2)+1):]
    for character in res_first:
        number = ord(character) - 96
        output1.append(number)
    for character in res_second:
        number = ord(character) - 96
        output2.append(number)
    s = [str(i) for i in output1]
    res1 = int("".join(s))
    s1 = [str(i) for i in output2]
    res2 = int("".join(s))
    print(res1+res2)
split_sum('petpan')
