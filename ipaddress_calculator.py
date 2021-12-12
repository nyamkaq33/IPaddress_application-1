import ipaddress

def verify_ip_address(address):

    try:

        net = ipaddress.ip_network(address, strict=False)

        # ip = ipaddress.ip_address(address)

        return net

    except ValueError:

        return False



while True:

    print("Welcome to IPv4 calculator")

    ipadd = input("Enter your IP address (format: 192.168.1.1/24) /Type q to exit/: ")



    if ipadd == "quit" or ipadd == "q":

        break

    

    if verify_ip_address(ipadd) == False:

        print("Wrong IP address")

    else:

        net = verify_ip_address(ipadd)

        ip = ipaddress.IPv4Interface(ipadd)


        print("IP Address: % s"% str(ip.ip))

        print("Network Address: % s"% str(net.network_address))

        print("Usable Host IP Range: % s"% str(net.network_address + 1) + "~" + str(net.broadcast_address - 1))

        print("Broadcast Address: % s"% str(net.broadcast_address))

        print("Total Number of Hosts: % s"% str(net.num_addresses))

        print("Number of Usable Hosts: % s"% str(net.num_addresses - 2))

        print("Subnet Mask: % s"% str(net.netmask))

        print("Wildcard Mask: % s"% str(ipaddress.IPv4Address(int(net.netmask)^(2**32-1)))) 

        print("Binary Subnet Mask: % s"% bin(int(net.netmask))[:0] + bin(int(net.netmask))[2:])

        print("IP Class: % s"% str(net.with_netmask))

        print("CIDR Notation: % s"% str(net.prefixlen))

        print("Binary ID: % s"% bin(int(ip.ip))[:0] + bin(int(ip.ip))[2:]))

        break