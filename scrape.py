from selenium.webdriver import Remote, ChromeOptions
import time
from bs4 import BeautifulSoup

SBR_WEBDRIVER = 'https://brd-customer-hl_b91c48ff-zone-ai_scrape:qgjt104vpz3h@brd.superproxy.io:9515'


def scrape(website):
    print("Launching Browser ...")

    # Use ChromeOptions
    options = ChromeOptions()
    # Optional: run browser in headless mode
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    # Connect to remote WebDriver using command_executor
    with Remote(command_executor=SBR_WEBDRIVER, options=options) as driver:
        print(f'Connected! Navigating to {website} ...')
        driver.get(website)

        print('Navigated! Scraping page content...')
        html = driver.page_source

        return html


def body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script in soup(['script', 'style']):
        script.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content


def split_content(dom_content, max_length=6000):
    return [dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)]
