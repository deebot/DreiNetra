import RPi.GPIO as GPIO
import os
import subprocess
subprocess.call(["shutdown", "-h", "now"])
import time
import subprocess
import reset_lib
MONITOR=23
LED1=24
LED2=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(MONITOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED1, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

counter = 0
serial_last_four = subprocess.check_output(['cat', '/proc/cpuinfo'])[-5:-1].decode('utf-8')
config_hash = reset_lib.config_file_hash()
ssid_prefix = config_hash['ssid_prefix'] + " "
hostapd_reset_required = reset_lib.hostapd_reset_check(ssid_prefix)


if hostapd_reset_required == True:
    reset_lib.update_hostapd(ssid_prefix, serial_last_four)
    os.system('reboot')

# This is the main logic loop waiting for a button to be pressed on GPIO 18 for 10 seconds.
# If that happens the device will reset to its AP Host mode allowing for reconfiguration on a new network.
while True:
    while GPIO.input(MONITOR) == 1:
        time.sleep(1)
        counter = counter + 1

        print(counter)
		
		if counter ==9:
			GPIO.output(LED1, GPIO.HIGH)
			time.sleep(2)
			subprocess.call(["shutdown", "-h", "now"])

        if counter == 5:
			GPIO.output(LED2, GPIO.HIGH)
			time.s;eep(1)
			
            reset_lib.reset_to_host_mode()

        if GPIO.input(MONITOR) == 0:
            counter = 0
            break

    time.sleep(1)
