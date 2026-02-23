# logical operators = evaluate multiple conditions(or, and, not)

# or = at least one condition must be True
# and = both the condition must be True
# not = inverts the condition (not True, not False)


temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
