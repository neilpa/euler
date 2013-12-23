-- Self powers
-- Problem 48
--
-- The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
--
-- Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

p48 = drop ((length n)-10) n
    where n = show $ sum [ x^x | x <- [1..1000] ]

