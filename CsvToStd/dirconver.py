# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:40:15 2017

@author: dell
"""

import os
import pricecsv_pb2

def listdir(path):
    pathdir = os.listdir(path)
    for fname in pathdir:
        childpath = os.path.join('%s\\\%s' %(path, fname))
        print childpath
        

def read_file(infilename):
    try:
        rfd = open(infilename, 'rb')
    except IOError, e:
        print "file read err", e
        return None
    else:
        lines = rfd.readlines()
        rfd.close()
        rline = []
        for line in lines:
            if line.strip()!='':
                rline.append(line)
            else:
                continue
        return rline
        
def write_file(serialdata, filenm):
    try:
        wfd = open(filenm, 'ab')
    except IOError, e:
        print "file write err", e
    else:
        for vk in serialdata:
            wfd.write(vk)
        wfd.close()
        return 0

def serialize_data(data):
    pbfirstprice = pricecsv_pb2.price()
    for i, data[i] in enumerate(data):
        if data[i].strip() == "":
            data[i] = "0"   
    pbfirstprice.date = data[0]
    vopen = round(float(data[1]),2)*100
    pbfirstprice.open = int(vopen)
    vhigh = round(float(data[2]),2)*100
    pbfirstprice.high = int(vhigh)
    vlow = round(float(data[3]),2)*100
    pbfirstprice.low = int(vlow)
    vclose = round(float(data[4]),2)*100
    pbfirstprice.close = int(vclose)
    vvolume = int(data[5])
    pbfirstprice.volume = vvolume
    vadjclose = round(float(data[6]),2)*100
    pbfirstprice.adjclose = int(vadjclose)

    price_serial = pbfirstprice.SerializeToString()
    return price_serial    
    
def handle_inputdata(datas):
    list_serial = []
    for vdata in datas:
        vdata = vdata.split(',')
        vserial = serialize_data(vdata)
        list_serial.append(vserial)
    return list_serial
        
    
def transform(in_file, out_file):
    datelines = read_file(in_file)
    if datelines == [] or datelines == None:
        print "read blank file"
        return None
  
    serialdata = handle_inputdata(datelines)
    if serialdata == [] or serialdata == None:
        print "serial data wrong"
        return None

    ret = write_file(serialdata, out_file)
    if ret != 0:
        print "write wrong"
        return None

    print "done"
    return 0

def main(srcpath, despath):
    
    pathdir = os.listdir(srcpath)
    for fname in pathdir:
        desname = fname[0:-4]
        outpath = os.path.join('%s\\\%s' %(despath, desname))
        print outpath
        inpath = os.path.join('%s\\\%s' %(srcpath, fname))
        print inpath
        ret = transform(inpath, outpath)
        if ret != 0:
            print "sth wrong in transform process"
            return None
    print "write in success!"
    return 0
        
    
if __name__ == "__main__":
    
    srcmenu = "C:\workmenu\protobuf\src"
    desmenu = "C:\workmenu\protobuf\des"
    main(srcmenu, desmenu)




    