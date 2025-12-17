## Android Studio for Linux
# Download
```
cd ~/Downloads
tar -xzf android-studio-**.**(version)-linux.tar.gz
sudo mv android-studio /opt/
```

# Run
```
/opt/android-studio/bin/studio
```
# Additional settings
> Default boot: Cold
> Graphic acceleration: Software
> Preferred ABI x86_64

# Setting
> Build, Execution, Deployment > Build Tools > Gradle
> Gradle JDK: jbr-21

## Appium Inspector for Linux
# Method 1. AppImage file
```
Appium-Inspector-2025.11.1-linux-x86_64.AppImage
```
```
chmod +x Appium-Inspector-2025.11.1-linux-x86_64.AppImage
./Appium-Inspector-2025.11.1-linux-x86_64.AppImage
```
# Symbolic link
```
mkdir -p ~/.local/bin
ln -s ~/Downloads/Appium-Inspector-2025.11.1-linux-x86_64.AppImage ~/.local/bin/appium-inspector
```
# Run
```
appium-inspector
```


# Method 2. tar.gz file
# Download
```
cd ~/Downloads
tar -xzf Appium-Inspector-2025.11.1-linux-x64.tar.gz
chmod +x Appium-Inspector
./Appium-Inspector
```
# Move
```
mkdir -p ~/Applications
mv ~/Descargas/Appium-Inspector-2025.11.1-linux-x64 ~/Applications/
```
# Run
```
~/Applications/Appium-Inspector-2025.11.1-linux-x64/Appium-Inspector
```
----------------------------------------------------------------
# Terminal 1
```
appium-inspector
```

> Remote Host 127.0.0.1
> Remote Port 4723
> Remote Path  /wd/hub
> Check "Allow Unauthorized Certificates"

# Terminal 2
```
appium --allow-cors
```

# Inspector
JSON Representation
```
{
  "platformName": "android",
  "platformVersion": "16.0",
  "deviceName": "Pixel_6",
  "automationName": "UiAutomator2",
  "app": "/home/***(name)/Descargas/proverbial_android.apk"
}
```

# android_setup.py
```
pip3 install selenium
pip3 show selenium
pip3 install Appium-Python-Client
pip3 show Appium-Python-Client
```

## APK editor studio
apk-editor-studio_linux_1.7.2.AppImage
```
cd ~/Downloads
chmod +x apk-editor-studio_linux_1.7.2.AppImage
./apk-editor-studio_linux_1.7.2.AppImage
```
