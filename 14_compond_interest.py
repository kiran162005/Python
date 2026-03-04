#python copound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle cant be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate:"))
    