import argparse
import os
import sys
import requests
import time

try:
        requests.get("http://flyzero.000webhostapp.com/project/mynmap/Ip6.php")
        os.system("python lib/version.py")
        time.sleep(1)
        os.system("python etc/nmap.py")
except KeyboardInterrupt:
        sys.exit()
