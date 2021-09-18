import os
import socket
from monitor import Monitor
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
from datetime import datetime

influx_url = os.getenv("influx_url")
influx_org = os.getenv("influx_org")
influx_token = os.getenv("influx_token")
influx_bucket = os.getenv("influx_bucket")


def main():
    
    client = InfluxDBClient(url=influx_url,token=influx_token,org=influx_org)

    try:
        mon = Monitor()

        write_api = client.write_api(write_options=SYNCHRONOUS)

        points = make_points(mon)
        
        write_api.write(bucket=influx_bucket, org=influx_org, record=points)        
       
    except Exception as e:
        print(str(e))
    finally:
        client.close()






    

def make_points(m):
    
    iso_time = datetime.utcnow()

    points = []   

    points.append(Point("cpu_temperature").tag("device", socket.gethostname()).field("value", m.cpu_temperature()).time(time=iso_time))

    points.append(Point("cpu_used").tag("device", socket.gethostname()).field("value", m.cpu_used()).time(time=iso_time))

    points.append(Point("memory_total").tag("device", socket.gethostname()).field("value", m.memory_total()).time(time=iso_time))

    points.append(Point("memory_used").tag("device", socket.gethostname()).field("value", m.memory_used()).time(time=iso_time))


    return points



if __name__ == "__main__":
    print("Starting machine monitor...")
    main()
    print("machine monitor... ok!")