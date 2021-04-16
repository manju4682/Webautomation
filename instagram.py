#importing all the required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, username, password):
    #this is function that logs in using the username and password
    driver.get("https://www.instagram.com/")

    #We wait till the entire login page is loaded making make sure that is clickable and then we send in the keys
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button/div[text()='Log In']").click() # clicking on the login button

    #this try block handles the pop windows
    try:
        #this one handles the save login info window
        not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

        #this one handles the notification window
        not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    except:
        pass    

def get_followers(driver):  
    
    #getting the page
    #driver.get("https://www.instagram.com/{0}".format(account))
    
    #The wait is to make sure that everything is loaded and the links are clickable, otherwise we get the not found exception
    #this one clicks on the profile button
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     ']"))).click()
    
    #This one is for followers link in the profile page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
    
    #this is to make sure that followers dialog is loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]')))

    PAUSE = 1.5 # We will pause to allow loading of content
    driver.execute_script("followersbox = document.getElementsByClassName('isgrP')[0];")
    previous_height = driver.execute_script("return followersbox.scrollHeight;")

    # We will scroll down the followers modal to try and get all followers 
    while True:
        driver.execute_script("followersbox.scrollTo(0, followersbox.scrollHeight);")

        # We will wait for the dialog to load
        time.sleep(PAUSE)

        # Calculating new scrollHeight and comparing it with the previous height
        new_height = driver.execute_script("return followersbox.scrollHeight;")
        if new_height == previous_height:
            #if old height is equal to previous height that means the scrolling has not loaded any new followers, so we break 
            break
        previous_height = new_height

    followers = []

    while True:
        #this while loop is to make sure that we have got all the followers
        #If we have recieved all the followers it prints and breaks out
        #if not we get a staleelementexception and we will force it to scroll again
        try:
            followers_elems = driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')
            for i in followers_elems:
                item = i.text.split()
                followers.append(item[0])
            break
        except:
            while True:
                print("In the inside while of second loop ")
                driver.execute_script("followersbox.scrollTo(0, followersbox.scrollHeight);")

                
                time.sleep(SCROLL_PAUSE)

                
                new_height = driver.execute_script("return followersbox.scrollHeight;")
                if new_height == last_height:
                    break
                last_height = new_height

    print(len(followers))
    #Printing the followers
    print(followers)

    #this one closes the dialog box 
    cancel = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/button'))).click()

def get_following(driver):


    PAUSE = 1.5 #the pause

    #Navigating to the following link and clicking
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()

    #making sure that the following dialog box has loaded 
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    
    driver.execute_script("followingbox = document.getElementsByClassName('isgrP')[0];")
    previous_height = driver.execute_script("return followingbox.scrollHeight;")
    following = []
    while True:
        driver.execute_script("followingbox.scrollTo(0, followingbox.scrollHeight);")

        # Waiting for page to load
        time.sleep(PAUSE)

        # Calculating the new scrollHeight and comparing with the previous height
        new_height = driver.execute_script("return followingbox.scrollHeight;")
        if new_height == previous_height:
            break
        previous_height = new_height

    while True:
        try:
            following_elems = driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')
            for i in following_elems:
                # In this for loop we are generating the list of following 
                item = i.text.split()
                following.append(item[0])
                
            break    
        except:
            while True:
                driver.execute_script("followingbox.scrollTo(0, followingbox.scrollHeight);")
                time.sleep(PAUSE)
                new_height = driver.execute_script("return followingbox.scrollHeight;")
                if new_height == last_height:
                    break
                last_height = new_height
    print(len(following))
    print(following)    

if __name__ == '__main__':    

    driver  = webdriver.Chrome()
    username = "#"
    pwd = "#"
    login(driver,username,pwd)
    get_followers(driver)
    get_following(driver)


