import pytest
import os
from utils.custom_logger import CustomLogger

logger = CustomLogger.get_logger()

@pytest.fixture(scope="function")
def ui_page(page):
    logger.info("Opening Browser Tab Context")
    base_url = "https://demoqa.com/"
    page.goto(base_url, wait_until="load")
    yield page
    logger.info("Closing Browser Page")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page') or item.funcargs.get('ui_page')
        
        if page:
            screenshots_dir = os.path.join(os.getcwd(), "logs", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}_FAILED.png")
            
            # 1. Save screenshot file on disk
            page.screenshot(path=screenshot_path)
            logger.error(f"Test FAILED! Screenshot saved: {screenshot_path}")

            # screenshot into HTML Report
            if pytest_html:
                html_media = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:600px;height:300px;" ' \
                             f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html_media))
                report.extra = extra