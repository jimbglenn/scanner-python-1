import paramiko


def run_commands(server_config):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_config["ip"], username=server_config["user"], password=server_config["password"])
    for com in server_config["commands"]:
        _stdin, _stdout, _stderr = client.exec_command(com)
        print(_stdout.read().decode())
    client.close()


def parse_config(file_lines):
    result = dict()
    if len(file_lines) > 3:
        counter = 0
        server_number = 0
        for testLine in file_lines:
            line = testLine.strip()
            if line:
                if counter == 0:
                    result[server_number] = dict()
                    result[server_number]["ip"] = line
                    counter = counter + 1
                elif counter == 1:
                    result[server_number]["user"] = line
                    counter = counter + 1
                elif counter == 2:
                    result[server_number]["password"] = line
                    result[server_number]["commands"] = []
                    counter = counter + 1
                else:
                    result[server_number]["commands"].append(line)
                    counter = counter + 1
            else:
                if server_number in result:
                    server_number = server_number + 1
                counter = 0
    return result


def read_config_file():
    with open("config.txt", "r") as file1:
        lines = file1.readlines()
        result = parse_config(lines)
        for server in result:
            print("Running commands on", result[server]["ip"])
            run_commands(result[server])
        file1.close()


def scanner():
    read_config_file()


if __name__ == '__main__':
    read_config_file()
