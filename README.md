# Footprinting & Reconnaisance Automation Script

A Python script that automates subdomain enumeration, live subdomain filtering, and Nmap scanning for deeper reconnaissance.


## Features:
- **Subdomain Enumeration** using Subfinder.  
- **Live Subdomain Filtering** (checks which subdomains are active)  
- **Nmap Fingerprinting** (detects open ports and services)  
- Optimized for **fast** and **efficient** recon.  

## Requirements:
- Python 3
- Subfinder (`go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`)
- Nmap (`sudo apt install nmap -y`)
- (Optional) httpx for faster live subdomain verification (`go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest`)

## Usage:
```bash
python3 fingerprint.py
