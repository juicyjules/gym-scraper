from unittest import IsolatedAsyncioTestCase
from scraper import Scraper
import re
import json
import datetime
import time

URL = "https://www.unifit.uni-kl.de/"
TARGET = "/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/p"
BUFFERSIZE = 1 << 10
INTERVAL = 60
DATAFILE = "./scrape.json"

def write_data(file,data):
    try:
        with open(file,"r") as f:
            old_data = json.load(f)
    except (ValueError, FileNotFoundError) as e :
            old_data = {}
    with open(file,"w") as f:
        f.write(json.dumps(data | old_data))
    return True
def main():
    s = Scraper(URL)
    buffer = {}
    while 1:
        t = s.isolate(TARGET)[0].text
        value = re.findall("([0-9\.]*) *%", t) 
        buffer[time.time()] = value[0]
        print(f"value {value}")
        if len(buffer) >= BUFFERSIZE:
            if write_data(DATAFILE, buffer):
                buffer = {}
            else:
                raise IOError("Writing buffer failed")

        time.sleep(INTERVAL)

        
if __name__ == "__main__":
    main()