# interface_descriptions_csv
Script to set Physical Interface Configuration Description in Cisco ACI reading the data from a CSV

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
```cd /aci-automation-and-scripts/interface_descriptions_csv```

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

### Update the CSV with the important data
vi interfaces.csv
```
node,interface,description
101,1/1,Testing123
101,1/2,TestingABC
101,1/3,Testing456
102,1/1,Working123
102,1/2,WorkingABC
```
### Run the script
```python interface_description.py```

### Output
```
(venv) $ python interface_description_csv.py
Password: 
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
