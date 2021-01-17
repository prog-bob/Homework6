def test_success_login(admin_page):
    admin_page.login('demo', 'demo')
    assert admin_page.driver.title == 'Dashboard'


def test_logout(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.logout()
    assert admin_page.driver.title != 'Dashboard'


def test_dropdown_catalog(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.click_catalog()


def test_dropdown_sales(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.click_sales()


def test_developer_settings(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.click_developer_settings()
