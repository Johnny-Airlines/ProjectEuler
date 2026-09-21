import Prelude hiding (gcd, lcm)

divisibleBy :: Int -> Int -> Bool
divisibleBy n d = n `mod` d == 0

gcd :: Int -> Int -> Int
gcd !a !b
  | b == 0 = a
  | otherwise = gcd b (a `mod` b)

lcm :: Int -> Int -> Int
lcm a b = (a * b) `div` (gcd a b)

lcmMany :: [Int] -> Int
lcmMany list = go (drop 2 list) (lcm (list !! 0) (list !! 1))
  where
    go list result
      | list == [] = result
      | otherwise = go (drop 1 list) (lcm result (list !! 0))

main = print (lcmMany [1 .. 20])
