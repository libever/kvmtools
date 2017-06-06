#!/bin/env python
#coding=utf-8

from optparse import OptionParser
import os

options = {}
functionList = ["list","add","remove"]

def init_options():
  global options
  global functionList
  parser = OptionParser()
  parser.add_option("-o","--opt",dest="opt",help="optiont to port , <list,add,remove>",metavar="option to this file",default="list")
  (options,args) = parser.parse_args()
  if options.opt in functionList:
    f = getattr(OptList(),options.opt)
    f(args)
  else:
    print "error option"

class OptList():

    def list(self,args):
        cmd = "cat user.pwd"
        print self._run_shell(cmd)

    def add(self,args):
        passwd = self._run_shell("openssl passwd -crypt %s" % (args[1]))
        cmd = "printf \"%s:%s\" >> %s " % (args[0],passwd,"user.pwd")
        print self._run_shell(cmd)

    def remove(self,args):
        cmd = "sed -i '/%s/d' %s " % (args[0],"user.pwd")
        print self._run_shell(cmd)

    def _run_shell(self,cmd):
        return os.popen(cmd).read()


if __name__ == "__main__" :
    init_options()
