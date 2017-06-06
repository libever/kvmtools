# 192.168.182.100 ~ 192.168.182.104


ADD_PORT="python port.py -o add "

iptables -F 

for((i=0;i<5;i++))
do

  #virsh shutdown vmcloud_${i}
  virsh start vmcloud_${i}

done

$ADD_PORT 10022 192.168.182.100:22
$ADD_PORT 10080 192.168.182.100:8000
$ADD_PORT 11022 192.168.182.101:22
$ADD_PORT 12022 192.168.182.102:22
$ADD_PORT 13022 192.168.182.103:22
$ADD_PORT 14022 192.168.182.104:22
