""" As part of this implementation we were required to have product data in the mysql table
    I created this program to generate random product information data and insert the data into the mysql database
    This is a parameterised program and can be used to dynamically read the table from mysql server and  insert the data into it
    I have used the random function to generate the random datasets.
"""


import datetime
import time

import mysql.connector
import pandas as pd
import random as rd
import datetime as dt
def main():

    """
    This function is responsible for establishing the connection to mysql ,
     get the table details and insert data into it
    :return: null
    """

    """
        Define the connection properties and esablish the connection
    """
    config={
        'user':'root',
        'host':'xxxx',
        'password':'xxxx',
        'database':'buy_online',
        'raise_on_warnings':True

    }

    #Create the dataset
    name=['Television','Sofa','Chair','Bed','Cupboard','Bottle','Adaptor','Wires']
    category=['Houseold','Office','Educational Institutions','Shopping Mart']
    price=[10000,20000,300,5000,4000,790,3000,25000]

    schema_name='buy_online'
    table_name='product_information'


    try:
        cnx=mysql.connector.connect(**config)
    except:
        print("Connection failed")
        exit(1)
    else:
        print("Connection Successful")

    my_cursor=cnx.cursor()

    # Get the columns of the required table

    column_query="select column_name from information_schema.columns \
    where table_schema= '" + schema_name + \
    "' and table_name='" + table_name + \
    "' order by ordinal_position; "

    #print(column_query)


    my_cursor.execute(column_query)
    result=pd.DataFrame(my_cursor.fetchall())

    # Creation of the insert query by readin the columns

    columns=[]
    q=""
    for idx,row in result.iterrows():
        q+=row[0]+", "
        columns.append(row[0])

    # Insertion of the dataset into the mysq table
    now=datetime.datetime.now()
    id=1
    data=[]
    tmp=[]
    while id<201:
        tmp=[]
        input_name=rd.choice(name)
        input_category=rd.choice(category)
        input_price=rd.choice(price)
        tmp.append(id)
        tmp.append(input_name)
        tmp.append(input_category)
        tmp.append(input_price)
        tmp.append(now)
        tmp.append(now)
        data.append(tmp)
        id+=1
    # Create a dataframe so that we can iterate over the rows and insert the data into mysql server .

    total_data=pd.DataFrame(columns=columns,data=data)

    q_val='%s, '*6
    q_val=q_val[:-2]
    print(q_val)
    for idx,col in total_data.iterrows():

        insert_query="insert into " + schema_name +"." + table_name + "(" + q[:-2] + ")\
        values (" + q_val + ")"
        print(insert_query)
        print(tuple(col))
        try:
            my_cursor.execute(insert_query,tuple(col))
        except:
            print("Insert query failed")
            exit(1)
        else:
            print("Performed the following insert : {}".format(tuple(col)))
        time.sleep(1)
        cnx.commit()


    cnx.close()


if __name__=='__main__':
    main()
