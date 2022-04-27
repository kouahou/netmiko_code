from netmiko import ConnectHandler


class SSHConnection(object):
    def __init__(self, device_type, host, port, username, password):
        self.device_type = device_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cli: ConnectHandler = self._get_connection()

    def _get_connection(self):
        return ConnectHandler(
            device_type=self.device_type,
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password)

    def show_commands(self):
        output = self.cli.send_command("show ip int brief")
        print("show ip int brief".format(output))

    def loopback_interface(self):
        config_commands = [
            'int loopback 1',
            'ip address 2.2.2.2 255.255.255.0',
            'description WHATEVER']
        output = self.cli.send_config_set(config_commands)
