# Jetson Nano System Information Viewer

## Overview
The `jetsoninfo.py` script is designed to retrieve and display various system information from a Jetson Nano device. It collects data such as the IP address, Wi-Fi signal strength, RAM usage, disk space, CPU usage, and CPU clock speed, and then sends this information to a 16x2 LCD display connected to the Jetson Nano via an I2C interface.

## Requirements
- Jetson Nano device
- 16x2 LCD display with I2C interface
- Python 3.x
- Required Python libraries:
  - `subprocess`
  - `psutil`
  - `serial`
  - `time`
  - `smbus` (for I2C communication)

## Installation
1. Connect the 16x2 LCD display to the Jetson Nano using the I2C interface.
2. Install the required Python libraries using pip:
   ```
   pip install subprocess psutil serial smbus
   ```
3. Save the `jetsoninfo.py` script to a directory on your Jetson Nano.

## Usage
1. Connect the 16x2 LCD display to the Jetson Nano.
2. Run the `jetsoninfo.py` script on the Jetson Nano:
   ```
   python jetsoninfo.py
   ```
3. The script will start sending system information to the 16x2 LCD display, which will display the data.

## Displayed Information
The script displays the following information on the 16x2 LCD display:
- IP Address
- Wi-Fi Signal Strength
- RAM Usage (Free/Total)
- Disk Space Usage
- CPU Usage
- CPU Clock Speed

The information is updated every 5 seconds (configurable through the `lcd_delay` variable).

## Troubleshooting
- Ensure that the I2C connection between the Jetson Nano and the 16x2 LCD display is working correctly.
- Check the I2C address of the LCD display and update the script accordingly.
- Verify that the required Python libraries, including `smbus` for I2C communication, are installed correctly.

## Contributing
If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request on the project's repository.

## License
This project is licensed under the [MIT License](LICENSE).
