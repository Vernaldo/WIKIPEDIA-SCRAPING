# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Table_name = scrapy.Field()
    Logo = scrapy.Field()
    Photo =  scrapy.Field()
    Photo_Caption =  scrapy.Field()
    Formerly =  scrapy.Field()
    Type =  scrapy.Field()
    Traded_as =  scrapy.Field()
    ISIN =  scrapy.Field()
    Industry =  scrapy.Field()
    Founded =  scrapy.Field()
    Founders =  scrapy.Field()
    Headquaters = scrapy.Field()
    Number_of_locations =  scrapy.Field()
    Area_Served =  scrapy.Field()
    Key_People=  scrapy.Field()
    Products =  scrapy.Field() 
    Services =  scrapy.Field()
    Revenue =  scrapy.Field()
    Operating_income =  scrapy.Field()
    Net_income =  scrapy.Field()
    Total_assets =  scrapy.Field()
    Total_equity =  scrapy.Field()
    Number_of_employees =  scrapy.Field()
    Subsidiaries =  scrapy.Field()
    Website =  scrapy.Field()
   
