# How to setup VPN to access home server by WireGuard

## Conceptual overview

WireGuard associates tunnel IP addresses with public keys and remote endpoints. When the interface sends a packet to a peer, it does the following:

This packet is meant for 192.168.30.8. Which peer is that? Let me look... Okay, it's for peer ABCDEFGH. (Or if it's not for any configured peer, drop the packet.)
Encrypt entire IP packet using peer ABCDEFGH's public key.
What is the remote endpoint of peer ABCDEFGH? Let me look... Okay, the endpoint is UDP port 53133 on host 216.58.211.110.
Send encrypted bytes from step 2 over the Internet to 216.58.211.110:53133 using UDP.

When the interface receives a packet, this happens:

I just got a packet from UDP port 7361 on host 98.139.183.24. Let's decrypt it!
It decrypted and authenticated properly for peer LMNOPQRS. Okay, let's remember that peer LMNOPQRS's most recent Internet endpoint is 98.139.183.24:7361 using UDP.
Once decrypted, the plain-text packet is from 192.168.43.89. Is peer LMNOPQRS allowed to be sending us packets as 192.168.43.89?
If so, accept the packet on the interface. If not, drop it.

## 安装

``` sh
sudo apt install wireguard
```

## 配置步骤

``` sh
wg genkey | tee wg_server.key | wg pubkey > wg_server.pub && cat wg_server.key && cat wg_server.pub
```

服务器端的配置 /etc/wireguard/wg0.conf

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

启动服务

``` sh
sudo wg-quick up wg0
```

检查哪些端口处于监听状态

``` sh
sudo netstat -tuln
```

如果需要开机自启，则可以

``` sh
sudo systemctl enable wg-quick@wg0
```

客户端的配置

``` ini
[Interface]
PrivateKey = aDHxtVvZodTWj3a0jFVpsb6ZYyZDIBkEnVIRVC6mUFY=
Address = 192.0.2.2/32

[Peer]
PublicKey = 4jqjWGiinulgYYGVGfMzQc+D9tfwUIR5nnlrWYmu10A=
AllowedIPs = 192.0.2.1/32
Endpoint = 8.137.11.23:51820
PersistentKeepalive = 25
```

home server client:

``` ini
[Interface]
PrivateKey = aDHxtVvZodTWj3a0jFVpsb6ZYyZDIBkEnVIRVC6mUFY=
Address = 192.168.31.2/32

[Peer]
PublicKey = 4jqjWGiinulgYYGVGfMzQc+D9tfwUIR5nnlrWYmu10A=
AllowedIPs = 192.168.31.3/32
Endpoint = 125.71.119.43:51820
PersistentKeepalive = 25
```

How to restart in server 

``` sh
sudo wg show wg0
sudo wg-quick down wg0
sudo wg-quick up wg0
sudo systemctl start wg-quick@wg0.service
sudo systemctl status wg-quick@wg0.service
```

## 配置为网关

To configure a WireGuard interface to act as a gateway or handle routing, you need to configure the routing table and enable IP forwarding. Here's how you can do it:

1. **Enable IP Forwarding**:
   - Open the `/etc/sysctl.conf` file for editing:

     ```bash
     sudo nano /etc/sysctl.conf
     ```

   - Uncomment the following line to enable IP forwarding:

     ```plaintext
     net.ipv4.ip_forward=1
     ```

   - Save and close the file.

   - Apply the changes:

     ```bash
     sudo sysctl -p
     ```

2. **Configure Routing**:

    ``` bash
    PostUp = iptables -t nat -A POSTROUTING -s 192.0.3.0/24 -j SNAT --to-source 192.168.31.188
    PostDown = iptables -t nat -D POSTROUTING -s 192.0.3.0/24 -j SNAT --to-source 192.168.31.188
    ```
  
    ref to <https://devld.me/2020/07/27/wireguard-setup/>

3. **Configure Allowed IPs in WireGuard**:
   - Ensure that the `AllowedIPs` setting in your WireGuard configuration includes the IP addresses of the networks you want to route through the WireGuard interface.

     For example, if you want to route traffic for `92.168.32.0/24`, your WireGuard configuration (`wg0.conf`) should include:

     ```plaintext
     AllowedIPs = 10.0.0.0/24
     ```

   - Reload or restart the WireGuard service to apply the changes.

4. **Firewall Configuration**:
   - If you have a firewall enabled, ensure that it allows traffic to pass through the WireGuard interface and that it allows forwarding packets.

5. **Testing**:
   - Test the routing by sending traffic from a device within the WireGuard network to a destination in the specified network. Verify that the traffic is routed correctly.

By following these steps, you can configure a WireGuard interface to act as a gateway and handle routing for specific networks. Make sure to adjust the configuration according to your specific network setup and requirements.

## 配置详解

WireGuard 使用 INI 语法作为其配置文件格式。默认路径是 /etc/wireguard/wg0.conf。

### [Interface]

定义本地 VPN 配置。

- 本地节点是客户端，只路由自身的流量，只暴露一个 IP。
  
  ``` ini
    [Interface]
    # Name = phone.example-vpn.dev
    Address = 192.0.2.5/32
    PrivateKey = <private key for phone.example-vpn.dev>
  ```

- 本地节点是中继服务器，它可以将流量转发到其他对等节点（peer），并公开整个 VPN 子网的路由。
  
  ``` ini
    [Interface]
    # Name = public-server1.example-vpn.tld
    Address = 192.0.2.1/24
    ListenPort = 51820
    PrivateKey = <private key for public-server1.example-vpn.tld>
    DNS = 1.1.1.1
  ```

### Address

定义本地节点应该对哪个地址范围进行路由。如果是常规的客户端，则将其设置为节点本身的单个 IP（使用 CIDR 指定，例如 192.0.2.3/32）；如果是中继服务器，则将其设置为可路由的子网范围。

``` ini
    Address = 192.0.2.3/32
```

### ListenPort

当本地节点是中继服务器时，需要通过该参数指定端口来监听传入 VPN 连接，默认端口号是 51820。常规客户端不需要此选项

### PrivateKey

本地节点的私钥，所有节点（包括中继服务器）都必须设置。不可与其他服务器共用。
私钥可通过命令 `wg genkey > example.key` 来生成

### DNS

通过 DHCP 向客户端宣告 DNS 服务器。客户端将会使用这里指定的 DNS 服务器来处理 VPN 子网中的 DNS 请求，但也可以在系统中覆盖此选项。

### [Peer]

定义能够为一个或多个地址路由流量的对等节点（peer）的 VPN 设置。对等节点（peer）可以是将流量转发到其他对等节点（peer）的中继服务器，也可以是通过公网或内网直连的客户端。

中继服务器必须将所有的客户端定义为对等节点（peer）

对等节点（peer）是路由可达的客户端，只为自己路由流量：

``` ini
    [Peer]
    # Name = public-server2.example-vpn.dev
    Endpoint = public-server2.example-vpn.dev:51820
    PublicKey = <public key for public-server2.example-vpn.dev>
    AllowedIPs = 192.0.2.2/32
```

对等节点（peer）是中继服务器，用来将流量转发到其他对等节点（peer）

``` ini
    [Peer]

    # Name = public-server1.example-vpn.tld
    Endpoint = public-server1.example-vpn.tld:51820
    PublicKey = <public key for public-server1.example-vpn.tld>
    # 路由整个 VPN 子网的流量
    AllowedIPs = 192.0.2.1/24
    PersistentKeepalive = 25
```

### Endpoint

指定远端对等节点（peer）的公网地址。如果对等节点（peer）位于 NAT 后面或者没有稳定的公网访问地址，就忽略这个字段。通常只需要指定中继服务器的 Endpoint，当然有稳定公网 IP 的节点也可以指定。

通过 IP 指定：

``` ini
    Endpoint = 123.124.125.126:51820
```

通过域名指定：

``` ini
    Endpoint = public-server1.example-vpn.tld:51820
```

### AllowedIPs

允许该对等节点（peer）发送过来的 VPN 流量中的源地址范围。同时这个字段也会作为本机路由表中 wg0 绑定的 IP 地址范围。如果对等节点（peer）是常规的客户端，则将其设置为节点本身的单个 IP；如果对等节点（peer）是中继服务器，则将其设置为可路由的子网范围。可以使用，来指定多个 IP 或子网范围。该字段也可以指定多次。

当决定如何对一个数据包进行路由时，系统首先会选择最具体的路由，如果不匹配再选择更宽泛的路由。例如，对于一个发往 192.0.2.3 的数据包，系统首先会寻找地址为 192.0.2.3/32 的对等节点（peer），如果没有再寻找地址为 192.0.2.1/24 的对等节点（peer），以此类推。

对等节点（peer）是常规客户端，只路由自身的流量：

``` ini
    AllowedIPs = 192.0.2.3/32
```

对等节点（peer）是中继服务器，可以路由其自身的流量和它所在的内网的流量：

``` ini
    AllowedIPs = 192.0.2.3/32,192.168.1.1/24
```

### PublicKey

对等节点（peer）的公钥，所有节点（包括中继服务器）都必须设置。

### PersistentKeepalive

如果连接是从一个位于 NAT 后面的对等节点（peer）到一个公网可达的对等节点（peer），那么 NAT 后面的对等节点（peer）必须定期发送一个出站 ping 包来检查连通性，如果 IP 有变化，就会自动更新 Endpoint。

## Reference

<https://www.wireguard.com/>
<https://i.nickyam.com/article/wireguard-vpn>