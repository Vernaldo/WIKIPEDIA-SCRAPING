import scrapy
from..items import WikiItem


class MywikiSpider(scrapy.Spider):
    name = 'mywiki'
    #allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Apple_Inc.']

    def parse(self, response):
        
        items = WikiItem()
        required_table = response.css('.vcard')
        
        Table_name = required_table.css('.org::text').extract()
        Logo = required_table.css('tr:nth-child(1) .logo img::attr(src)').extract()
        Photo = required_table.css('tr+ tr .image img::attr(src)').extract()
        Photo_Caption = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/div//text()').getall()  
        Formerly = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[3]/td/div/ul//text()').getall()
        Type = required_table.css('.category > a::text').extract()
        Traded_as = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td/div/ul//text()').getall() 
        ISIN = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td/span//text() ').getall() 
        Industry = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td/div/ul//text()').getall()  
        Founded = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td//text()').getall() 
        Founders = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[9]/td//text()').getall() 
        Headquaters = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[10]/td//text()').getall() 
        Number_of_locations = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[11]/td//text()').getall()
        Area_Served = required_table.css('tr:nth-child(12) .infobox-data::text').extract()
        Key_People= required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[13]/td//text()').getall() 
        Products = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[14]/td//text() ').getall() 
        Services = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[15]/td//text()').getall() 
        Revenue = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[16]/td//text()').getall() 
        Operating_income = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[17]/td//text()').getall()
        Net_income = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[18]/td//text()').getall()
        Total_assets = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[19]/td//text()').getall()
        Total_equity = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[20]/td//text()').getall()
        Number_of_employees = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[21]/td//text()').getall()
        Subsidiaries = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[22]/td//text()').getall()
        Website = required_table.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[23]/td//text()').getall()
        
        
        
        items['Table_name'] = Table_name
        items['Logo'] = Logo
        items['Photo'] = Photo
        items['Photo_Caption'] = Photo_Caption
        items['Formerly'] = Formerly
        items['Type'] = Type
        items['Traded_as'] = Traded_as
        items['ISIN'] = ISIN
        items['Industry'] = Industry
        items['Founded'] =  Founded
        items['Founders'] = Founders 
        items['Headquaters'] = Headquaters
        items['Number_of_locations'] = Number_of_locations
        items['Area_Served'] = Area_Served
        items['Key_People'] =  Key_People
        items['Products'] = Products
        items['Services'] = Services
        items['Revenue'] =  Revenue
        items['Operating_income'] = Operating_income
        items['Net_income'] = Net_income
        items['Total_assets'] = Total_assets
        items['Total_equity'] =  Total_equity
        items['Number_of_employees'] = Number_of_employees
        items['Subsidiaries'] = Subsidiaries 
        items['Website'] = Website
       
        
        
        
        
        yield items