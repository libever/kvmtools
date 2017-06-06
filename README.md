fabric批量运行
fab simple:cmd='yum install openssl-devel -y'

fab simple:cmd='yum install python-devel -y'
fab simple:cmd='yum install openssl-devel -y'
fab simple:cmd='yum install docker -y '
fab -P simple:cmd=' systemctl enable docker'
fab -P simple:cmd=' systemctl start docker'
fab -P simple:cmd='useradd -p "sina123" xingyue '
fab -P simple:cmd=" echo 'xingyue:sina123' | chpasswd " 
fab simple:cmd='echo "xingyue ALL\=(ALL)   NOPASSWD: ALL" >> /etc/sudoers '
fab simple:cmd='su xingyue -c "mkdir ~/.ssh/"'
fab simple:cmd='su xingyue -c "touch ~/.ssh/authorized_keys"'
fab simple:cmd='echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDev0iSgDlZUpmOzlar4igf7x5OAoTwA2ULJ0AnuHIzHoIZxc1BP5x194ToXQ2QJ1QRK4O+5D9fH0wzyGYmQRTDzZmTk2wPpFKVTmYqMpw7h5z2181MqEZ19zYnTXGz4wJdnPdBTfgIBvOZPzc6CtfE6o9IMVg/iiUt88ihuOKb+InhVBuiBG3wajRWBT42sBzbr/h7N6Xu03II2maiRe9+PonleePN67BLyDevn286so0lgK/HTBDh4G1XwM2bZtCZQ8EWlaN5z4DzBYpgWtZ8VG5aLxuACmB2d6HnDWe9lYN6yDfD4cEo5bghXTzj9uOqF5UEFxqG2ZLx9IaIYkTd xingyue@simplemac.local" >> /home/xingyue/.ssh/authorized_keys'
fab simple:cmd='su xingyue -c "chmod 0600  ~/.ssh/authorized_keys"'
fab simple:cmd='sed -i "s/#PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config '
fab simple:cmd='systemctl restart sshd'
fab yum:p=git
