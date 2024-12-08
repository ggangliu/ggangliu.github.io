# Home Server Configuration

## Wireguard

``` sh
sudo apt install wireguard
sudo wg-quick up wg0
sudo netstat -tuln
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0.service
sudo systemctl status wg-quick@wg0.service
sudo vim /etc/sysctl.conf # net.ipv4.ip_forward=1
sudo sysctl -p
```

/etc/wireguard/wg0.conf

``` ini
[Interface]
PrivateKey = GIZEVov6oTpWsaHUKyN4jvORvNZdw5kHZoBikpBUR0o=
Address = 192.0.2.1/32
ListenPort = 51820

PreUp = echo WireGuard PreUp
PostUp = iptables -I FORWARD -i wg0 -j ACCEPT; iptables -I FORWARD -o wg0 -j ACCEPT; iptables -I INPUT -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PreDown = echo WireGuard PreDown
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -D FORWARD -o wg0 -j ACCEPT; iptables -D INPUT -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# remote pc
PublicKey = 63EmJHn3Ki6JKhQ1lrbr235soT4qfECahuBb1zJZixc=
AllowedIPs = 192.0.2.2/32
```

``` ini
[Interface]
PrivateKey = GIZEVov6oTpWsaHUKyN4jvORvNZdw5kHZoBikpBUR0o=
Address = 192.0.3.1/32
ListenPort = 51820

PreUp = echo WireGuard PreUp
PostUp = iptables -t nat -A POSTROUTING -s 192.0.3.0/24 -j SNAT --to-source 192.168.31.188
PreDown = echo WireGuard PreDown
PostDown = iptables -t nat -D POSTROUTING -s 192.0.3.0/24 -j SNAT --to-source 192.168.31.188

[Peer]
# remote pc
PublicKey = 63EmJHn3Ki6JKhQ1lrbr235soT4qfECahuBb1zJZixc=
AllowedIPs = 192.0.3.2/24

#[Peer]
# remote pc
#PublicKey = PbpAvIVLJ5rl3KD1LXqVjKoH7YnxgxMul3lvLxuDZjE=
#AllowedIPs = 192.0.3.3/32
```

## SSH Server

``` sh
sudo apt install openssh-server
sudo systemctl status ssh
sudo systemctl enable ssh
systemctl cat ssh # 确保 After=network.target 行存在，这意味着 SSH 服务将在网络服务启动之后启动
sudo systemctl daemon-reload
ssh-keygen.exe -f ggangliu188
ssh-copy-id ggangliu@192.168.31.188
ssh-copy-id -i ggangliu188.pub ggangliu@192.168.31.188
sudo reboot
```

/etc/ssh/sshd_config

## Samba Server

``` sh
sudo apt install samba
sudo vim /etc/samba/smb.conf
sudo systemctl restart smbd
sudo systemctl enable smbd
```

/etc/samba/smb.conf

``` ini
[ubuntu_smb]
path = /home/ggangliu
available = yes
browseable = yes
public = yes
writable = yes
create_mask = 0755
force user = ggangliu
force group = ggangliu
```

### How to mount

``` sh
sudo apt-get install cifs-utils
sudo mkdir /mnt/31-52
sudo mount -t cifs -o username=ggangliu //192.168.31.52/ggangliu /mnt/31-52
```

add to /etc/fstab file:

``` ini
//192.168.31.52/ggangliu  /mnt/31-52 cifs user=ggangliu,pass=liuyg628 0 0
```

## VNC [Undone]

<https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04>

``` sh
sudo apt update
sudo apt install tightvncserver
sudo apt install xfce4 xfce4-goodies
tightvncserver :1
sudo ufw allow 5900
sudo ufw allow 5901
vim ~/.vnc/xstartup
chmod +x ~/.vnc/xstartup
vncserver -localhost # restart VNC server
sudo vim /etc/systemd/system/vncserver@.service
sudo systemctl daemon-reload
sudo systemctl enable vncserver@1.service
vncserver -kill :1 # kill instance of VNC
vncserver :1
sudo systemctl start vncserver@1
sudo systemctl status vncserver@1
```

``` ini
#!/bin/sh

xrdb "$HOME/.Xresources"
startxfce4 &
```

restart vncserver

```sh
vncserver -localhost 
```

/etc/systemd/system/vncserver@.service

``` ini
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=ggangliu
Group=ggangliu
WorkingDirectory=/home/ggangliu

PIDFile=/home/ggangliu/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 -localhost :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```


## V2Ray [Undone]

App Center "V2rayX"

``` sh
# 解压
unzip v2ray-linux-64.zip
# 建立目录
sudo mkdir -p /usr/bin/v2ray
# 将两个可执行文件复制至新目录
sudo mv v2ray /usr/bin/v2ray/
sudo mv v2ctl /usr/bin/v2ray/
# 将文件所有者设为root
cd /usr/bin/v2ray/
sudo chown root:root ./*
```

## Mail

Installation

``` sh
sudo apt-get install mailutils
sudo systemctl status postfix
sudo systemctl start postfix
sudo systemctl enable postfix
echo "This is a test email" | mail -s "Test Email" rider628@qq.com
sudo tail -f /var/log/mail.log
```

``` bash
#!/bin/bash

# Define the file to store the WAN IP address
IP_FILE="wan_ip.txt"
EMAIL="rider628@qq.com"
SUBJECT="WAN IP Address Updated"
MAIL_BODY="Your WAN IP address has been updated. The new IP address is:"

# Get the current WAN IP address
CURRENT_IP=$(curl -s ifconfig.me)

# Check if the IP address was successfully retrieved
if [ -z "$CURRENT_IP" ]; then
  echo "Failed to retrieve WAN IP address"
  exit 1
fi

# If the file does not exist, create the file and write the current IP
if [ ! -f "$IP_FILE" ]; then
  echo "$CURRENT_IP" > "$IP_FILE"
  echo "File does not exist, created file and wrote current IP: $CURRENT_IP"
  # Send email notification and check if it was successful
  echo "$MAIL_BODY $CURRENT_IP" | mail -s "$SUBJECT" "$EMAIL"
  if [ $? -eq 0 ]; then
    echo "Email successfully sent to $EMAIL"
  else
    echo "Failed to send email"
  fi
  exit 0
fi

# Read the old IP address from the file
OLD_IP=$(cat "$IP_FILE")

# Compare the current IP with the old IP
if [ "$CURRENT_IP" != "$OLD_IP" ]; then
  echo "$CURRENT_IP" > "$IP_FILE"
  echo "IP address updated: $OLD_IP -> $CURRENT_IP"
  
  # Send email notification and check if it was successful
  echo "$MAIL_BODY $CURRENT_IP" | mail -s "$SUBJECT" "$EMAIL"
  if [ $? -eq 0 ]; then
    echo "Email successfully sent to $EMAIL"
  else
    echo "Failed to send email"
  fi
else
  echo "IP address has not changed: $CURRENT_IP"
fi
```

To run this script periodically

``` sh
crontab -e
crontab -l
```
