-----Guidelines-----
Open the Automessage.py file in your code runner (VScode, PyCharm,...), there will be customizable areas:
Facebook_pages: put in the facebook links to profiles you want to message
Look for options.add_argument("user-data-dir=C:Your Chrome Path here") and put in your chrome path (find it by typing chrome://version in the searchbar and get the Profile Path)
message_versions: put in the messages you want to send, separate each message version with [ ] (there are examples in the code for you)
random_delay(a,b) and time.sleep(x): you can adjust the delays to your liking by changing the number in side the brackets ()

---Potential Errors---
if it doesn't click the message or close chat button you can adjust:
message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']"))) # might be 'message'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message']"))) # might be 'message'
enter_button = driver.find_element(By.XPATH, "//div[@aria-label='Press Enter to send']") # might be 'Press enter to send'
exit_button =  driver.find_element(By.XPATH, "//div[@aria-label='Close chat']") # might be 'close chat'
