import uuid
import socket
# MAC AND IP ADDRESS
# can be modify to input 3rd party website and get IP addresses.
hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# joins elements of getnode() after each 2 digits.
# get your mac address.
print("The MAC address in formatted way is : ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))
