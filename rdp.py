print("This script was created by thewickedkarma. Follow them on github https://github.com/thewickedkarma")
import os, subprocess
username=input("Enter your username: ")
password=input("Enter a password: ")
print("remember this password as it will be used while providing superuser commands on your dektop \n creating your user....have some patience")
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print(f"User created and configured having username `{username}` and password `{password}`")
CRP= input("Paste your Chrome Remote Desktop Command you had copied: ")
Pin=input("Choose a pin for your chrome RDP(minimum 6 digits): ")
print("Explore my youtube channel while it completes installing the RDP:  https://www.youtube.com/channel/UC-w_mhTHR6-Lc28PSiv7kaQ/videos")
Autostart = True
class CRD:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.finish(user)
        print("\nRDP created succesfully move to https://remotedesktop.google.com/access")
    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Installing Google Chrome")
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
        os.system("wget https://dl1.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUzMDc3NDYwMCwidSI6bnVsbCwibHQiOiJkb3dubG9hZCIsInMiOiIzM2ExNWQ3YWU0MTNhMTE2ZWJlY2E4YzZmOWFmYjhkNTE0Y2NmMmU0Y2U3ZTUzZDUyOWU0NDQ5YjY1N2Y3YmQ3MjMxNTIwZDRlZGE5ZjhiMWRmYjZiOTQ2Y2ZiNzU0OGJiODFhYjcxNTZhYTZiYWQ4M2UwYjA2MmEyMTY3NzcyNCIsInQiOjE2NDU1MTM0OTcsInN0ZnAiOiIyNGFhYWZiMWVhZmU2ZjU1YzUwMTI3ZmViMGJmOTdkNCIsInN0aXAiOiIzNS4xNTQuMTY2LjE1NSJ9.pfHVPOG-fhRwKRsVdNWiyaoepEIsw-3wqAosQcbwAE4/ocs-url_3.1.0-0ubuntu1_amd64.deb")
        os.system("dpkg -i ocs-url_3.1.0-0ubuntu1_amd64.deb")
        os.system("sudo apt install -f -y")

    @staticmethod
    def finish(user):
        print("Finalizing")
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "https://github.com/thewickedkarma/"
            colab_autostart = """[Desktop Entry]

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")

        os.system(f"adduser {user} chrome-remote-desktop")
        os.system("wget -O ~/Pictures/wall.jpg https://w.wallhaven.cc/full/9m/wallhaven-9m7l2k.jpg")
        os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s ~/Pictures/wall.jpg")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        

        print("Finished Succesfully")
        print("RDP created succesfully move to https://remotedesktop.google.com/access")

try:
    if CRP == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRD(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
