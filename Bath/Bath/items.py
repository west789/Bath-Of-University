# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BathItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HooliItem(scrapy.Item):
    university = scrapy.Field()
    department = scrapy.Field()
    programme = scrapy.Field()
    degree_type = scrapy.Field()
    overview = scrapy.Field()
    ucas_code = scrapy.Field()
    start_date = scrapy.Field()
    mode = scrapy.Field()
    duration = scrapy.Field()
    modules = scrapy.Field()
    teaching_assessment = scrapy.Field()
    career = scrapy.Field()
    application_date = scrapy.Field()
    deadline = scrapy.Field()
    application_fee = scrapy.Field()
    entry_requirements = scrapy.Field()
    tuition_fee = scrapy.Field()
    IELTS = scrapy.Field()
    IELTS_L = scrapy.Field()
    IELTS_S = scrapy.Field()
    IELTS_R = scrapy.Field()
    IELTS_W = scrapy.Field()
    TOEFL = scrapy.Field()
    TOEFL_L = scrapy.Field()
    TOEFL_S = scrapy.Field()
    TOEFL_R = scrapy.Field()
    TOEFL_W = scrapy.Field()
    Alevel = scrapy.Field()
    IB = scrapy.Field()
    url = scrapy.Field()
    location = scrapy.Field()
    other = scrapy.Field()
    how_to_apply = scrapy.Field()
    description_degree = scrapy.Field()
    GPA = scrapy.Field()
    interview = scrapy.Field()
    portfolio = scrapy.Field()
    degree_level = scrapy.Field()
    city = scrapy.Field()
    website = scrapy.Field()
    country = scrapy.Field()
    teaching = scrapy.Field()
    rntry_requirements = scrapy.Field()
    chinese_requirement = scrapy.Field()
