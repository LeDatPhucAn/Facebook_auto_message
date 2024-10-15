from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

import time
import random
# List of Facebook page URLs for sending messages
facebook_pages = [
    
    'https://www.facebook.com/tienganhnghenoi/', #sample facebook page


]
# List to keep track of successfully messaged pages
successfully_messaged_pages = []

# File to store the list of successfully messaged pages (can be read later)
log_file = "messaged_pages_log.txt"

# Function to log successfully messaged pages to a file
def log_success(page):
    # Get current time
    current_time = datetime.now().time()
    successfully_messaged_pages.append(page)
    with open(log_file, 'a') as file:
        file.write(page + '\n')
    print(f"Successfully logged {page} to {log_file} at",current_time)

# Function to read already messaged pages (in case the script is interrupted and resumed later)
def read_logged_pages():
    try:
        with open(log_file, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to log the failure
def log_failure(page):
    with open(log_file, 'a') as file:
        file.write(f"Failed to send message on {page}\n")
    print(f"Logged failure for {page}")

# Initialize the WebDriver with your Chrome user profile
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:Your Chrome Path here")  # Adjust path
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Sample messages
message_versions = [
    [
    "Em quan tâm đến các khóa học tiếng Anh của trung tâm và muốn tìm hiểu thêm một số thông tin ạ.",
    "Trung tâm có dạy lớp nhóm, 1 kèm 1, hay cả hai?",
    "Trung tâm có bao nhiêu chi nhánh tại Việt Nam?",
    "Trung tâm có những khóa học nào?",
    "Số học viên mỗi lớp là bao nhiêu?",
    "Trung tâm có những cấp độ nào?",
    "Một khóa học kéo dài bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cung cấp chi tiết giá cho từng khóa học và dịch vụ không?",
    "Giáo viên là người nước ngoài hay người Việt Nam?",
    "Điểm IELTS và TESOL trung bình của giáo viên là bao nhiêu?",
    "Cảm ơn trung tâm rất nhiều! Em mong là được nhận được câu trả lời qua tin nhắn ạ.",
],
# Version 2
[
    "Em đang quan tâm đến các khóa học tiếng Anh của trung tâm và muốn được tư vấn thêm thông tin ạ.",
    "Trung tâm có tổ chức lớp học nhóm, 1 kèm 1 hay cả hai loại hình không ạ?",
    "Hiện tại, trung tâm có bao nhiêu chi nhánh tại Việt Nam?",
    "Trung tâm đang có các khóa học nào vậy ạ?",
    "Mỗi lớp học trung bình có bao nhiêu học viên tham gia ạ?",
    "Trung tâm có các khóa học theo cấp độ nào?",
    "Một khóa học kéo dài trong thời gian bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể gửi chi tiết về giá của các khóa học và dịch vụ được cung cấp không ạ?",
    "Các giáo viên của trung tâm là người nước ngoài hay người Việt Nam?",
    "Điểm IELTS và TESOL trung bình của giáo viên tại trung tâm là bao nhiêu?",
    "Cảm ơn trung tâm nhiều! Em mong nhận được phản hồi qua tin nhắn ạ.",
],
# Version 3
[
    "Em đang tìm hiểu về các khóa học tiếng Anh của trung tâm và mong muốn được tư vấn thêm ạ.",
    "Trung tâm có mở lớp học theo hình thức nhóm, 1 kèm 1, hay cả hai không ạ?",
    "Trung tâm có bao nhiêu chi nhánh tại Việt Nam?",
    "Trung tâm hiện đang cung cấp các khóa học gì ạ?",
    "Số lượng học viên tham gia trong mỗi lớp là bao nhiêu vậy ạ?",
    "Trung tâm phân chia các khóa học theo cấp độ nào?",
    "Một khóa học thông thường kéo dài bao lâu và có bao nhiêu buổi (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cho em biết chi tiết về giá từng khóa học và dịch vụ không ạ?",
    "Giáo viên giảng dạy là người Việt Nam hay người nước ngoài ạ?",
    "Trung bình giáo viên tại trung tâm có điểm IELTS và TESOL là bao nhiêu?",
    "Cảm ơn trung tâm nhiều! Em rất mong nhận được phản hồi qua tin nhắn ạ.",
],
# Version 4
[
    "Em muốn tìm hiểu thêm về các khóa học tiếng Anh của trung tâm và rất mong được cung cấp thêm thông tin ạ.",
    "Trung tâm có dạy lớp học theo nhóm, 1 kèm 1 hay cả hai loại hình không ạ?",
    "Trung tâm hiện có bao nhiêu chi nhánh trên toàn quốc ạ?",
    "Những khóa học nào đang được trung tâm cung cấp hiện nay?",
    "Số lượng học viên mỗi lớp học trung bình là bao nhiêu?",
    "Trung tâm phân chia khóa học thành những cấp độ nào?",
    "Thời gian kéo dài của một khóa học là bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể gửi em bảng giá chi tiết cho từng khóa học và dịch vụ không ạ?",
    "Giáo viên của trung tâm là người Việt Nam hay người nước ngoài ạ?",
    "Điểm IELTS và TESOL trung bình của giáo viên tại trung tâm là bao nhiêu ạ?",
    "Cảm ơn trung tâm rất nhiều! Em hy vọng sẽ nhận được phản hồi qua tin nhắn ạ.",
],
# Version 5
[
    "Em rất quan tâm đến các khóa học tiếng Anh của trung tâm và mong muốn được cung cấp thêm thông tin chi tiết ạ.",
    "Trung tâm có mở các lớp học theo hình thức nhóm, 1 kèm 1, hay kết hợp cả hai không ạ?",
    "Hiện tại, trung tâm có bao nhiêu chi nhánh ở Việt Nam?",
    "Trung tâm hiện đang cung cấp những khóa học nào?",
    "Số lượng học viên tham gia mỗi lớp học là bao nhiêu ạ?",
    "Trung tâm có chia các khóa học theo cấp độ nào không ạ?",
    "Một khóa học thường kéo dài trong bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cho em biết chi tiết giá của từng khóa học và dịch vụ không ạ?",
    "Các giáo viên của trung tâm là người nước ngoài hay người Việt Nam vậy ạ?",
    "Trung bình giáo viên của trung tâm có điểm IELTS hoặc TESOL là bao nhiêu ạ?",
    "Em cảm ơn trung tâm rất nhiều và mong sớm nhận được phản hồi qua tin nhắn ạ.",
],
# Version 6
[
    "Em đang muốn tìm hiểu thêm về các khóa học tiếng Anh của trung tâm, rất mong trung tâm cung cấp thêm thông tin giúp em ạ.",
    "Trung tâm có các khóa học theo hình thức lớp nhóm, 1 kèm 1, hay cả hai loại hình không ạ?",
    "Trung tâm có tất cả bao nhiêu chi nhánh tại Việt Nam?",
    "Những khóa học mà trung tâm đang cung cấp hiện tại là gì ạ?",
    "Trung bình mỗi lớp học có bao nhiêu học viên tham gia?",
    "Trung tâm có phân cấp các khóa học theo cấp độ hay không ạ?",
    "Một khóa học thông thường sẽ kéo dài bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể gửi cho em bảng giá chi tiết của các khóa học và dịch vụ không ạ?",
    "Các giáo viên giảng dạy tại trung tâm là người nước ngoài hay người Việt Nam ạ?",
    "Điểm IELTS và TESOL của giáo viên tại trung tâm trung bình là bao nhiêu ạ?",
    "Cảm ơn trung tâm rất nhiều! Em rất mong được nhận phản hồi từ trung tâm qua tin nhắn ạ.",
],
# Version 7
[
    "Em muốn biết thêm thông tin về các khóa học tiếng Anh của trung tâm, rất mong được hỗ trợ thêm ạ.",
    "Trung tâm có tổ chức các lớp học nhóm và 1 kèm 1 không ạ? Hoặc có cả hai loại hình?",
    "Hiện nay, trung tâm có bao nhiêu chi nhánh tại Việt Nam?",
    "Trung tâm hiện đang cung cấp những khóa học nào?",
    "Số lượng học viên tham gia mỗi lớp học là bao nhiêu vậy ạ?",
    "Trung tâm có phân chia khóa học theo cấp độ nào không ạ?",
    "Một khóa học kéo dài bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cho em biết chi tiết về giá cho từng khóa học và các dịch vụ được cung cấp không?",
    "Giáo viên tại trung tâm là người Việt Nam hay người nước ngoài?",
    "Điểm trung bình của giáo viên tại trung tâm là bao nhiêu với các chứng chỉ như IELTS và TESOL?",
    "Cảm ơn trung tâm rất nhiều! Em mong nhận được phản hồi qua tin nhắn ạ.",
],
# Version 8
[
    "Em đang muốn tìm hiểu các thông tin về các khóa học tiếng Anh của trung tâm, rất mong được tư vấn thêm ạ.",
    "Trung tâm có dạy lớp học theo nhóm hay 1 kèm 1, hoặc cả hai không ạ?",
    "Trung tâm hiện có bao nhiêu chi nhánh tại Việt Nam?",
    "Những khóa học nào đang được trung tâm cung cấp hiện nay?",
    "Số lượng học viên trung bình trong mỗi lớp học là bao nhiêu?",
    "Trung tâm có các cấp độ học như thế nào?",
    "Thời gian một khóa học là bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể gửi bảng giá chi tiết cho từng khóa học và dịch vụ được không?",
    "Giáo viên giảng dạy tại trung tâm là người Việt hay người nước ngoài?",
    "Điểm IELTS và TESOL trung bình của giáo viên tại trung tâm là bao nhiêu?",
    "Cảm ơn trung tâm nhiều! Em hy vọng sẽ sớm nhận được phản hồi qua tin nhắn ạ.",
],
# Version 9
[
    "Em đang có nhu cầu tìm hiểu về các khóa học tiếng Anh tại trung tâm, rất mong được tư vấn thêm thông tin ạ.",
    "Trung tâm có tổ chức các lớp nhóm và 1 kèm 1 không? Hay có cả hai loại hình?",
    "Trung tâm có bao nhiêu chi nhánh ở Việt Nam ạ?",
    "Trung tâm hiện tại đang cung cấp các khóa học nào?",
    "Mỗi lớp học có trung bình bao nhiêu học viên tham gia?",
    "Trung tâm phân loại các khóa học theo cấp độ như thế nào?",
    "Một khóa học kéo dài bao nhiêu thời gian và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cung cấp bảng giá chi tiết cho từng khóa học và dịch vụ được không?",
    "Giáo viên của trung tâm là người nước ngoài hay người Việt Nam?",
    "Điểm IELTS và TESOL trung bình của giáo viên là bao nhiêu ạ?",
    "Em rất cảm ơn trung tâm và mong sớm nhận được phản hồi qua tin nhắn ạ.",
],
# Version 10
[
    "Em muốn tìm hiểu thêm về các khóa học tiếng Anh của trung tâm và mong được cung cấp thêm thông tin chi tiết ạ.",
    "Trung tâm có cung cấp các khóa học nhóm và 1 kèm 1 không ạ? Hoặc có cả hai hình thức?",
    "Trung tâm có tất cả bao nhiêu chi nhánh trên khắp Việt Nam?",
    "Hiện trung tâm đang cung cấp các khóa học nào?",
    "Số lượng học viên tham gia trong mỗi lớp học trung bình là bao nhiêu?",
    "Trung tâm chia khóa học theo những cấp độ nào?",
    "Một khóa học kéo dài trong bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể gửi em bảng giá chi tiết cho từng khóa học và các dịch vụ được không ạ?",
    "Giáo viên tại trung tâm là người nước ngoài hay người Việt Nam?",
    "Trung bình giáo viên tại trung tâm đạt điểm IELTS và TESOL là bao nhiêu?",
    "Cảm ơn trung tâm rất nhiều! Em mong nhận được câu trả lời qua tin nhắn ạ.",
],
# Version 11
[
    "Em quan tâm đến các khóa học tiếng Anh của trung tâm và muốn tìm hiểu kỹ hơn về thông tin ạ.",
    "Trung tâm có tổ chức các lớp học nhóm và 1 kèm 1 không ạ? Hay cả hai?",
    "Trung tâm hiện có bao nhiêu chi nhánh tại Việt Nam?",
    "Trung tâm hiện đang có những khóa học nào?",
    "Số học viên trung bình trong mỗi lớp học là bao nhiêu?",
    "Trung tâm có chia khóa học theo các cấp độ không ạ?",
    "Một khóa học thường kéo dài bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cung cấp bảng giá chi tiết cho từng khóa học và dịch vụ không ạ?",
    "Giáo viên của trung tâm là người nước ngoài hay người Việt Nam?",
    "Điểm trung bình của giáo viên tại trung tâm là bao nhiêu về IELTS và TESOL?",
    "Cảm ơn trung tâm rất nhiều! Em mong nhận được phản hồi qua tin nhắn ạ.",
],
# Version 12
[
    "Em muốn tìm hiểu về các khóa học tiếng Anh của trung tâm, mong được cung cấp thêm thông tin chi tiết ạ.",
    "Trung tâm có các lớp học theo nhóm và 1 kèm 1 không ạ? Hoặc có cả hai?",
    "Trung tâm hiện có bao nhiêu chi nhánh trên cả nước?",
    "Trung tâm hiện đang cung cấp những khóa học nào ạ?",
    "Số lượng học viên trong mỗi lớp học là bao nhiêu vậy ạ?",
    "Trung tâm có phân chia các khóa học theo các cấp độ học khác nhau không?",
    "Thời gian kéo dài của một khóa học là bao lâu và có bao nhiêu buổi học (ví dụ: 3 tháng, 24 buổi)?",
    "Trung tâm có thể cho em biết bảng giá chi tiết cho từng khóa học và các dịch vụ không ạ?",
    "Giáo viên giảng dạy tại trung tâm là người Việt hay người nước ngoài ạ?",
    "Điểm IELTS và TESOL trung bình của giáo viên tại trung tâm là bao nhiêu?",
    "Cảm ơn trung tâm rất nhiều! Em rất mong sớm nhận được phản hồi qua tin nhắn ạ.",
],

]

# Function to simulate human typing
def slow_typing(element, text, delay_range=(0.09, 0.15)):
    actions = ActionChains(driver)
    for char in text:
        actions.send_keys(char)
        actions.perform()
        time.sleep(random.uniform(*delay_range))  # Random typing speed between each character


# Random delay between actions
def random_delay(min_seconds=3, max_seconds=5):
    delay = random.uniform(min_seconds, max_seconds)
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

def random_scroll():
    scroll_distance = random.randint(100, 1000)  # Scroll distance in pixels
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    random_delay(2, 5)  # Add a delay after scrolling

def random_mouse_move(driver, element=None):
    actions = ActionChains(driver)
    if element:
        actions.move_to_element(element)
    else:
        # Move to a random point on the page
        width, height = driver.execute_script("return [window.innerWidth, window.innerHeight];")
        x = random.randint(0, width)
        y = random.randint(0, height)
        actions.move_by_offset(x, y)
    actions.perform()
    random_delay(1, 3)

def random_click(element):
    random_delay(2, 5)  # Random delay before clicking
    element.click()

def add_typo(text):
    if random.random() <= 0.1:  # 10% chance of adding a typo
        typo_index = random.randint(0, len(text) - 1)
        return text[:typo_index] + random.choice('abcdefghijklmnopqrstuvwxyz') + text[typo_index + 1:]
    return text
def simulate_mistake():
    if random.random() <= 0.05:  # 5% chance of making a mistake
        print("Simulating mistake: refreshing the page.")
        driver.refresh()
        random_delay(4, 6)  # Delay after the "mistake"
# Check which pages have already been messaged
already_messaged_pages = read_logged_pages()

# Filter out pages that have already been messaged
pages_to_message = [page for page in facebook_pages if page not in already_messaged_pages]

# Open each Facebook page and attempt to send a random version of the message
for page in facebook_pages:
    try:
        random_scroll()  # Random scroll before
        driver.get(page)
        random_delay(4, 6)  # Wait for the page to load

        simulate_mistake()  # Occasionally simulate a mistake

        # Check if the Message button is available and click it
        try:
            random_delay(2, 5)  # Random delay before clicking
            message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']"))) # might be 'message'
            random_click(message_button)
        except Exception as e:
            print(f"No 'Message' button available for {page}: {e}")
            continue

        random_scroll()  # Random scroll after clicking the Message button
        random_delay(3,5)
        # Check if there is a "Get Started" button and click it
        try:
            get_started_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Get Started']"))) # might be 'Get_started'
            random_click(get_started_button)
            print(f"Clicked 'Get Started' button on {page}")
            random_delay(2, 5)
        except Exception:
            print(f"No 'Get Started' button found for {page}. Proceeding with messaging...")
                # Select a random version of messages to send
        random_version = random.choice(message_versions)

        # Send each message in the selected version with simulated typing and random delays
        try:
            for word in random_version:
                message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message']"))) # might be 'message'
                slow_typing(message_box, add_typo(word))  # Simulate typing with small variations
                enter_button = driver.find_element(By.XPATH, "//div[@aria-label='Press Enter to send']") # migth be 'Press enter to send'
                random_click(enter_button)  
            
            # Log the successful page
            log_success(page)

        except Exception as e:
            print(f"Error sending message to {page}: {e}")
                        # Log the successful page

        exit_button =  driver.find_element(By.XPATH, "//div[@aria-label='Close chat']") # might be 'close chat'
        exit_button.click() # click on the button
        # Wait for a short period before moving to the next page
        time.sleep(7)

    except Exception as e:
        print(f"An error occurred on page {page}: {e}")

# Close the browser after operations are complete
driver.quit()