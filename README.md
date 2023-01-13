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

## Networking

<details>
<summary>'How the Internet Really Works' notes</summary>

#### Chapter 1
* A network is composed of nodes which represent devices that transceive information.
* Every node has an address (in the internet's case, an Internet Protocol (IP) address).
* Devices called routers connect to different networks for directing IP packets (data between nodes).
* Servers are network nodes that provides services by transmitting, processing and receiving information from clients, devices which connect to these and consume services.
* A network can be centralized (with clients connecting through a main router), decentralized (where many routers and clients connect to each other) and **distributed** (where are nodes all equal and can act as clients and servers)>

#### Chapter 2
* Devices talk through packets of data which contain both routing information and content.
* Packets are codified into binary data that can be transmitted via different physical phenomena (electrical, optical and radiofrequency)

#### Chapter 3
* There are different protocols that define the details of how a device can transmit and interpret packets (TCP, UDP, QUIC).
* Different international organizations are in charge of designing, defining, implementing and standarizing internet protocols.
* Each device is assigned a unique IP address in a network for identifying it. In the present we use IPv4 and IPv6 formats for these.
* When a device sends a packet from a private address to the internet, it does through its network router and it retags packets using NAT (Network Adress Translation) before sending them to the next router the can (probably the ISP's), this next router does the same. Each router will verify if the destination address is located inside its own network so it knows where to send the packet next, until it reaches its destination.
* The Internet Protocol Security (IPSec) authenticates packets and drops those that appear invalid or maliciously modified (for example, the packet may have a fake sender IP address, this being called IP spoofing). IPSec is not widely used because of its complexity.

#### Chapter 4
* The internet is made by the interconnection of small networks called autonomous systems, which are administered independently from each other.
* This interconnection is made possible by the border Gateway Protocol (BGP), which defines information about packets routes and makes possible calculating the shortest path for a packet.
* Two big AS can *peer* with each other, by letting data flow between each other toll free. BGP also considers *transit*, by calculating the toll that an AS needs to pay for communicating with a non-peer.
* An Internet Exchange Point (IXP) is a physical connection of hundreds of ASs. ASs connected in a same IXP are automatically peers. These devices help create faster interconnections between networks.
* Data can be split in multiple packets and transported following several protocols (UDP, TCP, QUIC).
* UDP splits data in "datagrams" and packages it with information about the software that process the data both in the source and origin. UDP is used when delayed packets and error correction aren't critical issues (like video streaming and online gaming).
* TCP on the other hand offers guarantees for packet reliability and correctness by establishing a communication channel (pipe or stream) between two nodes and verifying that all required packets arrive and are valid. If a packet gets lost or is damaged, it needs to be resent and every other packet needs to wait for it. This makes TCP slower.
* QUIC aims to be a middle option between these two, by using UDP for transmitting but adding extra information to datagrams that will be used in the receveing end for verifying data integrity. Packets don't need to wait for errors to be solved.

#### Chapter 5
* A Domain Name System (DNS) is used for linking an IP address (or other data formats) to a unique text name. This is because addresses are long a difficult to remember.
* Domain names can be split in different components which are sold and administered by different entities.
* **Example:** *unique-and.memorable.com*
  * *unique-and* is the hostname, which is administered by the domain owner.
  * *.memorable* is the second-level name, administered by registrars and domain owners.
  * *.com* is the top-level name, administered by registries and TLD Operators.
* A home router contains a local DNS resolver that is in charge of delivering your device the IP address associated with a domain name. If the local DNS doesn't know it, it asks the root server (highest hierarchy). If the root doesn't know, it sends the address of the top-level name registry server so the local can ask. This cycle repeats all the way to the bottom of the hierarchy until the full domain name is retrieved.
* The DNS Security Extensions protocol (DNSSEC) digitally signs DNS data for authentication so DNS lookups can not be hijacked by a malicious actor.
* Even with DNSSEC, every DNS request is public. So DNS over HTTPS protocol (DOH) was created to protect the requests from intermediaries and identify trusted DNS providers.
* HTTP (Hypertext Transfer Protocol) is the widely used protocol for exchanging hypertext over the WWW. It defines how data will be requested and sent between web browsers and servers using TCP under the hood.
* Secure HTTP (HTTPS) adds a layer of encryption into HTTP messages using the Transport Layer Security protocol (TLS).
* TLS works by establishing a connection between two nodes by sharing a secret key through a handshake, which will enable the transmission of encrypted data. Third-party organizations called certificate authorities issue certificates to services, so users can verify they are communicating with a trusted node via TLS.
* Cryptography is used for securing internet communications. Two cryptographic techniques are used today: signing and encryption.
  * Signing works by applying a unique sign into data that wants to be sent. The recipient will have a copy of that sign and will compare it with the message received. If the sign is missing or altered from the original, then the message can not be authenticated.
  * Encryption is an operation whereby a text message is *encrypted* into ciphertext, which can't be interpreted directly, one needs to know the encryption algorith (cipher) and the key that was used with it to decrypt the message.
    * If the encryption technique is symmetric, this means that both the sender and the receiver have the same key.
    * If the technique is asymmetric, then the receiver has a private key and the sender has the receiver's public key, which can use to encrypt a message only the receiver can decrypt with its private key.
* Transport encryption is used to secure communications between nodes in a network.
* Seemingly secure encrypted communications can have many weaknesses, like being vulnerable to machine-in-the-middle attacks or secret backdoors.
</details>


<details>
<summary>'Practical Packet Analysis with Wireshark' notes</summary>

#### Chapter 1
* Packet analysis is the process of capturing and interpreting data flowing across a network. Packet analysis is performed by a packet sniffer.
* The Open Systems Interconnection (OSI) model is an industry-recommended standard defined by the ISO, which establishes a hierarchical classification of network protocols depending on its different purposes. These are, from top to bottom: Application (HTTP, FTP), Presentation (ASCII, MPEG, JPEG), Session (NetBIOS, SAP, SDP, NWLink), Transport (TCP, UDP, SPX), Network (IP, IPX), Data Link (Ethernet, Token Ring, FDDI, AppleTalk) and Physical (wired, wireless. A useful mnemonic for these is *Please Do Not Throw Sausage Pizza Away*.
* When data needs to be transported it travels from the top to the bottom of the model, suffering different transformations (data encapsulation) until reaching the physical layer, in which the data is communicated from one device to another, and then climbs up again to the top layer where the user can consume it.
* There are three main kinds of network devices. Hubs operate at layer 1 and they repeat packets sent to it into every device that's connected to. Switches operate at layer 2 and transmit a packet only to its destination, by knowing every device identity (through a MAC address). Routers operate at layer 3 and work in a more complex way, enabling multiple networks of devices to communicate with each other.
* There are three ways of classifying traffic: broadcasting, in which a node sends packets to every device in its system; multicasting, in which packets are transmitted from a single source to multiple destinations simultaneously and unicasting, in which packets are transmitted from a source into a single destination.

#### Chapter 7
* The Address Resolution Protocol (ARP) is used for resolving an IP address into a MAC address when communication occurs in a local network and the addressee's MAC is missing. This protocol acts as a bridge between layers 3 and 2.
* An IPv4 address is a 32 bit number composed of a network portion and a host portion, defined by a network mask (which masks in binary the part of the address that identifies the network that a device is in. The remaining portion identifies the device itself).
* Every packet has a Time to Live (TTL), which defines how many times a packet can be sent from a router to another before it is discarded (so transmission loops can't exist).
* If a packet's data is bigger than the Maximum Transmission Unit (MTU), IP Fragmentation will split the packet
* An IPv6 address is 128 bits, as one of its reasons for existing is expanding the possible addresses that can exist in a network.
* The IPv6 address is also divided in a network and host portion, which distributions depends on its context. For example, in link-local unicast traffic (this is, direct traffic between two devices) starts with a characteristic set of 64 bits, and continues with the endpoint interface identifier, which could be a MAC address on an Ethernet network.
* IPv6 fragmentation doesn't happen too often as a device transmitting packets is expected to adjust its data to comply with the MTU before sending it.
* The Internet Control Message Protocol (ICMP) is used by TCP/IP for providing information about a network. The ping utility uses ICMP's echo request packets.

</details>

---

- How are data transmitted over the Internet?
  * Data needs to be parsed, transformed, encapsulated and encoded in packets through layers of network protocols (OSI model) until reaching an electromagnetic medium of transport. Inverse operations need to be made on the receiving end so data will appear the same as the one that was sent to the end user (traveling up the OSI layer).
- What functions do the layers of the OSI model perform?
  * Every layer manipulates data and executes actions with the goal of transmitting it. The top layers are in charge of manipulating and presenting data for the user to consume, and the lower are in charge of getting the data prepared and transmitting over devices in a network, by the use of many protocols.
- What is the difference between TCP and UDP?
  * TCP establishes a communication channel between two devices and strictly controls the flow and validity of the packets transceived. UDP transmits data in a format called "datagrams" and reconstructs it on the receiving end, without guaranteeing that packets will arrive in a valid state. This makes UDP faster than TCP at the expense of packet correctness.
- What does ARP mean?
  * ARP is the Address Resolution Protocol, which uses multicasting over a network to determine the hardware address of a device when only the IP address is known.
- What range corresponds to private IP addresses?
  * For IPv4: 10.0.0.0 to 10.0.255.255, 172.16.0.0 to 172.16.255.255 and 192.168.0.0 to 192.168.255.255
  * For IPv6, a link-local unicast address starts with the prefix *fe80* followed by padding and has 64 bits of addressable space, so: fe80:0000:0000:0000:/64.
- What does IPv6 propose to solve against IPv4?
  * The limited space of the 32 bit IPv4 addresses for representing information and devices.
- What does IPsec guarantee?
  * That packets received will be valid and not maliciously modified.
- What does DNS mean? How does it work?
  * DNS means Domain Name System, it is used for resolving domain names into IP addresses. The local router will resolve an address if it knows which corresponds to the solicited domain. If not, it will ask the root server. If the root server doesn't satisfy the request, it will lead the router into the next server which stores addresses corresponding to the top-level name of the domain. This is repeated through the layers of a domain name until the domain is found in a table list and the address is retrieved.
- What is the difference between HTTPS and HTTP?
  * HTTPS (or Secure HTTP) uses the TLS (Transport Layer Security) protocol, which works by establishing an encrypted communication stream between two nodes. The server needs to be certified by a CA (third-party) for it to use HTTPS. 
- What is the difference between asymmetric and symmetric cryptography?
  * In symmetric crypthography the origin and the receiver have the same copy of a public key which they can use to decrypt a message. In asymmetric the sender has a receiver's public key which can be used for encrypting a message only the receiver can decrypt using its private key.

## Git
I'll be writing only about things that caught my attention or that I didn't know before.

### Introduction
- Git is a distributed version control system. This means every device has a copy of all the history of a project in its own machine, and operations are mostly local.
- `git commit -a` stages every tracked file and commits.
- `git commit --amend` for replacing the last commit with a new one that includes the previous changes and the staged ones.

### Remotes
- Remote repositories (or remotes) are versions of a project which are hosted in a network. Collaborators may have their own remotes where they make changes to a project.
- The `origin` remote is the repo from where you cloned the project.
- `git remote add <shortname> <url>` adds a new remote as a shortname that you can reference for fetching (`git fetch <remote>`) or pushing (`git push <remote> <branch>`) changes.

### Tagging
- Git has the ability to tag specific snapshots of a repository's history.
- `git tag -l <expr>` searches for tags that matches the expression.
- There are lightweight and annotated tags. Annotated tags are chesummed, contain the tagger's information, a message and can be signed. `git tag -a <tag> -m <message>` for annotated, `git tag <tag>` for lightweight. 
- For sharing tags with other remotes, they need to be pushed: `git push <remote> <tag>/--tags`
- `git tag -d <tag>` removes tags, `git push <remote> --delete <tag>` shares the change.
- You can detach HEAD and explore where a tag is pointing with `git checkout <tag>`

### Branching
- Branches are pointers to commits (with each one having a pointer to the commit that precedes it in time).

### Rebasing
- Rebasing differs from a merge in that it changes a repository's history, by applying the current branch's commits that diverge from main (for ex.) after that branch. The current branch gets moved to that last commit and then you can fast forward main to your current branch for finishing the merging.
- **The Golden Rule of Rebasing** is to never use it on public branches, as you could create messy histories in your local machine or a peer's by fetching and pushing rebased commits.

Guide questions:

- Why is branching necessary?
  * To separate different versions of a project, depending whether a version is, for example, WIP (fixes and features are being developed) or released to production.
- What is the difference between `merge` and `rebase`?
  * Rebasing differs from a merge in that it changes a repository's history, by applying the current branch's commits that diverge from main (for ex.) after that branch. The current branch gets moved to that last commit and then you can fast forward main to your current branch for finishing the merging.
- What is a stash?
  * The stash is a stack of unfinished diffs from modified tracked files, which are stored for applying later in the same or a different branch, so the developer can work on something else.
- What does `cherry-pick` do?
  * When on a diverging branch, `cherry-pick` helps by cloning commits from another branch and adding them after the current branch.
- What does `reflog` do?
  * git stores local information about where was HEAD everytime it was moved. `reflog` returns a list of reference names that can be used in other commands.
- What does `git reset --hard HEAD` do?
  * It discards changes (and commits) made after the commit where HEAD points. `--hard` allows to modify the current working directory.
- How to get back to a previous commit?
  * `git checkout`
- How to do a pull request?
  * Fork the repo, create a new branch with a descriptive name about the changes, commit changes, push and then create the PR. If the changes are already made or commited it will be necessary to stash them (after soft-reset them if they were commited) and start again by creating a new branch, then popping the changes.
- Why are pull requests important?
  * They offer control over a projects development by allowing changes to be reviewed and tested.
- How to clone a repository using SSH?
  * First generate an SSH key pair in the machine and add it o GitHub. Then you can use the SSH domain for cloning a repo.

## Python
**Guide questions**
- How do you return how many times a certain character appears in a string using Python?
  * With the `count()` builtin.
- How do you handle different routes for your web app in Flask?
  * By making use of the `@app.route()` decorator.
- Using the `logging` library, how do you log to a file?
  * A FileHandler needs to be created to specify a file for logging into. This can be made manually or through the `basicConfig()` function.

## Docker
- Docker is a lightweight virtualization tool, it allows a machine to set a customized virtual environment from an *image*, coded through a simple script language (Dockerfile), without using a VM.
- Docker runs on the host OS and apps are executed inside *containers*, which are isolated processes with their own file system (UFS), networking, CPU and RAM allocated resources.
- Because of the isolated nature of containers, ports need to be explicitely exposed and mapped to machine's ports. Multiple services can communicate with each other by exposing ports with the help of an internal DNS, with these need to be mapped to the machine's so they can be externally accessed.
- Images can be pushed into DockerHub where they can be pulled back from another machine. They can also run through CI/CD or other services like AWS.
- Multiple docker services can be configured an run through *docker compose* **on a single machine**.
- Kubernetes is the most popular container orchestrator (this means that it can manage communications, resource management, error handling and scalability issues) that can work in a cluster of machines.
- Files copied into an image are burned one time and are read-only. A *volume* can be create for synchronizing files and directories from the local machine into the service.
- Docker will interpret each instruction in a dockerfile as a layer, this means that layers can be cached to optimize build times. When a layer needs to be updated, all layers below will too, this means that instructions need to be set in a specific order so that they're executed only when necessary.
- Dockerfiles can be multi-stage, for example, a builder stage can be made before a second stage, so the final image can be burned with the binaries built by the first stage.
- Docker containers are *volatile* and *short-lived*, they need to be designed so they can be easely discarded and replaced.

**Guide questions**
- In which scenarios would you use containers and in which you would prefer to use VMs?
  * VMs are preferred when needing to run an entire OS or different kernels than the host's. Containers would be preferred in every other situation where a VM's features aren't necessary, as containers are more lightweight and practical.
- How do you retrieve and run the latest ubuntu image?
  * By pulling an ubuntu image with `docker pull ubuntu:<optional tag>` and `docker run`
- In a Dockerfile, what is the difference between RUN and CMD?
  * With `CMD` you specify a command to run after launching the built image, there can be only one `CMD` in a dockerfile. `RUN` executes commands for setting up the environment and can create layers on final image as it may modify the file tree.
- Using port 8080, how do you run an image that exposes port 80?
  * With the `-p` flag with `docker run/create` you can map a container's port into a host's. In this case: `-p 8080:80`. This is also possible to do in a `docker-compose.yml` file, if using docker compose, via the `ports` key.

## Databases
### SQL
- The Structured Query Language (SQL) is desgined to query, manipulate and transform data from a relational database.
- A relational database represents related (two-dimensional) tables.
- A Database Management System (DBMS) is used for creating and managing databases. There're many DBMS for every database paradigm.
- SQL follows the CRUD mnemonic (Create, Read, Update, Delete) in its instructions.
#### PostgreSQL
- PostgreSQL is a reational DBMS (RDBMS). It's one of the most robust and tested DBMS.
- PostgreSQL allows for *stored procedures* to be created and use. These are a set of imperative instructions with logical control flow written in a language called PL/pgSQL (Procedural Language/PostgreSQL). PostgreSQL also supports Tcl, Perl and Python.
- Triggers can be created so they can fire up functions when events happen in the database (like a table update)>
- After a complex query, a virtual table cloning the result can be created, this is called a *view*.
- PostgreSQL performs better in a monolithic environment than in a partitioned one.
#### Redis
- Redis (Remote Dictionary Service) is a NoSQL key-value store DBMS focused on speed.
- Redis has builtin a set of plenty data types, like floats, strings, (linked) lists, hashes, sets and sorted sets.
- A special data type called a HyperLogLog (HLL) is used for estimating the size of a set in constant time with an error less than 1%.

**Guiding Questions**
- How to use a wildcard as a character?
  * By wrapping the string in quotes and using the `ESCAPE` clause.
- What dodes `COALESCE` do?
  * `COALESCE` is a funcion that returns its first non-null argument.
- What dodes `LIKE 'S%` do in a query?
  * This is a condition that gets satisfied with a string which starts with an `S`.
- What is the difference between PostgreSQL and Redis?
  * PostgreSQL is robust, SQL and relational, while Redis is NoSQL, key-value and fast.
- What type of databases are the following? PostgreSQL, Redis, MongoDB, MySQL, HBase, Neo4J, DynamoDB.
  * Relational, key-value, document, relational, column-oriented, graph, key-value
- What makes each database type unique?
  * Its type and implementation or extension depending if its SQL or NoSQL.
