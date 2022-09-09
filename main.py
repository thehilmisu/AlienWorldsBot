import pickle
import random
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

###fzk34.c.wam wax account

driver_path = "/usr/bin/chromedriver" # location of chromedriver
brave_path = "/usr/bin/google-chrome"#"/snap/bin/brave" # location of Brave browser

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }

option = webdriver.ChromeOptions()
option.add_argument('log-level=3')
option.add_argument('window-size=929, 1012')
option.binary_location = brave_path

driver = webdriver.Chrome(driver_path)
main_page = driver.current_window_handle

###
email = "ozcanhakanzi@gmail.com"
password = "0561995hH*"
sleeptimeMin = 30 # Minimum time the bot will sleep between actions to look more human
sleeptimeMax = 90 # Maximum time the bot will sleep between actions to look more human
###
debugResolution = True
debugBarsAdd = 0
debugLogfile = "debug.log"
###
version = "1.1.4"
###

driver.get("https://all-access.wax.io/")

def debugger(t = "init"):
    nl = "\n"
    if t == "init":
        f = open(debugLogfile, "w+")
        f.write(f"AWA {version} | {datetime.now().strftime('%c')}{nl}")
        f.close()
    else:
        f = open(debugLogfile, "a")
        print(t)
        f.write(f"{datetime.now().strftime('%X')} | {t}{nl}")
        f.close()


def sleeptime():
    x = random.randint(sleeptimeMin, sleeptimeMax)
    print(f"Going sleep: {x}s")
    return x

size = 0,0

def preload(): # logs into wax.io
    now = datetime.now()
 
    debugger(now)
    debugger("Preloading...")
    while True:
        debugger("Clicking loggin")
        try:
            debugger("trying ....")

            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[5]/div/div/div/div[1]/div[1]/input').send_keys(email)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[5]/div/div/div/div[1]/div[2]/input').send_keys(password)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[5]/div/div/div/div[4]/button').click()

        except:
            print(driver.current_url)
            if driver.current_url == "https://wallet.wax.io/dashboard":
                debugger("Successfully logged in, breaking")
                break
            else:
                debugger("except else ....")
                time.sleep(0.5)
        else:
            debugger("Broke ....")
            break
    time.sleep(3)
    while True:
        if driver.current_url != "https://wallet.wax.io/dashboard":
            debugger("Waiting for dashboard")
            time.sleep(0.6)
        else:
            break
    debugger("Switching to AW")
    driver.get("https://play.alienworlds.io/")


def login(): # login into alienworlds
    debugger("Loging into AW...")
    while True:
        debugger("Clicking loggin")
        try:
            debugger("trying ....")
            driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div[1]/div/div/div').click()

        except:
            debugger(driver.current_url)
            if driver.current_url == "https://wallet.wax.io/dashboard":
                debugger("Successfully logged in, breaking")
                break
            else:
                debugger("except else ....")
                time.sleep(0.5)
        else:
            debugger("Broke ....")
            break
    time.sleep(3)
    while True:
        if driver.current_url != "https://play.alienworlds.io/inventory":
            debugger("Waiting for AW dashboard")
            time.sleep(0.6)
        else:
            debugger("Successfully logged in, start mining")
            break


def miner(force = False): # activates miner menu button
    debugger("Mining")
    global btn
    while True:
        debugger("Clicking mine")
        try:
            debugger("trying to click mine....")
            #driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div/div/div').click()
            #driver.find_element_by_link_text("Mine").click()
            time.sleep(5)
            btn = driver.find_element(By.CLASS_NAME, value="css-3vja5m")
            btn.click()
            time.sleep(5)
            btn.text
            time.sleep(5)
            
        except:
            
            if driver.find_element(By.CLASS_NAME, value="css-3vja5m").text == "Claim Mine": #TODO: look at mine or claim mine
                time.sleep(1)
                debugger("clickinasljkdhlkashdlkashlkdhaslkdhasklhdasklhlkashdlk")
                driver.find_element(By.CLASS_NAME, value="css-1jqmj0w").click()
                time.sleep(1)
                break
            else:
                debugger("except else ....")
                time.sleep(1.5)
        else:
            debugger("Broke ....")
            break
    
    mainwindowhandle = driver.current_window_handle
    time.sleep(3)
    while True:
        time.sleep(2)
        
        popupwindowhandle = None
        
        for handle in driver.window_handles:
            if handle != mainwindowhandle:
                popupwindowhandle = handle

        driver.switch_to.window(popupwindowhandle)


        debugger(driver.current_url)
        driver.find_element(By.XPATH, value="/html/body/div/div/section/div[2]/div/div[5]/button").click()
        time.sleep(2)
        break
        #/html/body/div/div/section/div[2]/div/div[5]/button
                                            
        #/html/body/div/div/section/div[2]/div/div[5]/button
        #https://all-access.wax.io/cloud-wallet/signing/
        

def end(force = False): # resets
    driver.close()
    
def wait(): # finds sleep time and waits
    s = ""
    found = False
    while not found:
        for e in driver.get_log('browser'):
            if "until next mine" in e["message"]:
                found = True
                s = e["message"]
                break
        time.sleep(0.6)
    debugger("Sleeping")
    time.sleep(int(s[s.find("mine ")+5:s.find("\"'")])/1000)
    debugger("SleepStop")

debugger("init")

preload()
login()
miner()
end()

while True:
    time.sleep(495)

    preload()
    login()
    miner()
    end()
    time.sleep(sleeptime()/4)
