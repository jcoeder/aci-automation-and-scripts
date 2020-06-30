# interface_descriptions
Script to set Physical Interface Configuration Description in Cisco ACI

### Install Python3.7 CentOS7
Make sure Python3.7 is installed on your system in one way or another.  Here is how you do it in CentOS7
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
```

### Clone this repository
```git clone https://github.com/jcoeder/aci-automation-and-scripts.git```

### Navigate to this directory
```cd /aci-automation-and-scripts/interface_descriptions```

### Create your virtual environment to run Python
```
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the script
```python interface_descriptions.py```

### Output
```
(venv) $ python interface_description.py 
Password: 
Node ID (Ex: 101): 102
Interface ID (Ex: "1/1"): 1/44
Interface Description: Testing1234
<Response [200]>
