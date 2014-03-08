
import os
import urllib
import itertools
import urllib2

month_list=range(1,13,1)
year_list=range(1987,2014,1)

def build_yearmonth_combination(year_list,month_list):
    yearmonth = list()
    for i in itertools.product(month_list,year_list):
        yearmonth.append(i)
    return(yearmonth)

def build_urls(yearmonth):
    
    #year,month = zip(*yearmonth)
    root_url='www.transtats.bts.gov/Download/On_Time_On_Time_Performance_'
    urls = list()
    for month_it,year_it in yearmonth:
        url_temp = 'http://www.transtats.bts.gov/Download/On_Time_On_Time_Performance_%s_%s.zip' %(year_it,month_it)
        entry = (url_temp,str(year_it) +'_' + str(month_it))
        urls.append(entry)
    return urls


def dlfile(url,file_name):
    # Open the url
    try:
        f = urllib2.urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(file_name, "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except urllib2.HTTPError, e:
        print 'HTTP error'
        return
        #print "HTTP Error:", e.code, url
    except urllib2.URLError, e:
        print 'URL error'
        return
        #print "URL Error:", e.reason, url

 
if __name__ == "__main__":

    yearmonth = build_yearmonth_combination(year_list,month_list)
    print "yearmonth combination built"
    
    files_urls = build_urls(yearmonth)
    print files_urls[0]
    for file_url,file_name in files_urls:
        print 'download file %s' %file_url
        dlfile(file_url,file_name + '.zip')
        #retrieve(file_url,str(file_name[0])+"_"+str(file_name[1]) + '.zip')

