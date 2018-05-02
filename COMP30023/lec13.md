# Computer Systems - Lecuture 13 - Datalink Layer

### Data Link Layer
##### Ethernet
###### Two flavours:
- Classic
- Switched

Ethernet is old af and not made with a lot of modern features in mind.

##### Link Layer Purpose
- Provides algorithms for *communicating between two adjacent machines*
	- Adjacent means two machines connected by a wire or something equivalent
- Focus on Local Area Networks (LAN)
- Link layer Abstractly Provides:
	- Interface for the network layer
	- Error detection/correction
	- Flow control
- Protocol data unit is a *frame*
- 3 possible services
	- Unacknowledged connectionless service
		- Ethernet - low error rate
	- Acknowledged connectionless service
		- 802.11 wifi - unreliable channel
	- Achnowledged connection-oriented services
		- Asychronised Transfer Mode
		- This is dying out

#### Medium Access Control Sublayer
- Sublayer below the link layer
- Sublayer allows you to abstract different methods of transfer
- Network links categorised as:
	- point to point
	- Broadcast channels
- In broadcast channels we need some way or determining why can use the channel when there is conpetition for it
	- Who gets to send their shit first??

##### Duplex connections
- Duplex connections are point-to-point connections between two parties
- **Full Duplex**: You can communicate *simultaneously* like on a telephone
- **Half Duplex**: one at a time e.g. walkie-talkie radios
- Half duplex lets you have a longer cable
- Originally had a huge effect on the length of the cable we could use

### Broadcast channels collicions
- We need to avoid collisions where two people broadcast shit at the same time
- **CSMA/CD** - Carrier sense multiple access with collision detection
	1. Station that wants to send listens to channel
	2. If the channel is idle it sends its data
	3. Otherwise waits for channel to become idle
	4. If a collision occurs, wait a random amount of time and start all over again
		- Stops 'deadlocks' where we keep colliding and waiting
- Ethernet started as broadcast but now it's point-to-point 
	- Bus -> hubs -> switches
- Collisions checked by monitoring and checking if the *same signal that was transmitted is received*, if not, indicates a collision has occured
- Time taken to determine whether a collision has occured is based on the time for data to propagate between the two furthest stations
- The time taken to detect collisions puts a limit on cable length and send speed.
	- If the cable is too long and you send data too fast and collide before you can detect it then you have no way of avoiding collisions and everything's shit

### Ethernet
- Most ubiquitous kind of network in the world
- Classic ethernet - broadcast - no longer used
- Switched ethernet - point-to-point - used today
- Defined mostly in IEEE 802.3

#### Classic Ethernet
- Standardised in 1978 by Xerox
- Became 802.3
- Ether/Bus - all people tap into this really long cable together
	- Send something along the line, if it's for you take it otherwise pass it along
	- Terminate at ends of line

##### Ethernet Frames
```
[8][6][6][2][0-1500][0-46][4]

Ethernet (DIX)
[Preamble][Destination Address][Source Address][Type][Data][Pad][Check-sum]

Ethernet IEEE802.3
[Preamble][SOF][Destination Address][Source Address][Length][Data][Pad][Check-sum]
```
- Link layer kinda breaks layer structure
- People don't like type vs length
	- Breaks layers
	- Ambiguity since everything under size 1500 is length, otherwise it's type
- Preamble contains 8 bytes
- Destination and source address - 6 bytes each
	- If destination begins with 0 it's an ordinary address
	- Otherwise it's multicast
	- If all bits are 1 it's broadcast
- Have to pad it if it's under a certain length

### Classic Ethernet
- **t h i c c** ethernet (10BASE5)
	- thick coaxial cable
	- maximum length of 500m per segment
	- maximum of 100 machines per segment
	- vampires
		- Drill holes into network cable to insert connection
- Thin ethernet (10BASE2)
	- Coaxial cable like your TV cable
	- Maximum length of 185m per segment
	- Max of 30 machines

### Classic Ethernet - Bus Model
- Repeaters
	- Device that receives, amplifies and retransmits signals to allow two segments to be joined
- Simple to setup and operatoe
- No need for additional networking hardware beyond the cable
- Easy to add additional station
- Susceptible to problems with bad connections
- Tripping over a cable = bring down the entire network

### Classic Ethernet - Hub Model
- Everything would run to the hub
- Hub acts like all cables are connected together
- Increased cabling complexity
- Literally cost more with more cables to do the same thing as the bus model
- Fixed capacity
- Have to share power between number of hosts

### Switched Ethernet
- Switches are devices which send data to specific destinations instead of flooding the entire network
- Determined by monitoring incoming packets with their machine's MAC addresses
	- Learnt MAC addresses by flooding all ports to test (i.e. like ARP)
- Needs a intense backplane to handle all the different data going into different places
- Why people spend millions on switches - no saturation
- Every port also needs a buffer since two people may communicate with something on the same port

### Hubs vs Switches
- Hubs have to handle collisions since everything is broadcast and run on the same line
- Switches are point-to-point so we don't need to account for collisions and they're *so much faster*
	- Switches also improve performance
	- Security benefits since everyone only receives data directed for them

### Fast Ethernet
- Eventually everyone had a mix of bus, hub and switched ethernet
- Still not fast enough
- Cables everywhere and now everything is on fire
- I want to die
- We need to *i m p r o v e* this
- `we have the technology`
- They just made the cable faster lol
	- This is the cat5 cable we now all know
	- They're hard to wire up
	- Backwards compatible
	- For some reason the spec says they should be yellow
	- Some of them have fibre optics and those are real fast and long cause you can send more

### 10 Gigabit Ethernet
- 1000x faster than original Ethernet
	- Also 420x cooler and healthier
- Primarily used in data centers and exchanged
	- Requires high end routers/interfaces 
- Full duplex point to point
- No collision detection CSMA/CD so it's fast af

### Summary
- 30 years later and it's still pretty popular
- Backwards compatability was the most useful part since you could upgrade incrementally
- You could swap out a hub for a switch and get a magnitude of speed faster
- TCP/IP works well with ethernet
	- Still annoying cause link layer breaks structure
- For home networks classic ethernet
- Adding a new device is expensive on the small scale
- New cable/socket has to be wired all the way from the switch to the new device
- In the old days we'd just connect our devices to each other instead of connecting everything to the router/switch
- Switch model **does not scale correctly**
	- please label your cables
	- please
	- for the love of all that is good pls
