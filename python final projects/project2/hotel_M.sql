mysql> use hotel_M;
Database changed
mysql> desc user;
+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| menu_no    | int         | NO   | PRI | NULL    | auto_increment |
| menu_list  | varchar(30) | YES  |     | NULL    |                |
| menu_price | int         | YES  |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+
3 rows in set (0.07 sec)

mysql> select * from user;
+---------+------------------------+------------+
| menu_no | menu_list              | menu_price |
+---------+------------------------+------------+
|       1 | chicken_biriyani       |        130 |
|       2 | Mutton_biriyani        |        210 |
|       3 | chicken Rice           |         70 |
|       4 |  kerala pepper chicken |        255 |
|       5 | chicken masala         |        255 |
|       6 | muttar panner masala   |        190 |
|       7 | panner butter masala   |        185 |
|       8 | aloo gobi masala       |        175 |
|       9 | gobi manchurian/chilly |        185 |
|      10 | veg chettinad curry    |        185 |
+---------+------------------------+------------+
10 rows in set (0.05 sec)