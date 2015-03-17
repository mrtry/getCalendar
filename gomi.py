#!/usr/bin/python 
# coding: utf-8

#memo_site	datetime:http://www.python-izm.com/contents/basis/date.shtml
#		main	:http://blog.livedoor.jp/k_urushima/archives/1062211.html

import gdata.calendar.service
import datetime
import locale

client = gdata.calendar.service.CalendarService()
client.email = 'UID'
client.password = 'PW'
client.source = 'Google-Calendar_Python_Sample-1.0'
client.ProgrammaticLogin()

query = gdata.calendar.service.CalendarEventQuery('calendarID', 'private', 'full')

today = datetime.datetime.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=2)
print "to = %s" % today.strftime("%Y-%m-%d") 
print "tm = %s" % tomorrow.strftime("%Y-%m-%d")

query.max_results = 3 
query.start_min = today
query.start_max = tomorrow
query.singleevents = 'true'

feed = client.CalendarQuery(query)
for i, an_event in enumerate(feed.entry):
	title = an_event.title.text
	when = an_event.when
	print '件名: %s' % (title)
#	print '場所: %s' % (an_event.where[0].value_string)
#	print '詳細: %s' % (an_event.content.text)
	print '日付: %s' % (an_event.when[0].start_time)
#	print '参照: %s' % (an_event.GetEditLink().href)
	print ''
