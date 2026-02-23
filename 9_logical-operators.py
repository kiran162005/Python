# logical operators = evaluate multiple conditions(or, and, not)

# or = at least one condition must be True
# and = both the condition must be True
# not = inverts the condition (not True, not False)


temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


temp = 29
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0  and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28  and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
