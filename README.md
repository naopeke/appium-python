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

## Folder structure
1. src/ : source code like libraries, utilities, common functions
2. tests/ : test cases
3. testdata/ : JSON, XML, CSV, configuration files for different environments or test suites
4. reports/ : output reports of test runs, logs, screenshots and metrics
5. lib/ : third-party libraries, dependencies required by the framework or tests
6. config/ : configuration files for the automation framework, settings for the test environment, test data, test execution parameters
7. resources/ : any addithional resources, images, videos, audio files
8. utils/ : utility scripts and functions such as date/time functions, file manipulation utiilities

project-root/
│
├── src/
│   ├── core/               # framework core (driver, base classes)
│   ├── pages/              # Page Object / Screen classes
│   ├── services/           # API clients, business logic
│   └── constants/          # constant values, enums
│
├── tests/
│   ├── ui/                 # UI test cases
│   ├── api/                # API test cases
│   ├── integration/        # integration tests
│   └── regression/         # regression test suites
│
├── testdata/
│   ├── json/               # JSON test data
│   ├── csv/                # CSV test data
│   ├── xml/                # XML test data
│   └── environments/       # env-specific data (dev, qa, prod)
│
├── config/
│   ├── appium.yaml         # Appium configuration
│   ├── test-config.yaml    # test execution parameters
│   └── env.config.yaml     # environment settings
│
├── utils/
│   ├── date_utils.py       # date/time helpers
│   ├── file_utils.py       # file handling utilities
│   ├── logger.py           # logging utilities
│   └── wait_utils.py       # wait/retry helpers
│
├── lib/
│   └── drivers/            # browser/mobile drivers if needed
│
├── resources/
│   ├── images/             # images
│   ├── videos/             # test recordings
│   └── audio/              # audio resources (if any)
│
├── reports/
│   ├── html/               # HTML reports
│   ├── logs/               # execution logs
│   ├── screenshots/        # screenshots on failure
│   └── metrics/            # performance metrics
│
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies (if used)
├── README.md               # project documentation
└── .gitignore
