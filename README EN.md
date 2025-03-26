# SMS control led  Solution for QuecPython



[中文](README.md) | English

Welcome to the SMS control led  Solution for QuecPython! This warehouse provides an open source project focusing on LED control and SMS notification functions, which is suitable for remote control and status reporting to improve the efficiency of equipment management.

## Table of Contents



- [Introduction](#introduction)
- [Features](#features)
- Getting Started
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Support](#support)

## Introduction

QuecPython has introduced a remote control method for LED lights, such as SMS control LED on and off.

With the QuecPython-encapsulated interface, remote control of lights can be easily achieved in just a few steps, eliminating the need for traditional manual switching.

## Features

- **Identify custom verification code ** : If you want to control the device, you need to send a command (LIGHT) with the correct verification code to the device to improve device security.

-  **LIGHT L1 ON** : The mobile phone sends verification code (LIGHT) + Custom device number (L1) + Device action (ON) to enable L1 device to turn on lights
-  **LIGHT L1 OFF** : The mobile phone sends verification code (LIGHT) + Custom device number (L1) + device action (OFF) to turn off the light of the L1 device

### Prerequisites



Before you begin, ensure you have the following prerequisites:

- **Hardware**:
  - A QuecPython wearable development board
  - USB Data Cable (USB-A to USB-C)
  - PC (Windows 7, Windows 10, or Windows 11)
- **Software**:
  - USB driver for the QuecPython module
  - QPYcom debugging tool
  - QuecPython firmware and related software resources
  - Python text editor (e.g., [VSCode](https://code.visualstudio.com/), [Pycharm](https://www.jetbrains.com/pycharm/download/))

### Installation



1. **Clone the Repository**:

   ```
   git clone https://github.com/aaronchenzhihe/SMS_LED.git
   cd LED_SMS
   ```

   

2. **Flash the Firmware**:

   Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Firmware) to flash the firmware to the development board.

### Running the Application



1. **Connect the Hardware**:
   - Insert the SIM card into the SIM card slot.
   - Connect the antenna.
   - Use a USB data cable to connect the development board to the computer's USB port.
2. **Download Code to the Device**:
   - Launch the QPYcom debugging tool.
   - Connect the data cable to the computer.
   - Press the **PWRKEY** button on the development board to start the device.
   - Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Script) to import all files within the `code` folder into the module's file system, preserving the directory structure.
3. **Run the Application**:
   - Select the `File` tab.
   - Select the `main_t.py` script.
   - Right-click and select `Run` or use the run shortcut button to execute the script.

## Directory Structure



```plaintext
solution-LED_SMS/
├── code/
│   ├── _main.py        # Startup control module
└── README.md               # Company of Heroes Readme
```



## Usage



![image-20250320095741386](./docs/media/1.png)

## Contribution



We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](https://github.com/QuecPython/solution-wearable/blob/master/LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en).
