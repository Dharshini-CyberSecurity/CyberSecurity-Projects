import subprocess

def nmap_sweep(subnet_prefix):
    subnet = f"{subnet_prefix}.0/24"
    print(f"\nScanning subnet {subnet} using Nmap...\n")
    try:
        result = subprocess.check_output(["nmap","-sn","-PE",subnet], universal_newlines=True)
        lines = result.splitlines()
        ip_list = []
        for i in range(len(lines)):
            if "Nmap scan report for" in lines[i]:
                ip = lines[i].split()[-1]
                if i+1 < len(lines) and ("Host is up" in lines[i+1]):
                    print(f"{ip} is UP")
                    ip_list.append(ip)
                else:
                    print(f"{ip} is DOWN")

        if not ip_list:
            print("No Hosts are UP")
    except subprocess.CalledProcessError as e:
        print("Scan failed: ", e)
    except FileNotFoundError:
        print("Nmap not found. Please Install it first")

def main():
    subnet_prefix = input("Enter subnet prefix ( e.g., 192.188.205 ): ").strip()
    if subnet_prefix.count('.') == 2:
        nmap_sweep(subnet_prefix)
    else:
        print("Invalid subnet prefix")

main()