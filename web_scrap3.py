from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from collections import Counter
import re

# URL of the homepage
URL_homepage = "https://www.dailymotion.com/in"

# Set up the Selenium WebDriver for the homepage
driver_homepage = webdriver.Chrome()
driver_homepage.get(URL_homepage)
driver_homepage.implicitly_wait(10)

# Directly navigate to "https://www.dailymotion.com/tseries2"
driver_homepage.get("https://www.dailymotion.com/tseries2")

# Wait for the page to load after navigating
time.sleep(5)  # Adjust the time as needed

# Scroll down to load more content
for _ in range(10):  # You can adjust the number of times to scroll
    driver_homepage.find_element("tag name", "body").send_keys(Keys.END)
    time.sleep(2)  # Adjust the time as needed

# Get the page source after JavaScript execution on the new page
html_tseries2 = driver_homepage.page_source

# Parse the HTML content with BeautifulSoup
soup_tseries2 = BeautifulSoup(html_tseries2, "html.parser")

# Find all links with href attribute on the new page
print("Finding video links on https://www.dailymotion.com/tseries2...")
video_urls = []
count = 1
for a_href in soup_tseries2.find_all("a", href=True):
    if "/video/" in a_href["href"]:
        match = re.search(r'/video/([a-zA-Z0-9_-]+)', a_href["href"])
        if match:
            video_id = match.group(1)
            video_urls.append(video_id)
            print(video_id + '-->' + str(count))
            count = count + 1
            if len(video_urls) == 50:
                break

# Close the Selenium WebDriver for the homepage
driver_homepage.quit()
print("Browser for the homepage closed.")

# Concatenate all video IDs into a single string
all_video_ids_string = ''.join(video_urls)

# Count the occurrences of each character
character_counts = Counter(all_video_ids_string)

# Find the most frequent English alphabet and its frequency
english_alphabets = [char for char in all_video_ids_string if char.isalpha()]
most_frequent_alphabet, frequency = Counter(english_alphabets).most_common(1)[0]

# Print the results
print(f"The most frequent English alphabet is '{most_frequent_alphabet}' with a frequency of {frequency}.")
