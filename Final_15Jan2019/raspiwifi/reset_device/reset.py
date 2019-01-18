import RPi.GPIO as GPIO
import os
import time
import subprocess
import reset_lib
MONITOR=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(MONITOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.OUT,initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(25, GPIO.OUT,initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
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
# while True:
    # while GPIO.input(MONITOR) == 1:
        # time.sleep(1)
        # counter = counter + 1

        # print(counter)

        # if counter == 9:
            # reset_lib.reset_to_host_mode()

        # if GPIO.input(MONITOR) == 0:
            # counter = 0
            # break

    # time.sleep(1)
while True:
	while GPIO.input(MONITOR) == 1:
		time.sleep(0.5)
		counter = counter + 1
	if(counter>1 and counter<5):
		GPIO.output(24, GPIO.HIGH) # Turn on
		GPIO.output(25, GPIO.LOW) # Turn on
		time.sleep(2)
		#if(GPIO.input(MONITOR) == 1):
		print("shutting down.....")
		subprocess.call(["shutdown","-h","now"])
	elif(counter>5):
		GPIO.output(24, GPIO.LOW) # Turn on
		GPIO.output(25, GPIO.HIGH) # Turn on
		time.sleep(2)
		print("Resetting the system")
		reset_lib.reset_to_host_mode()
	if GPIO.input(MONITOR) == 0:
		GPIO.output(24, GPIO.HIGH) # Turn on
		GPIO.output(25, GPIO.HIGH) # Turn on
		counter = 0		
	print(counter)
	time.sleep(1)
