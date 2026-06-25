"""
**Statistical Functions**
1. np.sum(a)
   -> Sum of all elements
 
2. np.mean(a)
   -> Average = Sum of elements / Number of elements
 
3. np.median(a)
   -> Middle value after sorting
 
4. np.min(a)
   -> Smallest value in array
 
5. np.max(a)
   -> Largest value in array
 
6. np.var(a)
   mean,difference,square,average | (sum = ddof) -> divide by array length
 
7. np.std(a)
   -> Standard Deviation = √Variance
   -> Measures spread of data
 
8. np.prod(a)
   -> Multiplication of all elements
 
9. np.cumsum(a)
   -> Cumulative (running) sum
 
10. np.cumprod(a)
    -> Cumulative (running) product
 
11. np.argmin(a)
    -> Index position of minimum value
 
12. np.argmax(a)
    -> Index position of maximum value
 
13. np.abs(a)
    -> Converts negative values to positive
    -> Absolute value (distance from zero)
 
14. np.unique(a)
    -> Returns unique values only
    -> Removes duplicates
 
15. np.percentile(a, 50)
    -> Finds percentage-based value
    -> 50th percentile = Median
 
16. np.quantile(a, 0.5)
    -> Similar to percentile
    -> 0.5 = 50%
 
17. np.ptp(a)
    -> Range = Max - Min
 
28. np.any(a)
    -> True if at least one value is True
"""

import numpy as np
arr=np.array([10,20,30,40])
print("Sum of element:",np.sum(arr))
print("Average of elements:",np.mean(arr))
print("Median of elements:",np.median(arr))
print("Minimum element:",np.min(arr))
print("Max element:",np.max(arr))




