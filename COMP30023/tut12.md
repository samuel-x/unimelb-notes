# COMP30023: Computer Systems Tutorial Week 12
## Revision
### 1. Which of the OSI layers handles each of the following:
### a) Dividing the transmitted bit stream into frames.
- Data link layer

### b) Determining which route through the subnet to use.
- Data link layer

### 2. True or false? Consider congestion control in TCP. When the timer expires at the sender, the value of ssthresh is set to one half of its previous value.
- False
- Half of the *current* window size *not the threshold*

### 3. Consider the effect of using slow start on a line with a 10-msec round-trip time and no congestion. The receive window is 24 KB and the maximum segment size is 2 KB. How long does it take before the first full window can be sent?
- Each round trip doubles the segment size
- So about 40 msec
- 2kb 10msec, 4kb 20msec, 8kb 30msec, 16kb 40msec, 32kb 

### 4. TCP waits until it has received three duplicate ACKs before performing a fast retransmit. Why do you think the TCP designers chose not to perform a fast retransmit after the first duplicate ACK for a segment is received.
- Why do we wait for three ACKs?
- If your packets arrive out of order and you receive newer packets than what you expected then you need to make sure the old packets arrive
	- If it's three ACKs, it's unlikely to be an ordering issue

### 5. Your friend states that the Transport Layer in routers do not need to worry about in-order forwarding of packets when TCP is employed. Do you agree with their statement? In in-order delivery which layer receives packets in order?
- Disagree
	- This statement is correct but the transport layer in routers doesn't exist - routers only go up to the network layer
	- Transport is *end to end* so client to host
- *Application Layer gets packets in order*, but *Transport layer does not*

### 6. In what way does an encrypted message hash using public-key cryptography provide a better digital signature than an encrypted message?
- Recap: Signature is a message which is hashed and then encrypted with the private key of a CA
- Encrypted message hash is easier to compute since encrypting the whole message is *resource intensive*

### 7. Consider a subnet with prefix 128.119.40.128/26. Give an example of one IP address (of form xxx.xxx.xxx.xxx) that can be assigned to this network. Suppose an ISP owns the block of addresses of the form 128.119.40.64/26. Suppose it wants to create four subnets from this block, with each block having the same number of IP addresses. What are the prefixes (of form a.b.c.d/x) for the four subnets?
- What is a subnet mask?
	- Lets us split an IP between the *host* and *network* part
- What's the subnet in 128.119.40.128/26? 26
	- `128.119.40.10|000000`
	- `128.119.40.10|000001`
	- ...
	- `128.119.40.10|111111`
- You can have a range from .128-.191 in that example
- Now for the question:
	- `128.119.40.64/26`
	- `128.119.40.01|000000`
	- `128.119.40.01|00|0000` .64/28 <- four subnets
	- `128.119.40.01|01|0000` .80/28
	- `128.119.40.01|10|0000` .96/28
	- `128.119.40.01|11|0000` .112/28
		- 

### 8. Consider a router that interconnects three subnets: Subnet 1, Subnet 2, and Subnet 3. Suppose all of the interfaces in each of these three subnets are required to have the prefix 223.1.17/24. Also suppose that Subnet 1 is required to support up to 63 interfaces, Subnet 2 is to support up to 95 interfaces, and Subnet 3 is to support up to 16 interfaces. Provide three network addresses (of the form a.b.c.d/x) that satisfy these constraints.
- All required to have the prefix 223.1.17/24
- `223.1.17.|00000000`
- Subnet 1 needs 63 interfaces -> (2^6) -> 6 host bits
	- `223.1.17.|10000000`
- Subnet 2 needs 95 interfaces -> (2^7) -> 7 host bits
	- `223.1.17.|01000000`
- Subnet 3 needs 16 interfaces -> (2^4) -> 4 host bits
