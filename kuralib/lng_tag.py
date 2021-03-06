from dbobj.dbobj import dbRecord
from dbobj.dbobj import dbTable

class lng_tag(dbRecord):

  def __init__(self, app, **args):
    if args.has_key("fields"):
      dbRecord.__init__(self, app, "lng_tag", args["fields"])
    else:
      dbRecord.__init__(self, app, "lng_tag", args)

  def getTagTypeCode(self):
    return self.app.getObject("lng_tagtypecode", tagtypecode=self.tagtypecode)
  
  def getDomainTags(self):
    """
      Return all tags that are based on a domain.
    """
    domainRows=[]
    for row in self.app.getObjects("lng_tagtypecode", isdomain=1):
      domainRows=domainRows + self.app.getObjects("lng_tag", tagtypecode=row.tagtypecode)
    return domainRows #self.app.getObjects("lng_tag", tagtypecode="DABBR")

 
class lng_tags(dbTable):
  """
    Collection class for all tag data.
  """
  def __init__(self, app):
    dbTable.__init__(self, app, "lng_tag", lng_tag)

__copyright__="""
/***************************************************************************
    copyright            : (C) 2000 by Boudewijn Rempt 
                           see copyright notice for license
    email                : boud@rempt.xs4all.nl
    Revision             : $Revision: 1.2 $
    Last edited          : $Date: 2002/11/16 12:37:03 $
 ***************************************************************************/
"""
