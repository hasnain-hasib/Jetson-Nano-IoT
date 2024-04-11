import subprocess
import psutil
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

lcd_delay = 5 

while True:
    # Retrieve the IP address
    output = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    ip_address = output.decode().strip()

    # Send the IP address to the Arduino
    ser.write("".format(ip_address).encode())
    time.sleep(lcd_delay)

    # Retrieve the IP address
    output = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    ip_address = output.decode().strip()

    # Send the IP address to the Arduino
    ser.write("IP Address\n:{}".format(ip_address).encode())
    time.sleep(lcd_delay)

    # Retrieve the wifi signal strength
    output = subprocess.check_output("iwconfig wlan0 | grep 'Signal level' | awk '{print $4}'", shell=True)
    wifi_signal_strength = output.decode().strip()

    # Send the wifi signal strength to the Arduino
    ser.write("Wifi Signal :{}".format(wifi_signal_strength).encode())
    time.sleep(lcd_delay)

    # Retrieve the free and total RAM
    output = subprocess.check_output("free -m | awk 'NR==2{print $3\" MB /\", $2\"MB\"}'", shell=True)
    ram_info = output.decode().strip()

    # Send the RAM information to the Arduino
    ser.write("RAM Info\n:{}".format(ram_info).encode())
    time.sleep(lcd_delay)

    # Retrieve the free and total disk space
    output = subprocess.check_output("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'", shell=True)
    disk_space = output.decode().strip()

    # Send the disk space information to the Arduino
    ser.write("{}\n".format(disk_space).encode())

    # Retrieve the CPU total usage and real-time clock speed
    cpu_usage = psutil.cpu_percent()
    cpu_clock_speed = psutil.cpu_freq().current / 500

    # Send the CPU information to the Arduino
    ser.write("".format(cpu_usage).encode())
    time.sleep(lcd_delay)


# Retrieve the CPU total usage and real-time clock speed
    cpu_usage = psutil.cpu_percent()
    cpu_clock_speed = psutil.cpu_freq().current / 500

    # Send the CPU information to the Arduino
    ser.write("CPU Usage\n:{}%".format(cpu_usage).encode())
    time.sleep(lcd_delay)

    # Send the real-time clock speed information to the Arduino
    output = subprocess.check_output("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq", shell=True)
    cpu_clock_speed_realtime = float(output) / 1000000
    ser.write("".format(cpu_clock_speed_realtime).encode())
    time.sleep(lcd_delay)

 # Send the real-time clock speed information to the Arduino
    output = subprocess.check_output("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq", shell=True)
    cpu_clock_speed_realtime = float(output) / 1000000
    ser.write("Cpu Clock Speed:{:.2f}GHz".format(cpu_clock_speed_realtime).encode())
    time.sleep(lcd_delay)

# Close the serial connection
ser.close()
