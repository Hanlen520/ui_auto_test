#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 13:00
# @Author  : mrwuzs
# @Site    :
# @File    : initializeEnv.py
# @Software: PyCharm

from public.common.log import Log
from config import globalparam
from config.confRelevance import ConfRelevance

CONF_PATH = globalparam.config_file_path + "\\config.ini"
ENV_PATH = globalparam.xml_report_path + "\\environment.xml"

class Init_Env:
    """初始化环境信息，更新xml文件"""

    def __init__(self):
        log = Log()
        log.info("获取环境配置信息")
        # 读取配置文件，返回字典格式
        self.data = ConfRelevance(CONF_PATH, "env").get_relevance_conf()

    def dict_to_xml(self):
        parameter = []
        for k in sorted(self.data.keys()):
            xml = []
            v = self.data.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<key>{value}</key>'.format(value=k))
            xml.append('<value>{value}</value>'.format(value=v))
            parameter.append('<parameter>{}</parameter>'.format(''.join(xml)))

        return '<environment>{}</environment>'.format(''.join(parameter))

    def init(self):
        data = self.dict_to_xml()
        with open(ENV_PATH, 'w') as f:
            f.write(data)


if __name__ == '__main__':
    Init = Init_Env()
    Init.init()
