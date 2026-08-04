import paramiko


HOST = "192.168.150.133"
USERNAME = "maram"
PASSWORD = "maram"

def get_ssh_connection():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=HOST,
        username=USERNAME,
        password=PASSWORD
    )

    return ssh

def execute_command(command: str):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=HOST,
        username=USERNAME,
        password=PASSWORD
    )

    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    output = stdout.read().decode()
    error = stderr.read().decode()

    ssh.close()

    return {
        "stdout": output,
        "stderr": error,
        "returncode": exit_status

    }

def upload_file(local_path, remote_path):

    ssh = get_ssh_connection()

    sftp = ssh.open_sftp()

    sftp.put(
        local_path,
        remote_path
    )

    sftp.close()
    ssh.close()


    return {
        "message": "File uploaded successfully",
        "remote_path": remote_path
    }    