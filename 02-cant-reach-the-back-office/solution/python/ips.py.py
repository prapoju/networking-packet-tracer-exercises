from ipaddress import *

ivy: IPv4Address = IPv4Address("10.20.30.20")
ivy_mask: IPv4Address = IPv4Address("255.255.255.0")

theo: IPv4Address = IPv4Address("10.20.30.70")
theo_mask: IPv4Address = IPv4Address("255.255.255.192")

print(f"{ivy:#b}", ": Ivy's IP")
print(f"{ivy_mask:#b}", ": Ivy's mask")
print(f"{IPv4Address(int(ivy) & int(ivy_mask)):#b}", ": Ivy's network")
print(f"{theo:#b}", ": Theo's IP")

print("------")

print(f"{theo:#b}", ": Theo's IP")
print(f"{theo_mask:#b}", ": Theo's mask")
print(f"{IPv4Address(int(theo) & int(theo_mask)):#b}", ": Theo's network")
print(f"{ivy:#b}", ": Ivy's IP")

print("----")


def get_network(ip: IPv4Address, mask: IPv4Address) -> IPv4Network:
    ip_object: IPv4Address = IPv4Address(int(ip) & int(mask))
    network: IPv4Network = IPv4Network((ip_object, str(mask)))
    return network


n_ivy: IPv4Network = get_network(ivy, ivy_mask)
n_theo: IPv4Network = get_network(theo, theo_mask)

n_theo_hosts: list[IPv4Address]=list(n_theo.hosts())


ivy_new:IPv4Address=n_theo_hosts[0]
n_theo_hosts.remove(ivy_new)
n_theo_hosts.remove(theo)

print(f"Ivy's new IP: {ivy_new}")
print(f"Ivy's new mask: {theo_mask}")
print(f"Number of available host IPs: {len(n_theo_hosts)}")
print(f"Available IPs: {n_theo_hosts}")

