-- SQL Verification Script
-- Detect duplicate IDs
SELECT ID, COUNT(*) AS CountOccurrences
FROM sql_verification_sample_data
GROUP BY ID
HAVING COUNT(*) > 1;

-- Detect missing amounts
SELECT *
FROM sql_verification_sample_data
WHERE Amount IS NULL;

-- Compare amounts between two tables (simulate verification)
-- CREATE TABLE sql_verification_sample_data_verification (...);
SELECT a.ID, a.Amount AS OriginalAmount, b.Amount AS VerifiedAmount
FROM sql_verification_sample_data a
LEFT JOIN sql_verification_sample_data_verification b
ON a.ID = b.ID
WHERE a.Amount <> b.Amount;
