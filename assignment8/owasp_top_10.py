

# Task 6: Scraping Structured Data
# Goal: Extract a web page section and store the information.
# Use your browser developer tools to view this page: https://owasp.org/www-project-top-ten/.  
# You are going to extract the top 10 security risks reported there.  
# Figure out how you will find them.
# Within your python_homework/assignment8 directory, write a script called owasp_top_10.py.  
# Use selenium to read this page.
# Find each of the top 10 vulnerabilities.  
# Hint: You will need XPath.  
# For each of the top 10 vulnerabilities, keep the vulnerability title and the href link in a dict.  
# Accumulate these dict objects in a list.
# Print out the list to make sure you have the right data.  
# Then, add code to the program to write it to a file called owasp_top_10.csv.  
# Verify that this file appears correct.
# Create a file, challenges.txt, also within your assignment 8 directory.  
# In this file, describe any challenges you faced in completing this assignment and how you resolved them.


# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import csv

# setting up Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # loading webpage
    driver.get("https://top10.owasp.org/2025/")

    # Find the Top 10:2025 List heading
    heading = driver.find_element(By.ID, "top-102025-list")

    # Find the ordered list immediately following the heading
    vulnerability_list = heading.find_element(By.XPATH, 'following-sibling::ol[1]')

    # collecting links from list
    link_elements = vulnerability_list.find_elements(By.CSS_SELECTOR, 'a')

    # storing the vulnerability names and URLs
    vulnerabilities = []

    # looping through links, appending title and href in a dict
    for link in link_elements:
        name = link.text.strip()
        url = link.get_attribute("href")
        if name and url:
            vulnerabilities.append({"name": name, "url": url})

    # printing list
    print(vulnerabilities)

    # saving results to CSV
    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])

        for vulnerability in vulnerabilities:
            writer.writerow([vulnerability["name"],vulnerability["url"]])

    # checking for count
    print(f"\nSuccessfully saved {len(vulnerabilities)} vulnerabilities.")

# raises this exception if nothing matches
except NoSuchElementException as e:
    print("Could not find the expected elements:", e)

# closing to release session
finally:
    driver.quit()

