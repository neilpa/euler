-- 10001st prime
-- Problem 7
--
-- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
--
-- What is the 10 001st prime number?


primes :: [Integer]
primes = 2 : 3 : filter isPrime [5,7..]
  where
    isPrime n   = all (notDivs n) $ takeWhile (\p -> p^2 <= n) (tail primes)
    notDivs n p = n `mod` p /= 0


x = 10001
p7 = last $ take x primes
--
