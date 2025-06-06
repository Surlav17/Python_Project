train_class = input("Enter class (1st/2nd/3rd): ").lower()
distance = int(input("Enter distance in km: "))

# Initialize fare_per_km
if train_class == "1st":
    fare_per_km = 3
elif train_class == "2nd":
    fare_per_km = 2
elif train_class == "3rd":
    fare_per_km = 1
else:
    print("Invalid class selected.")
    fare_per_km = 0

# Only calculate if class is valid
if fare_per_km > 0:
    total_fare = fare_per_km * distance

    # Nested if: apply discount if distance > 1000
    if distance > 1000:
        discount = total_fare * 0.10
        total_fare -= discount
        print(f"You're eligible for a 10% long-distance discount of ₹{discount:.2f}")

    print(f"Class: {train_class.capitalize()}, Distance: {distance} km")
    print(f"Your total fare is ₹{total_fare:.2f}")