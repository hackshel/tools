#app/search/developer/trunk/apicenter

import pprint
import os
import os.path
import sys
import subprocess

base_url = 'https://svn.baidu.com/'
home = 'project'
prefixdir = os.path.dirname(os.path.abspath(sys.argv[0]))

def readProjects( project_list ):
    projects = []
    with open( project_list , 'r') as fp :
        lines = fp.readlines()
        for line in lines:
            projects.append( line.split('\n')[0] )
        fp.close()

    return projects


def cratePath( project ):
    paths = project.split( '/' )
    abpath = os.path.join( prefixdir + '/')

    for path in paths:
        abpath += '/' + path
        if os.path.exists( abpath ):
            #path = path + '/'
            #print path
            pass
        else:
            #print path
            os.mkdir( abpath )

    return abpath

def checkout ( url , path ):
    if os.path.exists( path +'/' + '.svn' ):
        cmd = 'svn up ' + url + ' ' + path
    else:
        cmd = 'svn co ' + url + ' ' + path

    print cmd

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE ,shell=True )
    res = p.communicate()[0]
    if p.returncode == 0 :
        print cmd + 'exec OK'
    else:
        print cmd + 'exec FAILD'

def main( projects ):
    for project in projects:
        path = project.split( '/' )
        print path
        if project.startswith('app'):
            path.insert(3 , 'trunk' )
        elif project.startswith('qing'):
            path.insert(2 , 'trunk')
        svn_url = base_url + '/'.join( path )
        abpath = cratePath( home +'/' + project )
        checkout( svn_url , abpath )


if __name__ == '__main__':

    projects = readProjects( 'project.list' )
    main ( projects )
