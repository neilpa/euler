-- Powerful digit sum
-- Problem 56
--
-- A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100
-- is almost unimaginably large: one followed by two-hundred zeros. Despite their size,
-- the sum of the digits in each number is only 1.
--
-- Considering natural numbers of the form, ab, where a, b < 100, what is the maximum
-- digital sum?

-- Digits without converting to string
digits :: (Integral a) => a -> a -> [a]
digits b n
    | (n < 0) = digits b (abs n)
    | n < b = [n]
    | otherwise = (n `mod` b) : digits b (n `div` b)

p56 = [sum $ digits 10 (x^y) | x <- filter (\x -> x `mod` 10 /= 0) [99,98..2], y <- [99,98..2]]

