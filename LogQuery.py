import psycopg2
from psycopg2 import extras
import simplejson
from psycopg2.extras import RealDictCursor


DBNAME = "news"


def popArticle():
    """This function provides data for most popular three articles."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor(cursor_factory=RealDictCursor)
    strQuery = ""
    strQuery += "select count(*) as num,articles.title, path,"
    strQuery += "articles.slug, name, authors.id, status from log,"
    strQuery += "articles, authors group by path, articles.slug, name,"
    strQuery += "authors.id, articles.author, log.status, articles.title "
    strQuery += "having articles.slug = substr(log.path,10)"
    strQuery += "and authors.id=articles.author order by num desc limit 3"
    c.execute(strQuery)
    Reportdata = []
    Reportdata = c.fetchall()
    db.close()
    return Reportdata


def popArtAuthor():
    """This function provides data for most popular article authors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor(cursor_factory=RealDictCursor)
    strQuery = ""
    strQuery += "select dummy.name AS author ,sum(dummy.num) AS total "
    strQuery += ",dummy.id from (select count(*) as num,path,"
    strQuery += "articles.slug,name,authors.id from log,articles,authors "
    strQuery += "group by path,articles.slug,name,authors.id,"
    strQuery += "articles.author,log.status "
    strQuery += "having articles.slug = substr(log.path,10)"
    strQuery += "and authors.id=articles.author "
    strQuery += "and log.status like '%200%') as dummy "
    strQuery += "group by dummy.id,dummy.name order by total desc"

    c.execute(strQuery)
    Reportdata = []
    Reportdata = c.fetchall()
    db.close()
    return Reportdata


def logErrPerc():
    """This function provides data for which days did more than 1%
    of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor(cursor_factory=RealDictCursor)
    strQuery = ""
    strQuery += "select dummy.errdate,dummy.num,count(dummy.num) as count,"
    strQuery += "log.status,date_trunc('day',log.time) as repDay,"
    strQuery += "(count(dummy.num) * 100 / dummy.num ) as per "
    strQuery += "from log, (select count(*) as num,"
    strQuery += "date_trunc('day',time) as errdate from log "
    strQuery += "group by date_trunc('day',time) ) as dummy "
    strQuery += "group by dummy.errdate,dummy.num,"
    strQuery += "log.status,date_trunc('day',log.time) "
    strQuery += "having log.status like '%404%' and "
    strQuery += "date_trunc('day',log.time) = dummy.errdate "
    strQuery += "and (count(dummy.num) * 100/dummy.num) > 1 ; "
    c.execute(strQuery)
    Reportdata = []
    Reportdata = c.fetchall()
    db.close()
    return Reportdata
