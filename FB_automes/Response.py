from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# List of Facebook page URLs for sending messages
facebook_pages = [
    # Example page
    'https://www.facebook.com/HelloEnglishDaLat/',
    'https://www.facebook.com/jlmeducation/',
    # Add more page URLs here
]

responses = []
# Initialize the WebDriver with your Chrome user profile
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=Your Chrome Path here")  # Adjust path
# Add this line to avoid Chrome's 'User data directory is already in use' error
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
def check_for_new_messages():
    try:
        # Find all messages in the conversation
        message_bubbles = driver.find_elements(By.XPATH, "//div[contains(@class, 'xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx')]")
        
        # Loop through each message bubble to extract and print the received messages
        for bubble in message_bubbles:
            received_message = bubble.text  # Get the text content of each message bubble
            # if received_message:  # Only print if the message is not empty
                # print(f"Received message: {received_message}")
        # Return a list of all non-empty messages
        return [bubble.text for bubble in message_bubbles if bubble.text]  
    except Exception as e:
        print(f"Error while checking messages: {e}")
        return None
# Open each Facebook page and attempt to send a message
for page in facebook_pages:
    try:
        # Open the Facebook page
        driver.get(page)
        time.sleep(5)  # Wait for the page to load

        # Check if the Message button is available and click it
        try:
            message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']")))
            message_button.click()
        except Exception as e:
            print(f"No message option available for {page}: {e}")
            continue
            
        # Wait for the message window to open
        time.sleep(3)
        # Wait for any potential response (optional)
        response=check_for_new_messages()
        if response:
           split_response = [line.strip() for message in response for line in message.split("\n")]
           data =  {
            "ID" : page,
            "Response" : split_response
           }
           responses.append(data)
        else:
            print(f"No response received from {page} within the wait time.")
        
        # Clicking the close bubble chat button
        exit_button =  driver.find_element(By.XPATH,"//div[@aria-label='Close chat' and @role='button']")
        exit_button.click() # click on the button
    except Exception as e:
        print(f"An error occurred on page {page}: {e}")
print(responses)
with open("responses.json","w", encoding='utf-8') as file : 
     json.dump(responses,file,indent=4,ensure_ascii=False)
# Optional print statement for verification
print(f"All responses saved to responses.json: {responses}")
# Close the browser after operations are complete
driver.quit()