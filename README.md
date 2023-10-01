# Python-Selenium-Pytest
## Pre Requirements
* Python

## Setup Your Working Enviorment with terminal 
* pip install selenium
* pip install pytest
* pip install pytest-html
* pip install webdriver-manager

## For Report And Parallel Tests
* pip install pytest-html
* pip install pytest-xdist
* pip install pytest-parallel

## How to Run
To get only report:
* pytest -v     
To get report and run parallel tests (n= test cases)
* pytest -v -n=2

## About Structure
* You can configure credentials from conftest.fy
* You can find reports under reports directory and reachable from terminal

## Report Preview:
![Screenshot 2023-10-01 at 17.26.51.png](..%2F..%2FDesktop%2FScreenshot%202023-10-01%20at%2017.26.51.png)