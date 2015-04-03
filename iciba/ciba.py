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
            'host':'www.iciba.com',
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
    wordMeans = []
    soup = BeautifulSoup( html )
    #print soup.find_all('div' , class_="group_pos" , limit=1 )
    div =  soup.select( '.group_pos' )
    for d in div:
        text = d.get_text()
        x = text.split('\n')
        for xx in x:
            if xx != '':
                wordMeans.append( xx )

    return wordMeans

if __name__ == '__main__':


    if len(sys.argv)>=2 and sys.argv[1]:
        word = sys.argv[1]

    else:
        print 'please input your word in it.'
        sys.exit()

    print word.lower()

    res = request( config , word.lower() )
    means = htmlParser( res )
    if len( means ) == 0 :
        print 'iciba cannot find the world means ... '
    else:
        for x in means:
            print x,

