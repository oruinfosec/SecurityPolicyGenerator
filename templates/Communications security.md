# Communications security

## Network security management

### Network monitoring

Networks must be monitored for capacity, availability and malicious activities. Events must be handled as per the incident management process.

Monitoring is essential to be able to see what is happening on a network. Without monitoring, network management departments are “blind” and are not in control of a network.
Includes, monitoring a network link for over-usage or being able to detect a virus outbreak on the network.

### Network separation

The equipment that is not part of network infrastructure and has multiple interfaces, must be configured to upheld the segmentation. Therefore this equipment may not route/leak between two segments. The owner must ensure that no firewalls or network security can be bypassed. Per interface this equipment must only handle traffic bound to the purpose of that equipment. This is also required for VPN interfaces on a system.

This ensures that unintended network traffic is prevented.

### Network segmentation and security zoning

Segments must be defined and implemented for a network environment to support a layered security model.

This can be achieved by building services in accordance to a security zoning model. The following is a high-level description of the {{company}} standard zoning model:

| Black (external) |
| ---------------- |
| Red (DMZ)        |
| Orange(Internal) |
| Green(Protected) |
| Blue(Management) |

A typical service would have the systems users (who are in the Black zone) need to interact with in the Red zone, systems that are purely for service internal use in the Orange zone and servers containing confidential data in the Green zone. All systems also need a connection into the Blue zone in order to be managed. 

Just as in physical security, not everything happens in one room. Network segments should have a specific purpose and should be separated from other segments with their specific purpose. Segmentation must be done on function and classification of network data.

A webserver that is used for serving webpages to internet should not be in the same segment as the backup system for this server.

### Logical network separation and services

Services must be separated from each other by usage of logical network separation. If a service spans multiple zones, it must have a separate logical network for every zone.

If a service is composed out of multiple (smaller) sub-services, the services must be separated from each other.

For infrastructures identified as vital infrastructure the network separation must not be performed nor dependent upon a hypervisor or container.

*Example technology: VLAN’s, Q-in-Q, VXLAN, Private VLAN, VRF, Oracle Solaris Zones* 

### Communication between logical networks

When a system has multiple logical network connections in a zone, routing between them must be disabled by default.

Where routing between logical networks is necessary, traffic that passes the boundary between these networks must be filtered.

### Communication between services

Communication between services must be done through a common production zone (i.e. red, orange or green).

### Communication Matrix

For a service a communication matrix must be in place, stored in a CMDB and kept up to date, stating the following for each communication flow the service has:
* Originating and target System name
* Originating and target System IP address
* Originating and target System Ports used (TCP/UDP)
* Originating and target System Protocol used (ICMP, VRRP, HTTP)
* Originating and target System VLAN
* Originating and target System Service name
* Originating and target System Owner

### Network filtering

Between network segments a network filter must be in place through which only necessary traffic can pass.

Network segments are defined because of their different uses, security wise and functionality wise. To keep these separated, filtering of networking traffic is necessary.

A webserver may need a database server backend to be able to serve content to clients. This communication must be limited to only the necessary database communication to prevent misuse. This communication is registered in a communication matrix.

### Filtering traffic

Traffic that passes a zone boundary inbound or outbound must be filtered. This can be done by either ACLs or Firewalls. Any traffic that isn’t explicitly allowed and registered in a communication matrix must be denied and logged.

### Windows Domain Trusts relationships

Windows Domains must only be trusted in a one-way non-transitive connection between each other, with a trust relationship exclusively towards {{trusted_windows_domain}}. Bi-directional trusts, transitive and non-transitive are not allowed.

### Implementation of a secure channel to a Cloud Service Provider (CSP)

Establish a site-to-site VPN between the Cloud Service Provider (CSP) infrastructure and the corporate access management system to adhere to the zoning and segmentation guidelines. For IaaS and PaaS solutions this is a must. For SaaS solutions directly interacting with the end-users, additional measures may prevent the site-to-site requirement on a per interface basis.

### Transport Layer Protection using TLS

All pages with sensitive data must use TLS. Also, the location to which sensitive data is being posted to must use TLS without redirection from a non-TLS target.

Pages containing sensitive data are:

- pages displaying sensitive information, e.g. information impacting the privacy of the end-user.
- pages which are used for consuming sensitive information, e.g. login forms.

Possible exception: when a redirect from the non-TLS location to the TLS location ensures that the end-user is not capable of using the unsecured page.

### Secure communication downgrade prevention

The app must prevent that the TLS cipher suite will be downgraded and in this way provides insufficient transport layer protection.

### WiFi Protected Setup

No form of use of Wifi Protected Setup (WPS) is allowed.

### WLAN configuration and connectivity

When implementing a WLAN the following must be used:

* {{company}} WLAN with large user base (for example {{company}} Office Network)
  use wpa2-enterprise
* {{company}} managed client device must validate the authentication server based on certificate
* Users may access the {{company}} Office Network after authentication only when offered over the SSID.

{{company}} WLAN with small user base, dedicated or personal scope:

* must be secured with WPA2 with minimal key of 16 characters
* distribute and keep access keys conform private key requirements
* the accessed network must be segmented from the {{company}} Office Network

{{company}} CPE WLAN for business and residential:

* must be secured with WPA2 with minimal key of 16 characters initially
* the accessed network must be the on premise network of the customer

*Example of implementation with windows: [Microsoft’s guide - Configure PEAP and EAP methods](http://technet.microsoft.com/en-us/library/cc784383(v=WS.10).aspx)*

*[Client validation settings enforcement](http://technet.microsoft.com/en-us/library/cc759575(v=ws.10).aspx#cert_based)*

### WiFi Direct

No form of use of Wifi-Direct is allowed.

### Key Rollover

A ZSK rollover must happen every month. A KSK rollover must happen every 365 days.

 As the cryptographic material of a ZSK and KSK is often shared it reduces the strength of the key material. Therefore both keys need to be changed on a regular basis. 

### NSEC3 hashing

The number of hashing iterations used for NSEC3 must be 2.

Hashing used in NSEC3 does not provide a meaningful increase in security if the number of iterations is more than 2.

### Single-type key signing schemes

Single-type signing schemes are not allowed. The KSK or ZSK shall never be reused. Only 1 active KSK and ZSK is allowed per zone. Other ZKSs are and KSKs are allowed but only temporarily for the purpose of a key rollover.

To reduce the operational impact of a ZSK or KSK rollover, unique keys are required. 

### DNS Zone Transfer

Zone transfers that are not explicitly authorized via a written statement by the responsible {{company}} personnel or are not encrypted using {{company}} compliant algorithms are not allowed and shall be blocked.

Zone transfers may contain sensitive information and shall therefore not be shared with entities outside of {{company}} to prevent the leakage of information

### Signing of domains

All DNS-domains that can be resolved via the internet and owned by or directly related to {{company}}, her Brands as determined by CIPO, or a daughter organization must be signed by DNSSEC.

To be able to always guarantee the integrity of a DNS response sent by {{companys}} systems or received by {{companys}} customers DNSSEC must be used by all systems, applications, and domains owned by {{company}} which can be reached from the internet. This requires all domains of the {{company}} brand, or that of her daughters, to use this technique to secure their DNS responses.

For example SPF, DKIM, DMARC, DANE, and CAA DNS records improve the security of Email and HTTPS connections however these records can be manipulated when sent via normal DNS message thereby mitigating the benefit these records provide. DNSSEC prevents this from happening by protecting the integrity of the DNS responses containing the records.

### TLSA DNS records

{{company}} Systems using certificates for authentication, including but not limited to SMTP, must publish their certificate in a DNSSEC signed TLSA record.

To increase the trust of the certificate supplied by a system (e.g. during setup of a HTTPS connection), the receiving system can verify it by resolving the system and getting a signed TLSA record. The TLSA record is also what is used for DANE.

### Storage of DNSSEC keys

DNSSEC keys will always be stored in a HSM compliant with FIPS 140-2 security level 3 or higher.

The DNSSEC keys are critical for delivering trustworthy domains to anyone who accesses the domains of owned, hosted, or managed by {{company}}. Loss or compromise of these keys must be prevented at all costs.

### CAA DNS records

Any internet-facing {{company}} domain that uses certificates must have a DNSSEC signed CAA record in their authoritative DNS platform. The email address '{{company_abuse_report_email_address}}' must be used for the incident reporting field.

To prevent a Certificate Authority from signing certificates that they are not authoritative for a CAA record is used to state the Certificate Authority authoritative for that domain. All CAs shall check, as per the 8th of September 2018 that a CAA record exists and shall only sign certificates they are allowed to.

### Third party resolvers

All recursive DNS traffic originating from a system owned by {{company}}, excluding customers, shall be handled by a DNS platform owned and managed by {{company}}. Recursive queries using a different DNS resolver as destination shall be dropped and logged. The logs must immediately be sent to a central logging entity.

To prevent data exfiltration or leaking of information to third parties the use of 3rd party resolvers is not allowed. 

### Non-existing domains

To indicate that a domain does not exist, an NSEC3 record or better must be used.

NSEC is a DNS record that indicates that a certain domain name does not exist on the server however it also leaks information on which domains do exist. NSEC3, the evolution of NSEC, prevents this by hashing the answer however rainbow tables allow the domain name to be retrieved. As some domain names need to be kept secret newer mechanisms, such as NSEC5, are being developed and should, with agreement of CISO, be used.

### DNSSEC resolving

All systems or applications owned by {{company}} that use DNS resolving must always resolve using DNSSEC.

All DNS (stub)resolvers must indicate they are DNSSEC capable by resolving with the DO flag enabled.

DNSSEC protects the integrity of a DNS answer. To be sure that the systems of {{company}} use this protection mechanism they need to let others know that they support DNSSEC as a feature. This indication is given by the (stub) resolver setting the D0 (D zero) flag in a DNS request.

If the requested domain does not use DNSSEC then a normal DNS response will be sent.

### DNSSEC algorithms

The cryptographic algorithms used for DNSSEC shall be compliant to the {{company_preferred_list_of_cryptographic_algorithms}}.

 Strong, future proof algorithms are also required for DNSSEC.

### NSEC3 Salt

If NSEC3 is used a random salt of 8 bytes shall be used. This salt shall be automatically regenerated when a ZSK key-rollover takes place.

To prevent an attacker from finding the hashed domain names stored in an NSEC3 record a random salt shall be used. To reduce the effectiveness of an attack the salt shall be changed regularly.

### DNS Exfiltration

DNS resolvers must be able to detect and block any attempts at using the DNS protocol for the exfiltration of data from networks or systems of {{company}} or subsidiaries. All detected and/or blocked events must be logged and sent to a central logging server.

An attacker wanting to get data out of a network or system wants to do that in a manner so that they are not detected. By encoding the data into a DNS request, for example in the domain field (eW91IGdldCBhIGNvb2tpZQ==.baddomain.ng) an attacker can make it seems like valid DNS traffic, get it out of the victims network, and receive it at the domains authoritative DNS server that they control. A mechanism to prevent this from happening needs to be in place to be able to detect, and prevent, this from happening. For example, by detecting that a system is sending tens of DNS resolve messages to the same domain (baddomain.ng), and blocking and logging the event.

## Information transfer

### File sharing with third parties

Exchange of files with external parties must be done via a separate environment which has capabilities to check for malware and logs the information being exchanged.

### Use of the {{email_platfrom}} platform

All outgoing e-mail sent from the {{company_email_domain}} domain must be handled by the {{email_platfrom}} platform.

### Use of e-mail addresses

In e-mail communication in the name of {{company}} the e-mail address must be used under the {{company_email_domain}} domain. The platform administrator decides which e-mail address is given to what kind of e-mail communication.

### E-mail security

The owner of a service that sends out e-mail in the name of {{company}} must ensure the service is connected to the {{email_platfrom}} platform

### Use of Domain Keys Identified Mail (DKIM)

All e-mail communication originating from the {{company_email_domain}} domain must be signed with a DKIM key.

### Use of Sender Policy Framework (SPF)

All e-mail communication originating from the {{company_email_domain}} domain must be send through a SMTP server that is included in the SPF record for {{company_email_domain}}.

### Use of Transport Layer Security (TLS) on a Mail eXchanger (MX)

All e-mail communication originating from the {{company_email_domain}} domain must be send through a SMTP server that uses TLS on MX.

### Reference in the e-mail body to a URL

All email towards {{company}} consumers must use URLs in its message body which are build-up from a hostname component which is within the {{company_domain}} DNS zone.

A (transparent) re-direct is allowed from a URL within the {{company_domain}} DNS zone towards a page outside this zone.

Good examples:
www.{{company_domain}}/invoices/
service.{{company_domain}}/

Bad examples:
facebook.com/{{company}}/
youtu.be/{{company}}

### Including an URL towards a login page

In e-mail communication from the {{company_email_domain}} domain towards customers the body of the e-mail message may never include an URL towards a direct login page.

Example:
*When a customer is asked for an action in the {{company}} environment, direct the customer towards {{link_to_the_company_webpage}} and explain the customer to login to the required environment.*

### Mobile Mail for MSPs

Managed Service Providers may not receive emails from or containing information pertaining to {{company}} or her daughter companies on their mobile device(s).

### Use of Secure/Multipurpose Internet Mail Extensions (S/MIME) certificate

In e-mail communication towards customers from the {{company_email_domain}} domain the email message must be signed with a S/MIME certificate. The receiver must be able to verify the authenticity and integrity of the message.

### Sending e-mail from a domain

{{company}} branded domains that send e-mail must have implemented a DMARC record and tied to the SPF configuration for this domain

