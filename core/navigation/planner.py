from typing import List, Dict, Any, Tuple

class PathPlanner:
    """
    Handles path planning functionality for the autonomous vehicle.
    """

    def plan_route(self, field_map: Dict[str, Any]) -> List[Tuple[float, float]]:
        """
        Generates a list of waypoints based on the provided field map.

        Args:
            field_map (Dict[str, Any]): The map of the field, containing row coordinates.

        Returns:
            List[Tuple[float, float]]: A list of coordinate tuples (x, y) representing the route.
        """
        waypoints = []
        rows = field_map.get("rows", [])
        for row in rows:
            waypoints.extend(row["coordinates"])
        return waypoints
