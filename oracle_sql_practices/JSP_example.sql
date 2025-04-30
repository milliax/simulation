-- SELECT * FROM SIM_STUDENT.sim_jsp
-- WHERE user_id = '111704011';


-- 1. Calculate the total processing time for the student with user_id = 'your id' on each machine
--    and sort the results in descending order based on the total processing time.

SELECT
    machine,
    SUM(time) AS total_processing_time
FROM
    SIM_STUDENT.sim_jsp
WHERE
    user_id = '11704011'
ORDER BY
    total_processing_time DESC;

-- 2. Correct the processing time of student 'your id' on machine 'M3' by adding 10 minutes.
UPDATE SIM_STUDENT.sim_jsp
SET
    time = time + 10
WHERE
    user_id = '111704011'
    AND machine = 'M3';

-- 3. Insert a new record for student 'your id' assigned job 'J7' to machine 'M1' with a processing time of 25 minutes.
INSERT INTO
    SIM_STUDENT.sim_jsp (user_id, job, machine, time)
VALUES
    ('111704011', 'J7', 'M1', 25);