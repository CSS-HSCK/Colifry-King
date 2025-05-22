import time
import os
from datetime import datetime

# Windows hosts file location
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

# List of popular online game sites
blocked_sites = [
    "www.coolmathgames.com", "coolmathgames.com",
    "www.poki.com", "poki.com",
    "www.kizi.com", "kizi.com",
    "www.crazygames.com", "crazygames.com",
    "www.miniclip.com", "miniclip.com",
    "www.y8.com", "y8.com",
    "www.friv.com", "friv.com",
    "www.agame.com", "agame.com",
    "www.kongregate.com", "kongregate.com",
    "www.addictinggames.com", "addictinggames.com",
    "games.msn.com", "www.games.msn.com",
    "www.roblox.com", "roblox.com",
    "www.nitrome.com", "nitrome.com",
    "www.primarygames.com", "primarygames.com",
    "www.pbskids.org", "pbskids.org",
    "www.nick.com", "nick.com",
    "www.funnygames.org", "funnygames.org",
    "www.cbeebies.com", "cbeebies.com"
]

def block_sites():
    try:
        # Remove read-only attribute so we can write
        os.system(f'attrib -R "{hosts_path}"')

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in blocked_sites:
                entry = f"{redirect_ip} {site}"
                if entry not in content:
                    file.write(f"{entry}\n")

        # Make hosts file read-only to prevent tampering
        os.system(f'attrib +R "{hosts_path}"')

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Blocked {len(blocked_sites)} gaming sites.")
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: {e}")

if __name__ == "__main__":
    print("Starting persistent game blocker... Press Ctrl+C to stop.")
    while True:
        block_sites()
        time.sleep(30)  # Check every 30 seconds
