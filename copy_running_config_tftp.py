#!/usr/bin/env python
import datetime
import os
import re
import netmiko
from netmiko import ConnectHandler

print("Please wait seconds. Connecting ... \n")

my_device = {
        "host": "192.168.xxx.xxx", #cisco 2811
        "username": "xxx",
        "password": "xxx",
        "device_type": "cisco_ios",
        # "global_delay_factor": 2,
    }
starttime = datetime.datetime.now()
net_connect = ConnectHandler(**my_device)
net_connect.enable()

print(net_connect.find_prompt())
# cmd ="copy running-config tftp:/192.168.xxx.xxx/BackUp_cisco_2811_config"
cmd ="copy running-config tftp:"
result = net_connect.send_command(
    cmd,
    expect_string=r'Address or name of remote host',
    )
    # Address or name of remote host
    # Destination filename
result+=net_connect.send_command("192.168.xxx.xxx",expect_string=r"Destination filename")
result+=net_connect.send_command("R1_config",expect_string=r"#")

print(result)
endtime = datetime.datetime.now()
print("total time: {}".format(endtime - starttime))

net_connect.disconnect()

