# aci-automation-and-scripts
Cisco ACI Automation and Scripts

### Install Python3.7 CentOS7
```
sudo yum install gcc openssl-devel bzip2-devel libffi libffi-devel sqlite sqlite-devel -y
sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
sudo tar xzf Python-3.7.3.tgz
cd Python-3.7.3
sudo ./configure --enable-optimizations
sudo make altinstall
pip3.7 install virtualenv --user
pip3.7 install --upgrade pip
pip3.7 install --upgrade wheel
