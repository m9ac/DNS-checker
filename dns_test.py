import dns.resolver
import argparse

def test_dns_servers(servers, num_requests=10):
    results = {}
    for server in servers:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [server]
        response_times = []
        for _ in range(num_requests):
            try:
                query = resolver.resolve("example.com")
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
    parser = argparse.ArgumentParser(description="Test DNS servers")
    parser.add_argument("--servers", nargs="+", help="List of DNS servers to test")
    parser.add_argument("--use-predefined", action="store_true", help="Use predefined list of DNS servers")
    args = parser.parse_args()

    if args.use_predefined:
        # Predefined list of DNS servers
        dns_servers = [
            "8.8.8.8",  # Google DNS
            "1.1.1.1",  # Cloudflare DNS
            "208.67.222.222",  # OpenDNS
            "9.9.9.9",  # Quad9 DNS
            "64.6.64.6"  # Verisign DNS
        ]
    elif args.servers:
        dns_servers = args.servers
    else:
        dns_servers = input("Enter DNS servers separated by space: ").split()

    results = test_dns_servers(dns_servers)

    print("Results:")
    for server, response_time in results.items():
        print(f"Server: {server} | Avg. Response Time: {response_time:.2f} ms")

if __name__ == "__main__":
    main()
