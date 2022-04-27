from SSHConnection import SSHConnection


if __name__ == '__main__':
    connection = SSHConnection('cisco_ios', '192.168.10.20', 22, 'S1', 'cisco')

    # show commands and display the output
    connection.show_commands()


