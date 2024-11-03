# RVCE
Proof Of Concept
## architecture:

```mermaid
graph LR
    %% Define Remote Control
    remote[Remote Control Center]
    wifi[WiFi Router]
    
    %% Define Cameras and Raspberry Pis
    cam_front[Front Camera]
    cam_back[Back Camera]
    cam_left[Left Camera]
    cam_right[Right Camera]
    
    rpi_front[Raspberry Pi 5 Front]
    rpi_back[Raspberry Pi 5 Back]
    rpi_left[Raspberry Pi 5 Left]
    rpi_right[Raspberry Pi 5 Right]
    
    %% Define Network and Processing
    switch[Ethernet Switch]
    orin[NVIDIA AGX Orin]
    
    %% Define CAN and Controls
    can[CAN Controller]
    brake[Brake Controller]
    gear[Gear Controller]
    steering[Steering Controller]
    
    %% Connect Remote to WiFi
    remote <--> |Control Commands & Feedback| wifi
    wifi <--> |Wireless Link| orin
    
    %% Connect cameras to respective RPis
    cam_front --> rpi_front
    cam_back --> rpi_back
    cam_left --> rpi_left
    cam_right --> rpi_right
    
    %% Connect RPis to Ethernet Switch
    rpi_front --> |Processed Video| switch
    rpi_back --> |Processed Video| switch
    rpi_left --> |Processed Video| switch
    rpi_right --> |Processed Video| switch
    
    %% Connect Switch to Orin
    switch --> |Video Data| orin
    
    %% Connect Orin to CAN Controller
    orin --> |Control Commands| can
    
    %% Connect CAN to Controllers
    can --> |CAN Bus| brake
    can --> |CAN Bus| gear
    can --> |CAN Bus| steering
    
    %% Add styles
    classDef sensor fill:#a8d5ff,stroke:#333,stroke-width:2px
    classDef processor fill:#ff9b9b,stroke:#333,stroke-width:2px
    classDef network fill:#ffd700,stroke:#333,stroke-width:2px
    classDef control fill:#9fff9f,stroke:#333,stroke-width:2px
    classDef can fill:#ff9f9f,stroke:#333,stroke-width:2px
    classDef remote fill:#c8a2c8,stroke:#333,stroke-width:2px
    
    %% Apply styles
    class cam_front,cam_back,cam_left,cam_right sensor
    class rpi_front,rpi_back,rpi_left,rpi_right,orin processor
    class switch,wifi network
    class brake,gear,steering control
    class can can
    class remote remote
```

## Step by step work
1. [Trial of making the communication stack with Camera to Server](./com/communication.md)
2. Camera BOM (this is for development, inspired by [link](https://datarootlabs.com/blog/hailo-ai-kit-raspberry-pi-5-setup-and-computer-vision-pipelines#implementing-custom-detection-tracking-pipeline))

| Item No. | Component                                        | Specification      | Qty | Est. Cost (£) | Sample Image                                                                                              | Link                                                                                   | Notes                                                |
|----------|--------------------------------------------------|---------------------|-----|----------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------|
| 1        | Raspberry Pi 5 Model B                           | 8GB RAM             | 1   | 76.8           | <img src="https://thepihut.com/cdn/shop/files/raspberry-pi-5-raspberry-pi-40958498898115_700x.jpg?v=1695819922" alt="Raspberry Pi 5" width="100"/> | [Link](https://thepihut.com/products/raspberry-pi-5?variant=42531604955331) |                                                      |
| 2        | AI Bundle (Hailo 8L) for Raspberry Pi 5         | AI Bundle           | 1   | 91.8           | <img src="https://thepihut.com/cdn/shop/files/ai-bundle-hailo-8l-for-raspberry-pi-5-pineboards-106038-42832289726659_700x.jpg?v=1724824572" alt="AI Bundle" width="100"/> | [Link](https://thepihut.com/products/ai-bundle-hailo-8l-for-raspberry-pi-5) |                                                      |
| 3        | 12MP IMX708 HDR 120° Camera                     | 120° FOV            | 1   | 34.7           | <img src="https://thepihut.com/cdn/shop/files/arducam-12mp-imx708-hdr-120-camera-module-with-wide-angle-m12-lens-for-raspberry-pi-arducam-b0310-40596338049219_700x.jpg?v=1724774228" alt="12MP Camera" width="100"/> | [Link](https://thepihut.com/products/arducam-12mp-imx708-hdr-120-wide-angle-camera-module-with-m12-lens-for-raspberry-pi) | Arducam 12MP IMX708 HDR 120° Camera Module with Wide-Angle M12 Lens for Raspberry Pi |
| 4        | Pinedrive 256GB NVMe SSD (2280)                 | 256GB, 2280         | 1   | 35.91          | <img src="https://thepihut.com/cdn/shop/files/pinedrive-256gb-nvme-ssd-2280-pineboards-105969-42368160202947_700x.jpg?v=1717692241" alt="Pinedrive SSD" width="100"/> | [Link](https://thepihut.com/products/pinedrive-256gb-nvme-ssd-2280) |                                                      |
| 5        | Active Cooler                                    | Pi 5 Compatible     | 1   | 5.2            | <img src="https://thepihut.com/cdn/shop/files/argon-thrml-30mm-active-cooler-for-raspberry-pi-5-argon40-41416718024899_700x.jpg?v=1704902893" alt="Active Cooler" width="100"/> | [Link](https://thepihut.com/products/argon-thrml-30mm-active-cooler-for-raspberry-pi-5) | Argon THRML 30mm Active Cooler for Raspberry Pi 5  |
| 6        | MicroSD Card                                    | 32GB Class 10       | 1   | 9.9            | <img src="https://thepihut.com/cdn/shop/files/official-pi-hole-raspberry-pi-4-kit-the-pi-hut-105033-43171441311939_700x.jpg?v=1726632845" alt="MicroSD Card" width="100"/> | [Link](https://thepihut.com/products/noobs-preinstalled-sd-card) | Official Raspberry Pi Micro SD Card with RPi OS Pre-Installed |
| 7        | Custom Case                                      | Fits Pi 5 + AI bundle | 1   | 8              | <img src="https://thepihut.com/cdn/shop/files/layer-case-for-pineboards-hats-the-pi-hut-tph-078-42874102055107_700x.jpg?v=1724811056" alt="Custom Case" width="100"/> | [Link](https://thepihut.com/products/layer-case-for-pineboards-hats) | Just for a development                               |
| 8        | Mounting Kit                                     | Tripod Mount        | 1   | 8.4            | <img src="https://thepihut.com/cdn/shop/files/die-cast-tripod-mount-for-raspberry-pi-camera-modules-entaniya-106019-42832871063747_700x.jpg?v=1724814306" alt="Mounting Kit" width="100"/> | [Link](https://thepihut.com/products/die-cast-tripod-mount-for-raspberry-pi-camera-modules) | Die-cast Tripod Mount for Raspberry Pi Camera Modules |
| 9        | Camera Mount                                     | Adjustable          | 1   | 5              | <img src="https://thepihut.com/cdn/shop/files/extendable-tripod-for-raspberry-pi-hq-camera-the-pi-hut-106062-42899004326083_700x.jpg?v=1724815391" alt="Camera Mount" width="100"/> | [Link](https://thepihut.com/products/extendable-tripod-for-raspberry-pi-hq-camera) | Extendable Tripod for Raspberry Pi HQ Camera       |
| 10       | Mini HDMI Cable                                  | 1m length           | 1   | 3.8            | <img src="https://thepihut.com/cdn/shop/products/micro-hdmi-to-hdmi-cable-for-raspberry-pi-4-the-pi-hut-103596-29915930689731_700x.jpg?v=1646362088" alt="Mini HDMI Cable" width="100"/> | [Link](https://thepihut.com/products/hdmi-to-micro-hdmi-cable-2m-gold-plated?variant=40818117050563) |                                                      |

Total Cost : £279.51



