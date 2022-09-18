
mysql> use t_online;
Database changed
mysql> show tables;
+--------------------+
| Tables_in_t_online |
+--------------------+
| pass               |
| train_detail       |
+--------------------+
2 rows in set (0.64 sec)

mysql> desc pass;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| name        | varchar(30) | YES  |     | NULL    |       |
| age         | varchar(30) | YES  |     | NULL    |       |
| train_no    | varchar(30) | YES  |     | NULL    |       |
| no_of_pass  | varchar(30) | YES  |     | NULL    |       |
| class       | varchar(30) | YES  |     | NULL    |       |
| destination | varchar(30) | YES  |     | NULL    |       |
| amount      | varchar(30) | YES  |     | NULL    |       |
| status      | varchar(30) | YES  |     | NULL    |       |
| rno         | varchar(30) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
9 rows in set (0.05 sec)

mysql> desc train_detail;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| tname       | varchar(30) | YES  |     | NULL    |       |
| tnum        | varchar(30) | YES  |     | NULL    |       |
| source      | varchar(30) | YES  |     | NULL    |       |
| destination | varchar(30) | YES  |     | NULL    |       |
| fare        | varchar(30) | YES  |     | NULL    |       |
| ac1         | varchar(30) | YES  |     | NULL    |       |
| ac2         | varchar(30) | YES  |     | NULL    |       |
| slp         | varchar(30) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
8 rows in set (0.07 sec)

mysql> select * from pass;
+---------+------+----------+------------+-------+-------------+--------+--------+------+
| name    | age  | train_no | no_of_pass | class | destination | amount | status | rno  |
+---------+------+----------+------------+-------+-------------+--------+--------+------+
| swetha  | 22   | 1234     | 1          | ac1   | chennai     | 250    | conf   | 21p1 |
| punitha | 25   | 1235     | 1          | ac2   | madurai     | 1000   | conf   | 21p2 |
| sindhu  | 23   | 123456   | 2          | ac1   | goa         | 5000   | conf   | 21p3 |
| sakthi  | 22   | 12376    | 1          | ac2   | delhi       | 5000   | conf   | 21p5 |
+---------+------+----------+------------+-------+-------------+--------+--------+------+
4 rows in set (0.05 sec)

mysql> select * from train_detail;
+-------------------+------+--------+-------------+------+------+------+------+
| tname             | tnum | source | destination | fare | ac1  | ac2  | slp  |
+-------------------+------+--------+-------------+------+------+------+------+
| bangalore_express | 1234 | delhi  | chennai     | 5000 | 23   | 34   | 65   |
| chennai_express   | 1235 | delhi  | madurai     | 5500 | 23   | 33   | 45   |
+-------------------+------+--------+-------------+------+------+------+------+
2 rows in set (0.07 sec)