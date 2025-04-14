import subprocess

def enumerate_subdomains(target_domain):
    """Run Subfinder to enumerate subdomains."""
    result = subprocess.run(["subfinder", "-d", target_domain], capture_output=True, text=True)
    return result.stdout.splitlines()

def filter_live_subdomains(subdomains):
    """Check for live subdomains using 'ping'."""
    live_subdomains = []
    for subdomain in subdomains:
        response = subprocess.run(["ping", "-c", "1", subdomain], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if response.returncode == 0:
            live_subdomains.append(subdomain)
    return live_subdomains

def run_nmap_scan(live_subdomains):
    """Run Nmap scan on live subdomains."""
    for subdomain in live_subdomains:
        print(f"\nScanning {subdomain} with Nmap...\n")
        result = subprocess.run(["nmap", "-Pn", "-sV", subdomain], capture_output=True, text=True)
        print(result.stdout)

if __name__ == "__main__":
    target = input("Enter target domain: ")
    subdomains = enumerate_subdomains(target)

    if not subdomains:
        print("No subdomains found.")
    else:
        live_subdomains = filter_live_subdomains(subdomains)
        if live_subdomains:
            print(f"\nLive Subdomains ({len(live_subdomains)} found):")
            for sub in live_subdomains:
                print(sub)

            # Run Nmap scan
            run_nmap_scan(live_subdomains)
        else:
            print("\nNo live subdomains found.")
