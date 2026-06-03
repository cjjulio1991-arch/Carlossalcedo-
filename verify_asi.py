from playwright.sync_api import sync_playwright
import time

def verify_asi_hive(page):
    time.sleep(5)
    page.goto("http://localhost:3000")
    page.wait_for_selector("text=ASI Hive")
    page.screenshot(path="/home/jules/verification/asi_hive_final.png", full_page=True)
    print("ASI Hive screenshot saved.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 2400})
        try:
            verify_asi_hive(page)
        finally:
            browser.close()
