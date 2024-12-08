# FileSystem includes APP

1. Ensure that the pre-compiled code has been compiled for your PetaLinux target architecture
2. Create an application with the following command

   ```sh
   petalinux-create -t apps --template install --name myapp --enable
   ```

3. Change to the newly created application

   ```sh
   cd <plnx-proj-root>/project-spec/meta-user/recipes-apps/myapp/files/
   ```

4. Remove existing myapp app and copy the prebuilt myapp into myapp/files directory

   ```sh
   rm myapp
   cp <path-to-prebuilt-app> ./
   ```
