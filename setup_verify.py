#!/usr/bin/env python3
# coding: utf-8

"""
rftoolクライアント サンプルプログラム: 疎通確認プログラム
"""


from RftoolClient import client, rfterr
import sys
import time
import socket
import logging

# Parameters
ZCU111_IP_ADDR = "192.168.1.3"

# Log level
LOG_LEVEL = logging.WARN


def main():
    status = 0
    rft = client.RftoolClient(logger=logger)

    try:
        rft.connect(ZCU111_IP_ADDR)
        rft.command.Version()
        rft.close()
    except Exception as e:
        status = 1
        print("exception:", e)

    return status


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(LOG_LEVEL)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(handler)

    status = main()

    if status == 0:
        print("Connection test succeeded")
    else:
        print("Connection test failed")

    sys.exit(status)
