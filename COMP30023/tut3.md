# COMP30023: Computer Systems Tutorial Week 3
# DNS, Mail
### 1. Consider a situation in which a cyberterrorist makes all the DNS servers in the world crash simultaneously. How does this change ones ability to use the Internet?
- Would have to use IP addresses
- Hyperlinks would break
- Google would no longer work

### 2. Is it possible for an organizations Web server and mail server to have exactly the same alias for a hostname (for example, foo.com)? What would be the type for the RR that contains the hostname of the mail server?
- Yes, it's possible.
- The RR will have a record type - so one could be an *"A" (area) code* while the other could be a *"MX" (mail exchange) code* 

### 3. DNS uses UDP instead of TCP. If a DNS packet is lost, there is no automatic recovery. Does this cause a problem, and if so, how is it solved?
- TCP has a "reliable" method of conection where if a packet is lost, there is a way to recover the lost packet.
- UDP does not have this, and ignores lost packets. 
- DNS uses UDP. Why?
	- Less resource intensive - faster way to establish connection - don't have to wait
	- Normally a file is sent in parts
	- DNS just requires one part -> Domain for IP address
		- Request/Respond structure - if a response does not come back just send it again
- DNS is idempotent
	- Operations repeated without harm

### 4. Suppose you can access the caches in the local DNS servers of your department. Can you propose a way to roughly determine the Web servers (outside your department) that are most popular among the users in your department? Explain.
- Why are caches used?
	- Speeds up lookups of domain names
	- Makes DNS reolution faster
	- Can be utilized by a "proxy" to speed up DNS lookup for an organisation
- You can find out by looking at how long one domain has been in the cache
- You can look at the cache throughout the day and recording what domains are in the cache
- pyHole - can block adds - hosts your own DNS cache


### 5. Suppose that your department has a local DNS server for all computers in the department. You are an ordinary user (i.e., not a network/system administrator). Can you determine if an external Web site was likely accessed from a computer in your department a couple of seconds ago? Explain.
- Time it
- If it was requested and it took close to zero milliseconds (as in it's cached) then it was probably accessed a moment ago.

### 6. Is the vacation agent part of the user agent or the message transfer agent?
- User Agent
	- Responsible for the actual writing of emails
		e.g. Outlook, Gmail, Yahoo! mail
- Message Transfer Agent
	- Responsible for transferring emails 
	- E-mail server
- Vacation Agent
	- Can't have the user agent on all the time
	- 

### 7. Suppose that John just set up an auto-forwarding mechanism on his work email address, which receives all of his business-related emails, to forward them to his personal email address, which he shares with his wife. John’s wife was unaware of this, and activated a vacation agent on their personal account. Because John forwarded his email, he did not set up a vacation daemon on his work machine. What happens when an email is received at Johns work email address?
- The vacation agent would send mails via his work address, but fail due to no-reply
- This will result in a massive loop since the no-replies will also result in vacation emails and etc.

### 8. Bonus: Read up on the history of the .au Top Level Domain and the role of the University of Melbourne Computer Science department in its creation.
