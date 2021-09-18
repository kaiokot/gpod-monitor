# Importing the library
import psutil
from psutil._common import bytes2human
import os
import json

class Monitor:   
    def __init__(self):
     pass

    def cpu_used(self):
        cpu_percent = psutil.cpu_percent(4)
        print('cpu_used:',cpu_percent)
        return cpu_percent
    
    def cpu_temperature(self):
        # print('cpu_temperature:', psutil.sensors_temperatures())    
        cpu_temp = psutil.sensors_temperatures()["coretemp"][0].current
        print('cpu_temperature:', cpu_temp)
        return cpu_temp      

    def memory_available(self):
        mem_avl = psutil.virtual_memory().available
        print('memory_available:',mem_avl)
        return mem_avl

    def memory_percent(self):
        mem_pct =  psutil.virtual_memory().percent
        print('memory_percent:',mem_pct)
   
    def memory_used(self):
        mem_usd = psutil.virtual_memory().used
        print('memory_used:', mem_usd)
        return mem_usd


    def memory_free(self):
        mem_fre =  psutil.virtual_memory().free
        print('memory_free',mem_fre)   
        return mem_fre     


    def memory_total(self):
        mem_ttl = psutil.virtual_memory().total
        print('memory_total:', mem_ttl)
        return mem_ttl

    def fan_speed(self):
        fan = psutil.sensors_fans()
        print('fan_speed:', fan)

   



        