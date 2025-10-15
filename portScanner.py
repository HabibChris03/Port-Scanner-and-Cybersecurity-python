import socket
import threading
from datetime import datetime

def port_scan(target_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port}: OPEN")
            try:
                service = socket.getservbyport(port)
                print(f"  Service: {service}")
            except:
                pass
        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Couldn't connect to server")


def scan_ports(target_host, start_port, end_port):

    print(f"Scanning target: {target_host}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    for port in range(start_port, end_port + 1):
        port_scan(target_host, port)


def threaded_port_scan(target_host, port_list, max_threads=100):
    """
    Multi-threaded port scanning for faster results
    """
    print(f"Threaded scan started for: {target_host}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    threads = []

    for port in port_list:
        thread = threading.Thread(target=port_scan, args=(target_host, port))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    # Wait for remaining threads to complete
    for thread in threads:
        thread.join()


def common_ports_scan(target_host):
    """
    Scan common ports
    """
    common_ports = [
        21,  # FTP
        22,  # SSH
        23,  # Telnet
        25,  # SMTP
        53,  # DNS
        80,  # HTTP
        110,  # POP3
        143,  # IMAP
        443,  # HTTPS
        993,  # IMAPS
        995,  # POP3S
        1433,  # MSSQL
        3306,  # MySQL
        3389,  # RDP
        5432,  # PostgreSQL
        5900,  # VNC
        6379,  # Redis
        27017  # MongoDB
    ]

    print(f"Scanning common ports on: {target_host}")
    print("-" * 50)

    for port in common_ports:
        port_scan(target_host, port)


def main():
    print("Python Port Scanner")
    print("=" * 50)

    # Get user input
    target_host = input("Enter target host (IP or domain): ").strip()

    print("\nScan options:")
    print("1. Scan specific port range")
    print("2. Scan common ports")
    print("3. Fast threaded scan (common ports)")

    choice = input("Choose option (1/2/3): ").strip()

    if choice == "1":
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scan_ports(target_host, start_port, end_port)

    elif choice == "2":
        common_ports_scan(target_host)

    elif choice == "3":
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995,
                        1433, 3306, 3389, 5432, 5900, 6379, 27017]
        threaded_port_scan(target_host, common_ports)

    else:
        print("Invalid choice!")
        return

    print("-" * 50)
    print("Scan completed!")


if __name__ == "__main__":
    main()