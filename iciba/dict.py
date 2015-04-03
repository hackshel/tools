#!/home/users/wangxiaochen02/.jumbo/bin/python2.7
# -*- coding: utf-8 -*-

import httplib
import pprint
import sys

try:
    from bs4 import BeautifulSoup
except:
    print 'please install BeautifulSoup ... '
    print 'download URL http://www.crummy.com/software/BeautifulSoup/'
    sys.exit()

config = {
            'host':'dict.cn',
            'port':80,
            'url': '/'
         }


def request( args , word ):

    url = args['url'] + word

    conn = httplib.HTTPConnection( args['host'] , args['port'] )
    conn.request( 'GET' , url  )
    response = conn.getresponse()

    if response.status == 200:
        res = response.read()
        return res

    else:
        return {'state': response.status }


def htmlParser( html ):
    soup = BeautifulSoup( html )
    #print soup.find_all('div' , class_="group_pos" , limit=1 )
    div =  soup.select( '.dict-basic-ul li' )

    pro =  soup.select( '.phonetic span' )

    wordMeans = wordMeansParser( div )
    pronunce  = pronunciationParser( pro )

    return wordMeans , pronunce

def wordMeansParser( div ):

    wordMeans = []

    for i in range(len(div) -1 ):
        text = div[i].get_text()
        x = text.split('\t')
        for xx in x:
            if xx != '' and xx.startswith('\n') == False:
                wordMeans.append( xx )

    return wordMeans



def pronunciationParser( pro ):

    pronunce = []

    for p in  pro:
        pronunciation = p.get_text()
        px = pronunciation.split( '\t' )
        for pxx in px:
            if pxx != '' and pxx.startswith('\r') == False:
                pronunce.append( pxx.strip() )


    return pronunce


if __name__ == '__main__':


    if len(sys.argv)>=2 and sys.argv[1]:
        word = sys.argv[1]

    else:
        print 'please input your word in it.'
        sys.exit()

    print word.lower()

    res = request( config , word.lower() )
    means , pronunce = htmlParser( res )
    if len( means ) == 0 :
        print 'iciba cannot find the world means ... '
    else:
        for p in pronunce:
            print p,

        print "\r"

        for x in means:
            print x,

