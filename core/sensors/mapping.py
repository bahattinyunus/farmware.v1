from core.sensors.gps import GPSHandler
from core.sensors.camera import CameraHandler

class FieldMapper:
    """Handles field mapping using GPS and camera data."""

    def __init__(self, gps_port, camera_index):
        self.gps_handler = GPSHandler(gps_port)
        self.camera_handler = CameraHandler(camera_index)

    def map_field(self, num_boundaries=4):
        """Map the field by collecting GPS and camera data."""
        field_map = {"boundaries": [], "rows": []}

        # Collect GPS boundaries
        print("Collecting GPS data for field boundaries...")
        for i in range(num_boundaries):
            coord = self.gps_handler.get_coordinates()
            if coord:
                field_map["boundaries"].append(coord)
            else:
                print("Failed to retrieve GPS data.")
        
        # Capture images for rows (example: two rows)
        print("Capturing camera data for rows...")
        for i in range(2):  # Example: two rows
            frame_path = self.camera_handler.capture_frame(f"row_{i}.jpg")
            if frame_path:
                field_map["rows"].append({
                    "id": i + 1, 
                    "image": frame_path,
                    "coordinates": [(10.0 + i, 10.0), (10.0 + i, 20.0)] # Mock coordinates
                })

        # Clean up resources
        self.gps_handler.close()
        self.camera_handler.release()

        return field_map
