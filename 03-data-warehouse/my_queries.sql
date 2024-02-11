# SELECT count(*) FROM `machinelearningzoomcamp1.greentaxi_dataset1.2022_greentaxi` 
#840402


# Question 2
#select count(distinct(PULocationID)) from `machinelearningzoomcamp1.greentaxi_dataset1.green_2`
#select count(distinct(PULocationID)) from `machinelearningzoomcamp1.greentaxi_dataset1.green_mat`

#Question 3 
#3 select count(*) from `machinelearningzoomcamp1.greentaxi_dataset1.2022_greentaxi` WHERE fare_amount = 0

#select distinct(PULocationID) from `machinelearningzoomcamp1.greentaxi_dataset1.green_mat` WHERE lpep_pickup_date > DATE(2022, 06, 01) and lpep_pickup_date < DATE(2022, 06, 30) 
select distinct(PULocationID) from `machinelearningzoomcamp1.greentaxi_dataset1.green_part_clus` WHERE lpep_pickup_date > DATE(2022, 06, 01) and lpep_pickup_date < DATE(2022, 06, 30) 

-- CREATE OR REPLACE TABLE `machinelearningzoomcamp1.greentaxi_dataset1.green_part_clus` 
-- PARTITION BY
--   lpep_pickup_date 
-- CLUSTER BY PULocationID
--   AS
-- SELECT * FROM `machinelearningzoomcamp1.greentaxi_dataset1.green_mat` 


