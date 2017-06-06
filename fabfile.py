#coding=utf-8
from fabric.api import run, env
import sys

hs = []
for i in range(100,103):
	hs.append('root@192.168.122.%d' % (i))
env.hosts = hs
env.password = '-----'

def simple(cmd="exit"):
	run(cmd)

