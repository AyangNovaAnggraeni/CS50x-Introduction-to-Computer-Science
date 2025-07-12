-- Keep a log of any SQL queries you execute as you solve the mystery.

--To see all the tables in databases
.schema

--to see all field in the crime_scene_reports table
SELECT * FROM crime_scene_reports;

--to select crime scene based on certain condition and find its id
SELECT * FROM crime_scene_reports WHERE year = '2024' AND month = '7' AND day = '28' AND street = 'Humphrey Street';


| 295 | 2024 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the
Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their
interview transcripts mentions the bakery.

| 161 | Ruth    | 2024 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2024 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2024 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

| 259 | 2024 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95

+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
+--------+---------+----------------+-----------------+---------------+

+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 745650 | Sophia | (027) 555-1068 | 3642612721      | 13FNH73       |
+--------+--------+----------------+-----------------+---------------+

SELECT * FROM passengers WHERE passport_number = '3642612721';
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 2         | 2963008352      | 6C   |
| 20        | 2963008352      | 6B   |
| 39        | 2963008352      | 8C   |
+-----------+-----------------+------+

+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 6         | 3642612721      | 8A   |
| 31        | 3642612721      | 9B   |
| 43        | 3642612721      | 2C   |
+-----------+-----------------+------+

sqlite> SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE id IN (SELECT flight_id FROM passengers WHERE flight_id = '2');
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 2  | 2                 | 8                      | 2024 | 7     | 30  | 12   | 44     | 2         | 2963008352      | 6C   |

sqlite> SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE id IN (SELECT flight_id FROM passengers WHERE flight_id = '31');
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 31 | 8                 | 3                      | 2024 | 7     | 30  | 20   | 21     | 31        | 3642612721      | 9B   |

sqlite> SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE id IN (SELECT flight_id FROM passengers WHERE flight_id = '20');
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 20 | 6                 | 8                      | 2024 | 7     | 28  | 15   | 22     | 20        | 2963008352      | 6B   |

 SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE id IN (SELECT flight_id FROM passengers WHERE flight_id = '39');
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 39 | 5                 | 8                      | 2024 | 7     | 27  | 22   | 37     | 39        | 2963008352      | 8C   |


 6  | 8                 | 5                      | 2024 | 7     | 28  | 13   | 49     | 6         | 3642612721      | 8A   |

sqlite>SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE id IN (SELECT flight_id FROM passengers WHERE flight_id = '31');
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| id | origin_airport_id |   | year | month | day | hour | minute | flight_id | passport_number | seat |
+----+-------------------+------------------------+------+-------+-----+------+--------+-----------+-----------------+------+
| 31 | 8                 | 3                      | 2024 | 7     | 30  | 20   | 21     | 31        | 3642612721      | 9B   |

| 43 | 8                 | 1                      | 2024 | 7     | 29  | 9    | 30     | 43        | 3642612721      | 2C   |
