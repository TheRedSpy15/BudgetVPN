import urllib.request
import json
import string
import subprocess
import time
import argparse
import os

def main():
    afile = open("proxies.json", "a")
    rfile = open("proxies.json", "r", encoding='utf-8')
    provider = "https://api.getproxylist.com/proxy"
    updateSize = 3

    daily(afile, rfile, provider, updateSize)


def createList(provider, size, afile):
    print("Creating/Adding to list")

    i = 1
    for i in range(size):
        proxyData = str((fetchProxy(provider))).replace(r"\n","").replace("b'","").replace("}'","")
        afile.write(proxyData + "\n")
    afile.close()


def fetchProxy(provider):
    print("Getting proxy")
    return urllib.request.urlopen(provider).read()


def readProxy(rfile):
    print("Reading proxy")
    return json.loads(rfile.readline())


def setProxy(proxyData):
    print("Setting proxy")
    print("IP:", proxyData["ip"])
    print("Port:", proxyData["port"])
    print("Protocol:", proxyData["protocol"])

    os.environ[str(proxyData["protocol"]).upper() + "_PROXY"] = str(proxyData["ip"]) + ":" + str(proxyData["port"])


def daily(afile, rfile, provider, updateSize):
    #createList(provider, updateSize, afile)
    setProxy(readProxy(rfile))
    # set random proxy chain from json file

    print("Starting daily loop")
    while True:
        print("Next update in 24 hours")
        time.sleep(86400)
        createList(provider, updateSize, afile)
        # set random proxy chain from json file
        # remove week old proxies from json file


if __name__ == '__main__':
    main()