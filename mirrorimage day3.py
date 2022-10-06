def reverse(s):
    num =""
    for i in s:
        num =i+num
    return num
s=input("enetr the number:")
print("the mirror image is:",end=" ")
print(reverse(s))
