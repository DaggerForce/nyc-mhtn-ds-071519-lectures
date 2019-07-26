DB_NAME = 'yelp_project'
TABLES = {}
TABLES['business'] = (
    "CREATE TABLE business ("
    "  business_id varchar(24) NOT NULL,"
    "  business_name varchar(128) NOT NULL,"
    "  rating varchar(16) NOT NULL,"
    "  price int(10) NOT NULL,"
    "  PRIMARY KEY (business_id)"
    ") ENGINE=InnoDB")

TABLES['reviews'] = (
    "CREATE TABLE reviews ("
    "  review_id varchar(256) NOT NULL,"
    "  review varchar(256) NOT NULL,"
    "  business_id varchar(128) NOT NULL,"
    "  PRIMARY KEY (review_id),  "
    "  CONSTRAINT foreign "
    "  FOREIGN KEY business_name(business_id)"
    "     REFERENCES business(business_id) ON DELETE CASCADE"
    ") ENGINE=InnoDB")
