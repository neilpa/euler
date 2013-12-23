-- 1000-digit Fibonacci number
-- Problem 25
-- The Fibonacci sequence is defined by the recurrence relation:
--
-- F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
-- Hence the first 12 terms will be:
--
-- F_1 = 1
-- F_2 = 1
-- F_3 = 2
-- F_4 = 3
-- F_5 = 5
-- F_6 = 8
-- F_7 = 13
-- F_8 = 21
-- F_9 = 34
-- F_10 = 55
-- F_11 = 89
-- F_12 = 144
--
-- The 12th term, F_12, is the first term to contain three digits.
--
-- What is the first term in the Fibonacci sequence to contain 1000 digits?

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
limit = 1000

-- The first term with 1000 digits
--p25 = head $ dropWhile (\x -> (length x) < limit) (map show fibs)

-- The answer to the question - we have an extra 0 as the first element of
-- fibs so we don't have to add one to get the first time with >1000 digits
p25 = length $ takeWhile (\x -> (length x) < limit) (map show fibs)

