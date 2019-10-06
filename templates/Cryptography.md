# Cryptography

## Cryptographic controls

### Cryptography generic

In order to fulfill requirements for confidentiality, and integrity only peer reviewed and approved cryptographic methods should be used; underlying mechanisms, protocols, as well as storage techniques must use secure methods.

This rationale contains the requirements for all cases of encrypted communication, signed communication, use of PKI certificates, and use and management of encryption keys.
This excludes requirements for when to use cryptography as those are described in other parts of the policy and those parts will refer to this document for the how-to.

### Encryption of sensitive data at rest

Encrypt all sensitive data at rest in a manner that defends against threats.

### Mixed Content

To ensure the proper level of trust with a recipient content must not mix encrypted and unencrypted content. This includes encrypted web pages. 

[Related info Mozilla Developer Network: Mixed Content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content)

### Strong standard algorithms and keys

Ensure appropriate strong standard algorithms and strong keys are used to protect sensitive data, and key management is in place.

### Encryption of {{company}} data on End User Devices.

{{company}}-data stored on an end user device or on external storage media, must be encrypted.

When {{company}} data can be stored it may contain customer or {{company}} confidential information and this information can be breached when lost outside {{company}} domain, hacked or reached through unwanted connectivity (e.g. Wi-Fi, blue tooth, man-in-the-middle).

Full encryption on all end user equipment and removable media must be used.

### Transport Layer Protection using strong algorithms only

Use transport layer security services that are provided by validated cryptomodules.

### Transport Layer Protection: certificate validation

Certificates must be centrally managed, valid, not expired and not revoked. Certificates must also be valid for the domains they serve.

http://tools.ietf.org/html/rfc5280
http://tools.ietf.org/html/rfc2818
https://tools.ietf.org/html/rfc6125

### Application of cryptographic rules

 All technology involving cryptography used in any network protocols, e.g. TLS-based (SMTP, FTP, HTTPS), SSH, EAP, IPsec and security of means (disk encryption, Hardware Security Modules, certificates) must adhere to the cryptography requirements of the {{company}} Security Policy. The scope includes, and is not limited to:
- confidentiality techniques, e.g. encryption and pseudonimity
- integrity control, e.g. Message Authentication Code (MAC) and one-way hash techniques
- key exchange and key transport methods, e.g. forward secrecy and key exchange techniques
- key storage quality, hardware security module quality
- cryptographic processing norms, e.g. ETSI, FIPS, etc
- proofs and non-repudiation techniques, like fingerprints and digital signatures, PKI and Web-of-Trusts as foundation to other systems including identity systems.
- Quality in randomization techniques with specific focus towards cryptographic fundamental techniques.

### DNS namespacing for certificates

Internally and externally trusted certificates must use Subject Alternative Names (SANs) of the type DNS and Common Name fields (CNs) containing registered Fully Qualified Domain Names (FQDNs) with a registration to {{company}} as owner. For internally trusted certificates, the registration can be omitted when the Top Level Domain (TLD) ".local" is used.

### No internally trusted certificates for customers

Customer owned Fully Qualified Domain Names must not be signed by {{company}} internally trusted certificates, e.g. {{company}} N.V. Workspaces Root CA or {{company}} N.V. Private Root CA.

### Protecting data by encryption and digital signature techniques

Data transport of customer data, any kind of credential, internal data, confidential data and secret data must be protected by using protocols that ensure confidentiality, message integrity and authenticity between users and systems, and also machine to machine interaction.

The transport of public files, system update files or packages, CRLs, CMPv2 are not considered confidential, thus encrypted protocols are not required for the security of the platform. Inbound data must be integrity protected by itself using a digital signature scheme to ensure the authenticity of the data and to ensure against tampering of the data before use.

Systems using a STARTTLS protocol version, like XMPP with explicit TLS, FTP, SMTP, must enforce that credential and data exchange only occurs after both parties established a TLS handshake.

*Exception: Mail Transfer Agents who communicate to MTAs outside of KPN may deviate from this policy on advise from CISO.*

Network traffic can be intercepted. Whether it’s in a green, orange or red zone; it’s not possible to guarantee that traffic will not be intercepted. For this reason the use of secure protocols is mandatory in most cases.

FTP is a protocol that can be used to transfer data. SCP or SecureFTP are secure alternatives for this.

Standard unencrypted LDAP is not allowed however, when TLS is enforced by STARTTLS then it is allowed or when a LDAP discovery is started to be followed up by an encrypted data enchange.

For some traffic or protocols there is no safe alternative. Additional measures must be taken to reduce the risk of information leakage.

Known exceptions are:

* High volume traffic where encrypting poses an insurmountable problem.
* Systems communicating unencrypted public data, like updates, between verified peers. A KSP compliant method of detecting tampering with data has to be in place.
* Systems communicating in the same VLAN (not spanning more than one building).

### Forbidden protocols

The following protocols are forbidden to be used for any reason: SMBv1, RSH, SNMPv1, REXEC, NFSv1, Telnet, rsync without SSH or TLS, HTTP without a (forced) redirect to HTTPS, Cisco Smart Install.

Use of alternative and secure protocols are required.

### Secure access

All connections between {{company}} End user devices (Endpoints) and devices such as printers and {{company}} corporate networks must be secured.

To protect {{company}} End user devices, infrastructure and information against illegitimate, unauthorized (remote) access, and to secure remote connectivity from the Endpoint to the {{company}} infrastructure.

Use encrypted communication and two factor authorization (such as the company card) for remote access of laptops.

### Communication Security

To prevent data across a WLAN from interception at least one of the following measure must be taken:
- Encrypt communication between client and access point using WPA2Enterprise with 802.1x authenticated clients to the {{company}} WLAN.
- Encrypt communication using a VPN solution.

Example of implementation with windows: Microsoft’s guide - [Windows firewall and IPSEC Policy deployment guide](http://technet.microsoft.com/library/cc732400.aspx )

### Certificate Transparency

Any certificates used for internet-facing systems that are signed by a central CA must be registered in a Certificate Transparency repository.

### Encryption Algorithms

One of the following encryption primitives must be used for encryption and decryption:

- AES-256, AES-192 and AES-128
- XSalsa20/20
- Salsa20/20
- Twofish
- IDEA; the key must be generated using a hash algorithm from KSP-RE-483, like SHA2.

For AES use known good AES-authenticated modes:

- GCM
- CCM

Use non-authenticated AES modes only in combination with an authentication method, like HMAC:

- CTR
- XTS

The following encryption primitives should not be used. Use only for legacy support or explicit compatibility requirements:

- AES-256-CBC, AES-192-CBC and AES-128-CBC
- Three-key Triple DES
- Blowfish

All not explicitly mentioned encryption algorithms are not allowed. Example are:

- RC4
- All EXPORT ciphers
- All encryption algorithms resulting in less than 112 security bits

The use of a random nonce or initialisation vector (IV) with sufficient length is mandatory with each of these encryption algorithms. To generate a good nonce or IV use a good random bit generator.

More information can be found in: NIST Special Publication 800-131Ar1: Transitions: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths

### Pseudonymization

Personal data must be stripped from directly identifying characteristics by using hashing.

Personal data must be processed in such a way, that the identifiable personal information is encrypted. People may no longer be identifiable without undoing the encryption.

### Data transport encryption

When transporting data, physically or digitally, the use of encryption is mandatory.

### Disk encryption of databases

Disk encryption is not required for a database if all rules are verified to be inplace, auditable, and the data is stored in a {{company}} owned datacenter.

### Use of untrusted certificates

The use of untrusted certificates is not allowed. Known good CAs or alterations are vetted by CISO.

Untrusted certificates are:

* Self-signed certificates, i.e. certificates which have self-vetted and self-validated their own information and key material by signing itself.
* Certificates signed by an untrusted, unknown or vendor supplied CA, i.e. certificates which have not been vetted and validated by an open or known process.
* Certificates using key material not generated nor controlled by {{company}}.

*Exception: Exclusively for Puppet and VMWare VMCA it can provide and apply their own certificated. These certificates are explicitly scoped to the protocol used for inter-VMWare cluster or Puppet Master-Agent communication. Any other application for these certificates is prohibited*

Known good CAs are:
For internal trust:

* All certificates (ultimately) signed by the {{company}} Private Root CA.
* Per project CA solutions vetted by CISO.

For public/external trust:

* GlobalSign CAs
* Comodo CAs
* DigiCert CAs

### Choosing safe curves for elliptic curve cryptography

The use of safe elliptic curves is mandatory. Specific elliptic curves are regarded as safe after having passed (cryptographic) peer review. 

Applications can use the following safe curves:

- M-221 (Curve2213)
- E-222
- Curve1174
- Curve25519
- E-382
- M-383
- Curve383187
- Curve41417
- Ed448-Goldilocks
- M-511
- E-521
  Exception: If no safe curves are supported, the following elliptic curves are acceptable for usage:
- P-256
- P-384
- P-521

[SafeCurves](http://safecurves.cr.yp.to/)

### Key Compromise

Compromised keys must be regenerated and rekeyed, not updated. During generation the new key must be generated from a new set of data (no re-use of data used to generate the compromised key) to ensure its full independence from the compromised key. For PKI the CA must be informed of the compromise by means of the contract manager.

Example keys involved are:
• SSH private keys for hosts or users
• Private keys associated to PKI, PGP and other types of certificates
• Diffie-Hellman param files
• Group keys
• Key used for symmetric encryption of e.g. files, databases, file-systems or any other type of arbitrary data

### Password hashing

Passwords must be hashed and stored using known good salted password hashing methods. 

The following list of actions must be taken for each password from the service/tooling:
• Use a good random salt.
• Use a known good hash algorithm.
• Use a random salt per password.
• In client/server scenarios, like web applications, always hash on the server side
• To make cracking harder use key stretching to protect the passwords

*Exception for high-volume environments where key stretching is not applicable for performance reasons: use HMAC to protect the passwords with a key per password stored securely in an HSM solution.*

### Private key transport and storage

Private keys are one of the foundations for the security of a service and its data. A private key must be protected during both transport and its storage:
Storage:

- The private keys should be stored securely in an Hardware Security Module when multiple customer keys could be compromised during a service breach.
- Keys stored on a file system must be protected with the most strict possible file system permissions.
- Physical security steps must be taken to limit access to the key to authorized personnel. Any form of physical security in addition to building access, that allows verification of access (see point below) will do.
- If a stored key is accessed this must be verifiable/detectable.

Transport:

* Before transporting a private key between systems the private key must be encrypted and use message integrity rules to provide tamper resistance.
* For key encryption and integrity the following rules are mandatory requirements:
  • Encryption Algorithms (in this document)
  • Hash Algorithms (in this document)
  • Password length – for static passwords (check Access control chapter)
  • Password complexity (check Access control chapter)
* In addition:
  • The transport method must be encrypted itself, e.g. use SSH, HTTPS or FTPS.
  • Use HMAC or Digital Signatures to authenticate the sender of a private key when the sender and receiver are different entities.

### Key stretching algorithms

Apply known good key-stretching algorithms:

* PBKDF2, when FIPS certification or enterprise support on many platforms is required. Only use in combination with hash algorithms and a salt as mentioned in this document.
  * On mobile devices
    *  Minimum: 5.000 rounds
    *  Norm: 10.000 rounds
  * On servers and workstations:
    *  Minimum: 50.000 rounds
    *  Norm: 100.000 rounds
* Scrypt, where resisting any/all hardware accelerated attacks is necessary but support isn’t.
  * On mobile devices
    *  Norm: N = 2^14, r = 8, p = 1
  * On servers and workstations:
    *  Norm: N = 2^20,r = 8, p = 1

* Bcrypt, where PBKDF2 or scrypt support is not available
  * On mobile devices
    *  Norm: cost = 13
  *  On servers and workstations:
    * Norm: cost = 16

### Public Key Exchange

To authenticate a service, host, machine or user a public key must be exchanged to the peer using a key exchange method listed in {{company_cryptographic_algorithms_guide}}.

Proper key exchange methods prevent identity spoofing by enabling the peer to verify the authenticity of the public key and challenge the ownership of the private key.

[Wikipedia: Key Exchange (English)](http://en.wikipedia.org/wiki/Key_exchange)

### Key destruction

Cryptographic keys must be destroyed in such a way that restoration is impossible. This procedure must take platform specific properties into account, like removal of a file does not implicitly wipe the key from the disk nor does it implicitly nullify the data in memory.

### Certificate Authority

Public Key Infrastructure builds trust relationships using trusted third parties, the Certificate Authorities.

All used Certificate Authorities:

- Must comply with the European Telecommunications Standards Institute (ETSI) standard "ETSI TS 101 456”.
- Are FIPS 140-2 level 3 compliant or better.
- Have a published CPS (Certification Practice Statement), this also means that our use of the certificate must follow the CPS.

[ETSI TS 101 456: Electronic Signatures and Infrastructures (ESI); Policy requirements for certification authorities issuing qualified certificates](http://www.etsi.org/deliver/etsi_ts/101400_101499/101456/01.04.03_60/ ts_101456v010403p.pdf)
[FIPS 140-2: Security Requirements for Cryptographic Modules](http://csrc.nist.gov/publications/fips/fips140-2/fips1402.pdf)

### Certificates

Certificates in the format X.509 can be used in a Public Key Infrastructure or web-of-trust.

In a Public Key Infrastructure (PKI) context the follow applies:

- Certificates can identify hosts, servers, users, processes, end-points and (individual) products.
- Certificates comply to RFC5280.
- Domain validation when used for identification.
- Revocation must be implemented using CRLs (RFC5280), OCSP (RFC2560, RFC5019 or RFC6990) or OCSP stapling (RFC6066 and RFC6961), unless the clients are fully enclosed, i.e. no direct or proxied internet access exists.

In web-of-trust context the following applies:

- The certificates must comply to PGP/GPG standard, i.e. RFC 4880 and additional RFCs.
- The certificates are created for a group or individual.
- The certificates are digitally signed by others or a master key, after the full fingerprint is compared and matches.
  PGP/GPG keys which have been used publicly must be invalidated. The invalidation must be published.

*RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile*

### Use of certificates

The certificate and the applications in which they are used must support the relevant RFC extensions describing use of certificates in combination with application or transport protocols. For instance RFC2818 to bind the identity of a peer to a session.

*RFC 6125: Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)*

### Binding Certificates

Each certificate must be bound to use for an as small as possible set of identities, example one host, virtual machine, one service, person or department.

A TLS off-loader or load-balancer MAY hold the certificate and private key to serve/off-load the TLS sessions for one cluster of nodes serving the same service.

### Wildcard certificates

Wildcard certificates must be scoped as much as possible to the most specific Fully Qualified Domain Name (FQDN).
To limit impact on the infrastructure in case of compromise the use of wildcard certificate is:

- limited to a single application-type and purpose, i.e. exclusively for a cluster of mail servers or web-servers only, or another specific application-type.
- must be scoped to the most specific FQDN possible in a cluster of systems or load-balanced setup, i.e. *.service.domain.tld. For non-{{company}} infrastructure it is permitted to ommit this restriction.
- may use a scheme customer_name.service.domain.tld or customer_name.specific_domain.tld.
- must not use on a widely used domain, e.g. *.{{company}}.com, *.{{company}}net.org, *{{company}}.net, *.{{company}}, or *.any_subsidiarymaindomain.tld.
- must secure the private key according to "Private key transport and storage" request in this chapter
- For environments with a high demand on integrity and confidentiality the use of tamperproof solutions must be assessed. E.g. an Hardware Security Module (HSM) with a certification of FIPS140-2 level 2 or better in the context of health sector related services and vital infrastructure.

### Key pair lifetimes

Keys used must have a maximum lifetime of 36 months.

Examples of keys are:

- Keys belonging to certificates
- Diffie-Hellman keys
- Static passwords
- pre-shared keys (PSK)
- master keys
- SSH keys for systems and administrators
- PGP keys
  Exception to this is the key pairs used by a Certificate Authority.

Password used with these key pairs need to be compliant with requests found in Access control document. Because of the maximum lifetime of the key pairs these password don't need to change during this lifetime.

### Encryption Algorithms

One of the following encryption primitives must be used for encryption and decryption:

* AES-256, AES-192 and AES-128
* XSalsa20/20
* Salsa20/20
* Twofish
* IDEA; the key must be generated using a hash algorithm from KSP-RE-483, like SHA2.

For AES use known good AES-authenticated modes:

* GCM
* CCM

Use non-authenticated AES modes only in combination with an authentication method, like HMAC:

* CTR
* XTS

The following encryption primitives should not be used. Use only for legacy support or explicit compatibility requirements:

* AES-256-CBC, AES-192-CBC and AES-128-CBC
* Three-key Triple DES
* Blowfish

All not explicitly mentioned encryption algorithms are not allowed. Example are:

* RC4
* All EXPORT ciphers
* All encryption algorithms resulting in less than 112 security bits

The use of a random nonce or initialisation vector (IV) with sufficient length is mandatory with each of these encryption algorithms. To generate a good nonce or IV use a good random bit generator.

*Related info: NIST Special Publication 800-131Ar1: Transitions: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths*

### Digital Signatures Algorithms

One of the following digital signature algorithms must be used:
- CECPQ1-ECDSA
- EdDSA
- ECDSA
- RSA
- DSA

For Post Quantum resistance, the following algorithms must be used:

- CECPQ1-ECDSA (New Hope)
- NTRU-6130 (Lattice-based)
- McEliece or Goppa-based McEliece
- SPHINCS-256 (hash based signatures)

These algorithms can be used in authentication phases or integrity checks.

*Related info: NIST Special Publication 800-131Ar1: Transitions: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths*

### Digital Signature Generation and Verification

Digital signatures must have at least 112 bits of security strength. This means:
- For EC: key length ≥ 224
- For RSA: key length ≥ 2048
- For DSA: key length 3072/256 or 4096/256.

### Key exchange

For key exchange one of the following must be used:

* ECDH (Diffie-Hellman) with a minimal key length of 256 bits.
* DH (Diffie-Hellman) with a minimal key length of 2048 bits.

All ECDH and DH parameters must be newly generated before use to assure unicity and avoid default parameters reuse between various installations.

### Hash Algorithms

One of the following hash algorithms must be used:
- SHA-2: SHA-512, SHA-384, SHA-256 or better
- SHA-3
- GOST R 34.11-94 (256 bit hash)
- Skein
- JH
- Grøstl
- BLAKE and BLAKE2

The following hash algorithms should not be used. Use only for legacy support or explicit compatibility requirements:

- SHA-1: for Non-digital signature generation applications only, not for Digital signature verification nor Digital signature generation after 2013
- SHA-224: for Non-digital signature generation applications only, not for Digital signature verification nor Digital signature generation after 2014
- WIRLPOOL-T
- HAVAL, using >= 160 bit with 3 rounds

The following hash algorithms must not be used:

- SHA-0
- HAVAL, using 128 bit with 3 rounds
- RIPEMD
- MD5
- MD4
- MD2

*Exception: the use of MS-CHAPv2 is allowed, when transported as payload within an encrypted protocol, like TLS or various EAP protocols using a TLS based outer layer.* 

### HMAC (Hash-based Message Authentication Code)

HMAC is a keyed-hash message authentication code and must use:
- A hash algorithm as defined in KSP-RE-483
- A key with a length ≥ 128 bits
- The key should be generated using a known good random bit generator

Known good examples are:

- HMAC-SHA1 with a key length of 160 bit.
- HMAC-SHA2 with a key length of 256 bit.
- HMAC-SHA3 with a key length of 256 bit.

*HMAC-MD5 must not be used.*

*[Related info](http://csrc.nist.gov/publications/nistpubs/800-107-rev1/sp800-107-rev1.pdf)*

### SALT use

he length of the randomly-generated portion of the salt must be at least 128 bits. The salt must be generated using a known good random bit generator.

Example uses for a salt: 

* Password storage (Details in access control document)
* Encryption Algorithms (Details are found in this document)
* Password hashing (Details are found in this document)
* Key stretching algorithms (Details are found in this document)

### Maximum token lifetime

Authentication tickets/tokens, e.g. Kerberos, AFS and Windows logon, must have a maximum lifetime of 6 hours. During their period of validity tokens may be refreshed automatically.

### Web application data encryption

For encryption of transported application data applications:

* The highest available TLS version must be activated.
* Protection against downgrade attacks must be activated. When this feature is absent: TLSv1.0 must be de-activated.
* TLSv1.3 must be enabled, when available.
* TLSv1.2 must be enabled.
* TLSv1.1 may also be enabled.
* TLSv1.0 may only be enabled when there is a need to be able to communicate with legacy systems. When this need is absent, it must be disabled.
* SSLv3 is not allowed to be enabled and must be disabled.
* SSLv2 is not allowed to be enabled and must be disabled.

[Related info](http://tools.ietf.org/html/rfc5246)

### Cryptographic Key Generation, Random Bit Generator

Use a known good entropy source to generate cryptographic keys, identifiers or random seeds. Known good entropy sources for an application combine several random sources and use a cryptographic secure hash algorithm over the values of the sources.

Known good sources are:

- On Apple iOS use SecRandomCopyBytes
- On Android use java.security.SecureRandom and must not be combined with setSeed().
- On Unix and Linux systems use /dev/urandom
- On Windows use CryptGenRandom or RtlGenRandom
- In .Net use System.Security.Cryptography.RNGCryptoServiceProvider
- In Java use java.security.SecureRandom
- In Perl use Math::Random::Secure
- In PHP use openssl_random_pseudo_bytes or mcrypt_create_iv
- In Python use os.urandom
- In Ruby use SecureRandom

At (re)boot time of a system, when there isn't sufficient entropy gathered yet, all processes generating new key material must block until sufficient entropy has been gathered.
Random bit generators must be compliant with one of the following standards:

- SP 800-90A, revision 1.
- ANSI X9.62:2005, Annex D.

The use of the following methods or entropy sources are forbidden:

- EC_Dual_DRBG

*Related info: NIST Special Publication 800-90A (revision 1): Recommendation for Random Number Generation Using Deterministic Random Bit Generators*

### Use Perfect Forward Secrecy

Perfect Forward Secrecy must be used when setting up encrypted connections with any of the following protocols:
- IPSEC (Internet Protocol Security) met Group 14 (or better)
- SSH (Secure Shell)
- TLS (Transport Layer Security)
- OTR (Off-The-Record messaging for instant messaging)

Non-perfect forward secrecy protocols are allowed for legacy support and compatibility only. TLS cipher suite configuration should explicitly prefer ECDHE and DHE/EDH cipher suites above other cipher suites.

*[Related info](https://en.wikipedia.org/wiki/Forward_secrecy)*

### Cryptographic Key Generation, Cryptographic Module

For high-security services where the entropy source needs to be protected from tampering a cryptographic hardware module must be used. The Cryptography Module of the product used must be compliant with the FIPS-140-2 level 2 standard.

*Related info: FIPS PUB 140-2: Security Requirements for Cryptographic Modules*

### Use of multi-domain certificates

Certificates must be scoped to only one application. The application may use multiple FQDNs (Fully Qualified Domain Names) to be identified. The FQDNs must share the same domain name.

Example:

* "www.{{company}}.com" and "{{company}}.com" can be combined
* "www.{{company}}.com" and "{{company}}international.com" cannot be combined
* "reporting.{{company}}.com" and "www.{{company}}.com" and "{{company}}.com" may be combined in one certificate when the "reporting" hostname is explicitly part of the overall application.

### Registration of Key Pair properties

For each public/private key pair the following must be registered:
- The owner
- The intended use (infrastructure on which deployed)
- Key length
- Key Algorithm (including curve if Elliptic Curve is used)
- Hash function
- CA used for signing
- Serial number (if applicable, like for certificates)
- Validity from and to dates

Registration may be omitted when the certificates are ordered through the central certificate application process.

This rule is implicitly satisfied when the certificates are ordered via internal processes.

### Key Pair privacy

The private part of the key pair should be generated on the device on which it will be used.
To support this:
- Certificate signing request must be submitted by CSR (Certificate Signing Request).
- Alternatively, key pairs must be generated locally by the key-pair owner or a delegated party within KPN.
- For load balancing purposes, it is allowed to copy the private key into multiple devices.

*[Wikipedia: Certificate Signing Request ](http://en.wikipedia.org/wiki/ Certificate_signing_request)*

### Certificate pinning and mutual authentication

Mobile apps which form a cryptographic foundation by implementing key provisioning for other services must apply certificate pinning or implement mutual authentication based on PKI with mutual validation. 

*Note: The pinning method must guarantee business continuity, e.g. to allow for multiple public keys to be pinned. Also allowed is to pin on the intermediate CA.*

By following the specifications for TLS and PKI as specified in the KSP attackers will be limited to:
1. Compromising the endpoint, e.g. mobile device or computer system;
2. Attack the digitale signature scheme as the foundation to PKI;
3. Compromising a CA, i.e. DigiNotar;
4. Create certificate at another CA.

The first vector already compromised the endpoint severely. The second requires a mistake digital signature techniques or a quantum computer with sufficient qubits and the third requires misconduct or infiltration into a CA, whereafter the expectation is that the business for this CA will stop. The fourth problem is mitigated/lowered in risk by applying CAA records on all {{company}} domains.

### Safe key lengths for several algorithms

For every cryptographic methods is a safe key length.

These can be found in the tab "Safe Key Lengths" in the guideline {{company_cryptographic_algorithms_guide}} - Cryptographic algorithms and cipher suites.