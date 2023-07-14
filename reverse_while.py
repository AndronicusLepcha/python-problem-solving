#reverse String using while loop in Python
s=input('Enter the string ')
output='' #empty string
i=len(s)-1 # array start from 0th index so -1

while i>=0:
    output=output+s[i] # i will point to last char of the string
    i=i-1 # decrement the i value

print(output)