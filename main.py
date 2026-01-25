import time
from sensors.imu import IMU
from utils.influx import InfluxLogger
from utils.serial import SerialADC

imu = IMU()
influx = InfluxLogger(db="fsae_data")
adc = SerialADC(port="/dev/ttyACM0")

SAMPLE_RATE = 0.01   # 100 Hz
next_tick = time.perf_counter()

last_adc = None;

while True:
    # IMU
    imu_data = imu.read()
    # timestamp = time.perf_counter()

    # adc_data = adc.read()
    # if adc_data:
    #     last_adc = adc_data

    # if last_adc:
    #     influx.write(
    #         "vehicle",
    #         {
    #             "ax": imu_data["ax"],
    #             "ay": imu_data["ay"],
    #             "az": imu_data["az"],
    #             "tacho": last_adc["A0"],
    #             "tps": last_adc["A1"],
    #             "water": last_adc["A2"],
    #         },
    #         timestamp=timestamp
    #     )
    influx.write("imu", imu_data)

    adc_data = adc.read()
    if adc_data:
        influx.write(
            "adc",
            {
                "tps": adc_data["A1"],
                # "tps": adc_data["A1"],
            }
        )


 # ---- Timing (stable 100 Hz) ----
    next_tick += SAMPLE_RATE
    sleep_time = next_tick - time.perf_counter()
    if sleep_time > 0:
        time.sleep(sleep_time)
