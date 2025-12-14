import time

class SprayerController:
    def __init__(self, spray_rate=10, tank_capacity=200):
        self.spray_rate = spray_rate
        self.tank_capacity = tank_capacity
        self.current_tank_level = tank_capacity

    def spray(self):
        duration = 1
        spray_amount = self.spray_rate * duration

        if self.current_tank_level >= spray_amount:
            self.current_tank_level -= spray_amount
            print(f"Spraying for {duration} seconds. {spray_amount:.2f}L used.")
            print(f"Remaining tank level: {self.current_tank_level:.2f}L")
            time.sleep(0.1) # Reduced sleep for faster testing
            return True
        else:
            print("Tank is empty! Refill required.")
            return False
