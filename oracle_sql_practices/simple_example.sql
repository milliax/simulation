--SELECT from_city, SUM(distance)
--FROM SIM_STUDENT.sim_tsp
--WHERE (data_id='TSP_1' and user_id='111704034' and from_city=1)
--or (data_id='TSP_1' and user_id='111704034' and from_city=2)
--or (data_id='TSP_1' and user_id='111704034' and from_city=3)
--group by from_city
--HAVING SUM(distance) > 900
--ORDER BY SUM(distance)

SELECT from_city, SUM(distance) as total_distance
FROM SIM_STUDENT.sim_tsp
WHERE (data_id='TSP_1' and user_id='111704011' and from_city IN (1,2,3)) 
group by from_city
HAVING SUM(distance) > 900
ORDER BY SUM(distance);

--SELECT * FROM SIM_STUDENT.sim_tsp