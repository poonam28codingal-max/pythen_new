decimal = int(input("Enter a decimal number: "))
binary = ""
num = decimal
if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary 
        num = num // 2
print(f"The binary representation of {decimal} is {binary}")