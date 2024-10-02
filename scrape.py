from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
import time
from bs4 import BeautifulSoup

SBR_WEBDRIVER = 'https://brd-customer-hl_b91c48ff-zone-ai_scrape:qgjt104vpz3h@brd.superproxy.io:9515'


def scrape(website):
    print("Lunch Browser ...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print(f'Connected! Navigating to {website} ...')
        driver.get(website)
        # print('Waiting captcha to solve ...')
        # solve_res = driver.execute('executeCdpCommand', {
        #     'cmd': 'Captcha.waitForSolve',
        #     'params': {'detectTimeout': 10000},
        # })
        # print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source

        return html


def html_body(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""
