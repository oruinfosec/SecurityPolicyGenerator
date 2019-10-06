# Access Control

## Business requirements of access control

### Identity and access on the basis of necessity

{{company}} provides only authorizations and access to systems to those employees who need it to perform their work, because otherwise (un)intentional damage can be caused or needless authorizations could be exploited.

### Access based on necessity

Access to systems must only be granted to an individual based on his role.

Access must only be granted to individuals who need to access a system, otherwise this access could be abused or unintentional damage could be caused.

No access to a service provider front office customer relations management system for a back office network provider employee. The CRM system is already configured to pass any necessary information to the back office employee when necessary.

### Authorizations based on necessity

Authorizations on a system must be based on an individual’s role.

Authorizations must only be granted to individuals who need this levels to do their job, otherwise unintended damage could be caused or unintended authorization could be abused.

Admin accounts must not have user functionality and vice versa. Wholesale information must only be accessible to the user that is allowed to process this information (Chinese walls).

### Remote access necessity

At least annually a justification must be given for remote access accounts of external parties.

### Stepping stones

When using remote access to perform maintenance on production systems (manual and/or in an automated matter), a stepping stone system must be used.

### Defining and documenting authorizations

Authorizations within a system must be defined and documented.

To allow consistent assignment of authorizations in the system and to enable periodic review of the correctness.

Authorizations can be documented in Function Authorization Matrix (FAM), which can vary from a 1 to 1 matrix (there is only 1 function for all users) to matrix with many functions in different segments to many system resources.

### Registration of Reliable Financial Reporting (RFR) applications

All new applications which are defined as RFR application by Group Risk & Compliance must on-board in IAM Portal.

Furthermore, if as a result from an audit or a compliance test (e.g. a walkthrough) an existing application is defined as a RFR application, it is considered to be a new RFR application and must on-board in IAM Portal.

All RFR applications must follow the process steps for attestation, validation (by the owner on functional application matrix and Business Process Rules) and monthly reconciliation.

Registration of RFR applications in IAM Portal is essential:

• to stay in control of logical access
• to prevent unwanted impact on the KPN Financial Annual Account.

*Examples are granting more than needed access levels (need to have principle), insufficient Segregation of Duties in the application or not taking into account regulatory compliance (i.e. Chinese Walls).*

It is preferable to onboard a RFR application in IAM via direct provisioning (link to an Active Directory or LDAP which automatically make authorization mutations).

Registration of financial applications like ZEUS, critical applications like BOSS or WASP.
Exceptions need to be documented and founded. Approval is needed by Group Risk & Compliance.

### Identity Management Systems

Identity Management systems (and chains of systems), such as (but not limited to) Active Directory Servers, Kerberos Servers, Identity & Access Management systems must be located within {{company}} premises and maintained by {{company}} (EP) employees.

{{company}} must be in ultimate control of who can access information of {{companys}} customers and {{company}}.

An application owner must be able to grant or deny access to the information systems under his control, without possible intervention by third parties.

### Identities are linked to a natural person

The personal identities of direct contracted employees must be registered in the applicable central HR system together with a {{company}} digital identity.

In case of external companies, these must assure the link between the {{company}} digital identity and personal identity of persons working for {{company}}.

It must be able to link every action performed by a {{company}} digital identity to a natural person, both for reasons of accountability as well as for verification of potential digital identity theft. As the privacy act prohibits registration of some personal identities responsibility for making the link must be formally delegated to the third party that registered the personal identity.

Account in logging reveals the person who created an order.

When group accounts are necessary, the reasons must be documented together with the additional measures to ensure traceability of actions to the natural person and approved by an appropriate business representative.

### Functional accounts

For functional accounts a responsible natural person must be assigned who is responsible for the use of the account, will act as authoriser and must be aware of this assignment and the implications of it.

We must be able to link every action performed by a {{company}} digital identity to a natural person, both for reasons of accountability as well as for verification of potential digital identity theft.
Examples of functional accounts are:

- Service accounts (A digital identity used for transferring data between specific IT systems. Persons can not login with these accounts);
- Shared functional accounts (e.g. for the use of a monitoring station on a NOC);
- System accounts (Accounts that come with a system).

### Default accounts

Default accounts must be disabled. If their use is necessary, additional measures should be taken to prevent misuse of these accounts and the accounts must be assigned to a manager responsible for use and authorization.

Default accounts are known to hackers and the first attempt is to get in by guessing the password.
A default ‘root’ or ‘guest’ user must be disabled or removed if possible.

When technically not possible to disable or remove, a password must be used of at least twenty characters and which contains multiple upper case, lower case, base digits and non-alphanumeric characters.

### Identity registration

Both the personal and {{company}} digital identities of direct contracted employees must be registered in the applicable systems, whereas for external companies the {{company}} digital identities must be registered by {{company}} and the personal identities must be registered by the external party.

To enable the linking of actions to responsible parties identities must be registered. For {{company}} employees we can perform both personal and digital identity registration whereas for outsourced activities we are prohibited from registering their personal identity information by the privacy act.

For {{company}} employees we register personal identities in the central HR system and the digital identity in the identity and access management portal. For employees working in offshoring contracts we only register the {{company}} digital identity, personal identity is the responsibility of the external party.

### Inventory of authorization decision

Each application, system and network element must have an up to date administration registering the current granted accounts and authorizations and who authorised these (manager and additional authorisers) and at what time.

For all existing accounts and authorizations must be traceable who authorised whom and at what time. Therefore an account/authorization request must be registered including who authorised whom and when.

Excel list with agree of managers and second authorizers.

### Responsibility for authorization

The granting and reviewing of user and system accounts and authorizations in use by external parties for {{company}}-owned systems must be done by the party within {{company}} responsible for the outsourcing contract.

Final responsibility for external parties working for {{company}} must always reside within {{company}} to guarantee control and enable reconciliation process.

This can be accomplished by evaluating each authorization-requests by or through the party within {{company}} responsible for the outsourcing contract.

A Telecom administrator of a business customer can get the authorization (and the associated responsibility) for granting sub-authorizations to users of the customer.

### Approval of authorization

A line manager must evaluate the authorization requests of his/her direct reports and is responsible for the decision; delegation of this responsibility during absence must be done upwards in line.

The decision of a manager to grant a certain authorization requires oversight on processes and risks. The line manager is the first line of defence of security risks. Depending on the nature of the application, system or network element, additional authorisers can be in place.

In {{company}} IAM the manager automatically has to approve or reject an authorizations request of direct reports.

### Correctness of granted authorizations

It must be verified at least annually if the granted authorizations of each employee are still needed to do their work (attestation by manager for direct reports).

Attestation is needed because required authorizations levels may change. Insufficient authorization will reveal itself in time but for excess authorization attestation is needed.

Due to changing process or change in job-content of employee some authorizations are redundant, attestation reveals this.

### Function Change

In the case of change of function, dismissal or reorganization the former manager must revoke accounts and authorizations.

The manager is responsible that the credentials of leaving employees cannot be abused.
A move from wholesale environment to retail requires elimination of rights to stay regulatory compliant.

Credentials that stay necessary in a new function need not be revoked if appointments are registered between leaving and new manager.

### System Data protection

Logical access to system or application data must be restricted to users that have the correct access rights conform Identity and Access Management policy, and system and application data must be encrypted when the system is placed outside {{company}} premises. Physical security and access must comply to the company rationales {{physical_access_control_specification}} and {{physical_security_of_technical_buildings_specification}}.

{{company}} internal data must be securely segregated from data of clients and partners.

Data from different clients or partners must be securely segregated from each other.

To allow consistent assignment of authorizations in the system and to enable periodic review the correctness.

Authorizations can be documented in Function Authorization Matrix (FAM), which can vary from a 1 to 1 matrix (there is only 1 function for all users) to matrix with many functions in different segments to many system resources.

### Protection of infrastructure information

Access to source code and associated items (such as designs, specifications, verification plans and validation plans) must be controlled, in order to prevent the introduction of unauthorized functionality and to avoid unintentional changes. 

The following guidance must be considered to control access to source libraries in order to reduce the potential for corruption of computer programs:

1. Where possible, source libraries must not be held on production systems.
2. Procedure must be available to manage the source code and the source libraries.
3. Support personnel must not have (unrestricted) access to source libraries.

Attestation is needed because required authorizations levels may change. Insufficient authorization will reveal itself in time but for excess authorization attestation is needed.

Due to changing process or change in job-content of employee some authorizations are redundant, attestation reveals this.

## User access management

### User authentication

End-users must log-on to the {{company}} End User Device using their personal user account and credentials, whereby two-factor authentication is necessary for remote access and signed/encrypted mail. 

If a {{company}} user accesses a {{company}} device, including Bring-Your-Own devices, then he/ she must authenticate with his/her {{company}} credentials

### Known origin

External parties that require remote access to perform IT and TI management for {{company}} must come from a known origin (IP address), and network filters must be used to enforce this.

### System log-on with an administrator or root account is prohibited

Users with administrator rights must not be able to log on to a system directly to the root, administrator or domain administrator account. 

The users must log on to the system with their personal and unpriviledged account and elevate their effective rights after initial entry on the system. In effect this means that all entry possible protocols to directly log on to a system, like SSH, RDP, SMB, etc, must be hardened to disallow network log on to these privileged system accounts and allow elevation of effective rights when the user is explicitly privileged to do so on the target system.

 This must be enforced by configuration deployment, e.g. ansible, puppet or group policies.

### Restricted Domain Administrator log on

Accounts with Domain Administrator privileges must never be used on normal workstations.

### Screening of database administrators

Database administrators must be screened according to the content and value of the database and the data within.

## User responsibilities

### Password change responsibility

For functional (static/system) or shared accounts the account owner is responsible for changing the password in case of a personnel change or change of ownership. Accounts without a password must not result into an interactive logon nor shell.

If personnel leave {{company}} then their password and second factors need to be changed to prevent possible abuse.

This requirement is there to prevent abuse of accounts when a {{company_worker_abbreviation}} leaves the company. If one does not remove these accounts it might lead to the person leaving {{company}} to possibly abuse their previous rights and harm the systems and/ or services of {{company}}.

## System and application access control

### Elevated rights

Applications or programs may exclusively be started with elevated rights when there is a technical need, but must not execute tasks with elevated rights.

For example: a web-service or database.
It is allowed to execute tasks with elevated rights when these tasks service a system administrative role. For example: Puppet, Ansible or GPO-deployment.

### Configurable passwords

Passwords must not be hard-coded in software, but made changeable/configurable.

### Password length

Minimum password length a system must support is determined by the type of account:

| Account type                                                 | Example                                                      | Min. length |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ----------- |
| User account: account without special privileges.            | {{companys}} worker                                          | 10          |
| Admin/operator account: privileged account or has privileges of other accounts. | Admin/root account, billing account, functional administration | 16          |
| Functional account: accounts used by systems or applications, login and actions are usually automated, accounts are rarely changed. Also used for pre-shared keys | Printer account, VPN with PSK                                | 24          |

In older systems unable to meet these requirements maximum password age should be enforced.

Maximum password lengths must not exist. If, for performance reasons, a maximum password length must be imposed, a password of at least 64 characters must be possible.

### Password complexity

Systems must support and enforce passwords containing the full range of printable ASCII characters. 

Passwords must contain at least three of four groups of characters, which are: at least one uppercase, at least one lowercase, at least one number and at least one other readable character, also known as a special character.

This complexity requirement may also be lowered when the system can enforce passwords equal to or longer than 16 characters; guaranteeing that the secure storage of passwords is in accordance with the cryptography requirements for password storage and supports the usage of all printable ASCII characters as input, including the space character.

### Initial passwords

Systems must force a user to change an initially provided password (passwords not defined by the user, e.g. passwords provided by the Service Desk) at first usage.

The initial password provided to end users does not need to meet the complexity rules, with reservation that it is unique and must be changed at first login into a password that does meet the requirements. If the initial password does meet all password rules then the password needs only to be changed within 2 days after the first use.

This includes changing default passwords a system or application comes with before the system or application is put to use.

A reset password procedure must never reapply the initial password.

### Distribution of account name and password

Account names and passwords must be sent in separate electronic or hard-copy messages.

When sending a username and password then these may never be combined in the same message irrespective of the medium (e-mail, letter,etc) or manner of it being sent. 

*For example, when sending new account details with a colleague, the username is sent in email A and the password in email B.*

### Password storage

For user accounts:

* Passwords must be stored irreversible encrypted format (hashed) and salted (to prevent cracking hashed password using “rainbow tables”).

For password keeping tools:

- The password for the tool should comply with all requirements in this rationale.
- Passwords in the tool’s database should be protected with encryption and use message integrity to prevent tampering conform Encryption Algorithms and Hash Algorithms.
- Passwords may only be reversibly stored when there is an explicit reason to do so. An example use case is KeePass.
- Also, passwords may be necessary to be able to log on to an adjacent system at the beginning or end of a process. In this particular situation passwords must be stored encrypted and additional measures must be taken to secure the information.

### Password history

Systems must enforce a new password to be different from the last ten passwords.

### Use of biometrics for authentication on mobile devices (phones, tablets and laptops)

Biometrics are not allowed as part of a multi factor authentication process, but only as a means to unlock credentials stored in a hardware secure vault solution. 

*E.g. Apple TouchID, Apple FaceID, and fingerprint sensors on Samsung S5 devices or later are acceptable solutions as they all use a secure hardware vault solution to store the fingerprint details. Also Windows Hello is allowed as a biometric solution, assuming the credentials are protected on the device using a TPM 2.0 chip.*

Biometrics on mobile devices and/or PCs have, at this time, vulnerabilities allowing them to be spoofed by a malicious attacker. Therefore they may never be used as a means of authenticating a user. See *[Authentication methods](###Authentication methods)* subheading for the requirement and list of technically accepted authentication solutions.

### Password transmission

Before a password is transmitted, the transport channel must be encrypted. When resources need to be transported and viewed all related resources must be transmitted over an encrypted transport channel, e.g. a log on page.

### One Time Passwords

An One Time Password (OTP) must only be valid once per context. A context is a combination of a subject (e.g. an account), action (e.g. log on or reset), resource (e.g. particular service interface) and its validity period. An OTP must at least be 6 characters long with a validity period less than 15 minutes. 

An OTP is a temporary code that can be used as a value for a second factor.

### Maximum password age

The password age which a system must support is determined as shown in the table below:

| Account type                     | Minimal validity period | Maximum validity period |
| -------------------------------- | ----------------------- | ----------------------- |
| User account                     | 3 months                | 6 months*               |
| Administrator / operator account | 3 months                | 6 months*               |
| Functional account               | n/a                     | 24 months               |

** The passwords for these accounts are valid for 6 months, when the password storage is using {{company}} accepted encryption methods or when the account originates from the {{company}}.local domain, maintained by N&I Workspace Services.* 

###  Password reset procedure for applications

In case of a forgotten application password, the password must be reset and sent to the user’s already known (corporate) e-mail address or mobile phone number. An alternative is to send a reset-token or URL with embedded reset-token to guide the user through the reset-functionality process.

After receiving a password reset the user must change this password.

The replied temporary password or token must have a limited lifetime but must never exceed 24 hours. A good limit is a maximum of 15 minutes validity time.

When two factor authentication is part of the account, access to a system must be (re)established using two factor authentication as part of the obligatory password reset. All sessions or session tokens must be reset and a user must re-authenticate before having access to the respective system or application.

A strong reset process is required to prevent possible abuse when a users credentials have been compromised for whatever reason.

### Password reset procedure

When an account requires a password reset by a help desk, the help desk must identify the user by information not published on the intranet, nor by public information, like a secure question or information exclusively accessible on a national ID card or Company Card. A better solution is to challenge the user by sending an e-mail (when still accessible) or sending an SMS with an OTP. The user can prove his ownership to an account by exchanging the requested information from this message to the help desk employee.

The user must be informed by sending an e-mail, SMS or both to indicate that the password of the account has been reset and from which means, like a terminal or help desk.
Communicating passwords in a secure manner can be done over the phone (verbally), via SMS or a password reset link. 

A strong reset process at the help desk is required to prevent possible abuse when a users credentials have been compromised for whatever reason. If user credentials require a second reset within a short timeframe the role of the help desk is to prevent an attacker from getting access to the new credentials via social engineering.

### Password reset frequency

Network passwords, e.g. from a {{companys}} domain account, and/or second factor tokens may not be reset more than once every 4 hours. In case of an emergency, or if the account needs to be reset sooner, the respective help desk must be contacted.

To prevent a user from resetting his or her password to the same value, by quickly doing multiple password resets, a timer has been set. However when the help desk is not available a user can still regain access to his or her account by waiting.

### 2FA reset procedure

In case of a forgotten or lost second factor token the provisioning of the token must be restarted as with a new user. All sessions or session tokens must be reset and a user must re-authenticate before having access to the respective system or application.

A strong reset process is required to prevent possible abuse when a users credentials have been compromised for whatever reason.

### Hide password on screen

Passwords must not be visible on the screen in clear text during the login procedure. Use obfuscation such as * * * * * * * * and include confirmation field when defining passwords to avoid errors.

### System feedback of failed login

Systems must respond with a generic message when a log on fails *(e.g. “username or password is incorrect”)*.

### PIN code

The length of a PIN must be five or more digits.

The following PINs are series that must be excluded from use: 12345, 00000, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888 and 99999.

Using a different amount of digits will result in a similar restriction of use.

### Strong authentication and session management controls

A single set of strong authentication and session management controls must be used. 

### Authentication methods

Systems must authenticate users based on username and password and, if required, a second factor. The authentication method must comply to the level defined in {{password_security_rule}} and the technical and procedural requirements set in {{identity_and_access_management_standard}}. The authentication method must be traceable to a natural person unique user and shall not be copied or expire within a short period of time frame (e.g. 5 minutes).

Some applications and/or systems have a higher value for {{company}} and therefore have stricter security requirements. To make sure that the authentication procedure only lets in the correct users certain technical and procedural measures must be in place to support these security requirements. Technically strong authentication methods must be accompanied by an equally strong identity verification procedure in the enrolment of an account.

### User authentication by the backend

If user specific data will be obtained from the backend server, the app passes the user credentials through to the backend server, all authentication requests must be performed server-side. Upon successful authentication, application data will be loaded onto the mobile device.

This will ensure that application data will only be available after successful authentication.

### User authentication by the app

If user specific data is obtained from the backend server and/or stored within the app data, the user must be required to authenticate to the app.

It is not sufficient to trust only on device authentication.

### Proper authentication and authorization for each page

The enforcement mechanism(s) must deny all access by default, requiring explicit grants to specific users and roles for access to every page.

### Account lockout

Account must be locked for at least 15 minutes after five failed logon attempts.
When the failed logon attempts result in a lock-out, the user of the account must be notified about the attempts and informed about the origin of the attempts, e.g. source IP address, country of origin, etc.
In addition, the service must have additional measures in place to block the attempts, e.g. blocking the attempts based on source IP-address.
If possible the phone number of the security help desk must be included in the message to the user.

By informing the users that their login accounts are being abused the users can determine if this is them or if an attacker is trying to access their account and a response from the {{responsible_cert}} is required. By adding the number of the security help-desk the users can quickly respond if the block is not due to their actions.

### Session management

Session management must be handled correctly, using appropriate secure protocols, after the initial authentication. For example, require authentication credentials or tokens to be passed with any subsequent request (especially those granting privileged access or modification of data).

• Use unpredictable session identifiers.
• Invalidate cookies on logout.
• Session management should be controlled/managed at server-side. Implementations that rely on stateless sessions, e.g. using JSON Web Tokens (JWT), are not allowed for session management

### Session Timeout

When a user does not perform any action on a web site during a certain interval (defined by the web server) the status of the user session on the server side must be changed to "not used anymore" and instruct the web server to destroy the user session (deleting all data contained into it).

• Set session timeout to the minimal value possible depending on the context of the application.
• Avoid "infinite" session timeout.
• The session cookie must expire when the browser is closed.

### Use strong session tokens and protect these

• Session tokens may not be predictable and should be able to (reasonably) withstand brute-forcing attacks.

• The session ID must simply be an identifier on the client side, and its value must never include sensitive information (or Personal Identifiable Information). The contexts associated to a session ID must be stored on the server side.

• Session tokens must not be exposed through other channels.

• Session IDs must be have an entropy of at least 112-bit and the value must be derived from a cryptographically secure random number generator.

• Session IDs must have a suitable validity period.

• Session IDs must be replaced after logging in and deleted with a timeout on the server side.

• All existing session tokens/active sessions must expire immediately once credentials have been successfully changed, so that existing sessions on other devices/apps/etc. (based on the old account information) will not remain valid until the normal session expiration time.

### Page authorization in a workflow

If the page is involved in a workflow, it must be verified that conditions are in the proper state to allow access.

### Indirect Object References per user or session

Object references should not be predictable and able to withstand brute-forcing attacks.
• Per user or session indirect object references must be used.
• The application must map the per-user indirect reference back to the actual database key, file or other object on the server.

### Check Access when using Direct Object References

Each use of a direct object reference from an untrusted source must include an access control check to ensure the user is authorized for the requested object.

### Screen-lock and password security

After 15 minutes of inactivity on the end user device or steppingstone, the user must re-authenticate.

If a screensaver is enabled it must always go directly to the lockscreen to reauthenticate the user.
Non-interactive workstations with a dedicated purpose of monitoring a system or service on screens are exempt of this policy only when the logged on account can exclusively monitor, but not manipulate nor change anything.

Using a timeout prevents a laptop staying unlocked when not in use. If the user triggers a screensaver, for example by using 'Hot Corners' on a MacOS device, then this is a trigger that a user is away from the device therefore requiring the user to re-authenticate when he/she returns.

### Access to database

One application may connect to multiple databases, but must fulfill the following requirements:
- The application must ask for written permission from the respective administrators, the owner of the connected application(s), and the owner(s) of the data for all connected databases. This written permission must explicitly allow the interconnection between all other databases and be given for every (new) connection.
- The application acting as a data hub must adhere to the combined security requirements for all connected databases.
- The application one has the rights to access and is only able to manipulate the data as required for its correct functioning.

### Network segmentation and zoning for databases

Applications that do not have access rights to a database must not be able to reach the database over a network. If an unauthorised attempt is made to access the database it should be logged and immediately sent to a central logging entity.

### Zoning and segmentation for databases

Databases must be hosted on a platform which adheres to the network segmentation and zoning requirements. Databases that contain credentials, Personally identifiable information or information classified as internal or secret must reside in a green zone.

### Access to data on disk

The data on disk must not be accessible to people that do not have access. If a person has rights then this must be limited to whatever is required for them to fulfill their role.

### Forced path

Measures must be taken to enforce a user to follow a layered connection setup. No other connections than needed and allowed must be possible.

### Remote support connection duration

When remote support is needed on {{company}} devices, the lifetime of the connection must be limited to the time required to perform this support.