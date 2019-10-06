# System acquisition development and maintenance

## Security requirements of information systems

### Single use

Systems must be setup and configured to support one service type or application type (such as web services or database). In a virtualized environment, every Virtual Machine counts as one system.

### Stripping

All systems and applications must be stripped of non-essential functionality. If removal is not possible then the non-essential functions must be disabled.

### System interfaces

System interfaces must be exclusively assigned to one production zone.

In addition, systems must have a separate management interface in a management zone (physically or logically). Additional system interfaces must be added to the same configured zones.

When physical or logical zoning is not possible in for instance a phpmyadmin site, the logical zoning must incorporate a method like whitelisting the management stations in order to only allow management stations to address the management portal.

### Host based protection

Systems connected to the Internet must be equipped with host based protection mechanisms, such as ACLs, firewalls, IDSs, antivirus software and antimalware software.

### Portal Authority

All new or renewed {{company}} directly Internet facing products and services and new products and services using new technologies must be assessed from a security perspective by means of security testing by the {{company}} Portal Authority (PA). No project may go live without PA approval.

### Sharing of infrastructure

Multiple applications may store their data on a shared database, but must fulfill the following requirements:
- The security risk profile of all applications must be the same. i.e. for nationally defined vital infrastructure services the database must not be shared with nonvital infrastructure services.
- The applications shared on the platform must have similar uptime and at a loss requirements.

### Application security architecture

Shared hosting or virtual hosting must not be used without separation on all layers of the application, including the platform on which the application is active, the framework, application specific code and the database.

### Applications sharing a platform

When more than one application is hosted on a platform, the security measures needed for each application must be implemented for all hosted applications; applications must not share the same platform when they do not have approximately the same function.

Applications sharing a platform may influence each other or may be an attack surface for each other.

When two web applications with different risk classification share a system, the web application with the lowest risk classification must have the same security measures as the web application with the highest risk classification; otherwise it can be attacked to reach the highest classified information on the system. 

*The Security Architecture Guidelines give more insight in how to protect cloud solutions with regard to this requirement.* 

### Container image layer controle

Containers must be assembled and build from image layers containing supported software, which can be commercially supported or community supported. All image layers must be kept up to date.

### Container segmentation and zoning

Containers must not be consolidated on the same system (i.e. (virtual) machine) when they differ on zone, DTAP purpose (development, testing, acceptance and production), customer or risk-level. The administrator must classify the risk per group of containers in one particular zone and for one customer on the effects of:

- kernel panics, i.e. focus on the business continuity aspects.
- container break-out and information security, i.e. ensure that a container breakout does not escalate into data extraction from shared volume devices.
- network segmentation between containers on the network bridge devices.

*Exception: When the container serves an Network Function Virtualization role for OSI layer-2, layer-3 or layer-4 function, also regarded as part of data transport network, than this is allowed.*

### Security standard for databases

The storage of data in a database must be done securely to prevent unauthorized access and, indirectly, fines by third parties.

### Customer account database separation

For different (business market) customers, account databases must be split into separate Active Directory or LDAP directory systems. The databases may be combined to form one logical pool of accounts for a distinct purpose.

### Retrieving content from remote locations

If content is retrieved from remote locations (over the internet) then always communicate through HTTPS, even if the content does not contain any personal/sensitive information.

### Web and Mobile Applications

Web applications running on systems reachable from the internet and mobile applications running directly on a mobile device must comply to the (Web) Application Security respectively Mobile App Security rule.

The Portal Authority must give approval on first launch or on launch after a substantial change.

### File upload

The upload functionality of an application or system must be hardened to prevent the execution of code or a denial-of-service situation.

### Mapping values as destination parameter

If destination parameters can’t be avoided, the supplied value must be valid, and authorized for the user. Any such destination parameters must be a mapping value, rather than the actual URL or portion of the URL, and the server side code must translate this mapping to the target URL.

### Maintaining the integrity of information processed

The integrity of information processed by applications must be maintained by ensuring that:

• information is not corrupted when modified by more than one user
• information cannot be overwritten accidentally
• the processing of information is validated
• changes to key ‘static’ information such as customer master files or currency exchange rates are reviewed
• unauthorised or incorrect changes to information are detected

### Preventing inaccurate entry of information

Inaccurate entry of information must be prevented by:

• Only accepting data from trusted and authenticated information sources for data changes (creation, change, deletion)
• New records have initialization values
• Using error messages

### Data input from other sources

Data input through alternative sources directly loaded in the app is forbidden. This should only take place via the explicitly specified backend server.

### Output validation

Output validation routines must be used to allow a reader or subsequent processing system to determine if output is within predefined data range and all data is processed.

### Revealing application or system information

The application must not reveal server side information such as internal IP address, server name and other system information that could aid an attacker, to non-authenticated users. Unnecessary application or system information such as stack traces, codes and parameters must not be disclosed.

*Possible exception: the name of the application, without version indication, the protocol version number may be revealed*. 

### Brute-Force protection

Internet facing applications must protect its (user) accounts from brute-force attacks. A process must be in place to detect abusive behavior and a process must be in place to react upon the abuse.

Possible origins:
• Brute-forcing the password per account.
• Brute-forcing the accounts by fixating a password or PIN and brute-forcing this on all accounts.
Possible actions:
• Detect (rapid) automated login attempts and react by blocking the IP address temporarily. Report to SOC.
• After detecting abusive behavior; force the account to logon with a CAPTCHA. Report to SOC.
• After detecting abusive behavior; force the account to logon with a second factor. This option assumes there is an opportunity to use SMS or another out of band communication method. Report to SOC.

### User enumeration

User enumeration vulnerability must be prevented. User enumeration is not limited to username property of an account. All identifiable property of an account could be used for user enumeration.

*Possible exception: interfaces purposely developed to list users, accounts or identifiable objects are allowed.*

[User Enumeration explained](https://www.owasp.org/index.php/Testing_for_User_Enumeration_and_Guessable_User_Account_(OWASP-AT-002)) (OWASP)

### Sensitive data in URL or GET request

Personally identifiable information, tokens and passwords must not be visible in the URL or parameters of a GET request. Any accompanying credentials must be placed in the header or data fields.

### App Permissions

Make the set of permissions that will be required by the mobile app as small as possible.
For every permission, describe why it is needed.

### Correct date and time

Every system or application must use the central internal NTP platform as a time source or a directly connected time server. External sources are not permitted. The time zone must be configured with the local time zone.

It is important that all systems and applications have the same time at same moment. To accomplish this, it is necessary that everything synchronizes with the same time source or a directly connected time server. This way, all systems or applications will use a stratum 1 or stratum 2 timestamp.

Besides the fact that this accomplishes consistency in time, we also accomplish that systems are not influenceable through third party sources. Because of this, systems do not only have the correct time, but the time is also trustworthy.

It is permitted to set up an NTP server that is used to synchronize other systems deeper in the network. In this case, the NTP server must synchronize with the central NTP platform by using it as the only source. For example: Within a Windows domain it is enough if the domain controller with the PDC role is configured to use the central NTP platform if all other domain servers and clients are configured to synchronize their time with the PDC.

Please note that NTP does not synchronize time zone or daylight savings time. Therefore, it is necessary to configure this locally. If in doubt, configure the time zone {{company_time_zone}}.

### Stratum 0 sources for NTP servers

Time sources that are part of the central {{company}} NTP platform must use a minimum of two different stratum 0 sources.

Stratum 0 sources are e.g. Global Navigation Satellite Systems (GNSS) like GPS or Galileo, atom clocks, or the radio signal DCF77.

It is only permitted to use GNSS as a time source when mitigations are implemented against spoofing or jamming of the GNSS signal. This can be done by implementing e.g. a GPS firewall or a reference clock that must be used to detect the skew of time.

### CIS benchmarks

Network and server equipment, for which Center for Internet Security (CIS) benchmarks are available, must be hardened as described in these benchmarks, including default configuration values, default account and password blocking.

In case of a conflict between the CIS benchmark results and the {{company}}, the {{company}} is leading.

[CIS Benchmarks](https://benchmarks.cisecurity.org/downloads/multiform/index.cfm) 

### No CIS benchmarks available

Network or server equipment, for which Center for Internet Security (CIS) benchmarks are not available (such as applications), must be configured according to the security guidelines from the supplier of the equipment, or if available, application specific guidelines developed by {{company}}.

### CIS benchmark scenario choice

When the CIS benchmarks provide multiple scenarios, the most strict scenario should be followed.

Level 1 is a minimum requirement: This means that every deviation on the CIS baseline must be accepted by CISO.

Level 2 recommendations: must be configured in (highly) secure environments. Level 2 is mandatory for all services marked as vital.

### Relevant {{companys}} requirements

Relevant {{companys}} requirements must be selected and documented as part of the overall requirements.

### Project Classification

A Project Classification must be performed.

### Security Risk Assessment

If Project Classification result is high risk, a Security Risk Assessment must be performed.

### Innovation specific additional requirements

Additional requirements specific to the innovation (resulting from the security risk assessment) must defined and documented as part of the overall requirements.

### Coverage check

The project must perform the following check:

Before supplier or solution selection: verify that all applicable business continuity and security requirements on innovation are covered by the innovation or change which is developed by the project.

### Base security measures

All relevant {{company}} requirements must be implemented.

### Supplementary security measures

For high risk projects, a security risk assessment must be performed and resulting requirements must be implemented.

### Database hardening

Datastorage solutions, e.g. databases, file shares, sharepoint, NAS, SAN, etc, must be hardened according to best practises from the hardening guidelines. The {{company}} standard is leading in case of a conflict.

## Security in development and support processes

### Portal Authority approval

Before going live: Portal Authority conducts a security test. Any discrepancies found during security testing must be evaluated against the CVSS score. Discrepancies with a CVSS score of 4.0 or higher (medium or high) are deemed blocking.

### Follow guidelines and best practices

The development guidelines for security of the underlying platform (e.g. Android, iOS, Windows Phone) must be followed.

Platforms offer standard solutions for security, such as for authentication, secure data storage and secure network communications.

If best practices exists for security measures that are not explicitly described in the platform’s development guidelines, these best practices must be followed.

### Requirements for non-production platforms

Platforms for development, testing and acceptance must be separated from the production platform.

Testing the change in the production environment poses extra risks because of possible unexpected behaviour due to the change.

### Web-based and other application software

For all applications -self developed and delivered by a third party- the security life cycle has to be followed, where vulnerabilities are prevented, detected and corrected.

This rationale defines a set of requirements regarding the protection of (web) applications.
These requirements are based primarily on the OWASP Top 10 most critical web application security risks and the Framework Secure Software by the Secure Software Foundation.

The requirements provide security only under the assumption that an application runs on a system that is hardened according to system hardening requirements mentioned in this chapter as well as in *Access Control*, *Communications security* and *Operations security* chapters.

This policy is written for all {{company}} employees and managers who are involved in developing, maintaining and testing (web) applications. It concerns all applications owned by {{company}}or applications from vendors/partners that are used for {{companys}}purposes.

### Updating and patching of the (web) application

All source code, including libraries that are used for generating the (web) application must be maintained and patched for vulnerabilities and stability issues when applicable. Application (code) moving into production must be security tested via code reviews (adhere to [OWASP Secure Coding practices](https://www.owasp.org/index.php/OWASP_Secure_Coding_Practices_-_Quick_Reference_Guide)) or penetration tests.

### Rate limiting

Employ rate limiting and throttling on a per-user/IP basis (if user identification is available) to reduce the risk from DDoS attack.

### Preventing injection using white list input validation routines

Positive or “whitelist” input validation must be used. Such validation should decode any encoded input, and then validate the length, characters, format, type and range on that data before accepting the input. Perform consistency checks at various stages of information being processed.

This is not a complete defense as many applications require special characters in their input.

### HTTP Request Preflight

Setup a protection against CORS (Cross-Origin Resource Sharing) HTTP request that try to bypass the preflight process.

### Preventing Cross-Site Request Forgery (CSRF)

CSRF tokens may not be predictable and must be able to (reasonably) withstand brute-forcing attacks. An unpredictable token must be included in the server response, preferably in a hidden field in the form body. This token must be returned by the client and validated by the server. Such tokens must at a minimum be unique per user session, but can also be unique per request.

### Transport Layer Protection: sensitive cookies

The HttpOnly and Secure flag must be set on sensitive cookies.

### Transport Layer Protection: backend and other connections

Backend and other connections must also use TLS or other encryption technologies.

### Involvement of user parameters in calculating the destination in redirects and forwards

Don’t involve user parameters in calculating the destination in redirects and forwards.

### Support HTTP Strict Transport Security (HSTS)

The Strict Transport Security response header must be set to enforce HTTPS. The 'max-age' must be set to at least 5.184.000 seconds (=60 days).

### Preventing injection using a safe API

All APIs (in both consumer and producer role) must use a parameterized input methodology to avoid exploitation through an interpreter, e.g. SQL prepare statements or distinct key value pairs.

Also, buffer boundaries must be checked explicitly when the environment is susceptible to buffer over- or underflow attacks. If possible, the API must avoid the use of an interpreter.

### Preventing injection using a non-parameterized API

If a parameterized API is not available, special characters must be carefully escaped using the specific escape syntax for that interpreter.

### Preventing Cross-Site Scripting by escaping all untrusted data

All untrusted data based on the HTML context (body, attribute, JavaScript, CSS, or URL) must be carefully escaped. This escaping must be included in applications unless the UI framework does this for them.

### Referer header

When an application links to a third party application the leakage of sensitive information should be prevented. For relevant pages the web application must include the appropriate Referrer-Policy in the header.

In general applications should prevent the leakage of information. The referer header is one of the sources that could leak information.

Example: A web application uses HTTPS and a URL-based session identifier. The web application might wish to link to HTTPS resources on other web sites without leaking the user’s session identifier in the URL.

### Authorized Applications

Applications and apps involving security tooling, on end user devices which have access to {{companys}} (office) networks, must be authorized by the Portal Authority (CISO).

Other applications and apps used should be authorized by the Portal Authority (CISO).

### Portal Authority - handling new projects

All new or renewed {{companys}} directly internet facing products and services and new products and services using new technologies must be assessed from a security perspective by means of security testing by the {{companys}} Portal Authority (PA). No project may go live without PA approval.

### Innovation classification

For all innovations, projects and changes it must be determined if the security risk is high.

## Test data