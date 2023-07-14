# progrma to find the unique voewls present i nthe word
vowels =['a','e','i','o','u']
word=input('enter the string')
result=[]
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)
print(result)
print("length of unique vowel {}".format(len(result)))

#list comprehension
r=[ch for ch in vowels if ch in word]
print(r)