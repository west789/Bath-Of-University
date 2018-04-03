# -*- coding: utf-8 -*-
import scrapy
from Bath.items import HooliItem
import re
from Bath.middlewares import *
class BathSpider(scrapy.Spider):
    name = 'Bath_1'
    allowed_domains = ['bath.ac.uk']
    start_urls = ["http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-computer-science/",
                  "http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-conservation-of-historic-buildings/",
                  "http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-data-science/"
                  ]
    # base_url = "http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics/#course-structure"
    # last_list = ["/msc-applied-economics/#course-structure"]
    # for i in last_list:
    #     full_url = base_url + i
    #     start_urls.append(full_url)

    def parse(self, response):
        try:
            item = HooliItem()
            location = response.xpath("//dt[contains(text(), 'Location')]/following-sibling::dd[1]//text()").extract()
            location = ''.join(location).strip()
            department = response.xpath(
                "//dt[contains(text(), 'Department')]/following-sibling::dd[1]//text()").extract()
            department = ''.join(department)
            programme = response.xpath("//h1[@class='page-heading text-center reverse']//text()").extract()
            programme = re.sub('\s{3,}', ' ', ''.join(programme)).strip()
            degree_type = programme.split(' ')[-1]
            overview = response.xpath("//div[@class='markdown']//text()").extract()
            overview = re.sub("\s{3,}", " ", ''.join(overview))
            start_date = response.xpath(
                "//h1[@class='page-heading text-center reverse']/following-sibling::h2//text()").extract()
            start_date = re.sub('\s{3,}', ' ', ''.join(start_date))
            duration = response.xpath(
                "// h1[contains(text(), 'Course structure')]/following-sibling::p//text()").extract()
            duration = ''.join(duration)
            Modules_All = response.xpath("//section[@id='course-structure']//text()").extract()
            modules = re.sub('\s{3,}', '', ''.join(Modules_All))
            modules = re_group(r'Compulsory course units(?P<value>[\w\W]*)', modules)
            teaching_assessment = response.xpath("//section[@id='learning-assessment']//text()").extract()
            teaching_assessment = re.sub('\s{3,}', ' ', ''.join(teaching_assessment))
            teaching_assessment = re_group(r'Learning and assessment(?P<value>.*)',teaching_assessment)
            IELTS = response.xpath("//div[@class='section-content']/ul/li[1]//text()").extract()
            IELTS = ''.join(IELTS).replace('IELTS:', '').strip()
            TOEFL = response.xpath("//div[@class='section-content']/ul/li[3]//text()").extract()
            TOEFL = ''.join(TOEFL).replace('TOEFL IBT:', '').strip()
            deadline = response.xpath("//div[contains(text(),  'Overseas deadline')]/following-sibling::div//text()").extract()
            deadline = ''.join(deadline)
            other = response.xpath("//div[contains(text(),  'Application eligibility')]/following-sibling::div//text()").extract()
            other = ''.join(other).strip()
            rntry_requirements = response.xpath("//h1[contains(text(), 'United Kingdom qualifications')]/../../following-sibling::div[1]//text()").extract()
            rntry_requirements = ''.join(rntry_requirements).strip()
            chinese_requirement = response.xpath("//h1[contains(text(), 'China qualifications')]/../../following-sibling::div[1]//text()").extract()
            chinese_requirement = ''.join(chinese_requirement).strip()
            fee_geturl = response.xpath("//a[contains(text(), 'See the most')]").re(r'href="(.*?)"')[0]
            tuition_fee = fee_get(fee_geturl, programme, degree_type)
            university = 'University of Bath'
        except Exception as e:
            print("出现异常", e)
        item["university"]= university
        item['location'] = location
        item["department"] = department
        item["programme"] = programme
        item["degree_type"] = degree_type
        item["overview"] = overview
        item["start_date"] = start_date
        item["duration"] = duration
        item["modules"] = modules
        item['teaching_assessment'] = teaching_assessment
        item['IELTS'] = IELTS
        item["TOEFL"] = TOEFL
        item["deadline"] = deadline
        item["rntry_requirements"] = rntry_requirements
        item['chinese_requirement'] = chinese_requirement
        item["other"] = other
        yield item
