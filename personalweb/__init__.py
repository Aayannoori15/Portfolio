import pymysql
pymysql.install_as_MySQLdb()

# Patch version_info for Django 6.0 compatibility
pymysql.version_info = (2, 2, 4, 'final', 0)
