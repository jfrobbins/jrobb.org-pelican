#! /usr/bin/env python3
###
#  octopress2pelican.py
#syntax is:
#   ./octopress2pelican.py filename
#   or
#   ./octopress2pelican.py --dir /some/dirPath/
###

import sys,os
from datetime import datetime

def ensure_dir(f):    
    d = os.path.dirname(f)
    print("checking if dir exists: " + d)
    if not os.path.exists(d):
        print("creating dir")
        os.makedirs(d)

class post(object):

    def __init__(self):
        print("init object")
        self.authors = 'Jon Robbins'
        self.fname = ''
        self.title = ''
        self.category = ''
        self.d = './content/'
        self.date = ''
        self.slug = ''
        
    def getArgs(self,args):
        i = 0
        for arg in args:
            if self.title == '':
                self.title = arg
                print("title set: " + arg)
            else:
                print("setting category: " + arg)
                self.category = arg
                if self.category != '':                    
                    self.d = os.path.join(self.d, self.category)                    
                    print("directory updated: " + self.d)
                break
                
    def pelicanHeader(self):
        #pelican header:
        #Title: My super title
        #Date: 2010-12-03 10:20
        #Modified: 2010-12-05 19:30
        #Category: Python
        #Tags: pelican, publishing
        #Slug: my-super-post
        #Authors: Alexis Metaireau, Conan Doyle
        #Summary: Short version for index and feeds
        #        
        #print("summary: " + summaryText)
        #print("endsummary")
        
        #some adjustments:
        self.title = self.title.replace('-',' ').replace('"','')
        slug = self.title.lower().replace(' ', '-').replace('"','qt')
        self.title = self.title.replace('quot','"')
        
        hdr = ''
        hdr += "Title: " + self.title + '\n' #some titles have no spaces
        hdr += "Date: " + self.date + '\n'
        hdr += "Modified: " + self.date + '\n'
        hdr += "Category: " + self.category + '\n'            
        hdr += "Tags: " + self.category + '\n'
        hdr += "Slug: " + self.slug + '\n' #slugs can have no spaces/quotes,etc
        hdr += "Authors: " + self.authors + '\n'
        #hdr += "Summary: " + summaryText + '\n'
        
        return hdr

    def newpost(self, args):
        self.getArgs(args)
        
        if not self.title:
            print("no title in args\n" + str(args))
            return 0
            
        theNow = datetime.now()
        
        self.date = theNow.strftime("%Y-%m-%d")        
        
        self.title = self.title.replace('-',' ').replace('"','')
        self.slug = self.title.lower().replace(' ', '-').replace('"','qt')
        self.title = self.title.replace('quot','"')
        
        fname = self.date + '-' + self.slug + '.md'
        oFileName = os.path.join(self.d, fname)
        ensure_dir(oFileName)
        
        print("writing output to file: " + oFileName)
        of = open(oFileName, 'w')
        
        of.write(self.pelicanHeader() + '\n')
        of.close()
        
        print("done")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        #syntax:
        #   ./newpost.py "some title"
        # also optional category:
        #   ./newpost.py "some title" "category" 
        mypost = post()
        mypost.newpost(sys.argv[1:])
        
    else:
        print("no args, nothing to do")

    
    
