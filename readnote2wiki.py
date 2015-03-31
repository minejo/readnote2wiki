#!/usr/bin/env python
#-*- coding: utf-8 -*-
###   Author: Jonathan Li<jonathan.swjtu@gmail.com>  ###
import os

wikidir = '/home/li/Nutstore/vimwiki/readnote/'
readindex = '/home/li/Nutstore/vimwiki/readnote.wiki'
listfile = os.listdir(wikidir)
listfile.sort()
str = ''

for file in listfile:
    filename = file.title().split('.')[0]
    line  = '[[' + 'readnote/' + filename + '|' + filename + ']]' + '\n\n----------------\n\n'
    str = str + line

fp = open(readindex, 'w')
fp.write(str)
fp.close()

