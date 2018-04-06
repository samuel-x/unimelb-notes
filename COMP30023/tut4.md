# COMP30023: Computer Systems Tutorial Week 4
# TCP and Memory Management

### 1. Indicate whether TCP or UDP (or both or neither) provide the following services to applications:
**(a) Reliable data transfer between processes**

tcp

**(b) Minimum data transmission rate between processes**

neither

**(c) Congestion-controlled data transfer between processes**

tcp

**(d) A guarantee that data will be delivered within a specified amount of time**

neither

**(e) Preserve application-level message boundaries. That is, when a sender sends a group of bytes into a socket via a single send operation, that group of bytes will be delivered as a group in a single receive operation at the receiving application**

udp

**(f) Guaranteed in-order delivery of data to the receiver**

tcp

### 2. Why does UDP exist? Would it not have been enough to just let the user processes send raw IP packets?
You need port numbers - this allows us to forward packets from one process to another
IP address is what computer to go to - port number is the process to go to

### 3. Both UDP and TCP use port numbers to identify the destination entity when delivering a message. Give two reasons for why these protocols invented a new abstract ID (port numbers), instead of using process IDs, which already existed when these protocols were designed?
- Process IDs are not static - they're not constant - a process ID may be different every time it starts up.
- Using only process IDs only allow one connection - using port numbers allows multiple connections
- You also don't know your process ID since there's no way to advertise it
- "Well known ports" - e.g. web server is usually port 80 - 25 for mail, 22 for SSH, 194 for IRC
- An application will request to listen on a certain port
- Multiple processes cannot interact with the same port
	- Initial connection is usually the same port and then it'll set up a different session?
	- Can have a master process which will manage
	- two tabs in chrome will run on separate pors
- Process IDs are OS-dependent - hard to standardise that
- Port numbers are not related to port numbers

### 4. Suppose you use UDP to do a transaction from a remote client to a server. UDP provides no reliability, but you want your transaction request to be sent reliably. How could you do is?
- You don't only have to have reliability in the Transport layer, you could easily do that within the application
- 	just asking each process to send requests/acks whenever required even though the layer below it would not do it
- 	no in order delivery but will have reliability

### 5. A process on host 1 has been assigned port p, and a process on host 2 has been assigned port q. Is it possible for there to be two or more TCP connections between these two ports at the same time?
(1, p) (2, q)
- This cannot happen - since a TCP connection is only between two ports

### 6. Give an arithmetic expression connecting a given virtual address with the corresponding page number and offset. What does this tell you about page sizes that are not powers of two?
- Virtual address - a virtually assigned spot for your physical address
- Each process will have it's own virtual address
- Memory Management Unit will translate virtual addresses to physical addresses
- A section in the virtual address is called a "page"
- A section in the physical address is called a "pageframe"
- Swap space is on disk - take stuff out of page frames and put it on disk when required
- You find a virtual address by counting how many pages from the bottom
- The page file is determined by the architecture of the system
- Find the virtual page first: `virtual page = floor(virtual address/subject page)`
- Sizes of pages are usually in powers of 2 so you can always do bit operations and are easier on the CPU
- Find the address after you have the page:`virtual_address = virtual_page# x size_virtual_page + offset`


### 7. How much physical memory do you need to store a page table describing
**(a) 512 KB** 
- Each page is 512 bytes
	- Number of pages = `512 * 10^3 / 512` = 1000 pages
- Each page has a mapping of 4 bytes (1 page table entry)
	- `1000 * 4 bytes` = 4kB total

- Each page will correspond to a page frame
- This is recorded by the PTE (page table entry)

**(b) 4 GB given a page size of 512 bytes? How much do you need given a page size of 8 Kb? Assume that PTEs are 4 bytes in either case.**
- Each page is 512 bytes
	- number of pages = `4 * 10^6 / 512` = 7812.5

### 8. Consider a system with 32-bit logical addresses, 24-bit physical addresses, and the system uses paging to manage memory. A page frame holds 4096 bytes. What is the maximum number of entries in the page table?
- 12 bit offset
- Both logical/physical address have 12 bit offset
- so for virtual addresses -> we have 20 bits left over
- 2^20 ~ 1 million page table entries 
- 2^30 ~ 1 billion
- the MMU manages mapping but the offset is just stuck on the end

### 9. Bonus: What is meant by the term thrashing?
This is meant by when you don't have enough memory and you have a lot of swapping -> hard disk crash