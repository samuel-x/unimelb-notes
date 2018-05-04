# Computer Systems - Lecuture 15 - Cryptography

### What is Cryptography?
#### Encryption
- Hiding data from everyone except those holding the decryption key
- Output is a cipher text

#### Decryption
- Recovering the original text using a key

##### Modern Cryptography
- Modern cryptography is based on mathematics
	- Problems that are considered to be hard or are well studied
		- Factoring the product of 2 large primes (RSA)
		- Solving discrete logs (ElGamal)
		- AES - substitution - permutation network
- *There is not perfect security*
	- Ultimately there is a key and we can bruteforce the fuck out of it
	- Challenge is to make bruteforce as long as possible or infeasible within the useful timeline of the data
- Increasing the bit length of the keys is only a temporary measure
	- Years ago we used half of what we use today and now it's insecure
- Quantumn computing could fuck everything up

### Types of Cryptography
#### Symmetric Cryptography
- *Same key* is used for encryption and decryption
	- Not really that safe
	- Need to give the key to the other person in a secure way
	- Once the key is figured out found everyone's screwed
- Modern example is *AES* (Advanced Encryption Standard)
	- Encrypt(SecretKey, Message) -> Cipher Text
	- Decrypt(SecretKey, Cipher Text) -> Message
	- Useful for keeping your own data secure

##### AES Encryption
- AES breaks data into blocks and encrypts each block
- AES has different modes of operation
	- ECB - *Electronic Codebook* (really insecure)
		- Every block is encrypted the same way
			- Really fast since it's parallelizable
		- Doesn't have any randomness (this is called *diffusion*)
		- If you encrypt the same key with the same data it'll have the same output
			- The *pattern* of the data will be the same thing
		- *lol adobe did this and they leaked 153 million passwords and password hints*
			- If you figured out one password with the same pattern then you figured out *literally all the passwords with the same pattern since they're the same*
		- [Relevant XKCD](https://www.xkcd.com/1286/)
	- CBC - Cipher Block Chaining
		- XOR every block with the next block and key
		- Encryption must be done sequentially
		- Decryption can be done in parallel
		- Losing a block means you *lose the entire file*
	- Describes how each block is linked
	- Try it yourself!
		- `openssl enc -aes-256-cbc -in msg.txt -out ciphertext.enc -pass pass:"COMP30023"`
		- Encrypts with AES
		- Random salt stored in ciphertext.enc file
		- `openssl enc -aes-256-cbc -in ciphertext.enc -out plaintext.txt -pass pass:"COMP30023" -d`
	- **Salt vs Pepper**
		- Both are random values added to the encryption/hash
		- Salt is public
		- Pepper is secret
		- Why isn't it the other way round the alliteration potential is huge :sad:

#### Asymmetric Cryptography (Public Key Crypto):
- Two keys, encrypt with one, decrypt with the other
- One of the most important developments in modern computer science
- Called public key cryptography
- Heart of modern security
	- Digital signatures
	- TLS (Transport Layer Security)
	- PGP (Pretty Good Privacy)
	- Secure Messaging
	- End-to-End Encryption
- Consits of two related keys
	- Public key - as per the name, can be made public
	- Private key - must be kept secret by the owner/user
- Slower than symmetric
- *Not suitable for* encrypting *large amounts of data* or *even multiple blocks*
	- Usually the encrypted data can only be the size of the key
- Often used *together with Symmetric Cryptography* as a way of *exchanging a joint secret key like AES*
	- *This is sort of how TLS (HTTPS) works*
- Have to balance key size with encrypted data

#### Asymmetric Cryptography in Action
- Example:
	- Alice generates her key pair (PublicKey, PrivateKey)
	- She posts her PublicKey online
	- Bob wants to send Alice a secrete message
	- Bob runs Encrypt(PublicKey, message) -> Cipher Text
		- Using Alice's PublicKey
	- Bob sends the Cipher Text over to Alice over the internet
	- Alice runs Decrypt(PrivateKey, Cipher Text) -> Plaintext
		- Alice recovers the secret message
	- *No need to meet or securely exchange any keys! We can all be introverts now!*
	- Can also send *secret keys for symmetrical cryptography*

#### Sending something with Asymmetric Cryptography
- RSA is probably the most well known Public Key Cryptography System
- `openssl genpkey -algorithm RSA -out PrivateKey.pem -pkeyopt rsa_keygen_bits:2048`
	- Make a 2048bit key pair
- `openssl rsa -pubout -in PrivateKey.pem -out PublicKey.pem`
	- Extract PublicKey from key pair file
- Now for Encrypting the message:
	- Encrypt msg.txt with PublicKey.pub
	- `openssl rsautl -in msg.txt -out ciphertext.enc -pubin -inkey PublicKey.pub -encrypt`
	- Decrypt with private key
	- `openssl rsautl -in ciphertext.enc -out plaintext.txt -inkey PrivateKey.pem -dencrypt`
	- This is literally what we did to access our `nectar instance`

#### Public Key Signatures
- A bit like the inverse of encryption and decryption
- Provides link between key holder and message/document/file
- These are actually legally binding today
- Instead of encrypting with public key, encrypt with *the private key*
- Everyone can *decrypt and check that you made it with the public key*, but can't change it without the private key
- Can add timestamps
- I think this is what signing commits are like with Git
- What happens with large documents?
	- Use a **Cryptographic Hash Function**
	- *Takes a near arbitrary length input* and outputs a *fixed length version*
	- SHA256, SHA512, (MD5, SHA1 - now insecure/deprecated)
	- Sign the hash digest which can be recalculated by the verifier

#### Cryptographic Hashing
- Mistakenly called a one-way function
	- Only one-way under certain circumstances - large input set that is sampled at random
- Have been misused to protect confidentiality (hide unique identifiers in datasets, hash passwords, etc.)
	- ***this is a bad idea!***
	- Hashes can be bruteforced - try every possible input and see which one produces a match
		- Average machine will produce 500k hashes per sec
		- GPU Blockchain miner would be billions per sec
	- If you have 26 million possible identifiers it would take <1 min to try them all
	- Do not hide things with hashes, it's not a good idea
- Hash Properties:
	- Easy and fast to calculate
	- Infeasible to reverse
	- Extremely unlikely two slightly different documents produce the same hash
		- e.g. changing one bit in the document will completely change the hash result

#### Public Key Signature Example
- Alice signs a document
	- Sign(PrivateKey, Hash(document)) -> Digital Signature
- `openssl dgst -sha256 -sign PrivateKey.pem -out signature.txt plaintext.txt`
- Bob wants to verify Alice signed the document
	- Verify(PublicKey, Hash(document)) -> True or False
- `openssl dgst -sha256 -verify PublicKey.pem -signature signature.txt modified.txt`

#### Certificates (The vague version)
- Digitally signed documents that provide proof of identity or ownership
	- i.e. This Public belongs to Alice - signed by some Authority
	- The Authority should be someone you know or trust
- In reality the signer is a Certificate Authority (CA) pre-trusted by your browser/OS
	- Can create chains of certificates, so you only need to trust a few root certificates to trust a whole web of certificates

### Key Sizes
- Security is based on a computentially hard problem
- As such out security parameter is *dependent on the key size*
	- Normally expressed in bits
- Different key sizes are required for symmetric and asymmetric
	- Asymmetric is generally *longer than symmetric*, current minimums:
		- RSA - 2048 bits, AES - 128 bits
		- Previously much shorter - 512 bits for RSA in the '90s, 56 for DES

#### Randomness
- Cryptography is *dependent on good randomness*
	- Key generation
	- IV generation for ciphers
	- Padding
- Randomness must *never be reused or discoverable*
	- KRACK attack
	- Wholesale PrivateKey recovery can take place is randomness is reused in DSA
- Generating good randomness is hard
	- Must be unpredictable
	- Dependent on *good OS implementations*
	- Someone removed a line in Debian and randomness was shit and no-one noticed for a long time
- Don't do this:
``` C
int getRandomNumber()
{
	return 4; // chosen by dice roll, guarenteed to be random lol https://www.xkcd.com/221/
}
```

#### Make your own cryptography????
- Even if you're the Government, building your own cryptography scheme will likely end in failure lol
- Just because something looks random, doesn't mean it's securely encrypted
- Even the smallest mistake can weaken the approach

***Don't create your own crypto algorithm. It will not work unless you spend 10-20 years on it lol***

Compromosing randomness generation is a known attack.

NSA did this by making a thing that was 'random' and Juniper Networks implemented it and then they can now break into anything with Juniper Networks

Academic vs Spying lol

[Having people in control of the keys results in cryptography being shit](xkcd.com/538/)

Government can compel you to hand your keys to their broken system

Learn how this cryptography system works just in case things break

