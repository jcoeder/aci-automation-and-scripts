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
You may have to install git if your system does not come with it.

`yum install git -y`

`git clone https://github.com/jcoeder/aci-automation-and-scripts.git`

### Navigate to this directory
```cd /aci-automation-and-scripts/interface_descriptions```

### Create your virtual environment to run Python
```
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Edit the interface_description.py with the IP address of the APIC
You can use any editor you are familiar with.  I am using VIM.
```
vi interface_description.py 
```
Update the IP address in this section.  Do not change anything else in the file.
```
### Update this IP Address
### Update this IP Address
apic = '10.5.9.11'
### Update this IP Address
### Update this IP Address
```
Save and exit the file.

### Run the script
```python interface_description.py```

### Output
```
(venv) $ python interface_description.py 
Password: 
Node ID (Ex: 101): 102
Interface ID (Ex: "1/1"): 1/44
Interface Description: Testing1234
<Response [200]>
```
A 200 status code indicates that the script was successful.
