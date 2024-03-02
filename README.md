## [Termux](https://termux.com/)
Please note that root access is required.  

#### Using installer
 ```
 curl -sSf https://raw.githubusercontent.com/SiamApi/siamwifi/main/installer.sh | bash
 ```
#### Manually
**Installing requirements**
 ```
 pkg install -y root-repo
 pkg install -y git tsu python wpa-supplicant pixiewps iw openssl
 ```
**Getting OneShot**
 ```
 git clone --depth 1 https://github.com/SiamApi/siamwifi siamwifi
 ```
#### Running
 ```
 sudo python siamwifi/cracker.py -i wlan0 --iface-down -K
 ```
