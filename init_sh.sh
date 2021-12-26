#!/bin/sh
echo Y | sudo add-apt-repository main
echo Y | sudo add-apt-repository universe
echo Y | sudo add-apt-repository restricted
echo Y | sudo add-apt-repository multiverse
echo Y | sudo apt-get update
echo Y | sudo apt-get upgrade
echo Y | sudo apt-get install python
echo Y | sudo apt-get install python3
echo Y | sudo apt-get install gdb
echo Y | sudo apt-get install ssh
echo Y | sudo apt-get install net-tools
echo Y | sudo apt-get install git
echo Y | sudo apt-get install clang
echo Y | sudo apt-get install cmake
echo Y | sudo apt-get install lldb
echo Y | sudo apt-get install vim
echo Y | sudo apt-get install fail2ban
echo Y | sudo apt-get install python-pip
echo Y | sudo python -m pip uninstall pip
echo Y | sudo apt-get install python-pip --reinstall
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
echo Y | sudo apt-get upgrade
echo Y | sudo apt-get install python3-pip
echo Y | sudo apt-get install gunicorn
echo Y | sudo apt-get install nginx
sudo mkdir /home/webmaster
sudo mv ../simple_emr_api /home/webmaster
sudo mv /home/webmaster/simple_emr_api/gunicorn.service /etc/systemd/system/
sudo mv /home/webmaster/simple_emr_api/nginx.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled
sudo service nginx restart
sudo mkdir /home/webmaster/simple_emr_api/run
sudo chown www-data:www-data /home/webmaster/simple_emr_api/run
pip3 install gunicorn
pip3 install Django gunicorn
pip3 install -r /home/webmaster/simple_emr_api/requirements.txt
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart


