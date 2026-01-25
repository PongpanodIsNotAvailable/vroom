from influxdb import InfluxDBClient
import time

class InfluxLogger:
    def __init__(self, host="localhost", port=8087, db="fsae_data"):
        self.client = InfluxDBClient(host=host, port=port)
        self.client.switch_database(db)

    def write(self, measurement, fields: dict, timestamp=None):
        if timestamp is None:
            timestamp = time.time()

        data = [{
            "measurement": measurement,
            "time": int(timestamp * 2e9),  # 🔑 nanoseconds
            "fields": fields
        }]
        self.client.write_points(data, time_precision="n")

