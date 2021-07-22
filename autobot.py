import time
import itertools
import threading
from threading import Timer
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
#----------------------------------------------------------------
#----------------------------------------------------------------
user='your username'
passw='your password'

options = webdriver.ChromeOptions()
options.headless = True
driver= webdriver.Chrome(executable_path=r"path to your chrome driver",options=options)
#if you don't have chrome driver installed you can install it from here https://chromedriver.chromium.org/

action=ActionChains(driver)
wait=WebDriverWait(driver, 10)

def main(): #opens Login page and logs in
    print('Loading site...')
    driver.get("https://student.amizone.net/")


    username = driver.find_element_by_name('_UserName')
    username.send_keys(user)
    password = wait.until(EC.presence_of_element_located((By.NAME, '_Password')))
    password.send_keys(passw)

    print('Logging in...')

    signinButton = driver.find_element_by_class_name('login100-form-btn')
    signinButton.click()
    print('Logged in')
    print('Loading Home...')

def func1(): #opens navigation button
    navBtn=wait.until(EC.visibility_of_element_located((By.ID,'menu-toggler')))
    navBtn.click()

def func2(): #opens My Calendar in list view
    func1()
    myCal=wait.until(EC.visibility_of_element_located((By.ID,'2')))
    myCal.click()
    print('Opening Calendar...\n')

    lstBtn=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="calendarMain"]/div[1]/div[2]/button[1]')))
    lstBtn.click()

def func3(): #prints timetable
    calDay=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="calendarMain"]/div[2]/div/table/thead/tr/td/div/table/thead/tr/th[2]')))
    try:
        lec=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'fc-title')))
        lecTime=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'fc-time')))
        
        lst1=[]
        lst2=[]
        for elem in lecTime:
            lst1.append(elem.text)
        for elem in lst1:
            if len(elem)>8:
                lst2.append(elem)
        
        for (a,b) in zip(lst2,lec):
            print(a)
            print(b.text.title())
            print('-------------------------------------------------')
    except:
        print('No lecture on',calDay.text)

def func4(): #selects what to do based on the input
    if day=='1' or day=='' or day==None:
        func2()
        func3()
    
    if day=='2':
        func2()
        nxtBtn=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="calendarMain"]/div[1]/div[1]/div/button[2]')))
        nxtBtn.click()
        func3()
        
    if day=='3':
        func1()
        myCourses=wait.until(EC.visibility_of_element_located((By.ID,'18')))
        myCourses.click()
        print('Opening Courses...\n')

        cr=[]
        atn=[]
        tr=['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
        for i in tr: #runs until the names and timings of all 14 courses are selected
            course=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr['+i+']/td[2]')))
            attendance=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr['+i+']/td[6]/button/i')))
            cr.append(course.text)
            atn.append(attendance.text)

        for (a,b) in zip(cr,atn):
            print(a.title(),'|',b)
            
def exec(): #executes all the functions
    try: #when popup is present
        main()
        closeBtn=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ModalPopAppeLibrary"]/div/div/div[1]/button')))
        action.move_to_element(closeBtn).click().perform()
        func4()

    except: #when popup is not present
        func4()

def auto(): #automatically takes 1 as input and executes if no input is given
    print('\nAutopilot Initiated')
    global day  #if not declared globally then it can't be used outside the scope of this fn
    day='1'
    exec()
    print('Enter q to quit')

#--------------------------------------------------------------------
#--------------------------------------------------------------------

time=threading.Timer(4,auto)
time.start()    #timer for 4s starts
day=input('''Today's timetable: Enter 1
Tommorow's timetable: Enter 2
Attendance: Enter 3\n''')
time.cancel()   #if input is given within 4s timer is stopped and normal excution of script takes place

if day=='q':
    quit()
else:
    exec()
