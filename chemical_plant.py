"""
A Chemical plant has a tank for storing ethanol.
- When the tank is more than 80% full, it
     should raise an alarm to close the valve.
- When the tank is less than 20% full, it
     should send an SMS to buy more liquid.
- The total tank capacity is 900 litres.
- Write a program to simulate this.
- Ask user to enter current level of ethanol in the tank.
- Print the appropriate action based on value entered

"""
cur_ethanol = int(input("enter current level of ethanol in the tank in liters: "))
if cur_ethanol > 720:
    print("tank is more than 80%, please close the valve")
elif cur_ethanol < 180:
    print("tank is less than 20%, Please buy more liquid")
else:
    print("Tank is normal")
