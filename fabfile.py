#coding=utf-8
from fabric.api import run, env
import sys

hs = []
for i in range(100,103):
	hs.append('xingyue@192.168.122.%d' % (i))
env.hosts = hs
env.password = 'sina123'

def simple(cmd="exit"):
	run(cmd)

def yum(p):
	run('sudo yum install -y %s ' % (p))
