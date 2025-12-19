from appium import webdriver
from typing import Any, Dict #To use Type Hint
from appium.options.common import AppiumOptions # Capabilities管理Class
from appium.webdriver.common.appiumby import AppiumBy # Locator

# AppiumBy.ID
# AppiumBy.ACCESSIBILITY_ID
# AppiumBy.XPATH
# AppiumBy.ANDROID_UIAUTOMATOR
# AppiumBy.CLASS_NAME
# AppiumBy.NAME

cap:Dict[str, Any] = {
    "platformName": "android", #対象OS
    "deviceName": "Pixel_6", #エミュレータ名
    "automationName": "UiAutomator2", #自動化エンジン
    "appPackage": "com.android.settings", #起動するアプリのパッケージ名
    "appActivity": ".Settings", #最初に開く画面
    "language": "en", #端末言語
    "locale": "US" #地域設定
}

url = "http://localhost:4723"

#　WebDriverの接続（Appium Serverに接続、Capabilitiesを送信、エミュレータにセッション作成）
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# 要素を探す
# el = driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Battery']")
el = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.scrollIntoView(new UiSelector().textContains("Battery"))'
)
# Batteryをタップ
el.click()
# セッション終了
driver.quit()