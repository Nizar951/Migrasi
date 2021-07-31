import mysql.connector
from mysql.connector import Error
import datetime
import json
import collections

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="salam"
)

# mydbfix = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     database="salamv2"
# )

mycursor = mydb.cursor()
# fix = mydbfix.cursor()

# mycursor.execute("Select id, publicid, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, darah, desa_id, desa_id, kawin, noktp, created, updated, kepengurusan, is_verified, is_admin, veried_date, verifier, email, nokta, kta_lama, url_foto, url_ktp FROM member")

# qinsert = """insert into pribadi (Idpribadi, publicid, nama, tempat_lahir, tgl_lahir, kelamin, gol_darah, kelurahan_ktp, kelurahan_domisili, agama, stat_kawin, no_kk, no_ktp, is_wni, created, updated, is_pelatih, is_pengurus, is_verified, is_admin, verified_date, verifier, email, nokta, no_ktalama, kepengurusan id, url_foto, url_ktp) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

mycursor.execute("SELECT jalan, rt_rw FROM member limit 5")

hasil = mycursor.fetchall()

arr = []
json_alamat={}

for x in hasil :
    json_alamat['jalan']=x[0]
    json_alamat['rtrw']= x[1]

    
    # x = list(x)
    # print(f"{json.dumps(x)}")


# print(f"{json.dumps(hasil)}")