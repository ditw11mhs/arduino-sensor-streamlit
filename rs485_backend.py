import time
import serial
import streamlit as st


class SerialHandler:
    def __init__(self, port, baudrate=115200, timeout=0.1):
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def readline(self):
        """Read line from serial

        Returns:
            line: line of byte
        """
        time.sleep(0.01)
        line = self.ser.readline()

        return line

    def write(self, output: bytes):
        """Write a line to serial

        Args:
            output (bytes): bytes to write
        """
        self.ser.rts = False
        time.sleep(0.001)
        self.ser.write(output)
        time.sleep(0.001)
        self.ser.rts = True

    def to_byte(self, input: str):
        """Convert string to byte

        Args:
            input (str): Input String

        Returns:
            bytes : byte of input string
        """
        return bytes(input, encoding="utf-8")

    def to_string(self, input: bytes):
        """Convert byte to string

        Args:
            input (bytes): Input Byte

        Returns:
            string: string of input byte
        """
        return input.decode("utf-8")

    def get_naming(self, slave_name):
        """Convert Slave Name to GET Protocol

        Args:
            slave_name (str): Slave Name

        Returns:
            str: Slave Name in GET Protocol
        """
        return "G" + slave_name

    def post_naming(self, slave_name):
        """Convert Slave Name to POST Protocol

        Args:
            slave_name (str): Slave Name

        Returns:
            str: Slave Name in POST Protocol
        """
        return "P" + slave_name

    def get_slave_send(self, slave_name: str):
        """Send GET protocol to rs485

        Args:
            slave_name (str): Name of slave
        """
        self.write(self.to_byte(self.get_naming(slave_name)))

    def r_n_strip(self, data_input: str):
        """Strip spacing

        Args:
            data_input (str): Data Input

        Returns:
            str: Clean Data
        """
        data_input = data_input.strip("\r")
        data_input = data_input.strip("\n")
        return data_input

    def post_slave_check(self, slave_name: str):
        """Check if slave send POST protocol

        Args:
            slave_name (str): Name of Slave

        Returns:
            bool: True or False
        """
        line = self.readline()
        try:
            line_str = self.to_string(line)
        except:
            return None
        if line_str.startswith(self.post_naming(slave_name)):
            return self.r_n_strip(line_str)

    def call_and_get_data(self, slave_name: str):
        """Send GET Protocol and check if slave send POST protocol

        Args:
            slave_name (str): Name of slave

        Returns:
            string: [description]
        """
        self.get_slave_send(slave_name)
        string = self.post_slave_check(slave_name)
        if string != None:
            return string

    def split_data(self, slave_name: str, raw_data: str):
        """Split data

        Args:
            slave_name (str): Slave Name
            raw_data (str): Data from GET and POST

        Returns:
            float: Data in float or list of float
        """
        num = int(slave_name[1])
        data_only = self.r_n_strip(raw_data)[4:]
        if num == 1:
            return float(data_only)
        else:
            data_split = data_only.split("|")
            return [float(i) for i in data_split]

    def slave_1_handler(self, placeholder):
        """Slave 1 Handler

        Returns:
            string: [description]
        """
        raw_slave_data = self.call_and_get_data("S1")
        if raw_slave_data != None:
            slave_data = self.split_data("S1", raw_slave_data)
            placeholder.metric("Slave 1", slave_data)

    def slave_2_handler(self, placeholders):
        raw_slave_data = self.call_and_get_data("S2")
        if raw_slave_data != None:
            slave_data = self.split_data("S2", raw_slave_data)
            sensor_name = ["Sensor 1", "Sensor 2"]
            for i, placeholder in enumerate(placeholders):
                placeholder.metric(sensor_name[i], slave_data[i])

    def slave_3_handler(self, placeholders):
        raw_slave_data = self.call_and_get_data("S3")
        if raw_slave_data != None:
            slave_data = self.split_data("S3", raw_slave_data)
            sensor_name = ["Sensor 1", "Sensor 2","Sensor 3"]
            for i, placeholder in enumerate(placeholders):
                placeholder.metric(sensor_name[i], slave_data[i])
