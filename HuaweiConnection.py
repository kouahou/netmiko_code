from netmiko import ConnectHandler, Netmiko


class HuaweiConnection:
    def __init__(self, host, password):
        self.host = host
        self.username = 'root'
        self.password = password
        self.device_type = 'huawei'
        self.port = '22'
        self._con = None

    def get_connection(self):
        if not self._con:
            device = {
                'device_type': self.device_type,
                'port': self.port,
                'host': self.host,
                'username': self.username,
                'password': self.password,
                'global_delay_factor': 0.1
            }

            self._con = Netmiko(**device)

        return self._con

    def config_command(self):
        configs = ['display memory', 'display arp']
        return self.get_connection().send_config_set(configs, delay_factor=0.2)


if __name__ == '__main__':
    huawei_4b7c = HuaweiConnection('192.168.8.1', '1GTE96GEGAQ')
    output = huawei_4b7c.config_command()
    huawei_4b7c.get_connection().disconnect()
    print(output)
