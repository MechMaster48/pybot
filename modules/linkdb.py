#Link DB for practice by mech

import sys
import re
import pymysql
from datetime import datetime

from event import Event
try:
  if sys.version_info > (3, 0, 0):
    from .basemodule import BaseModule
  else:
    from basemodule import BaseModule
except (ImportError, SystemError):
  from modules.basemodule import BaseModule

class Linkdb(BaseModule):
  
  def post_init(self):
    linkdb = Event("__linkdb__")
    linkdb.define(msg_definition="https?://[\S]+") # What to look for to trigger event
    linkdb.subscribe(self)
    # register ourself to our new custom event
    self.bot.register_event(linkdb, self)

  def handle(self, event):
    if event.user == 'pybot-is-back':
      pass
    else:
      #Create connection to DB table irc_links
      connection = pymysql.connect(host='',
                  user='',
                  password='',
                  db=''
                  )
      cursor = connection.cursor()
      target_link = re.search("https?://[\S]+", event.line).group(0)
      current_time_date = datetime.now()
      time_string = current_time_date.strftime("%m/%d/%Y %H:%M:%S")
      values = (event.user, target_link, time_string)
      insert_link = """INSERT INTO irc_links (user, link, time) VALUES(%s, %s, %s)"""
      cursor.execute(insert_link, values)
      connection.commit()
      print("Records inserted succesfully!")
      show_info = """SELECT * FROM irc_links"""
      cursor.execute(show_info)
      results = cursor.fetchall()
#      print(results)
      connection.close()
  #    print(target_link)
  #    print(len(target_link))
  #    print(event.user)
