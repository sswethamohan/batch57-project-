mysql> use my_atm;
Database changed
mysql> desc user;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| user_name    | varchar(30) | YES  |     | NULL    |       |
| acc_no       | int         | YES  |     | NULL    |       |
| pin_no       | int         | YES  |     | NULL    |       |
| currrent_bal | int         | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
4 rows in set (1.57 sec)

mysql> select * from user;
+-----------+--------+--------+--------------+
| user_name | acc_no | pin_no | currrent_bal |
+-----------+--------+--------+--------------+
| swetha    |   1234 |   7230 |         7200 |
+-----------+--------+--------+--------------+
1 row in set (1.31 sec)