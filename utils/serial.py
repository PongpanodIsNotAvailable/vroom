import serial
import os
import time


class SerialADC:
    def __init__(
        self,
        port="/dev/ttyACM0",
        baudrate=9600,
        timeout=0.1,
        expected_fields=6
    ):
        """
        expected_fields:
            time_ms + A0..A3 = 5 fields
            Example: 1234,512,623,401,890
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.expected_fields = expected_fields
        self.ser = None

        self._connect()

    def _connect(self):
        if os.path.exists(self.port):
            try:
                self.ser = serial.Serial(
                    port=self.port,
                    baudrate=self.baudrate,
                    timeout=self.timeout
                )
                print(f"[SerialADC] Connected to {self.port}")
            except serial.SerialException as e:
                print(f"[SerialADC] Failed to open serial: {e}")
                self.ser = None
        else:
            print(f"[SerialADC] Port {self.port} not found")

    def read(self):
        """
        Returns:
            dict or None

        Example output:
        {
            "time_ms": 1234,
            "A0": 512,
            "A1": 623,
            "A2": 401,
            "A3": 890
        }
        """
        if not self.ser or not self.ser.is_open:
            return None

        line = self.ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            return None

        parts = line.split(",")

        if len(parts) != self.expected_fields:
            return None

        try:
            values = list(map(int, parts))
        except ValueError:
            return None

        return {
            "time_ms": values[0],
            "A0": values[1],
            "A1": values[2],
            "A2": values[3],
            "A3": values[4],
        }

    def close(self):
        if self.ser:
            self.ser.close()
