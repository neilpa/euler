-- Largest prime factor
-- Problem 3

-- The prime factors of 13195 are 5, 7, 13 and 29.

-- What is the largest prime factor of the number 600851475143?

import Data.Numbers.Primes

x = 600851475143
limit = floor $ sqrt x
candidates = reverse $ takeWhile (<limit) $ primes

p4 = head $ filter (\n -> x `mod` n == 0) candidates

--primes :: [Integer]
--primes = 2 : 3 : filter isPrime [5,7..]
--  where
--    isPrime n   = all (notDivs n) $ takeWhile (\p -> p^2 <= n) (tail primes)
--    notDivs n p = n `mod` p /= 0
--
--isSquare :: Integer -> Bool
--isSquare n = p * p == n
--
--primeFactors :: Integer -> [Integer]
--primeFactors n
--    | isSquare = replicate 2 (primeFactors p)
--    | otherwise = []
--    where
--        p = floor $ sqrt $ (fromIntegral n::Double)
--        isSquare = p * p == n
--
-- possibilities
--factors n = [2..(ceiling (sqrt n))]

