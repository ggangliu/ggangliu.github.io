# How to add ssh key

- ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
- eval "$(ssh-agent -s)"
- ssh-add ~/.ssh/id_rsa
- cat ~/.ssh/id_rsa.pub
- 添加公钥到 GitHub：登录到你的 GitHub 帐户，导航到 Settings -> SSH and GPG keys 页面，点击 New SSH key 按钮，将复制的公钥粘贴到 Key 文本框中，并为该密钥添加一个描述（如你的计算机名称），最后点击 Add SSH key 按钮。
- touch ~/.ssh/config
  
  ``` sh
   Host example.com
    ForwardAgent yes
  ```

## Power shell 中如何启动 ssh-agent

Start-Service ssh-agent
ssh-add path_to_your_private_key
& $(ssh-agent -s)

## Test

ssh -T git@github.com

touch ~/.ssh/config
  
``` sh
Host example.com
ForwardAgent yes
```

ssh -T git@github.com

git remote set-url origin git@github.com:minwegoal/3dgs_all_in_one.git