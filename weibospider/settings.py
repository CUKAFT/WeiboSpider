# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_T_WM=2a582f9f00aecfd3630c9e5c44840c2d; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https%3A%2F%2Fweibo.cn%2F; SUB=_2A25NCOVyDeRhGeFL7lYZ9ibLzDmIHXVu8os6rDV6PUJbktAfLVTskW1Nfef3VFRkfhfiYdr_uNDYcZiDgFPu9n_f; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5zqa.R3lO00qy66IZe3uSu5NHD95QNSK-X1hqRS0MfWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0-fShnc1hMNSBtt; SSOLoginState=1611437346'}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
