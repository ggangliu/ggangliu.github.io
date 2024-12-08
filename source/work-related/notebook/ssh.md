# SSH

[ssh-key](ssh-key.md)

``` sh
ssh-keygen -t ed25519-sk -C "your_email@example.com"
ssh-keygen -t ecdsa-sk -C "your_email@example.com"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

cat ~/.ssh/id_ed25519.pub
```

## vscode remote ssh vnc host

``` bash
ssh-keygen.exe -f my_key

// 测试远程服务器（这里需要保证链接服务器成功）
ssh user@host

//公钥复制到远程主机对应用户
ssh-copy-id user@host
ssh-copy-id -i my_key.pub <username>@<remote_host>

```

``` conf
Host remote_host
    HostName remote_host_address
    User your_username
    IdentityFile ~/.ssh/id_ed25519
```

## Install ssh server

``` sh
sudo apt update
sudo apt install openssh-server
```

## Windows

启动ssh服务：Start-Service sshd
重启ssh服务：Restart-Service sshd

设置开机启动
Set-Service sshd -StartupType Automatic

挂在目录

sshfs -o nonempty,allow_other,default_permissions rider@192.0.2.2:H:\\ggangliu_wps\\knowledge-libs\\ggangliu-doc /home/ggangliu/sphinx_docs/

sshfs -o nonempty username@remote_host:/remote/directory /local/mount/point

-o allow_other,default_permissions

[参考文章](https://blog.csdn.net/qq_41566366/article/details/128496098?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-128496098-blog-106295770.235%5Ev43%5Epc_blog_bottom_relevance_base9&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-128496098-blog-106295770.235%5Ev43%5Epc_blog_bottom_relevance_base9&utm_relevant_index=2)

## Ubuntu

``` sh
sudo systemctl status ssh
sudo systemctl enable ssh
```

``` sh
systemctl cat ssh
```

这将显示 SSH 服务的单元文件内容。你应该看到类似以下内容：

``` ini
[Unit]
Description=OpenBSD Secure Shell server
After=network.target auditd.service

[Service]
EnvironmentFile=-/etc/default/ssh
ExecStartPre=/usr/sbin/sshd -t
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartSec=42s
Type=notify
RuntimeDirectory=sshd
RuntimeDirectoryMode=0755

[Install]
WantedBy=multi-user.target
```

确保 After=network.target 行存在，这意味着 SSH 服务将在网络服务启动之后启动。

``` sh
sudo systemctl daemon-reload
sudo reboot
```
