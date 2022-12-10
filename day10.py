"""
Cathode Ray Tube

Consider the following small program:

```
noop
addx 3
addx -5
```
Execution of this program proceeds as follows:

    At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. After the
    first cycle, the noop instruction finishes execution, doing nothing.
    At the start of the second cycle, the addx 3 instruction begins execution. During the second cycle, X is still 1.
    During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes execution, setting X to
     4.
    At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth cycle, X is still 4.
    During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes execution, setting X
    to -1.


commands
--------
- addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
- noop takes one cycle to complete. It has no other effect.

signal strength: the cycle number multiplied by the value of the X register

Part 1: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these
 six signal strengths?

"""