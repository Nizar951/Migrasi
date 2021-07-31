import mysql.connector
from mysql.connector import Error
import datetime


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="salam"
)

mycursor = mydb.cursor()

# mycursor.execute("Create table pribadi (Idpribadi int auto_increment primary key, nama varchar(512), tempat_lahir varchar(512), tgl_lahir date, kelamin varchar(2), gol_darah varchar(4), kelurahan_ktp int, kelurahan_domisili int, agama varchar(512), stat_kawin varchar(50), no_kk int, no_ktp int, is_wni boolean, json_alamat text, json_pendidikan text, json_pekerjaan text, created datetime, updated datetime)")
# sql = """insert into pribadi (Idpribadi, nama, tempat_lahir, tgl_lahir, kelamin, gol_darah, kelurahan_ktp, kelurahan_domisili, agama, stat_kawin, no_kk, no_ktp, is_wni, json_alamat, json_pendidikan, json_pekerjaan, created, updated) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
# data = (2, 'Malik, S.Pd', 'Surabaya', '1979-9-21', 'p', 'b', '3578281003', '3578281003', 'Islam', 'None', '3578302109790001', '3578302109790001', True, 'Rejosari Pesantren IV no. 14', '', 'Pegawai Swasta', '2019-1-24 17:20:43', '2020-10-1 23:52:38')

# mycursor.execute(sql, data)

# mydb.commit()

# print(mycursor.rowcount, "record inserted")

# mycursor.execute("select * from pribadi")
# result = mycursor.fetchone()
# print(result)

mycursor.execute("SELECT id, publicid, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, darah, desa_id, desa_id, kawin, noktp, jalan, pendidikan_terakhir, pekerjaan, created, updated  FROM member limit 5")
result = mycursor.fetchall()

sql = """insert into pribadi (Idpribadi, publicid, nama, tempat_lahir, tgl_lahir, kelamin, gol_darah, kelurahan_ktp, kelurahan_domisili, agama, stat_kawin, no_kk, no_ktp, is_wni, json_alamat, json_pendidikan, json_pekerjaan, created, updated) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

data=""

print(result)

json_alamat = {}
for x in result :
    x = list(x)
    # json_alamat['jalan']=x[13]
    # json_alamat['rt_rw']= x[17]
    x.insert(9,'Islam')
    
    if len(x[11]) == 16 :
        x.insert(11,'')
    else :
        x.insert(12,'')
    x.insert(13, True)
    # x.insert(14, json_alamat)
    # data +=x
    # data +=','
    # print(x)
    
    # mycursor.execute(sql, x)
    # mydb.commit()

print(data)    
print(mycursor.rowcount, "record inserted")

# ispelatih= false
# is pengurus = kepengurusan
# is verified ada
# is admin ada 
