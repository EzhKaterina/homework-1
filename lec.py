#Ускоренная обработка данных: lambda, filter, map, zip, enumerate(3 задачи):

1.
#lst = ["Ульяновскс", "Москва", "Рязань", "Ярославль", "Тверь", "Тула"]
#b = map(len, lst)
#a = list(b)
#print(a)

#b = map(lambda x: x.replace("а", "1"), lst)
#c = map(sorted, b)
#res1 = list(c)
#print(res1)

2.
#a = [3,6,7,-5]
#b = [1,-1,2,1]
#it = zip (a, b)
#print (it)
#print(list(it))

3.
#maximum = (lambda a, b: a if a>b else b)
#print(maximum(6, 7))

#min = (lambda a, b, c: a if (a<=b)and(b<=c) else (b if (b<=a)and(b<=c) else c))
#print(min(5,6,7))
