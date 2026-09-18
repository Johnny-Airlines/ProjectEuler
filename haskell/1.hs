-- Determines if an Integral is divisible by another Integral
divisibleBy :: (Integral n) => n -> n -> Bool
divisibleBy n d = n `mod` d == 0

-- Determines if an Integral is a multiple of three or five
divisibleBy3or5 :: (Integral n) => n -> Bool
divisibleBy3or5 n = n `divisibleBy` 3 || n `divisibleBy` 5

result :: Integer
result = sum (filter divisibleBy3or5 [1 .. 999])

main = print result
