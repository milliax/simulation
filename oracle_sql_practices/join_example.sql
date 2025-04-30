SELECT
    sim_tsp.from_city,
    sim_tsp.to_city,
    sim_tsp.distance,
    sim_tsp.user_id,
    sim_tsp_cost.cost_per_distance
FROM
    SIM_STUDENT.sim_tsp
    LEFT JOIN SIM_STUDENT.sim_tsp_cost ON sim_tsp.from_city = sim_tsp_cost.region
WHERE
    sim_tsp.user_id = '111704011'
    AND sim_tsp.data_id = 'TSP_1'
    AND sim_tsp.from_city IN (1, 4);