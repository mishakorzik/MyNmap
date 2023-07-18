import argparse
import os
import sys
import requests
import time

try:
        os.system("python etc/version.py")
        time.sleep(2)
        os.system("python etc/nmap.py")
except KeyboardInterrupt:
        sys.exit()
