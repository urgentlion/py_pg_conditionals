num_ = 21
age_to_rent_car = 25

if num_ >= age_to_rent_car:
  print("You are old enough to rent a car")
else:
  gap_ = age_to_rent_car - num_
  print(f"You must wait {gap_} more years. You are not old enough to rent a car")
  
age_ = int(input("How old are you? "))

if age_ < 13:
  print("You can't ride the roller coaster.")
else:
  print("You can ride the roller coaster!")