print("Координаты точки:")
x = float (input("x = "))
y = float (input("y = "))

if x > 0 and y > 0:
    print("Точка в I четверти")
elif x < 0 and y > 0:
    print("Точка во II четверти")
elif x < 0 and y < 0:
    print("Точка в III четверти")
elif x > 0 and y < 0:
    print("Точка в IV четверти")
elif x == 0 and y == 0:
    print("Точка в центре координат")
elif x == 0:
    print("Точка на оси X")
elif y == 0:
    print("Точка на оси Y")
