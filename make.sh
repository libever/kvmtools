#!/bin/bash


### after this you need start virt-viewer install this image

name=vm_2
ram=2048
disk=./vdisk/vdisk_3.qcow2
disk_size=20G
vcpus=2
cdrom=iso/CentOS-7-x86_64-Minimal-1611.iso


qemu-img create -f qcow2 $disk $disk_size

virt-install \
 --name $name \
 --ram $ram \
 --disk path=$disk,size=8 \
 --vcpus $vcpus \
 --os-type linux \
 --network bridge=virbr0 \
 --graphics spice \
 --console pty,target_type=serial \
 --cdrom $cdrom 

