-- Determines if an Integral is divisible by another Integral
divisibleBy :: (Integral n) => n -> n -> Bool
divisibleBy n d = n `mod` d == 0

-- Determines if an Integral is prime
isPrime :: (Integral n) => n -> Bool
isPrime n = go 2
  where
    go !factor
      | factor * factor > n = True
      | n `divisibleBy` factor = False
      | otherwise = go (factor + 1)

-- Largest prime factor
largestPrimeFactor :: (Integral n) => n -> n
largestPrimeFactor n = go n 2
  where
    go n factor
      | factor * factor > n = n
      | n `divisibleBy` factor = go (n `div` factor) 2
      | otherwise = go n (factor + 1)

main = print (largestPrimeFactor 600851475143)
