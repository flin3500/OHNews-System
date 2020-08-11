# OHNews System
This is OHNews System written in python, and use Mysql, MongoDB, Redis as database.

# Preparation

1. OS: Mac OS Catalina v 10.15.5

2. IDE: Pycharm 2020.1( other IDE or editor is also fine)

3. FRONTEND: Not yet

4. BACKEND: Python 3.8.5  **I wll use pyenv to check if other version is also fine**

5. Database: Mysql v8.0.21, Redis, MongoDB

6. The module you need

   ```shell
   # if you have pip3 install
   pip3 install mysql.connector
   pip3 install colorama
   
   # if you have pip install
   pip install mysql.connector
   pip install colorama
   
   # if you have python3 install
   python3 -m pip install mysql.connector
   python3 -m pip install colorama
   
   # or if you do not have python install
   # emmm, google that and do the things above :)
   ```

7. dwsdsa

# Difficulty 😭

1. In Mysql 8.0, the **caching_sha2_password** is the default authentication plugin rather than **mysq_native_password**. So you may get error like NotSupportedError.There are two ways to fix that.

   ```bash
   mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported
   ```

   1. Change to other version of Mysql which use **mysq_native_password** as default.

   2. Set the default authentication plugin to **mysq_native_password**

      1. get into mysql

         ```bash
         mysql -u root -p
         ```

      2. Set default authentication plugin

         ```mysql
         ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
         -- Write your root passwoed inside the last ''
         ```

      3. check if the root default authentication change already

         ```mysql
         SELECT user,host,plugin FROM mysql.user;
         -- output should be like this
         +------------------+-----------+-----------------------+
         | user             | host      | plugin                |
         +------------------+-----------+-----------------------+
         | mysql.infoschema | localhost | caching_sha2_password |
         | mysql.session    | localhost | caching_sha2_password |
         | mysql.sys        | localhost | caching_sha2_password |
         | root             | localhost | mysql_native_password |
         +------------------+-----------+-----------------------+
         ```

      4. Change the my.conf. For me, I use homebrew, the conf is inside /usr/local/etc/my.cnf

         ```bash
         # add this at the end
         default_authentication_plugin=mysql_native_password
         ```

      5. Stop mysql

         ```bash
         mysql.server stop
         brew services stop mysql # if you use homebrew
         mysql.server status
         # ERROR! MySQL is not running
         ```

      6. Start mysql

         ```bash
         launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist # if has error ignore that and do the next commend
         mysql.server start
         mysql.server status
         SUCCESS! MySQL running (XXXXX)
         ```

      7. Now it is ok

2. Jhkjhnjk

