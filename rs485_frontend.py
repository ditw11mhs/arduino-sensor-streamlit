import serial.tools.list_ports
import streamlit as st
from rs485_backend import SerialHandler


class Main:
    def main(self):
        st.title("Project RS485")
        self.debug = st.checkbox("Debug")
        if "Start Connection" not in st.session_state:
            st.session_state["Start Connection"] = False
        self.initialization()
        self.start_connection()

    def start_connection(self):
        c1, c2, c3 = st.columns(3)
        if c1.button("Connect to Slave 1"):
            stop_connection = st.button("Stop Connection")
            st.header("Slave 1")
            master = SerialHandler(
                port=self.port, baudrate=self.baudrate, timeout=self.timeout
            )
            if self.debug:
                st.write("Slave 1 Open", master.ser.is_open)

            placeholder = st.empty()
            while True:
                master.slave_1_handler(placeholder)
                if stop_connection:
                    break

        if c2.button("Connect to Slave 2"):
            stop_connection = st.button("Stop Connection")
            master = SerialHandler(
                port=self.port, baudrate=self.baudrate, timeout=self.timeout
            )
            if self.debug:
                st.write("Slave 2 Open", master.ser.is_open)

            c1, c2 = st.columns(2)
            placeholders = [c1.empty(), c2.empty()]
            while True:
                master.slave_2_handler(placeholders)
                if stop_connection:
                    break

        if c3.button("Connect to Slave 3"):
            stop_connection = st.button("Stop Connection")
            master = SerialHandler(
                port=self.port, baudrate=self.baudrate, timeout=self.timeout
            )
            if self.debug:
                st.write("Slave 3 Open", master.ser.is_open)

            c1, c2, c3 = st.columns(3)
            placeholders = [c1.empty(), c2.empty(), c3.empty()]
            while True:
                master.slave_3_handler(placeholders)
                if stop_connection:
                    break

    def initialization(self):

        ports = serial.tools.list_ports.comports()
        port_list = []
        for port, _, _ in sorted(ports):
            port_list.append(port)
        c1, c2, c3 = st.columns(3)
        self.port = c1.selectbox("Select Port", port_list)
        self.baudrate = c2.selectbox(
            "Select Baudrate", [9600, 19200, 38400, 57600, 115200], index=4
        )
        self.timeout = c3.selectbox(
            "Select Timeout", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        )


# master = SerialHandler(port="COM6", baudrate=115200, timeout=0.1)
# while True:
#     string = master.call_and_get_data("S1")
#     print(string)
#     # master.get_slave_send("S1")

if __name__ == "__main__":
    main = Main()
    main.main()
