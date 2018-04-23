# COMP30023: Computer Systems Tutorial Week 7
### Network Layer - IP Addresses and Packet Switching

### 1. Do routers have IP addresses? If so, how many?
- Each interface can have a IP address
- As many as the router has interfaces

### 2. Datagram networks route each packet as a separate unit, independent of all others. Virtual-circuit networks do not have to do this, since each data packet follows a predetermined route. Does this observation mean that virtual-circuit networks do not need the capability to route isolated packets from an arbitrary source to an arbitrary destination? Explain your answer.
- This is connectionless - so we don't need to establish a connection
	- Therefore there is no handshake datagram
- In the virtual-circuit network you define the path
- We need the ability to establish the connection in order to define a route
- Yes we need a way to establish the connection - once you have this route, you can just arbitrarily send stuff
	- If a switch is removed from the route - you'd have to find a new path

### 3. A network on the Internet has a subnet mask of 255.255.240.0. What is the maximum number of hosts it can handle?
- IP is made up of two parts:
	- Network and Host
	- 32 bits in a binary representation
- What is a subnet mask?
	- Describes number of bits in the address that are part of the network path
- Convert 255.255.240.0 to binary
	- 11111111.11111111.11110000.0
	- 20 bits used for network path
	- How many hosts? - 12 bits in host path
	- `~2^12 = 4096`
- Can represent subnet mask as 255.255.240.0 (i.e. decimal representation for 20 bits) or /20

### 4. A router has just received the following new IP addresses: 57.6.96.0/21, 57.6.104.0/21, 57.6.112.0/21, and 57.6.120.0/21. If all of them use the same outgoing line, can they be aggregated? If so, to what? If not, why not?
- Yes
- What is aggregation?
	- A router, given a list of IP addresses, will send packets through a specified interface
	- This is a routing table
- Check each mask if they have the same network mask

##### In binary (21 bits):
- `57.6.01100`
- `57.6.01101`
- `57.6.01110`
- `57.6.01111`
- Notice how all of these are the same up until the 20th bit

- Your decision to send it out of an interface does not change for the first 19 bits
- So you don't have 4 entries in the routing table, you can *aggregate these into* `57.6.96.0/19` since they have a *common prefix*
- This is called *longest prefix matching*

Address/mask | Next Hop
--- | ---
57.6.96.0/21	| Interface 0
57.6.104.0/21	| Interface 0
57.6.112.0/21	| Interface 0
57.6.120.0/21	| Interface 0

into 

Address/mask | Next Hop
--- | ---
57.6.96.0/19	| Interface 0

### 5. A large number of consecutive IP addresses are available starting at 192.48.0.0. Suppose that three organizations, A, B, and C request 4000, 2000, and 8000 addresses, respectively, and in that order. For each of these, give the first IP address assigned, the last IP address assigned, and the mask in the w.x.y.z/s notation.
A
- 4000 hosts -> 2^12 -> 12 bits in HOST -> 20 bits in N/W
- 20 bits | 12 bits
- Have to waste 4 bits to define boundaries
```
192.48.0000|0000.00000000 // First Address
      .0000|0000.00000001
 	  .0000|0000.00000010
	  .0000|0000.00000011
							// and so on until
 	  .0000|1111.11111111 // Last Address
```

B
- This *prefix* is defined for the organisation
- 2000 hosts -> 2^11 -> 11 bits in HOST -> 21 bits in N/W
- `192.48.0000` already used up
- so we move to the closest possible one: `192.48.00010|.........` (remember 21 bits not 20)

C
- 8000 addresses
- 8000 hosts -> 2^13 -> 13 bits in HOST -> 19 bits in N/W
- `192.48.001|.....`

### 6. A router has the following (CIDR) entries in its routing table:
Address/mask | Next Hop
--- | ---
135.46.56.0/22 | Interface 0
135.46.60.0/22 | Interface 1
192.53.40.0/23 | Router 1
default | Router 2

### For each of the following IP addresses, what does the router do if a packet with that address arrives?
- First we convert these into binary representations
- `135.46.001110|00.0`
- `135.46.001111|00.0`
- `135.46.0010100|0.0`
- If any incoming packets don't match the prefix, then send it via `default`

##### (a) 135.46.63.10
- 135.46.001111|11.0
- Interface 1

##### (b) 135.46.57.14
- 135.46.001101|10.0
- Interface 0

##### (c) 135.46.52.2
- 135.46.001101|00.0
- Doesn't match
- Interface 0

##### (d) 192.53.40.7
- Router 1

##### (e) 192.53.56.7
- Router 2

### 7. List one motivation for a host to send an IP packet with the wrong source IP address. List two ways that this can adversely affect the legitimate owner of that IP address. 
- DDoS
- The response is sent somewhere else so you DDoS that target
```
[source C, dest B] sent from A
A -> B -> C
// C gets overwhelmed
// Alternatively A pretends they are C so C gets blamed for whatever A is doing

```

### 8. The IP packet header includes a time-to-live field that is decremented by each router along the path. Why is the time-to-live field necessary?
- Time to live: After the specified amount of hops a packet is discarded
- Stop loops from happening and traffic congestion

### 9. Bonus for fun: IPv6 uses 16-byte addresses. If a block of 1 million addresses is allocated every picosecond, how long will the addresses last?
Even if you allocate this every pico second you won't run out.
It would take 10^13 years??????? wtf.
That's a lot of addresses