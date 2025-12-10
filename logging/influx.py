from influxdb import InfluxDBClient

class InfluxLogger:
    def __init__(self, host="localhost", port=8086, db="fsae_data"):
        self.client = InfluxDBClient(host=host, port=port)
        self.client.switch_database(db)

    def write(self, measurement, fields: dict):
        data = [{
            "measurement": measurement,
            "fields": fields
        }]
        self.client.write_points(data)
