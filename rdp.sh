#!/bin/bash


echo "This script was created by thewickedkarma. Follow them on github https://github.com/thewickedkarma"
read -p $' ┌─[ Choose a username:]─[~]
 └──╼ ~ ' username
read -p $' ┌─[ Choose a password:]─[~]
 └──╼ ~ ' password
useradd -m {$username}
adduser {$username} sudo
echo '{username}:{password}' | sudo chpasswd
sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd
read -p $' ┌─[ Paste the Chrome desktop command you copied :]─[~]
└──╼ ~ ' CRP
read -p $' ┌─[ Choose a pin for Chrome RDP (not less than 6 digits):]─[~]
└──╼ ~ ' Pin
echo "Explore my youtube channel while it completes installing the RDP:  https://www.youtube.com/channel/UC-w_mhTHR6-Lc28PSiv7kaQ/videos"
sudo apt update
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
dpkg -i chrome-remote-desktop_current_amd64.deb
sudo apt install -f 
export DEBIAN_FRONTEND=noninteractive
sudo apt install --assume-yes xfce4 desktop-base xfce4-terminal
bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'
sudo apt install --assume-yes xscreensaver
systemctl disable lightdm.service
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install -f 
mkdir -p /home/{user}/.config/autostart
chown {user}:{user} /home/{user}/.config
adduser {user} chrome-remote-desktop
{CRP} --pin={Pin}
su - {user} -c '{command}'
sudo service chrome-remote-desktop start
echo "RDP created succesfully move to https://remotedesktop.google.com/access"
