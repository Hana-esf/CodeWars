from unittest import result


def bmi(weight, height):
    b = weight / height ** 2
    print(b)
    result = (b > 30) + (b > 25)#[(b > 30) + (b > 25) + (b > 18.5)]
    print(result)
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

w = input('enter weigh : ')
h = input('enter hight : ')
w = int(w)
h = int(h)
print(bmi(w,h))