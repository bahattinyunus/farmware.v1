import unittest
from core.sensors.gps import GPSHandler
from core.sensors.camera import CameraHandler

from unittest.mock import MagicMock, patch

class TestSensors(unittest.TestCase):
    @patch('core.sensors.gps.serial.Serial')
    def test_gps_coordinates(self, mock_serial):
        # Setup mock
        mock_instance = MagicMock()
        mock_instance.readline.return_value = b"49.12345,-123.12345"
        mock_serial.return_value = mock_instance

        gps = GPSHandler(port="COM1", baudrate=9600)
        gps_data = gps.get_coordinates()
        
        self.assertEqual(gps_data, {"lat": 49.12345, "lng": -123.12345})
        gps.close()

    @patch('core.sensors.camera.cv2.VideoCapture')
    @patch('core.sensors.camera.cv2.imwrite')
    @patch('core.sensors.camera.os.makedirs')
    def test_camera_capture_frame(self, mock_makedirs, mock_imwrite, mock_video_capture):
        # Setup mock
        mock_camera = MagicMock()
        mock_camera.read.return_value = (True, "fake_frame_data")
        mock_video_capture.return_value = mock_camera

        camera = CameraHandler(camera_index=0, output_dir="data/camera_frames")
        frame_path = camera.capture_frame("test_frame.jpg")
        
        self.assertIsNotNone(frame_path)
        self.assertTrue(frame_path.endswith("test_frame.jpg"))
        camera.release()

if __name__ == "__main__":
    unittest.main()

#use the following command to test /// python -m unittest discover -s tests -p "test_*.py" /// or else you will get module error