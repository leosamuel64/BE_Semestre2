ENV="development"
DEBUG=True
SEND_FILE_MAX_AGE_DEFAULT = 0
SECRET_KEY="jkqskdhvbjsd"

WEB_SERVER={
    "host": "localhost",
    "port": 8080
}


# sudo /etc/init.d/mysql start
DB_SERVER={
    "user":"root",
    "password":"",
    "host": "localhost",
    "port": 3306,
    "database": "gsea_cours",
    "raise_on_warning":True
}