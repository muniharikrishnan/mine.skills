n = int(input())
ones=["","one","two","three","four","five","six","seven","eight","nine"]
tens=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty"]
teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

if n>=1000:
    print(ones[n//1000]+" thousand",end=" ")

n=n%1000

if n>=100 and n<1000:
    print(ones[n//100]+ " hundred",end=" ")

n=n%100

if n>=10 and n<=19:
    print(teens[n%10],end=" ")

elif n>=20 and n<100:
    print(tens[n//10],end=" ")


if n>=1 and n<=9:
    print(ones[n],end=" ")



