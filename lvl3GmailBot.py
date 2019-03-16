from selenium import webdriver

bot = webdriver.Chrome(executable_path= "C:\\Users\\Avinesh\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
bot.get("http://www.gmail.com")

bot.find_element_by_name("identifier").send_keys("mohan.19.1@protosem.tech")
bot.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()

bot.implicitly_wait(4)

bot.find_element_by_name("password").send_keys("*********")
bot.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
bot.implicitly_wait(4)

var = bot.find_element_by_class_name("bsU").text
print("No of Unread Mail:",var)