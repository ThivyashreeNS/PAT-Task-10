# Extracting Instagram Follower and Following Counts

## Overview:
This script automates the process of extracting the follower and following counts from an Instagram profile using Selenium WebDriver.

## Table of Contents:
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Code Explanation](#Code-Explanation)
- [Running the test](#Running-the-test)

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `webdriver-manager`
 
 ## Installation:
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from  [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure
```
PAT Task 10/
│
├── Task_10.py                      # Contains the main logic for  interacting with Instagram using Selenium.
├── test_InstaCounts.py             # Contains the test case using pytest to checks if the follower and following counts are correctly extracted.
├── instaCounts.html                # Pytest html report
└── README.md                       # This README file
```

## Code Explanation
### Task_10.py
This script contains the main logic for automating the drag-and-drop task using Selenium.

- __Data class:__ Contains the url of the Instagram profile to scrape.

- __Locators class:__ Stores the XPath expressions for various elements on the Instagram profile page, such as the close button, the black ribbon, and the follower/following counts.

- __InstaCounts Class:__ The InstaCounts class handles the extraction of follower and following counts.

### Methods in `InstaCounts` class:
- __extract_counts():__
   - Initializes a Chrome WebDriver and opens the Instagram profile URL.

  - Handles waiting for and interacting with various page elements (closing modals and extracting the follower and following counts).

  - Returns the extracted counts as strings.

### test_InstaCounts.py:
- __test_extract_counts():__
  
  - Instantiate the InstaCounts class.

  - Call the extract_counts() method that returns the follower and following counts.

  -  It checks if the follower and following counts are correctly extracted.

## Running the test:
- The project uses pytest to test the extracted counts. To run the tests:
  
  - Make sure the project and dependencies are properly set up.

  - Run the following command to execute the test cases:
    ```
     pytest -v -s --capture=sys --html=Reports\instaCounts.html test_InstaCounts.py
    ```
    








        
