# Amizone Bot

### Amizone
Amizone is the online portal for the students of Amity University to get all academics related information like attendance, results and the list of lectures for the day.
### The problem
The site is very slow and even after signing in it shows multiple pop ups. Since I've to check it multiple times a day repeating the entire process gets very tedious and annoying.
### The solution
To tackle this problem I wrote a python script using the **Selenium library** to automatically load the site in *headless mode*, which is a functionality that allows the execution of a full version of the latest Chrome browser while controlling it programmatically and it runs without a GUI.

Currently it can do 3 things based on the input given,
  1. show list of lectures for the current day
  2. show list of lectures for the next day
  3. show attendance in each subject

Since the program runs without a GUI and minimal user input it saves a lot of time and the user can easily do other tasks while the program runs.

### Prerequisites
* Selenium

    ```
       pip3 install selenium
    ```
* Chrome Driver

  https://chromedriver.chromium.org

