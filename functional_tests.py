from selenium import webdriver

browser = webdriver.Firefox(
    executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
browser.get("http://localhost:8000")

assert "Congratulations" in browser.title
