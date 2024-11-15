palavra1=input("primeira palavra? ")
palavra2=input("segunda palavra? ")


a=set(palavra1)
b=set(palavra2)

intersection= a.intersection(b)

res="".join(intersection)

print(res)
