# client.py
import zmq
import json
import time
from dataclasses import dataclass, asdict
import sys
from typing import List

@dataclass
class SensorData:
    timestamp: float
    sensor_id: str
    sensor_type: str
    data: dict

class ADASClient:
    def __init__(self, server_ip, port=15555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        
        server_address = f"tcp://{server_ip}:{port}"
        print(f"Connecting to server at {server_address}")
        
        try:
            self.socket.connect(server_address)
            print("Successfully connected to server")
        except Exception as e:
            print(f"Error connecting to server: {e}")
            raise

    def send_radar_data(self, sensor_id: str, ranges: List[float], 
                       velocities: List[float], angles: List[float]):
        data = SensorData(
            timestamp=time.time(),
            sensor_id=sensor_id,
            sensor_type="radar",
            data={
                "ranges": ranges,
                "velocities": velocities,
                "angles": angles
            }
        )
        self._send_data(data)

    def _send_data(self, sensor_data: SensorData):
        try:
            message = json.dumps(asdict(sensor_data))
            self.socket.send_string(message)
            print(f"Sent {sensor_data.sensor_type} data from {sensor_data.sensor_id}")
        except Exception as e:
            print(f"Error sending data: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py SERVER_IP [PORT]")
        print("Example: python client.py 192.168.1.100 15555")
        sys.exit(1)
        
    server_ip = sys.argv[1]
    port = 15555  # default port
    
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Error: Port must be a number")
            sys.exit(1)
    
    try:
        client = ADASClient(server_ip, port)
        
        # Send test data
        while True:
            client.send_radar_data(
                sensor_id="test_radar",
                ranges=[50.0, 45.0, 30.0],
                velocities=[20.0, -10.0, 5.0],
                angles=[0.0, 10.0, -5.0]
            )
            time.sleep(1)  # Send every second
            
    except KeyboardInterrupt:
        print("\nClient stopped by user")

if __name__ == "__main__":
    main()
