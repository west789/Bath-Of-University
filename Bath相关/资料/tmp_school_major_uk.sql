/*
Navicat MySQL Data Transfer

Source Server         : mydata
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : hooli

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2018-03-29 11:15:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tmp_school_major_uk
-- ----------------------------
DROP TABLE IF EXISTS `tmp_school_major_uk`;
CREATE TABLE `tmp_school_major_uk` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `university` varchar(100) DEFAULT NULL COMMENT '学校名称',
  `country` varchar(100) DEFAULT NULL COMMENT '国家',
  `location` varchar(100) DEFAULT NULL COMMENT '专业城市',
  `website` varchar(255) DEFAULT NULL COMMENT '学校官网',
  `department` varchar(255) DEFAULT NULL COMMENT '学院/院系',
  `programme` varchar(255) DEFAULT NULL COMMENT '专业名称',
  `degree_level` int(11) DEFAULT NULL COMMENT '学位阶段',
  `degree_type` varchar(100) DEFAULT '' COMMENT '学位类型',
  `ucas_code` varchar(255) DEFAULT NULL COMMENT '本科专业ucascode',
  `application_date` varchar(255) DEFAULT NULL COMMENT '申请日期',
  `deadline` varchar(255) DEFAULT NULL COMMENT '截止日期',
  `start_date` varchar(100) DEFAULT NULL COMMENT '开学日期',
  `overview` text COMMENT '专业描述',
  `duration` varchar(255) DEFAULT NULL COMMENT '课程长度',
  `modules` text COMMENT '课程设置',
  `application_fee` varchar(255) DEFAULT NULL COMMENT '申请费用',
  `tuition_fee` varchar(255) DEFAULT NULL COMMENT '学费',
  `teaching_assessment` text COMMENT '授课方式&评估方式介绍',
  `career` text COMMENT '就业方向',
  `entry_requirements` text COMMENT '入学要求',
  `chinese_requirements` text COMMENT '入学要求',
  `Alevel` varchar(255) DEFAULT NULL COMMENT 'Alevel成绩要求',
  `IB` varchar(255) DEFAULT NULL COMMENT 'IB成绩要求',
  `IELTS` varchar(255) DEFAULT NULL COMMENT 'IELTS成绩要求',
  `IELTS_L` varchar(255) DEFAULT NULL COMMENT 'IELTS成绩要求',
  `IELTS_S` varchar(255) DEFAULT NULL COMMENT 'IELTS成绩要求',
  `IELTS_R` varchar(255) DEFAULT NULL COMMENT 'IELTS成绩要求',
  `IELTS_W` varchar(255) DEFAULT NULL COMMENT 'IELTS成绩要求',
  `TOEFL_code` varchar(255) DEFAULT NULL COMMENT 'TOFELCode',
  `TOEFL` varchar(255) DEFAULT NULL COMMENT 'TOFEL成绩要求',
  `TOEFL_L` varchar(255) DEFAULT NULL COMMENT 'TOFEL成绩要求',
  `TOEFL_S` varchar(255) DEFAULT NULL COMMENT 'TOFEL成绩要求',
  `TOEFL_R` varchar(255) DEFAULT NULL COMMENT 'TOFEL成绩要求',
  `TOEFL_W` varchar(255) DEFAULT NULL COMMENT 'TOFEL成绩要求',
  `interview` text COMMENT '面试要求的描述',
  `portfolio` text COMMENT '作品集要求的描述',
  `application_documents` text COMMENT '申请材料要求的描述',
  `how_to_apply` text COMMENT '申请过程的描述',
  `school_test` text COMMENT '学校测试要求的描述',
  `SATRelated` varchar(255) DEFAULT NULL COMMENT '美国学生要求',
  `other` text COMMENT '其它',
  `url` varchar(500) DEFAULT NULL COMMENT '专业的网址',
  `teacher_name` varchar(11) DEFAULT NULL COMMENT '负责老师',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `create_person` varchar(11) DEFAULT NULL COMMENT '创建人',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `update_person` varchar(11) DEFAULT NULL COMMENT '更新人',
  `status` int(11) unsigned DEFAULT '0' COMMENT '是否被操作（0否1是）',
  `sid` int(11) DEFAULT NULL COMMENT '学校id',
  `did` int(11) DEFAULT NULL COMMENT '学院id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `NewIndex1` (`id`),
  KEY `UNIVERSITY_INDEX` (`university`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
