import  scrapy
from scrapy.crawler import CrawlerProcess
#create the Spider Class
class DC_Chapter_Spider(scrapy.Spider):
    name = 'dc_chapter_spider'
    #start request method
    def start_request(self, response):
        yield scrapy.response(url=url_short,callback=self.parse_front)

    #First Parse method
    def parse_front(self, response):
        course_blocks = response.css('div.course_block')
        course_links = course_blocks.xpath('./a/@href')
        links_to_follow = course_links.extract()
        for url in links_to_follow:
            yield response.follow(url=url,  callback=self.parse_pages)
    
    #Second Parse Method
    def parse_pages(self, response):
        crs_title = response.xpath('//h1[contains(@class, "title)]/text()')
        crs_title_ext = crs_title.extract_first().strip()
        ch_titles = response.css('h4.chapter__title::text')
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        dc_dict[crs_title_ext] = ch_titles_ext

dc_dict = dict()

#run the Spider
process = CrawlerProcess()
proccess.crawl(DC_Chapter_Spider)
process.start()

#Print the review of the courses
previewCourses(dc_dict)