# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

script = '''
function main(splash, args)
  splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return splash:html()
  --{
    --html = splash:html(),
    --png = splash:png(),
    --har = splash:har(),
  --}
end
'''


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = ['www.baidu.com']
    url = 'https://item.jd.com/100000177760.html'

    # start request
    def start_requests(self):
        # yield SplashRequest(self.url, callback=self.parse, endpoint='execute', args={'lua_source': script})
        yield SplashRequest(self.url, callback=self.parse)

    # parse the html content
    def parse(self, response):
        a = response.request.headers
        print('=' * 40)
        # print(response.text)
        print('=' * 40)
        # with open('test.html', 'w', encoding='utf-8') as f:
        #     f.write(str(response.body, encoding='utf-8'))
