#!/data/data/com.termux/files/usr/bin/bash
pkg install -y root-repo 
pkg install -y git tsu python wpa-supplicant pixiewps iw

git clone --depth 1 https://github.com/SIAMRAHMAN000/siamwifi siamwifi

chmod +x siamwifi/siam.py
