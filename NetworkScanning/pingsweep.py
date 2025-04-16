import subprocess
import platform


def is_host_up(ip):
    try:
        if platform.system().lower() == "windows":
            result = subprocess.check_output(["ping", "-n", "1", "-w", "1000", ip], universal_newlines=True)
            if "ttl=" in result.lower():
                return True
        else:
            result = subprocess.check_output(["ping", "-c", "1", "-W", "1", ip], univeral_newlines=True)
            if "ttl=" in result.lower():
                return True
    except subprocess.CalledProcessError:
        pass
    return False



def ping_sweep(subnet_prefix):
    print(f"Scanning subnet: {subnet_prefix}.0/24\n")
    for i in range(1,255):
        ip = f"{subnet_prefix}.{i}"

        if is_host_up(ip):
            print(f"{ip} is UP")
        else:
            print(f"{ip} is DOWN")

def main():
    subnet_prefix = input("Enter subnet (e.g., 192.188.1) : ")
    ping_sweep(subnet_prefix.strip())

main()