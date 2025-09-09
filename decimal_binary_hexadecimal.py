#this alg is supposed to be used with linked list 
# as inserting at beggining in an array is not efficient

def decimal_to_binary(num):
    binary = []
    number = num
    while number > 0:
        r = number % 2
        binary.insert(0,r)
        number = number//2
    return binary

def binary_to_decimal(binary):
    result = 0
    j = 0
    for i in range(len(binary)-1,-1,-1):
        if binary[i]==1:
            result+=(2**j)
        j+=1
    return result

def add_binaries(a,b):
    max_length = max(len(a),len(b))
    #we need to pad to make sure a and b are same length
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    else:
        b = [0] * (len(a) - len(b)) + b

    result = []
    carry = 0
    for i in range(max_length-1,-1,-1):
        sum = a[i]+b[i]+carry
        carry = sum//2
        result.insert(0,sum % 2)
    if carry!=0:
        result.insert(0,carry)
    return result

def decimal_to_hexadecimal(num):
    decimal = num
    match = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    hexa = []
    while decimal>=1:
        current = decimal // 16
        #print(current)
        r = decimal % 16
        #print(r)
        r = match[r]
        hexa.insert(0,r)
        #print(hexa)
        decimal = current
    converted = ""
    for c in hexa:
        converted+=c
    return converted

def hexadecimal_to_decimal(hexadecimal):
    match = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    decimal = 0
    j = 0
    for i in range(len(hexadecimal)-1,-1,-1):
        #print(f"{match[hexadecimal[i]]}*16^{i}")
        decimal+=(match[hexadecimal[i]])*(16**j)
        j+=1
    return decimal

def compliment(binary):
    comp = []
    for bit in binary:
        if bit==0:
            comp.append(1)
        else:
            comp.append(0)
    comp = add_binaries(comp,[1])
    return comp

def main():
    print(hexadecimal_to_decimal("1DF"))
main()