# Computer Systems - Lecuture 18 - System Security

### System Security
- Protecting computer systems from theft and damage to their hardware/software and data
- More recently called *cyber security*
- Important to recognise *it is not just netowrk based threats, some of the most effective attacks are offline*

### System Security Threats
- Physical loss or theft - hardware or data devices
	- Hardware can be replaced, *the biggest concern is data*
- If the attacker gains physical access it is *generally considered they can do anything*
	- Two risks
		- Compromise - device is altered/infected for an ongoing attack
		- Removal - device is taken/lost, data may be extracted
- Physical access security
	- Multi-layered - building -> floor -> room -> cabinet
	- Easier the equipment is to access the more vulnerable it is
		- *Desktops* in particular reception desk
		- *Laptops/Mobile Phones* - Physical protection almost impossible
		- *Printers* - almost always in communal areas - not well protected
			- No-one updates this
			- Sees a bunch of sensitive information (since it prints it)
		- Dropping USB sticks everywhere
		- *takes 30 seconds to compromise something*
- Further mitigating strategies
	- Full disk encryption
	- Multi-factor authentication - biometrics
		- Don't rely on passwords

### Full Disk Encryption (FDE)
- Encrypts *every bit on the disk* with the exception of a small portion for the Master Boot Record
- Transparent - disk appears as normal, but everything is encrypted/decrypted transparently to the user
- Can be combined with a *Trusted Platform Module to allow decryption only on the machine the disk is in*
- Typically same key is used for entire volume which has to be held in memory - leading to a possible weakness
- Weakness of FBE is that the same key is used for everything

### Cold boot attack
- Relies on data remanence of DRAM/SRAM - data is still readable for a short period after power down
	- Attack relies on physical access
	- Attacker cold reboots machine with custom lightweight OS on removable disk
	- Take a copy of everything that was in memory when machine was last running - including encryption/decryption keys
	- There are even automated tools for finding the keys
- Mitigating techniques include *encrypting RAM* and memory scrambling
	- Xbox did this to stop piracy
	- Apple also does this to stop piracy

### File System Encryption
- File System Encryption is per file or folder
	- Different keys for more sensitive material
	- External keys - smartcards - *secure tokens for highly sensitive material*
	- Controlled access to secure tokens can provide location based security -i.e. access to data in the office but not outside

### Runtime Attacks
- File and disk encryption are *not effective against runtime attacks*
	- If the user can access or view the data, then so could an attacker
- In person runtime attacks are almost impossible to stop if *remote devices/access are allowed*
	- Recall the weakest link is the person
	- However such attacks are rare and high risk for the attacker
- Most common attack is a remote attack to *give pseudo-real-time access*
	- Provide a backdoor, screengrab or keylog your machine
- Malware
	- Keyloggers
		- Record all keystrokes and leaks them to attacker
		- Allows *recovery of username, passwords, clipboard contents and resource locations*
		- Example; Olympus Vision Keylogger
			- Business Email Compromise (BEC)
			- Detected in companies across 18 countries
			- Targets email accounts of senior finance staff to trick suppliers/customers to send payments to fraudulent bank accounts
			- Type of attack is becoming common, can be costly
				- A Belgium lost 10m euros and an Austrian parts manufacturer lost 70m euros
	- Ransomware
		- Recent form attack
		- Form of extortion
			- Dependent on bad backup practises that prevent easy recovery
		- Often combined with other attacs
		- Can be catastrophic to business/function operation
			- WannaCry/WannaCrypt - hit the UK national health service hard
				- Victorian traffic cameras
			- NotPetya - targeted attack on Ukraine - spread more widely
			- Cryptolocker - widespread attack
	- Viruses
	- Trojan horses
	- Worms
- Social Engineering

### WannaCry attack
- Based on EternalBlue exploints developed by the NSA
	- Stolen by ShadowBrokers and attempted to be sold on the black market - ultimately leaked
- Attack affected more than 200000 computers in 150 countries
- Would have been considerably worse if a kill switch had not been discovered (the malware checked if a URL resolved and if it did stopped spreading)
	- MalwareTech - discoverd the URL and registered the domain
- The US, UK and Australia formally asserted that North Korea was behind the attack
- Up to 70000 in the NHS may have been infected
- Non-critical emergencies were turned away in some instances
- Nissan car plant in the UK halted due to infection
- Renault car plants in France halted
- Deutsche Bahn - train information screens
- The list of companies and organisations is long

### WannaCry - Victoria
- Speed cameras in Victoria were infected with WannaCry
- Raised serious questions as to how since they are not networked
- Believed a contractor with an infected laptop managed to infect the cameras when copying updates from a laptop to a USB stick for the cameras

### NotPetya
- Used EternalBlue to spread
- Global attack but primarily targeted att he Ukraine (estimated to be 80% of infections)
	- Spread through a backdoor into the update process for Ukrainian tax preparation software
	- Global spread was partly caused by multinationals with offices in the Ukrain - TNT Express (FedEx) estimate it cost it 300m USD
- US, UK and Australia blamed Russia for the attack
- Cyber war which we will never see as civilians - attacking servers

### Viruses/Worms/Trojan Horses
- Trojan Horses
	- Software that misleads the user as to its true intent
	- More commonly seen as spyware today
	- Often included in pirated software or content
- Viruses
	- Infected documents, websites, downloads
	- Could be performing any number of malicious attacks from backdoors, installing Trojan horses, or keyloggers, or creating botnets of compromised machines
- Worms
	- Malicious software that replicates itself and spreads through a network or removeable device

### Malware
- Initially attacks were untargeted and more of a nuisance than a threat
	- Most problems were caused by badle written malware
- More recently malware has become *weaponised*
	- Targeted at countries or specific entities
	- EternalBlue is evidence of the *scale of nation state development of malware*
	- The problem is that even though the attacks start off targeted, once in the wild they get repurposed
- A lot of the damage we see today is *collateral damage caused by targeted attacks*
	- Likely to see more of that

### Malware - Critical Infrastructure
- Critical infrastructure is *particularly vulnerable*, especially industrial control
	- Equipment and systems *never intended to be put online have been put online to deliver efficiency*
	- Even when not directly online they have been successfully targeted
- Stuxnet - discovered in 2010, believed to be developed in 2005
	- Targeted SCADA (supervisory control and data acquisition) - industrial control systems. In particular centrifuges in the Iranian nuclear program
		- Destroyed all of the centrifuges
		- Spread by offline usbs
	- Spread widely but was inert unless it found *Siemens Step7 software*
	- Similar vulnerabilities to the Equation Group (NSA operation that developed EternalBlue)
- 2018 could be the year we see/hear of more critical infrastructure attacks
- Not new, but up until now attacks have been limited or exploratory

### Not just a network problem
- We view malware as coming from networks/internet but targeted attacks are *likely going to come from physical threats*
- Physical infection of devices that are accessible, printers, machines on the front desk, display screens
- Attacking remote hardware that will subsequently be taken into and connected to a secure network (BYOD)

### Social Engineering
- Spear Phishing - sending emails from a known entity to induce the target to open a file or click a link
	- Targeted against particular individuals or organisations
	- Often use background intelligence to improve likelihood of success
	- Good example is HBGary attack in 2011

### USB Drop Attack
- Create branded USB sticks
- Add compromised material/stick
	- Zero day exploit
	- HID spoofing to inject keystrokes
	- Malware infected file on the USB stick
- Drop the sticksa round the carpark and wait for a good samaritan in the company to pick one up and plug it into their machine
- How to make sure they will open the file?
- What filename always works?
	- redundancies2018.txt
		- Want to see if you're getting laid off lol

### Protection
- *Air-gapped networks*
	- One network for external access, one for internal
	- Essential there is no connectivity between - i.e. no CD/DVD, USB, Network
	- Significant impact on efficiency and productivity
- *Principle of Least Privilege* - only have the rights that are necessary to complete the task
	- User accounts with highly restricted access, only able to see the files they absolutely need
	- Segregated networks with minimal/controlled bridging
	- Running processes and services in *dedicated accounts*, *not as root*
- **Cyber security training**
	- Depends on the weakest link in the business
	- Senior execs are stupid and are always targeted
- *Sandboxing*
	- Create a new instance for every application - malware cannot expand out of this
- Assume there is an attack even if there is no evidence of one, by the time you realise one is around it is too late
- **Multi-layered security is vital**
	- Physical, software, network, social, process
- *Defence in depth*
	- *Don't want security to be like an egg* - hard outer shell, but once inside there is no security
	- Ideally we want many interwoven layers making it dificult to move through, even if each layer is not that strong
- Not necessarily about stopping the attacker outright, it's about getting enough time to take evasive action
	- Going offline, shutting down services, changing passwords


- Security is now a mainstay of IT marketing
- Most of it is not particularly interesting but occassionally a good advert is made
- [Nothing is secure](https://www.youtube.com/watch?v=FqibWHfn_Yc)
	- That was legit actually well shot and scripted lol