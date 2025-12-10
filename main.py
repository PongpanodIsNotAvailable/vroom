import time
from sensors.imu import IMU
from logging.influx import InfluxLogger

imu = IMU()
influx = InfluxLogger(db="fsae_data")

SAMPLE_RATE = 0.01   # 100 Hz

while True:
    imu_data = imu.read()

    influx.write("imu", imu_data)

    time.sleep(SAMPLE_RATE)
