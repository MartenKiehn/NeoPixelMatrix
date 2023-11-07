# NeoPixelMatrix

A simple library for controlling a NeoPixel matrix display.
Running the app.py file will display a simple animation on the matrix.
Written for Raspberry Pi and WS2812B LED matrix displays.

### Prepare the Raspberry Pi

# Setting up WLAN on Raspberry Pi Zero

In this guide, you will learn how to set up a wireless LAN (Wi-Fi) connection on a Raspberry Pi Zero.

## Prerequisites

Before you begin, make sure you have the following:

- Raspberry Pi (Zero 2)
- MicroSD card with Raspberry Pi OS (Raspbian) installed
- USB Wi-Fi dongle (if your Raspberry Pi Zero doesn't have built-in Wi-Fi)
- Access to a computer with an SD card reader

## Set Up Wi-Fi and Enable Auto-Connect on Raspberry Pi

This guide will help you configure a Wi-Fi connection on your Raspberry Pi and make it automatically connect on boot.

### 1. Update and Upgrade Raspberry Pi OS
```bash
sudo apt update
sudo apt upgrade
```

### 2. Install Wi-Fi Tools
```bash
sudo apt install wireless-tools wpasupplicant
```

### 3. Check Available Wi-Fi Interfaces
```bash
iwconfig
```

### 4. Edit Wi-Fi Configuration File
```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
Add the following lines, replacing "Your_SSID" and "Your_Password":
```bash
network={
    ssid="Your_SSID"
    psk="Your_Password"
}
```

### 5. Enable the Wi-Fi Interface
```bash
sudo ifup wlan0
```

### 6. Check Your Wi-Fi Connection
```bash
ifconfig wlan0
```

### 7. Edit the Network Interfaces File
```bash
sudo nano /etc/network/interfaces
```

Add the following lines to auto-start the Wi-Fi interface. Replace "Your_SSID" and "Your_Password":
```bash
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

### 8. Reboot to Apply Changes
```bash
sudo reboot
```

## Start Application

### Install Flask
```bash
$ pip install flask
```

### Usage

```bash
$ python app.py
```
