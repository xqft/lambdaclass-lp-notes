Personal notes for [LambdaClass' hacking learning path](https://github.com/lambdaclass/lambdaclass_hacking_learning_path/).

These may be useful to you, although that's not their purpose (for now).

# Foundations

## Unix

How does complexity relate to modularity? 

  * Why is the text-stream interface important in the Unix Philosophy?
    * Text-streams are simple, universal and they enforce the encapsulation of the programs (by not exposing internals needed by more complicated communication processes)
  * Why should design for transparency encourage simple interfaces? 
    * One of the pillars of transparency is prioritizing simple solutions to promote clarity. Simple interfaces are part of this, a developer can debug, fix and expand code more quickly and effective if they understand the simple ways that a software’s modules interact with each other.sho
  * How does robustness relate to transparency and simplicity? 
    * When software is transparent and simple, it’s easier to understand and develop. This means that more of a developers brain real-estate can be assigned in making the solution more robust, and deep understanding of it can make its caveats obvious.
  * Even now with video processing, why output of programs should be terse?
    * Simple output formats go along with Unix’s principles of transparency and simplicity.
  * According to the Unix Philosophy, how noisy do errors have to be?
    * A hell lot. The noisier a program fails, the better and quickly it is to diagnose and fix.
  * How does economy of programmer time relate to robustness?
    * A robust program is a program that needs fewer patches, and so less time spent working on.
  * Why premature local optimization reduces overall performance? 
    * Premature local optimization leads to overcomplex code that may not represent a boost in performance in the overall program, just a waste of present and future time.
  * There is the approach of doing things in "one true way", how does it affect extensibility? 
    * Definitive solutions don’t exist most of the times, code will break and grow indefinitely. Coding definitely directly weakens a program extensibility.
