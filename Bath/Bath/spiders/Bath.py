# -*- coding: utf-8 -*-
import scrapy
from Bath.items import HooliItem
import re
from Bath.middlewares import *
class BathSpider(scrapy.Spider):
    name = 'Bath'
    allowed_domains = ['bath.ac.uk']
    start_urls = [
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-advanced-quantitive-methods-in-social-science/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-clinical-psychology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-banking-and-financial-markets/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-behavioural-science/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-environmental-policy/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-economics-with-public-policy/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-applied-psychology-and-economic-behaviour/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-architectural-engineering-environmental-design/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-automotive-engineering/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-biosciences/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-biosciences/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-civil-engineering-innovative-structural-materials/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-computer-science/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-conservation-of-historic-buildings/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-data-science/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-data-science-including-placement-year/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-developmental-biology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-digital-entertainment-including-placement-year/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-digital-entertainment/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-drug-discovery/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-economics-and-finance/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-economics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-economics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-education/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-electrical-power-systems/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-electronic-systems-design/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-engineering-business-management/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-engineering-design/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-european-social-policy/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-evolutionary-and-population-biology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-evolutionary-biology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-global-political-economy/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-health-and-wellbeing/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-health-psychology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-human-computer-interaction/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-international-development/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-conflict-and-humanitarian-action/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-with-economics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-international-development-social-justice-and-sustainability/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-education-and-globalisation/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-relations-and-european-politics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-international-security/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-italian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-russian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-french-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-german-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-italian-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-italian-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-italian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-chinese/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-interpreting-and-translating-russian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-machine-learning-and-autonomous-systems-including-placement-year/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-machine-learning-and-autonomous-systems/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-mechatronics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-medical-biosciences/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-applications-of-mathematics/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-applications-of-mathematics-plus-6-month-placement-project/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-modern-building-design/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-molecular-microbiology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-molecular-microbiology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-molecular-plant-sciences/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-molecular-plant-sciences/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-politics-and-international-studies-full-time/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/pg-cert-professional-practice/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-protein-structure-and-function/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-protein-structure-and-function/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-psychology-full-time/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-regenerative-medicine/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-robotics-and-autonomous-systems-including-three-month-placement/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-robotics-and-autonomous-systems/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-security-conflict-and-human-rights/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-policy/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-social-work/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-sociology/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-software-systems/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-software-systems-including-placement-year/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/msc-sustainable-chemical-engineering/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/mres-sustainable-futures-full-time/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-teaching-english-to-speakers-of-other-languages/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-italian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-russian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-french-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-german-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-italian-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-german/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-italian/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-russian-and-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-and-professional-language-skills-spanish/',
        'http://www.bath.ac.uk/courses/postgraduate-2018/taught-postgraduate-courses/ma-translation-with-business-interpreting-chinese/'
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
            ucas_code = response.xpath("//dt[contains(text(), 'Course code')]/following-sibling::dd[1]//text()").extract()
            ucas_code = ''.join(ucas_code)
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
        item["ucas_code"] = ucas_code
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
        fee_geturl = response.xpath("//a[contains(text(), 'See the most')]").re(r'href="(.*?)"')[0]
        yield item
