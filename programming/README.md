# Programming
- [Big-O Notation](#big-o-notation)
- [Python Design Pattern](#python-design-pattern)

## Big-O Notation
> The purpose of the Big-O notation is to find what is the dominant factor in the asymptotic behavior of a function as the value tends towards the infinity.
1. Find the fastest growing term
- **Why?**: e.g. `n^2 vs n`, as the n gets larger, n^2 will get much larger than n, and n will become less relevant
2. Take out the coefficient
- **Why?**: 
    -  Big-O notation has its origins independently in number theory, where one of its uses is to create a kind of equivalence between functions: if a given function is bounded above by another and simultaneously is bounded below by a scaled version of that same other function, then the two functions are essentially the same from an asymptotic point of view. The definition of Big-O (actually, "Big-Theta") captures this situation: the "Big-O" (Theta) of the two functions are exactly equal.
    -  Different computers with different architectures have different constant factors. A faster computer might be able to access memory faster than a slower computer, **so faster computers will have a lower constant factor for memory access than slower computers**. However, we're just interested in the algorithm, not the hardware, when doing asymptotic analysis, so we ignore such constant factors.
    -  As 𝑛→∞, constant factors aren't really a big deal. Constant factors are very small in the face of arbitrarily large 𝑛.
    -  **Overall**: we ignore constant factors because it removes a lot of the noise from hardware and small changes in algorithms that really aren't important for analysis, making algorithms easier to compare.

## Python Design Pattern
