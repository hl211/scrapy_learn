# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import random
import uuid

import scrapy
import time


class ScprojectItem(scrapy.Item):
    # define the fields for your item here like:
    time = scrapy.Field()
    price = scrapy.Field()
    sid=scrapy.Field()
    mid=scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
                    insert into t_scjg(j_id, j_time, j_price, j_sid,j_mid)
                    VALUES (%s, %s, %s, %s,%s);
                """
        params = (
            str(uuid.uuid1()),self["time"], self["price"], self["sid"], self["mid"])
        return insert_sql, params