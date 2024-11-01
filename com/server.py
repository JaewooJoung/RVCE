# server.py
import zmq
import json
import socket
from dataclasses import dataclass

@dataclass
class SensorData:
    timestamp: float
    sensor_id: str
    sensor_type: str
    data: dict

class ADASServer:
    def __init__(self, port=15555):  # Using higher port number
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        
        try:
            # Get IP address
            hostname = socket.gethostname()
            self.ip_address = socket.gethostbyname(hostname)
            
            # Bind socket
            bind_addr = f"tcp://*:{port}"
            self.socket.bind(bind_addr)
            
            print("\n=== Server Started Successfully ===")
            print(f"IP Address: {self.ip_address}")
            print(f"Port: {port}")
            print(f"\nFor clients, use command:")
            print(f"python client.py {self.ip_address} {port}")
            print("\nWaiting for sensor data...")
            
        except Exception as e:
            print(f"Error starting server: {e}")
            self.cleanup()
            raise

    def cleanup(self):
        try:
            self.socket.close()
            self.context.term()
        except Exception as e:
            print(f"Error during cleanup: {e}")

    def receive_data(self):
        try:
            while True:
                message = self.socket.recv_string()
                data = json.loads(message)
                sensor_data = SensorData(**data)
                
                print(f"\nReceived {sensor_data.sensor_type} data from {sensor_data.sensor_id}")
                if sensor_data.sensor_type == "radar":
                    self.process_radar_data(sensor_data.data)
                elif sensor_data.sensor_type == "lidar":
                    self.process_lidar_data(sensor_data.data)
                    
        except KeyboardInterrupt:
            print("\nServer shutting down...")
        finally:
            self.cleanup()
            
    def process_radar_data(self, data):
        print("Radar Data:")
        print(f"Ranges (m): {data['ranges']}")
        print(f"Velocities (m/s): {data['velocities']}")
        print(f"Angles (deg): {data['angles']}")

    def process_lidar_data(self, data):
        print("Lidar Data:")
        print(f"X coordinates: {data['x']}")
        print(f"Y coordinates: {data['y']}")
        print(f"Z coordinates: {data['z']}")

if __name__ == "__main__":
    server = ADASServer()
    server.receive_data()
