from playwright.sync_api import sync_playwright, expect
import time

def verify_mythos_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            # Navigate to the streamlit app
            page.goto("http://localhost:3000")

            # Wait for title
            expect(page.get_by_text("Centro de Control: Enjambre Polímata")).to_be_visible(timeout=15000)

            # Check for RL metrics
            expect(page.get_by_text("RL Action Selection")).to_be_visible(timeout=10000)

            # Check for Mythos Guard Status
            expect(page.get_by_text("Mythos Guard Status:")).to_be_visible(timeout=10000)

            # Wait for data to populate
            time.sleep(3)

            # Take screenshot
            page.screenshot(path="/home/jules/verification/mythos_agi_final.png", full_page=True)
            print("Screenshot saved to /home/jules/verification/mythos_agi_final.png")

        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path="/home/jules/verification/error_mythos.png")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_mythos_dashboard()
