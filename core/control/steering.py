import time

class SteeringController:
    def navigate_to(self, waypoint):
        print(f"Navigating to waypoint: {waypoint}")
        time.sleep(1) # Reduced sleep for faster testing
        print("Arrived at waypoint.")
