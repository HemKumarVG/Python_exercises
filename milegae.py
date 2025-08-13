"""
Using the starting and ending values of your car's odometer, 
calculate its mileage.
"""

start_om_val = int(input("Enter the start odometer value before the drive: "))
end_om_val = int(input("Enter the end odometer value after the drive: "))
tank_capacity = int(input("Enter the tank capacity (in liters): "))
fuel_avail_before_trip = int(input("Enter the fuel available before trip (in liters): "))
fuel_recharge = int(input("Enter the fuel refilled during trip (in liters): "))
fuel_left = int(input("Enter the fuel left after trip (in liters): "))

# Calculate distance travelled
distance_travelled = end_om_val - start_om_val

# Calculate fuel used
fuel_total = fuel_avail_before_trip + fuel_recharge
fuel_used = fuel_total - fuel_left

milege = distance_travelled / fuel_used
print("the milege recieved is", milege)
