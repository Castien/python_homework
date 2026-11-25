# Task 1: Check robots.txt to Ensure Policy Compliance
# In this assignment, you collect data from Books to Scrape, a demo bookstore site designed for practicing web scraping. 
# As always, before you scrape a site, you need to check whether a robots.txt file exists and review its contents.
# Try to open https://books.toscrape.com/robots.txt.
# You should find that this URL returns a "Not Found" page — the site has no robots.txt file. 
# When a site has no robots.txt, that means it places no restrictions on automated access. 
# Combined with the fact that the site explicitly states it is built for scraping practice, we can proceed.
# For comparison, try opening https://durhamcounty.bibliocommons.com/robots.txt. 
# This is a public library catalog that used to allow scraping, but now returns: 
# User-agent: * / Disallow: /, which means all automated access to all pages is disallowed. 
# Many library sites have added restrictions like this in response to heavy traffic from AI bots. 
# This is a good example of why checking robots.txt matters — a site's policy can change at any time.


# Task 2: Understanding HTML and the DOM for Books to Scrape
# You are going to find where in the HTML page the data you want is located.
# Open https://books.toscrape.com/.
# Open your browser developer tools to show the HTML elements. 
# For Chrome, this is Shift-Ctrl-J (or Shift-Cmd-J on Mac).
# Find the HTML element for a single book listing. 
# When you select an element in the Chrome developer tools, that part of the web page is highlighted. 
# Start by selecting elements and expanding them until you get to an individual book. 
# Hint: You are looking for an article element with a specific class. 
# Note the class value — your program will need it.
# Within that article element, find the element that contains the book's title. 
# Note two things: the tag type, and also look at the title attribute of the link inside it. 
# The displayed text on the page may be truncated, but the full title is stored in this attribute. 
# Save these details — your program will need them.
# Within the same article element, find the element that contains the book's price. 
# Note the tag type and its class value. Save it.
# Within the same article element, find the element that indicates the book's star rating. 
# This one is a little different — the rating is not stored as text content. 
# Instead, look at the class attribute of the element. 
# The rating (One, Two, Three, Four, or Five) is part of the class name itself. 
# Note this pattern — your program will need to extract it.


# Task 3: Write a Program to Extract this Data
# Note: There are several tools for web scraping in Python. 
# This assignment uses Selenium, which controls a real browser. 
# Selenium is especially useful for scraping sites that render content with JavaScript — 
# the browser executes the JavaScript before you extract data, so you see the same page a human visitor would. 
# Other tools like requests + BeautifulSoup work well for simpler pages that serve static HTML. 
# Books to Scrape is a static site, but we use Selenium here because most real-world sites rely on JavaScript, 
# and learning Selenium prepares you for those.
# Create a file called get_books.py. 
# The program should import from selenium and webdriver_manager. 
# You also need pandas and json.
# Add code to load the Books to Scrape homepage: https://books.toscrape.com/.
# Find all the article elements on the page for the book listings. 
# Use the class value you identified in Task 2 step 3. 
# Also use the tag name when you do the find, to make sure you get the right elements.
# Within your program, create an empty list called results. 
# You are going to add dict values to this list, one for each book.
# Main loop: Iterate through the list of article elements. 
# For each one:
# Find the element that contains the title. 
# The displayed text may be truncated, so get the full title from the title attribute of the link 
# (the a tag inside the heading). Use get_attribute('title') for this.
# Find the element that contains the price, and get its text.
# Find the element that contains the star rating. Since the rating is encoded in the class name 
# (for example, star-rating Three), you need to get the class attribute and extract the rating word from it.
# Create a dict that stores these three values with the keys Title, Price, and Rating. 
# Then append that dict to your results list.
# Create a DataFrame from this list of dicts. 
# Print the DataFrame.
# Hint: You can add small print statements at each step to check whether that part works. 
# For example, when you find all the article elements, print the length of the list to verify you get 20. 
# Then implement just the title extraction and print it. 
# Build the program incrementally.
# For Further Thought (Optional): The homepage shows 20 books, but the site has 1,000 books across 50 pages. 
# How would you get all the books from all pages? 
# Look at how the "next" button works and what the URL pattern looks like for each page. 
# Optional: Change your program to page through all the results. 
# However — you need to make sure your program pauses between pages. 
# Fast scraping, where many requests are sent in short order, is an abuse of the privilege, even on a site that welcomes scraping.


# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd
import json

# setting up Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# loading webpage
driver.get("https://books.toscrape.com/")

# finding book articles
articles = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
print(len(articles))

# create results list
results = []

# creating book info
for article in articles:
    title_element = article.find_element(By.CSS_SELECTOR, 'h3 a')
    title = title_element.get_attribute('title')
    price_element = article.find_element(By.CSS_SELECTOR, 'p.price_color')
    price = price_element.text
    rating_element = article.find_element(By.CSS_SELECTOR, 'p.star-rating')
    rating_class = rating_element.get_attribute('class')
    rating = rating_class.split()[-1]
    book = {"Title": title, "Price": price, "Rating": rating}
    results.append(book)

# creating and printing DataFrame
df = pd.DataFrame(results)
print(df)



# Task 4: Write out the Data
# Modify your program to do the following:
# Write the DataFrame to a file called get_books.csv, within the assignment8 folder. 
# Examine the file to see if it looks right.
# Write the results list out to a file called get_books.json, also within the assignment8 folder. 
# You should write it out in JSON format. Examine the file to see if it looks right.


# saving DataFrame to CSV
df.to_csv('get_books.csv', index=False)

# saving results to JSON
with open('get_books.json', 'w') as json_file: 
    json.dump(results, json_file, indent=4)

# closing to release session (from task 3)
driver.quit()

# Task 5: Ethical Web Scraping
# Goal: Understand the importance of ethical web scraping and robots.txt files.
# Access the robots.txt file for Wikipedia: Wikipedia Robots.txt.
# Analyze the file and answer the following questions. 
# Put your answers in a file called ethical_scraping.txt in your python_homework/assignment8 directory
# Which sections of the website are restricted for crawling?
# Are there specific rules for certain user agents?
# Reflect on why websites use robots.txt and write 2-3 sentences explaining its purpose and how it promotes ethical scraping. 
# Put these in ethical_scraping.txt in your python_homework/assignment8 directory.


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