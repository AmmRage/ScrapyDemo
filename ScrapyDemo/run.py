# -*- coding: utf-8 -*-


from scrapy import cmdline


name = 'nw_lyrics'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())