#!/usr/bin/python3
#coding: utf-8

import time
import datetime
from spreadsheet import SpreadSheet
import bme280

# シート固有のid
sheet = SpreadSheet('xxx')

# データ取得のインターバル[sec]
delay = 600

while(1):
  start = time.time()
  d_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
  sensor = bme280.readData()
  sheet.append([d_time, sensor[0], sensor[1], sensor[2]])
  lap = time.time() - start
  #print("lap_time:{0}".format(end) + "[sec]")
  neri = delay - lap
  time.sleep(neri)
