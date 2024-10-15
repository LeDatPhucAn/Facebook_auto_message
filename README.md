## Prerequisites
1. You must log into your Facebook account in Google Chrome beforehand.
2. Close Google Chrome before activating the code.

## Guidelines

### 1. Customizable Areas in `Automessage.py`
- **Facebook_pages:** Insert the Facebook profile or page links that you want to message.
- **Chrome Profile Path:** Find `options.add_argument("user-data-dir=C:Your Chrome Path here")` and replace "Your Chrome Path here" with your actual Chrome path (found by typing `chrome://version` in the Chrome search bar and copying the Profile Path).
- **message_versions:** Insert the different versions of the messages you want to send. Separate each message version with square brackets `[ ]`. There are examples in the code.
- **random_delay(a,b) and time.sleep(x):** Adjust these numbers for delays based on your preferences. `a` and `b` are the time range for random delays, and `x` is the specific delay time.

### 2. Gathering Responses
- Open the `Response.py` file.
- Insert the Facebook pages you want to retrieve responses from.
- Run the program.
- Responses will be saved in `responses.json`.

## Potential Errors
If the script doesn't click the message or close chat button correctly, you can adjust the following XPATH elements in the code:

- **Message Button:**
  ```python
  message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']"))) 
  # might need to change 'Message' to 'message'
