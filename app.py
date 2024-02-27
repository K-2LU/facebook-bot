from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright, data) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # login page 
    page.goto("https://www.facebook.com/")
    page.wait_for_load_state('networkidle')
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("") # email
    page.get_by_test_id("royal_email").press("Tab")
    page.get_by_test_id("royal_pass").fill("")  # pass
    page.get_by_test_id("royal_pass").press("Enter")
    
    # cse 19 group
    page.goto("https://www.facebook.com/groups/2700477860050619")
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="Write something...").click()
    page.wait_for_load_state('networkidle')
    page.get_by_label("Write something...").fill(data)
    page.get_by_label("Post", exact=True).click()
    page.wait_for_load_state('networkidle')
    time.sleep(10)
    
    # droppers group
    page.goto('https://www.facebook.com/groups/droppers.group.cse.sust')
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="Write something...").click()
    page.wait_for_load_state('networkidle')
    page.get_by_label("Write something...").fill(data)
    page.get_by_label("Post", exact=True).click()
    time.sleep(10)
    # ---------------------
    context.close()
    browser.close()

def main():

    # read data.txt
    str = open("data.txt", "r")
    str = str.read()
    print(str)

    with sync_playwright() as playwright:
        run(playwright, str)

if __name__ == "__main__":
    main()