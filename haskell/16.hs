-- Power digit sum
-- Problem 16
--
-- 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
--
-- What is the sum of the digits of the number 2^1000?


-- Digits without converting to string
digits :: (Integral a) => a -> a -> [a]
digits b n
    | (n < 0) = digits b (abs n)
    | n < b = [n]
    | otherwise = (n `mod` b) : digits b (n `div` b)

p16 = sum $ digits 10 (2^1000)

