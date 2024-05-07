/* MEDIA table */

CREATE TABLE IF NOT EXISTS MEDIA (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    organization_id INT,
    name VARCHAR(255),
    s3_bucket_name VARCHAR(255),
    s3_key VARCHAR(255),
    processing_state VARCHAR(255),
    date_created DATETIME,
    Last_updated DATETIME
)

INSERT INTO MEDIA (organization_id, name, s3_bucket_name, s3_key, processing_state, date_created, Last_updated)
VALUES 
(1, 'Sample Media 1', 'sample-bucket', 'sample-key-1', 'success', NOW(), NOW()),
(2, 'Sample Media 2', 'sample-bucket', 'sample-key-2', 'success', NOW(), NOW()),
(3, 'Sample Media 3', 'sample-bucket', 'sample-key-3', 'success', NOW(), NOW()),
(4, 'Sample Media 4', 'sample-bucket', 'sample-key-4', 'success', NOW(), NOW()),
(5, 'Sample Media 5', 'sample-bucket', 'sample-key-5', 'error', NOW(), NOW()),
(6, 'Sample Media 6', 'sample-bucket', 'sample-key-6', 'success', NOW(), NOW()),
(7, 'Sample Media 7', 'sample-bucket', 'sample-key-7', 'success', NOW(), NOW()),
(8, 'Sample Media 8', 'sample-bucket', 'sample-key-8', 'error', NOW(), NOW()),
(9, 'Sample Media 9', 'sample-bucket', 'sample-key-9', 'success', NOW(), NOW()),
(10, 'Sample Media 10', 'sample-bucket', 'sample-key-10', 'success', NOW(), NOW());


/* # task_summary table */

CREATE TABLE IF NOT EXISTS task_summary (
    date DATE,
    successful_tasks INT,
    unsuccessful_tasks INT
);

INSERT INTO task_summary (date, successful_tasks, unsuccessful_tasks)
VALUES 
(20240506, 5, 5),
(20240507, 6, 4),
(20240508, 7, 3),
(20240509, 8, 2),
(20240510, 9, 1),
(20240511, 10, 0),
(20240512, 11, 0),
(20240513, 12, 0),
(20240514, 13, 0),
(20240515, 14, 0);


/* # Grafana query using the table task_summary */

SELECT 
    SUM(successful_tasks) / CAST((SUM(successful_tasks) + SUM(unsuccessful_tasks)) AS DECIMAL) * 100 AS overall_success_percentage
FROM task_summary;


/* # Grafana query accessing directly the table MEDIA */

SELECT 
    (SELECT COUNT(*) FROM MEDIA WHERE processing_state = "success") / CAST((SELECT COUNT(*) FROM MEDIA) AS DECIMAL) * 100 AS success_percentage;