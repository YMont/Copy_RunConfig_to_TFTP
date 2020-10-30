#!/usr/bin/env python
import datetime
import os
import re
import netmiko
from netmiko import ConnectHandler

print("Please wait seconds. Connecting ... \n")

my_device = {
        "host": "192.168.47.2", #cisco 2811
        "username": "yue",
        "password": "123",
        "device_type": "cisco_ios",
        # "global_delay_factor": 2,
    }
starttime = datetime.datetime.now()
net_connect = ConnectHandler(**my_device)
net_connect.enable()

print(net_connect.find_prompt())
# cmd ="copy running-config tftp:/192.168.47.47/BP_hackthon_2811-confg"
cmd ="copy running-config tftp:"
result = net_connect.send_command(
    cmd,
    expect_string=r'Address or name of remote host',
    )
    # Address or name of remote host
    # Destination filename
result+=net_connect.send_command("192.168.47.47",expect_string=r"Destination filename")
result+=net_connect.send_command("R1_config",expect_string=r"#")

print(result)
endtime = datetime.datetime.now()
print("total time: {}".format(endtime - starttime))

net_connect.disconnect()