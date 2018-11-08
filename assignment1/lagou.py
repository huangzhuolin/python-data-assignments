from selenium import webdriver
import csv
import time

LAGOU_URL = 'https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput='
NUM_OF_PAGES = 10


def output_to_csv(data):
    """
    :param data: A list of dict
    :return: None
    """
    if len(data) == 0:
        return
    with open('data.csv', 'w', newline='') as f:
        first_item = data[0]
        fieldnames = first_item.keys()

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def parse_page(page):
    # TODO: Add try/catch control and use `yield`.
    elements = page.find_elements_by_class_name('con_list_item')
    return [parse_element(e) for e in elements]


def parse_element(element):
    """
    :param element:
    :return: a dict
    """
    title = element.find_element_by_tag_name('h3').text
    company = element.find_element_by_class_name('company_name').find_element_by_tag_name('a').text
    industry = element.find_element_by_class_name('industry').text
    salary = element.find_element_by_class_name('money').text
    description = element.find_element_by_class_name('li_b_r').text

    return {
        'title': title,
        'company': company,
        'salary': salary,
        'industry': industry,
        'description': description
    }


def waiting():
    time.sleep(5)


def nav_to_next(element):
    """
    Navigate to next page
    :param element: the browser object
    :return:
    """
    element.execute_script("window.scrollTo(0,3000);")
    element.find_element_by_class_name('pager_next').click()


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get(LAGOU_URL)
    articles = parse_page(browser)

    for _ in range(1, NUM_OF_PAGES):
        nav_to_next(browser)

        waiting()  # Wait until the page is fully loaded.
        articles += parse_page(browser)

    output_to_csv(articles)
