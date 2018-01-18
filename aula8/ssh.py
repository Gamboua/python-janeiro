from paramiko.client import SSHClient
import paramiko

client = SSHClient()

# CARREGA KNOWN_HOSTS
client.load_system_host_keys()
# ACEITA FINGERPRINT AUTOMATICAMENTE
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# CONEXAO COM O HOST
client.connect(
    '10.100.0.192',
    username='root',
    password='4linux'
)

stdin, stdout, stderr = client.exec_command('ls -la')

if stderr.channel.recv_exit_status() == 0:
    print(stdout.read())