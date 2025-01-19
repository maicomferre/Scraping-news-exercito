CREATE TABLE IF NOT EXISTS `{table_name}`(
    id int NOT NULL,
    title varchar(256) NOT NULL,
    description TEXT NOT NULL,
    category varchar(80) NOT NULL,
    url varchar(2048) NOT NULL,
    publish_date DATETIME NOT NULL,
    image_url varchar(2048) DEFAULT NULL,
    local_image varchar(256) DEFAULT NULL,
    min_local_image varchar(256) DEFAULT NULL,
    PRIMARY KEY (id)
);