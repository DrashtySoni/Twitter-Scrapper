# Twitter-Scrapper
Advanced techniques to scrape user data efficiently

## Prerequisites

Before you begin, you’ll need a local copy of Python installed on your system. The latest stable distribution will work (which, at the time of writing this article, is `3.11.2`).

Once you have Python installed, you need to install the following dependencies via pip, Python’s official package manager:
1. Selenium
2. Webdriver Manager

You can run the following commands to install the dependencies:
```
pip install selenium
pip install webdriver_manager
```
Run the code:
```
python profile-page.py
```
## Code Explanation
This code is a Python script designed to scrape information from Twitter user profiles using Selenium and parallelism. Let's break down its main functionalities step by step:

### Importing Necessary Libraries:

* The `time` module is used for introducing delays in the script.
* `concurrent.futures` provides the `ThreadPoolExecutor` class, which enables parallel execution of functions.
* `webdriver` and related modules from the `selenium` package are used for web automation.
* `ChromeDriverManager` from `webdriver_manager.chrome` is used to manage the Chrome driver installation.

### Defining the Usernames:

* A list named `usernames` is defined with one or more Twitter usernames that you want to scrape.

### Defining the scrape_profile Function:

* This function takes a `username` as an argument and performs the scraping for that user's profile.
* It constructs the URL for the given username's Twitter profile.
* Sets up a new Chrome WebDriver instance using the ChromeDriverManager and loads the profile URL.
* Waits for the webpage to load using `WebDriverWait` and the CSS selector for a tweet element as an indicator of page readiness.
* If the tweets don't appear within the timeout, a message is printed, and the WebDriver is closed.
* The function then proceeds to extract various information from the profile using CSS selectors and XPath, similar to the original code. The information includes the user's name, bio, location, website, join date, following count, followers count, and tweets.
* The collected information is printed for the user's profile.
* Finally, the WebDriver instance is closed to release the resources.

### Setting Maximum Number of Workers:

* The variable `max_workers` is set to determine the maximum number of parallel threads (workers) that will be used to scrape profiles concurrently. You can adjust this value based on your system's capacity.

### Using Parallelism with ThreadPoolExecutor:

* A `ThreadPoolExecutor` is created using the defined max_workers value. It manages the parallel execution of the scrape_profile function for each username in the list.
* `The executor.map` method is used to distribute the usernames across the available workers and execute the scraping concurrently.

### Introducing Delay for Rate Management:

* After all usernames have been scraped by the parallel workers, a delay of 180 seconds (3 minutes) is introduced to manage the overall scraping rate. This helps in controlling the requests per hour as required.
