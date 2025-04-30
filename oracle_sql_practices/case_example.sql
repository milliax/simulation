SELECT from_city, to_city, distance,user_id,
(CASE 
    WHEN from_city = 1 THEN distance+1
    ELSE distance +2
END) AS new_QTY
FROM SIM_STUDENT.sim_tsp
WHERE (data_id='TSP_1' and user_id='111704011' and from_city IN (1,2));