Sanskriti Timseena

for number 1:
This question took me a long time to complete. I watched Daniel's video a few times and also this youtube video:
https://www.youtube.com/watch?v=jpmZp3eX-wI. I really liked the part where he talks about value iteration.
It took me a while to understand what kind of datatype Counter is and what methods to use with it.
What really helped was trying to go back to the high level picture of what we're trying to do.
After I was done with this one, i was relieved that question 2 and 3 weren't as difficult as this one.

for number 2:
I started by changing noise first.
When noise = 0, we win and go to the high reward terminal state.
0.1 or 0.2 also go to low reward terminal state.
0.3 low reward terminal state
When the noise is above 0.6, we have policy going to the chasm of high negative reward, that is bad.
Now let's change discount:
Keeping noise at 0.2 and decreasing discount, it seems that the values on each square of the grid increases to a bigger negative number, or closer to zero.
The policy has not changed until 0.2 discount
At discount 0, the policy in the bridge changes to pointing towards the charms upwards which is really bad.
With a really low (close to 0) noise, i changed the discount
When i decrease the discount, the values remain positive in the grid, but the values decrease.
So i think it's better to have a high discount and low noise

for number 3:
I decided to skip 3a and 3b. It was taking too long to figure out and i decided i needed to move on to the next project.
Using the visualization to look at the policy arrows really helped me in this one.

