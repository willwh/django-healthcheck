from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import BadRequest
import pyodbc
import redis

def index(request):
    # connect and test the things
    
    # MSSQL
    try:
        server = 'tcp:localhost'
        database = 'master'
        username = 'sa'
        password = 'SuperS3cr3t'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};TrustServerCertificate=yes;SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password, timeout=3)
        cursor = cnxn.cursor()
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        while row:
            print(row[0])
            row = cursor.fetchone()
    except:
        raise BadRequest('MSSQL is down yo')

    # Redis
    try:
        r = redis.from_url('redis://localhost:6379')
        r.ping()
    except:
        raise BadRequest('Redis is down yo')

    return HttpResponse("Things are okay.")