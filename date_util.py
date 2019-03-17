def remove_slash_from_datestring(date):
        dateparts = date.split('/')
        return '%04d%02d%02d' % (int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))