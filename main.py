# This program is a simple weight converter. This is my first Python program.

intro = "Hello, my name is Verty! I can convert weight from pounds to kilios, and from kilos to pounds."
instruction = "Please use only numeric values for your weight"
print(intro)
print(instruction)

weight = int(input("How do you weigh? "))
unit_of_measurement = input("Is that in (L)bs or (K)gs? ")

if unit_of_measurement.upper() == "L":
    conversion_kgs = weight * 0.45
    print(f"Wow you weigh {conversion_kgs} Kilograms!")

elif unit_of_measurement.upper() == "K":
    conversion_lbs = weight / 0.45
    print(f"Wow you weigh {conversion_lbs} Pounds!")

else:
    print("I don't UNDERSTAND!")