#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('Insert a number: '))
if 5 < n < 8:
    print("Day-off")
elif 0 < n < 6:
    print("Working days")
else:
    print("Incorrect number")
