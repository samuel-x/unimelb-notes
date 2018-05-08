# COMP30023: Computer Systems Tutorial Week 10
### Wireless LANs, Cryptography

### 1. What does it mean for a wireless network to be operating in ‘infrastructure mode’? If the network is not in infrastructure mode, what mode of operation is it in, and what is the different between that mode of operation and infrastructure mode?
- Access Points vs AD-HOC mode (point to point)

### 2. Describe the role of the beacon frames in 802.11.
- Show information of the access point, containing info regarding:
- BSSID (MAC of AP)
- SSID (Name of Network, e.g. uniwireless)
- Security Setting (WPA, WEP, WPA2)
- Channel
- Beacon Interval
- Also works in Network Discovery
	- Passive: just listen for beacon frames
	- Active: Send out probe requests
		- Get a response similar to beacon frame
			- Broadcast MAC
			- MAC of device
				- if you control a lot of access points you can figure out where devices are going
			- Previously connected SSIDs
				- You can figure out where this device has been
		- Reason why HTTP vs HTTPS is so important
			- Even if you connect to a bogus access point with HTTPS that point still cannot read your data

### 3. Why are acknowledgments used in 802.11 but not in wired Ethernet?
- Inherently unstable/lossy connection
	- High probability of losing packets
- Hidden terminal problem
	- Can't see all the other devices on the network so you need to send ACKs to make sure things get through
- Collision Avoidance vs Collision Detection?

### 4. What is the difference between a symmetric-key system and a public-key system?
- Symmetric-key system = one key encrypts and decrypts
	- Problem for transferring the key
	- Can't do it securely
	- However this is much faster than public
- Public-key system = one key encrypts and one key decrypts (public and private)
	- Use public key cryptography to connect to things
	- Public key can be published anywhere
	- Sender encrypts with this key and sends this to the receiver, who has the private key (the only person who can read this)
	- Decrypt with private key

### 5. Suppose N people want to communicate with each of N - 1 other people using symmetric key encryption. All communication between any two people, i and j, is visible to all other people in this group of N, and no other person in this group should be able to decode their communication. How many keys are required in the system as a whole? 
- Complete graph
	- Each of the hosts, N, wants to connect to N-1 hosts
	- Same key can be used between two hosts
	- Therefore, `n(n-1)/2`

### Now suppose that public key encryption is used. How many keys are required in this case?
- Just `2*n`
- Each person has a public key and a private key
- ez

### 6. Is AES an asymmetric or symmetric cryptography algorithm? Why should you never use ECB mode in AES?
- Symmetrical
- ECB mode uses the same key to encrypt every block
	- You can see a pattern
	- The pattern of the encrypted data is the same as the original data
	- No randomness since *two identical blocks encrypted with the same key will output the same ciphertext*
		- This is called diffusion
	- Adobe password hack lmao

### 7. Why is asymmetric key cryptography not often used to encrypt actual messages? Describe how asymmetric key cryptography is commonly used in combination with symmetric key cryptography to encrypt messages.
- More computationally expensive
	- S l o w
- Normally can only encrypt up to the size of the key
	- Not good to encrypt long messages
- You can transmit the symmetric key securely
	- Encrypt the key with the public key -> send it
	- HTTPS uses this

https://apps.eng.unimelb.edu.au/casmas/index.php?r=qoct/subjects
http://go.unimelb.edu.au/4jx6