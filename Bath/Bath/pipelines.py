# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class BathPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect('localhost', 'root', '123456', 'test', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接数据库失败：%s' % str(e))

    def close(self):
        self.cursor.close()
        self.conn.close()


class MyprojectPipeline (MysqlDB):
    def process_item(self, item, spider):
        # sql = 'insert into info2(university, department, programme, degree_type, overview, start_date, duration'\
        #       'modules, teaching_assessment)'\
        #       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ' \
            # 'on duplicate key update department = values (department),modules = values (modules),entry_requirements = values(entry_requirements),location = values(location),programme = values(programme),degree_type = values(degree_type),tuition_fee= values(tuition_fee),duration= VALUES (duration),start_date=VALUES (start_date),IELTS=VALUES (IELTS),TOEFL = values(TOEFL),start_date=VALUES (start_date)'
        sql = 'insert into tmp_school_major_uk(university, location, department, programme, degree_type, overview, ucas_code,' \
              'start_date, duration, ' \
              'modules, teaching_assessment, IELTS, TOEFL, deadline, entry_requirements, chinese_requirements, other)VALUES' \
              '  (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (item["university"], item['location'], item["department"], item["programme"], item["degree_type"],
                                      item["overview"], item["ucas_code"], item["start_date"], item["duration"], item["modules"], item['teaching_assessment'],
                                      item['IELTS'], item["TOEFL"], item["deadline"], item["rntry_requirements"], item['chinese_requirement'], item["other"]))
            #     item["overview"], item["start_date"], item["duration"],))
            # self.cursor.execute(sql, (
            #     item["university"]
            #     , item["department"], item["programme"], item["degree_type"],
            #     item["overview"], item["start_date"], item["duration"],
            #     item["modules"], item['teaching_assessment']
            # ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")

        return item

