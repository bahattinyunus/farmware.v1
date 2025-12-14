import json
from typing import Dict, Any, List
from core.navigation.planner import PathPlanner
from core.sensors.mapping import FieldMapper
from core.control.steering import SteeringController
from core.control.sprayer import SprayerController

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        Dict[str, Any]: The configuration dictionary.
    """
    with open(config_path, 'r') as f:
        return json.load(f)

def main() -> None:
    """
    Main entry point for the Farmware application.
    Initializes components, performs field mapping, plans path, and executes spraying.
    """
    # Load configurations
    config = load_config("data/config.json")
    print("Configuration loaded:", config)

    # Initialize components
    field_mapper = FieldMapper(
        gps_port=config.get("gps_port", "COM3"),
        camera_index=config.get("camera_index", 0)
    )
    path_planner = PathPlanner()
    steering_controller = SteeringController()
    sprayer_controller = SprayerController()

    # Step 1: Map the field
    print("Mapping the field...")
    field_map = field_mapper.map_field()
    print("Field map created:", field_map)

    # Step 2: Plan the route
    print("Planning the route...")
    route = path_planner.plan_route(field_map)
    print("Route planned:", route)

    # Step 3: Execute the route
    print("Executing the route...")
    for waypoint in route:
        steering_controller.navigate_to(waypoint)
        sprayer_controller.spray()

    print("Spraying completed successfully!")

if __name__ == "__main__":
    main()
