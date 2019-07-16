#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import urllib2
import urllib
from lxml import etree


class Spider:

    def run(self):
        url = "https://tieba.baidu.com/f?kw=gay"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"
        }
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request).read()
        content = etree.HTML(response)
        links = content.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        username = 1
        for link in links:
            url = 'https://tieba.baidu.com' + link
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request).read()
            images = etree.HTML(response)
            images_links = images.xpath('//img[@class="BDE_Image"]/@src')
            for image_link in images_links:
                file = open('./image/' + str(username) + '.png', 'wb')
                image = urllib2.urlopen(image_link).read()
                file.write(image)
                file.close()
                username += 1




if __name__ == '__main__':
    spider = Spider()
    spider.run()