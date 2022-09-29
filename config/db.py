import pymysql

from config.config import settings

conection = pymysql.connect(
    host=settings.DB_HOST,
    user=settings.DB_USER,
    passwd=settings.DB_PASS,
    db=settings.DB,
    cursorclass=pymysql.cursors.DictCursor
)
