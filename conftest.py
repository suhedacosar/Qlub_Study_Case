from datetime import datetime
from pathlib import Path
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


BaseUrl = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/88/_/_/a604e595eb?lang=en"
Amount = "10"
Tip = "5"
CardNumber = "4242424242424242"
CardExpiredDate = "0226"
CardCvv = "100"
Password = "Checkout1!"
msg = "success"  # check success url contains


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chr_option = Options()
    chr_option.add_experimental_option("detach", True)
    chr_option.page_load_strategy = "none"
    # chr_option.add_argument("--headless")
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_option)
    request.cls.driver.maximize_window()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Qlub Test Report"

