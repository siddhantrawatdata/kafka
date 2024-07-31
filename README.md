# kafka
### Problem Staement
 We need to  will build a Kafka producer and a consumer group that work with a MySQL database, Avro serialization, and multi-partition Kafka topics. The producer will fetch incremental data from a MySQL table and write Avro serialized data into a Kafka topic.
The consumers will deserialize this data and append it to separate JSON files.

### Introduction
Kafka is a scalable , fast and Fault tolerant messaging system which is used to transport data between producers and consumers. 
Earlier each producer used to generate data and each consumer went to the producer it needs data from and fetches it. This creaeted a lot of overhead on the producer end and resulted in failures. 
Kafka acts as a middle point where producer can publish the data and consumer can go in and fetch the data it needs for computation.

### Generation of data.
Instead of taking data from Kaggle or any other website , I decided to generate data via a python script and insert the data into MySql server.
#### my_sql_product_info_generation.py
##### Libraries
mysql.connector : To connect to mysql srver to fetch/push the data \
pandas : To use the dataframe functionaliteis to effectively visualize and insert the data\
random : To generate random datasets to be inserted into mysql
##### Execution
Step1 : Establish connection to the Mysql server 
Step2 : Fetch the column information at runtime from the database to generate the insert query dynamically.\
Step3 : Create a list of random column values that would be used to generate the data to be inserted .\
Step4 : We create a pandas dataframe out of the dataset and by using the functionality of iterrows() insert data into the database.\

### Producer Creation
#### kafka_producter_for_product.ipynb
##### Libraries
  ```import time``` : To find out the current timestamp \
  ```import pandas``` : To use the Dataframe functionalities and create robust datasets\
  ```import mysql.connector``` : To interact with the mysql database\
  ```from confluent_kafka import SerializingProducer``` : To serialize the data so that we can use the faster write functionality of avro\
  ```from confluent_kafka.schema_registry import SchemaRegistryClient``` : To interact with schema registry of Confluent Kafka\
  ```from confluent_kafka.schema_registry.avro import AvroSerializer``` : To read the serialized avro data\
  ```from confluent_kafka.serialization import StringSerializer``` : To read the serialized string data\
##### Execution
```def connect_mysql()``` : Establish the connection to MySQL server
```def fetch_data_from_table(my_cursor, last_run)``` : Fetch the data from the ```product_inormation``` table.\
```def kafka_producer(sel_query, my_cursor,col_list)``` : Fetch all the data from the table line-by-line and send it to the Producer with help of two underlying function
  ```def create_kafka_connection(product_data)``` : Create a kafka producer connection and publish the data to kafka brokers
  ```def date_update(my_cursor)``` : We update the ETL table ater successful reads so next time only changed data is picked from table

### Consumer Creation
#### kafka-consumer-for-product.ipynb
##### Libraries
 ```import pandas as pd``` : To use the Dataframe functionalities and create robust datasets\
 ```import datetime as dt``` : Date related transformations\
 ```from confluent_kafka import DeserializingConsumer``` : To de-serialize the data for consumption\
 ```from confluent_kafka.schema_registry import SchemaRegistryClient``` : To Interact with Schema registry of confluent Kafka\
 ```from confluent_kafka.schema_registry.avro import AvroDeserializer``` : To De-serialize the avro data.\
 ```from confluent_kafka.serialization import StringDeserializer``` : To De-serialize string data.\
##### Execution
```def kafka_consumer_connect()``` : Connect to the Kafka consumer and fetch the data from the topic
```def transform_data(data)``` : Read the data as it comes and transform as per requirements
```def write_to_json_file(transform_data)``` : Write the transformed data to json






