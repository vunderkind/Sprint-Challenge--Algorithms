#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
First line complexity: O(1) (because assignment)
Second-line complexity: O(n) (because it's a function of the number of items entering the while loop)
Third line complexity: O(1) because assignment.

Big O notation verdict: O(n)

b)


c)

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

The first assumption I'm making in this exercise is that there are more eggs than storey-buildings. Which means that we can theoretically drop eggs from each floor. The storeys can be represented as an array, with the indices/indexes representing floors. 

storey = [1,2,3,4,6,7,8,9...n]
We want to find a point in the story where, if we drop eggs, as few as possible are broken. 

The real challenge is we don't know where f will be (close to the top, or closer to the bottom?) but we also want to drop as few eggs as possible while testing for f. 

To this end, the first thing we'll do is set f to be len(story)/2. This gives us the midway point of the storey building.

At this point we drop the egg. If it breaks it means (new) f is higher than target f (the f we're looking for), so we divide f by 2 again, then drop an egg. We do this until we drop an egg that doesn't break, then we work our way upwards in increments of 1. 

Conversely, if we drop an egg at the first f and it doesn't break, it means that we've either found f or gone below f, so we have to keep 

In a nutshell, the solution for finding f is a binary search, and here's the pseudocode: 

1. last_floor = len(storey)
2. First_floor = 1
3. Middle_floor = len(story)/2
4. Drop an egg from middle floor. Does it break?
4a. If 'yes', it means we've gone too high up the storey building. Eliminate the whole upper half of the building. 
4b. If 'no' it means we're still too low on the building. Eliminate the whole lower half of the building.
5. Middle_floor = (find the halfway point of the remaining floors)
6. Iterate until we locate the one floor. 

The runtime complexity of this algorithm is O(log n)

