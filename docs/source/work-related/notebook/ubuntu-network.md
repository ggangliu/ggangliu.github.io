# Ubuntu网络图标消失

``` sh
sudo service network-manager stop

sudo vim /etc/NetworkManager/NetworkManager.conf
把false改成true
sudo rm /var/lib/NetworkManager/NetworkManager.state
 
sudo service network-manager start
```
