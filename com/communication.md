# RVCE Project: Sensor Data Communication Implementation Report

## Executive Summary
This report documents the successful implementation of a real-time sensor data communication system between a Raspberry Pi 4 and an Intel-based computer, demonstrating the feasibility of sensor data transmission between different computing platforms. This implementation proves that similar communication can be established between a Raspberry Pi 5 camera system and NVIDIA AGX Orin for the RVCE (Remote Vehicle Control Environment) project.

## System Architecture

### Hardware Setup
- **Sender Platform**: Raspberry Pi 4
- **Receiver Platform**: Intel-based computer
- **Network**: Local network connection (TCP/IP)
- **Test Environment**: Both devices connected to the same network (192.168.1.x)

### Software Components
- **Communication Protocol**: ZMQ (ZeroMQ)
- **Data Format**: JSON
- **Programming Language**: Python 3
- **Key Libraries**: 
  - pyzmq (ZeroMQ Python bindings)
  - json (data serialization)
  - dataclasses (structured data handling)

## Implementation Details

### 1. Server (Receiver) Implementation
The server runs on the receiving platform (Intel computer in our test, AGX Orin in production) and:
- Creates a ZMQ PULL socket
- Binds to a specified port (15555)
- Continuously listens for incoming sensor data
- Processes and displays received data in real-time

```python
# Key server configuration
class ADASServer:
    def __init__(self, port=15555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind(f"tcp://*:{port}")
```

### 2. Client (Sender) Implementation
The client runs on the sending platform (Raspberry Pi 4 in our test, Raspberry Pi 5 with camera in production) and:
- Creates a ZMQ PUSH socket
- Connects to the server's IP address and port
- Sends sensor data continuously
- Handles connection and data transmission errors

```python
# Key client configuration
class ADASClient:
    def __init__(self, server_ip, port=15555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.socket.connect(f"tcp://{server_ip}:{port}")
```

## Testing and Validation

### Test Setup
1. Server (Intel Computer):
   - IP Address: 192.168.1.7
   - Port: 15555
   - Running receiver code

2. Client (Raspberry Pi 4):
   - Connected to same network
   - Running sender code
   - Transmitting test sensor data

### Test Results
- Successfully established connection between platforms
- Achieved reliable data transmission
- Maintained stable communication over extended periods
- Demonstrated feasibility of cross-platform sensor data transfer

[![TESTED Image](RVCE/com/image.png)](RVCE/com/test.mp4)

## Deployment Instructions

### Server Setup (Receiver)
1. Install required packages:
```bash
pip install pyzmq
```

2. Run the server:
```bash
python server.py
```

### Client Setup (Sender)
1. Install required packages on Raspberry Pi:
```bash
pip install pyzmq
```

2. Run the client with server's IP:
```bash
python client.py 192.168.1.7 15555
```

### Network Configuration
- Ensure both devices are on the same network
- Configure firewall to allow port 15555:
```bash
sudo ufw allow 15555
```

## Feasibility for RVCE Project

### Key Findings
1. **Cross-Platform Compatibility**: Successfully demonstrated communication between different computing platforms (Raspberry Pi and Intel), indicating feasibility for Raspberry Pi 5 to AGX Orin communication.

2. **Performance**: ZMQ provides:
   - Low latency communication
   - High throughput capability
   - Reliable data transmission
   - Built-in error handling

3. **Scalability**: The implementation can handle:
   - Different types of sensor data
   - High-frequency transmission
   - Large data packets (suitable for camera data)

### Advantages for RVCE Implementation
1. **Flexibility**: Can easily adapt to different data types and formats
2. **Reliability**: Built-in error handling and recovery
3. **Simplicity**: Straightforward implementation and maintenance
4. **Performance**: Suitable for real-time camera data transmission

## Future Recommendations

1. **Camera Integration**
   - Implement camera data capture on Raspberry Pi 5
   - Add image compression for efficient transmission
   - Optimize packet size for camera data

2. **Performance Optimization**
   - Fine-tune ZMQ socket parameters
   - Implement data buffering if needed
   - Add monitoring for system performance

3. **Error Handling**
   - Add automatic reconnection
   - Implement data validation
   - Add logging system

## Conclusion
The successful implementation and testing of this communication system between Raspberry Pi 4 and Intel computer demonstrates that the proposed communication architecture is feasible for the RVCE project. The system can be readily adapted for camera data transmission between Raspberry Pi 5 and NVIDIA AGX Orin, providing a robust foundation for the project's communication requirements.

The ZMQ-based implementation offers the necessary performance, reliability, and flexibility needed for real-time sensor data transmission in the RVCE environment. This proof of concept validates the technical approach and provides a clear path forward for the full project implementation.
