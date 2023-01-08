Personal notes for [LambdaClass' hacking learning path](https://github.com/lambdaclass/lambdaclass_hacking_learning_path/).

These may be useful to you, although that's not their purpose (for now).

# Foundations

## Unix

  * How does complexity relate to modularity? 
    * Modularity, abstraction and composition are extremely useful in many areas of human knowledge. **Dividing** a big system in smaller and simpler parts is the best way of **conquering** complexity, agilizing development.
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
    * Definitive solutions don’t exist most of the times, code will break and grow indefinitely. Definitive coding weakens a program's extensibility.

## Linux

* What do the following commands do?:
  * ls -l /bin/usr > ls-output.txt 2>&1
    * Redirects the stdout (file descriptor 1) of ls -l /bin/usr (list of files in /bin/usr) into a file called ls-output.txt and redirects stderr (descriptor 2) into stdout.
  * ls /bin /usr/bin | sort | uniq | less
    * Sorts and filters for unique lines the file lists of /bin and /usr/bin directories, opens the result with less.
  * ls /bin /usr/bin | sort | uniq | grep zip
    * The same as above but outputs lines that contain 'zip' instead of opening in less.
* How does Linux determine how to interpret the format of a file?
  * The 'file' program executes different tests (filesystem tests, magic tests and language tests) over its arguments, and the first test that passes will determine that file's type (which the program will output in text). Info extracted from the 'file' manpage. In Linux there's no concept of a file type extension, each program will interpret a file depending on its contents.
* What does the sda2 folder represent?
  * 'sd' stands for SCSI disk, 'a' means that its the first disk device in the system (there could be 'b, c', 'd'... disks) and '2' stands for the second partition of that disk. So the 'sda2' folder contained in the /dev (device) directory represents the second partition of the first disk installed in the system.
* What do /root and /usr/bin store?
  * /root is the home directory of the root user. /usr/bin contains binaries shared by all users of a system.
