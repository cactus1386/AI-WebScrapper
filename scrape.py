import requests
from bs4 import BeautifulSoup


SBR_WEBDRIVER = 'https://brd-customer-hl_b91c48ff-zone-ai_scrape:qgjt104vpz3h@brd.superproxy.io:9515'


def scrape_website(website):
    print("Sending request to website...")
    response = requests.get(website)

    if response.status_code == 200:
        print("Website successfully fetched!")
        return response.text
    else:
        print(
            f"Failed to retrieve website. Status code: {response.status_code}")
        return ""


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
