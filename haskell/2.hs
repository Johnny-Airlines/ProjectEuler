-- Even fibonacci sum up to limit of fibonacci number
fibonacci :: (Integral n) => n -> n
fibonacci limit = go 0 1 0
  where
    go !a !b !sum
      | b >= limit = sum
      | even (a + b) = go b (a + b) (sum + a + b)
      | otherwise = go b (a + b) sum

result :: Integer
result = fibonacci 4000000

main = print result
