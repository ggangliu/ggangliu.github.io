# Samba

To install and start Samba on Ubuntu, you can follow these steps:

1. **Install Samba**:

   Open a terminal and run the following command to install Samba:

   ``` sh
   sudo apt update
   sudo apt install samba
   ```

2. **Configure Samba**:

   After installing Samba, you'll need to configure it to share directories. Samba's main configuration file is `/etc/samba/smb.conf`. You can edit this file using a text editor like `nano` or `vim`.

   For example, to share a directory named `shared_folder`, you can add the following configuration to `/etc/samba/smb.conf`:

   ``` sh
   [shared_folder]
       path = /path/to/shared_folder
       read only = no
       guest ok = yes
   ```

   Replace `/path/to/shared_folder` with the actual path to the directory you want to share.

3. **Restart Samba**:

   After making changes to the configuration file, restart the Samba service for the changes to take effect:

   ``` sh
   sudo systemctl restart smbd
   ```

4. **Access Shared Folder**:

   Once Samba is configured and running, you should be able to access the shared folder from other devices on your network. You can access it using the SMB protocol in file managers on other computers, or by using the `smbclient` command-line tool on Linux systems.

5. **Samba auto start after restart**:

    ``` sh
    sudo systemctl enable smbd  
    ```

That's it! Samba should now be installed, configured, and running on your Ubuntu system, allowing you to share files and directories with other devices on your network.
