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
* Secure HTTP (HTTPS) adds a layer of encryption into HTTP messages suing the Transport Layer Security protocol (TLS).
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
