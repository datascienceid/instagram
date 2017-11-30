# download pip install --user instaLooter

import os 
import sys
import instaLooter

arg1 = sys.argv[1]
arg2 = sys.argv[2]

# arg1 is taxonommy
# arg1 = ['Data','Science','Indonesia']
# arg2 is datelist
# arg2 = ['2017-01-31:2017-01-01','2017-02-28:2017-02-01','2017-03-31:2017-03-01','2017-04-30:2017-04-01','2017-05-31:2017-05-01','2017-06-30:2017-06-01','2017-07-31:2017-07-01','2017-08-27:2017-08-01','2017-09-30:2017-09-01']

hashtag_list = arg1
date_list= arg2

_thisfile = os.getcwd()
for hashtag in hashtag_list:
	curr_file_hashtag = os.path.join(_thisfile,hashtag)
	if not os.path.exists(hashtag):
		os.makedirs(curr_file_hashtag)
	for date in date_list:
		file_name = hashtag+'_'+date[:7]
		full_path = os.path.join(hashtag,file_name)
		#print 'full_path',full_path
		if not os.path.exists(full_path):
			os.makedirs(full_path)
		command = 'instaLooter hashtag '+hashtag+' '+full_path+' -D -e -t '+date
		print 'command',command
		os.system(command)




#instaLooter hashtag komunis komunis_2017_01 -D -e -t 2017-01-31:2017-01-01
#instaLooter hashtag Leninisme /media/adam/205C77EC5C77BADC/dsi/instagram  crawling/Leninisme/Leninisme_2017-09 -D -e -t 2017-09-30:2017-09-01
