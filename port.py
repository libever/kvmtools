#!/bin/env python
#coding=utf-8

from optparse import OptionParser
import os

options = {}

def getIfIp(ifname="em1"):
    import socket, fcntl, struct 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15])) 
    ret = socket.inet_ntoa(inet[20:24]) 
    return ret

def init_options():
  global options
  parser = OptionParser()
  parser.add_option("-o","--opt",dest="opt",help="optiont to port , <list,add,remove>",metavar="option to this file",default="list")
  parser.add_option("-i","--addr",dest="kvmip",help="kvm server ip",metavar="kvm server ip!",default=getIfIp())
  (options,args) = parser.parse_args()
  if options.opt in ["list","add","remove"]:
    f = getattr(OptList(),options.opt)
    f(args)
  else:
    print "error option"

class OptList:
  def list(self,params = []):
    print ""
    print self.run_system("iptables -t nat -S | grep DNAT | awk -F \"--dport\" '{print $2}'")
  
  def add(self,params = []):
    global options
    if(self.have(params)):
      print "ALREADY HAVE !"
      return self.list()
    cmd = "iptables -t nat -A PREROUTING -d %s/32 -p tcp -m tcp --dport %s -j DNAT --to-destination %s" % (options.kvmip,params[0],params[1])
    self.run_system(cmd)
    print "OK Now is : "
    self.list()
  
  def remove(self,params = []):
    global options
    cmd = "iptables -t nat -D PREROUTING -d %s/32 -p tcp -m tcp --dport %s -j DNAT --to-destination %s" % (options.kvmip,params[0],params[1])
    self.run_system(cmd)
    print "OK Now is : "
    self.list()

  def have(self,params):
    global options
    cmd = "iptables -t nat -nL | grep '%s to:%s' | wc -l" % (params[0],params[1])
    r = self.run_system(cmd).strip()
    return "1" == r

  def run_system(self,cmd):
    return os.popen(cmd).read()
    
if __name__ == "__main__" :
  init_options()

