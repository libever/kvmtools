#!/bin/env python
#coding=utf-8

from optparse import OptionParser
import os

options = {}

class OptList:

	def list(self,args,option):
		vm_name = options.kvm
		os.system("virsh snapshot-list " + vm_name)

	def set(self,args,option):
		vm_name = options.kvm
		if len(args) != 1:
			print "need snapshot name"
			exit(0)
		snap_name = args[0]
		os.system("virsh snapshot-create-as " + vm_name + " " + snap_name)

	def reset(self,args,option):
		vm_name = options.kvm
		if len(args) != 1:
			print "need reset snapshot name"
			exit(0)
		snap_name = args[0]
		os.system("virsh snapshot-revert " + vm_name + " " + snap_name)

	def remove(self,args,option):
		vm_name = options.kvm
		if len(args) != 1:
			print "need del snapshot name"
			exit(0)
		snap_name = args[0]
		os.system("virsh snapshot-delete " + vm_name + " " + snap_name)

def init_options():
  global options
  parser = OptionParser()
  parser.add_option("-v","--kvm",dest="kvm",metavar="<kvm name>",help="kvm instance you want to make,default is vm_1",default="vm_1")
  parser.add_option("-o","--opt",dest="opt",metavar="<operate name>",help="kvm operate name <list,set,reset,remove>",default="list")
  (options,args) = parser.parse_args()
  if options.opt in ["list","set","reset","remove"]:
    f = getattr(OptList(),options.opt)
    f(args,options)
  else:
    print "error option"


if __name__ == "__main__" :
  init_options()

