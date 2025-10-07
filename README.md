# 🌐 ARP Concepts — Educational Simulation

**⚠️ WARNING — FOR EDUCATIONAL USE ONLY**  
This repository contains a **safe, non-executable simulation** that models ARP behavior (requests, replies, and ARP table entries) for teaching and demonstration purposes. 

---

## 🧩 Features
- Manipulate ARP tables so that traffic between a target and the gateway is redirected
- Resolves a host’s MAC address for a given IP
- Forges and sends ARP reply frames claiming an IP is at a different MAC

---

## ⚙️ Requirements
- **Operating System:** Any (Linux / macOS / Windows)  
- **Python:** 3.8+ (3.10+ recommended)
- **Python package:** `scapy`  

---

## 🚀 Quick start

1. **Clone this repository**
   ```bash
   git clone https://github.com/alagskomahd/arp-spoof.git
   cd arp-spoof

2. **Edit the code on line 34 and 35 to add the target and gateway ip address**
   ```pgsql
   target_ip_ip = "192.168.43.88"
   gateway_ip = "192.168.43.1" 
   
3. **No root privileges**
   ```bash
   python3 arp_spoof.py

--- 

**Responsible Use and Ethics**

Any demonstration of active ARP manipulation must be performed only in an isolated lab environment where all devices and networks are owned by or explicitly permitted for testing.

Unauthorized testing of third-party networks is illegal and unethical.

If you discover a security issue in these materials, contact the repository owner privately—do not post exploit details.

---

🧾 Files in this repo

arp-spoof.py — main script

README.md — this file

---

👤 Author

Dennis Alagskomah
📫 Email: alagskomah25@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/alagskomah/
