# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key,Controller
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
######################################################################################################################

driver.get("file:///C:/Users/mtyag/PycharmProjects/pythonProject1/college%20project/HomePage.html")
time.sleep(6)
driver.get('file:///C:/Users/mtyag/PycharmProjects/pythonProject1/college%20project/index1.html')
time.sleep(6)
driver.forward()
time.sleep(4)
driver.back()
time.sleep(4)
###scrolling down
driver.execute_script("window.scrollBy(0,1600)","")
time.sleep(5)


###########################################################################################################################

select_state_name = driver.find_element(By.ID,'state_name')
select_state_namedd = Select(select_state_name)
select_state_namedd.select_by_visible_text('Uttar Pradesh')
time.sleep(5)
######################################################


applying_for = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[1]/select[1]")
applying_fordd = Select(applying_for)
applying_fordd.select_by_visible_text('Learning Licence')
time.sleep(2)

select_vehicle = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[1]/select[2]")
select_vehicledd = Select(select_vehicle)
select_vehicledd.select_by_visible_text("2 Wheeler without Gear + 4 Wheeler")
time.sleep(2)

first_name = driver.find_element(By.ID,"applicant_name")
first_name.click()
first_name.send_keys("Manik")
time.sleep(3)

middle_name = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[2]/input[2]")
middle_name.click()
time.sleep(3)

last_name = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[2]/input[3]")
last_name.click()
last_name.send_keys("Tyagi")
time.sleep(3)

relationship_with_applicant = driver.find_element(By.ID,"applicant_Relation")
relationship_with_applicantdd = Select(relationship_with_applicant)
relationship_with_applicantdd.select_by_visible_text("Mother")
time.sleep(3)

first_name_guardian = driver.find_element(By.ID,"guardian_name")
first_name_guardian.click()
first_name_guardian.send_keys("Neena")
time.sleep(3)

middle_name_guardian= driver.find_element(By.XPATH,"/html/body/section/form/fieldset[2]/input[5]")
middle_name_guardian.click()
time.sleep(3)

last_name_guardian = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[2]/input[6]")
last_name_guardian.click()
last_name_guardian.send_keys("Tyagi")

dob = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[2]/label[4]")
dob.click()
keyboard = Controller()
keyboard.press(Key.f4)
keyboard.release(Key.f4)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

gender = driver.find_element(By.ID,'gender_male')
gender.click()

phone_no = driver.find_element(By.ID,'applicant_phno')
phone_no.click()
phone_no.send_keys('1234567890')

email = driver.find_element(By.ID,'applicant_email')
email.click()
email.send_keys('xyz10@gmail.com')
time.sleep(2)
#
driver.execute_script("window.scrollBy(0,500)","")
#

house_no = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[1]")
house_no.click()
house_no.send_keys("642")
time.sleep(1)
landmark = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[2]")
landmark.click()
landmark.send_keys("near police station 10002")
time.sleep(1)

district = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[3]")
district.click()
district.send_keys("Gautam buddh nagar")
time.sleep(1)

tehsil = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[4]")
tehsil.click()
tehsil.send_keys("dadri")
time.sleep(1)

village = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[5]")
village.click()
village.send_keys("dadri")
time.sleep(1)

state = driver.find_element(By.XPATH,"/html/body/section/form/fieldset[3]/input[6]")
state.click()
state.send_keys("uttar pradesh")
time.sleep(1)

pincode = driver.find_element(By.XPATH,'/html/body/section/form/fieldset[3]/input[7]')
pincode.click()
pincode.send_keys("110087")
time.sleep(6)

validate_and_pay = driver.find_element(By.LINK_TEXT,"VALIDATE AND BOOK YOUR SLOT")
validate_and_pay.click()
########################################################################################
app_no = driver.find_element(By.XPATH,"/html/body/aside[2]/form/input[1]")
app_no.click()
app_no.send_keys("XYZVBH1234509876")

app_name = driver.find_element(By.XPATH,"/html/body/aside[2]/form/input[2]")
app_name.click()
app_name.send_keys("Manik Tyagi")
time.sleep(3)

driver.execute_script("window.scrollBy(0,500)","")
time.sleep(4)

dob2 = driver.find_element(By.XPATH,"/html/body/aside[2]/form/input[3]")
dob2.click()
keyboard = Controller()
keyboard.press(Key.f4)
keyboard.release(Key.f4)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(4)

select_time = driver.find_element(By.XPATH,"/html/body/aside[2]/form/select[1]")
select_timedd = Select(select_time)
select_timedd.select_by_visible_text("11:15 to 11:45")


time.sleep(3)
test_centre = driver.find_element(By.XPATH,"/html/body/aside[2]/form/select[2]")
test_centredd = Select(test_centre)
test_centredd.select_by_visible_text("Noida 62")
time.sleep(2)

slot_book_date = driver.find_element(By.XPATH,"/html/body/aside[1]/div[3]/ul/li[6]")
slot_book_date.click()
time.sleep(3)
book_button = driver.find_element(By.XPATH,"/html/body/aside[2]/form/input[4]")
book_button.click()
time.sleep(3)























