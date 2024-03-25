import dns.resolver

def test_dns_servers(servers, num_requests=10):
    results = {}
    for server in servers:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [server]
        response_times = []
        for _ in range(num_requests):
            try:
                query = resolver.query("example.com")
                response_times.append(query.response.time)
            except dns.resolver.NoNameservers:
                print(f"Error: No nameservers found for {server}")
                break
            except dns.resolver.NXDOMAIN:
                print(f"Error: NXDOMAIN for {server}")
                break
            except dns.exception.Timeout:
                print(f"Error: Timeout for {server}")
                break
        if response_times:
            avg_response_time = sum(response_times) / len(response_times)
            results[server] = avg_response_time
    return results

def main():
    predefined_dns_servers = [
        "8.8.8.8",  # Google DNS
        "1.1.1.1",  # Cloudflare DNS
        "208.67.222.222",  # OpenDNS
        "9.9.9.9",  # Quad9 DNS
        "64.6.64.6"  # Verisign DNS
    ]
    print("""Would you like to test these DNS servers (1):
    8.8.8.8          Google
    1.1.1.1          Cloudflare
    208.67.222.222   OpenDNS
    9.9.9.9          Quad9
    64.6.64.6        Verisign DNS
or
enter a list of your own DNS servers to test (2)?
Enter 'q' to quit.""")
    choice = input("Enter your choice: ")

    if choice == "1":
        dns_servers = predefined_dns_servers
    elif choice == "2":
        dns_servers = []
        print("Enter DNS servers (type 'go' to finish and test):")
        while len(dns_servers) < 5:
            server = input(f"Enter DNS server {len(dns_servers) + 1}: ")
            if server.lower() == "go":
                break
            elif server.lower() == "q":
                print("Exiting...")
                return
            dns_servers.append(server)
    elif choice.lower() == "q":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Exiting.")
        return

    results = test_dns_servers(dns_servers)

    print("Results:")
    for server, response_time in results.items():
        print(f"Server: {server:<15} | Avg. Response Time: {response_time:.2f} ms")
#        print(f"Server: {server}     |     Avg. Response Time: {response_time:.2f} ms")

if __name__ == "__main__":
    main()

