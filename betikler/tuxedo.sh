echo -e "deb https://deb.tuxedocomputers.com/ubuntu jammy main" | sudo tee -a /etc/apt/sources.list.d/tuxedocomputers.list
cd /etc/apt/trusted.gpg.d/
sudo wget https://deb.tuxedocomputers.com/0x54840598.pub.asc
sudo apt-get update
sudo apt-get install tuxedo-control-center
