import os
import socket
from monitor import Monitor
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
from datetime import datetime


def main():

     config = {}
    try:
        with open("./settings.json") as f:
            config = json.loads(f.read())
    except Exception as e:
        sys.stderr.write("Error: {}".format(e))
        sys.exit(1)


    influx_url = config["influx_url"]
    influx_org = config["influx_org"]
    influx_token = config["influx_token"]
    influx_bucket = config["influx_bucket"]

    if "" in (influx_url, influx_org, influx_token,influx_bucket):
        print("oops, the settings.json must be configured!")
        sys.exit(1)
    
    client = InfluxDBClient(url=influx_url,token=influx_token,org=influx_org)

    try:
        mon = Monitor()

        write_api = client.write_api(write_options=SYNCHRONOUS)

        points = create_points(mon)
        
        write_api.write(bucket=influx_bucket, org=influx_org, record=points)        
       
    except Exception as e:
        print(str(e))
    finally:
        client.close()






    

def create_points(m):
    
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