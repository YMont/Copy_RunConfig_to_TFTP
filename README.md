# Cisco with Netmiko

## command: copy running-config tftp
you can use python script instead of using console to connect network's device<br>
使用Python第三方庫Netmiko去下達命令至Cisco Switch/Router Interface

## installation
`pip install netmiko`

------
###### reference
[from author "Kirk Byers"](https://pynet.twb-tech.com/blog/automation/netmiko-what-is-done.html)

### Getting Started:

#### Import module
```py
import datetime
import os
import re
import netmiko
from netmiko import ConnectHandler
```

#### Login information
```py
my_device = {
        "host": "192.168.xxx.xxx", #cisco 2811
        "username": "xxx",
        "password": "xxx",
        "device_type": "cisco_ios",
        # "global_delay_factor": 2,
    }
```
#### Start timer and connect network device
```py
starttime = datetime.datetime.now()
net_connect = ConnectHandler(**my_device)
net_connect.enable()
```
#### Enable Cisco "privileged" mode use "send_command" function and find expect string
If you want to use global mode that you will use "send_config_set" function.
```py
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
```
#### Show endtime and disconncetion
```py
endtime = datetime.datetime.now()
print("total time: {}".format(endtime - starttime))

net_connect.disconnect(
```
---
YMont
Python for Network Engineers
