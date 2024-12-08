# Docker Notes

## Docker install

To install Docker on Ubuntu, you can follow these steps:

1. **Update Package Index**: First, update the package index on your Ubuntu system to ensure you have the latest version information for available packages.

   ```bash
   sudo apt update
   ```

2. **Install Required Packages**: Docker requires a few packages to be installed before it can be installed from the Docker repository. Install these packages by running:

   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **Add Docker's GPG Key**: Add Docker's official GPG key to your system.

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

4. **Add Docker Repository**: Add the Docker repository to your system's APT sources.

   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

5. **Update Package Index**: Update the package index again to ensure the system is aware of the newly added Docker repository.

   ```bash
   sudo apt update
   ```

6. **Install Docker**: Finally, install Docker Community Edition (CE) using the following command.

   ```bash
   sudo apt install docker-ce
   ```

7. **Start Docker Service**: Once Docker is installed, the Docker service should start automatically. You can verify its status with:

   ```bash
   sudo systemctl status docker
   ```

8. **Enable Docker Service (Optional)**: If you want Docker to start automatically at boot, you can enable the Docker service with:

   ```bash
   sudo systemctl enable docker
   ```

9. **Add User to Docker Group (Optional)**: By default, Docker commands require root privileges. If you want to run Docker commands without sudo, add your user to the `docker` group.

   ```bash
   sudo groupadd docker
   sudo chmod 666 /var/run/docker.sock
   sudo usermod -aG docker $USER
   ```

10. **Log Out and Log Back In (Optional)**: To apply the group membership changes, you may need to log out and log back in, or restart your system.

11. **Verify Docker Installation**: Verify that Docker is installed correctly by running the following command, which should display the Docker version information:

    ```bash
    docker --version
    ```

12. **Install SSHFS**: First, you need to install SSHFS on the host machine where Docker is running. You can typically install SSHFS using your package manager. For example, on Ubuntu, you can install it using the following command:

   ```bash
   sudo apt-get install sshfs
   sshfs user@remote_host:/remote/path /local/mount/point
   umount /local/mount/point
   ```

## Docker Container Operation

``` bash
docker run --name sphinx-server -v /home/ggangliu/sphinx_docs:/home/sphinx_docs -it -p 80:80 ggangliu/sphinx-server:latest /bin/bash
docker start my_container
docker exec -it my_container bash
```

remove containers

``` bash
docker rm -f mycontainer
```

## Docker Image Operation

building image

``` bash
docker build -f MyCustomDockerfile -t docker-image-name .
```

renaming image name

``` bash
docker tag my-node-app:latest my-renamed-app:v1.0
```

commit image to hub

``` bash
docker commit sphinx-server ggangliu/sphinx-server:v1.0
```

push

``` bash
docker push
```

remove image

``` bash
docker rmi
```

That's it! Docker should now be installed and ready to use on your Ubuntu system.
