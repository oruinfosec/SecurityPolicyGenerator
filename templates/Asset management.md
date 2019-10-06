# Asset management

## Responsibility for assets

### Destroying confidential information

Confidential information must be destroyed as soon as the information is no longer needed. Digital confidential information must be permanently deleted. Hardcopy confidential information must be destroyed using a paper shredder or a designated container for destroying confidential documents. When digital confidential information cannot be permanently deleted, the media containing the digital confidential information must be physically destroyed.

### Ownership of information

Information must have a designated owner. The “owner” is the individual or entity that has approved management responsibility for controlling the production, classification, processing, use and security of the information.

In case of damage resulting from non-compliance due to negligence, lacking due-care or due-diligence, the responsible employee or manager (”owner”) may be held personally liable for the damage and, in severe cases, may be subjected to an investigation.

### Ownership registration

The owner of an asset (including non-{{company}} assets used by {{company}}) must be registered, including contact information. Registration must be central and searchable.

Responsibility for each asset must be clear and easily accessible. Both for purpose of accountability as well as for incident support.

Registrations can be done in a CMDB. Hardware like a router or server, but also applications can be entries in a CMDB. New applications are registered in the IT Repository.

### Management registration

The party managing an asset (including non {{company}} assets used by {{company}}) must be registered, including contact information. Registration must be central and searchable.

Responsibility for each asset must be clear and easily accessible. Both for purpose of accountability as well as for incident support.

Registrations can be done in a CMDB. Hardware like a router or server, but also applications can be entries in a CMDB.

### Location registration

For each asset the physical location and network location must be unambiguously registered. Registration must be central and searchable. This includes non-{{company}} assets if hosted on {{company}} location or network.

There must be no confusion about the physical and logical location of an asset. This location is used for:
- Incident response.
- Implementation of continuity measures.
- Traceability.
- Implementation of security measures.

For unmanaged devices (e.g. media converter), address and room location might be sufficient. For a router, an address, room and rack/shelf/slot location is needed as well as ip addresses for each interface. For an application should not only be on what server(s) it resides but also the exact location of such server(s).

So the amount of location data needed for correct location registration might vary between but goal should always be clear, we must be able to quickly locate the assets without having to consult multiple sources.

An asset for which the location is kept secret (for whatever reason).

### Register {{company}} End User Devices

End User Devices (EUD) must be registered centrally to ensure the identity of the owner, license management, ensure proper security patch management, aid with stolen devices, whereby at least the following information must be stored in the registration functionality:

• Device type.
• Device ID.
• Owner information.
• Subscriptions.
• Dates of device handout, replacement and take-in.

A process must be in place to ensure accuracy and correctness of this registration function, until hand-in.

In case of theft, publication of security issues, misuse or dismissal the registration is needed.

Register serial numbers, software licenses, MAC addresses, user identity

### Automatic e-mail forwarding

It is forbidden to automatically or manually send {{companys}} mail to personal non-{{company}} mail addresses.

E-mails must not be automatically forwarded to email addresses outside of the {{company}} unless it concerns email for an external employee who contractually is working for (a hundred percent subsidiary of) the {{company}} and the mail is sent to a functional business group mailbox, for example, from a service desk.

In this case it is possible to forward the mail from the {{company_email_domain}} address to the correspondence address. The {{company_email_domain}} address remains accessible.

Forwarding is for exclusive functional use of call centers, technical management, support, etc.

### Network documentation

Network documentation must be present for network infrastructures describing:
The network design (including security requirements).

* Required service levels.
* IP number plan.
* Communication matrix.
* Dependency on external parties.

This documentation is needed mostly for daily maintenance, but in the case of a security incident this information can be used for assessing its impact and to support the solution of the incident. 

A network can for example be described using a network diagram that shows how the network is constructed. Included should be a list of all protocols that are needed for the correct working of the network and the service.

### Storage and destruction of customer data

{{company}} must ensure that personal data is always secure, commissioned by {{company}} and under secrecy by a processor. Furthermore personal data shall only be kept (in a form which permits identification of the data subject) for as long as necessary for achieving the purposes for which they are collected and/or further processed.

### Nature of Public Cloud

The confidentiality, integrity and availability security requirements for data classified as Internal use allow it to be stored on a cloud infrastructure that is provisioned for open use by the public. It is owned, managed and operated by a third party, and it exists on the premises of the cloud provider.

### Nature of Private Cloud

The confidentiality, integrity and availability security requirements for data classified as Confidential allow it to be stored on a cloud infrastructure that is installed for exclusive use by {{company}}. It is owned, managed and operated by a third party or in combination with {{company}}, and it exists on premise or off premise.

The cloud infrastructure is not a private cloud when a public cloud solution is required to operate it.

## Information classification

Information must be classified and labeled to indicate the expected degree of protection when handling information.

Classifications are used to ensure that the people who have knowledge of “confidential” or “secret” information are limited in number and remain identifiable at all times. Classified information requires measures to ensure an additional level of protection or special handling.

### Storage of security related data

Data that has specific security significance, such as passwords, keys and login tokens, must be stored using the platform’s secure storage facilities for security related data.

For example:

* For iOS, use the Keychain
* For Android, use the KeyStore*
* For Windows Phone, use the Data Protection API (DPAPI)

*For Android devices, which do not feature KeyStore, it is recommended to implement an encrypted container which requires user-input to decrypt. *Example: ask for a PIN, use the PIN as input to PBKDF2 and decrypt an AESencrypted file which holds the credentials.*

### Storing confidential information

Digital confidential information must be stored on an encrypted device or medium and secured as stated in Cryptography chapter or on a file server which can only be accessed by authorized users, whereby shared directories must include additional authorizations. Hardcopy confidential information must not be left unattended, but must be kept in a locked cabinet or in a safe.

### Labelling secret information

Documents containing information that is considered secret (as defined in chapter "Secret information") must contain the word “Secret”  on each page.

### Date secret information

In most cases the classification “Secret” is only temporary. Documents labelled “Secret”  are only considered sensitive until a specific date and must specify this date with the label, e.g. “Secret until 01-01-2019”.

### Access to secret information

Secret information must only be available to authorized people which are in a list added to the document. Copies of secret information must be individually numbered and an individual that has received such a copy must have signed for this in a register.

### Duplicating secret information

Duplication of secret documents is not allowed, unless permitted (and provably so) by the author or owner of the document.

The individual receiving a numbered copy of a document that is labelled “Secret” , remains accountable for every copy of that numbered document that will be made. (To ensure traceability, it helps to put the number of the copy on each page).

### Printing secret information

When printing secret information on shared (multifunctional) printers the “follow-me” process needs to be used. When this is not available the “Secure Printing” option must be used (using a pin code). Documents containing secret information must not be left unattended on printers or in the printer area.

### Follow me printing

In order to prevent physical data leaking, every printer must be configured to only start a print-job after the owner of the print-job has entered a release code on the specific printer or offers his company card.

A scanned document will only be sent to a known email address from the Whitelist HR. Every other email address is prohibited.

To avoid unauthorized access to printed information and to avoid data leakage to unregistered mail addresses.

Use of predefined pin code or company card credentials at the printer to get the print-out or to scan the document.

### Secure printers

Printers must be hardened to avoid access to information and data leakage.

To avoid unauthorized access to printed information.

Access to print-information in cache must be denied; scan-to-email only available to {{company}} email addresses, print-jobs not executed must be removed end of working day. Disk wipes performed every night to clean up storage space on printers.

### Sending secret information

Digital secret information must be encrypted with strong encryption and provided with a digital signature before sending.
The sender of secret information must ensure that the receiver has sufficiently secure equipment for reading (and/or otherwise processing) this information before sending the (encrypted) information and knows how to handle this information given its classification. Encrypted message and method of decrypting /password must be separated through another channel.

The sender must inform the recipient personally that the information is secret.

Hardcopy secret information must be sent in closed envelope labelled “Secret” enclosed in another envelope only containing address, send by registered mail with acknowledgement of receipt, trusted courier or by personal delivery.

### Storing secret information

Digital secret information must be stored locally on an encrypted device or medium and secured as stated in Data protection document. Secret information in hardcopy or encrypted digital storage must not be left unattended, and must be kept in a strong locked cabinet or in a safe. Keys to cabinets or safes must be assigned to registered persons who are responsible.



### Perform an (information) security risk assessment

Prior to purchasing or using cloud services an (information) security risk assessment must be performed, which takes into account:

the type, classification and importance of information that may be handled in the cloud (e.g., commercial information, financial information, intellectual property (IP), legal, regulatory and privileged information (LRP), logistical information, management information or personally identifiable information (PII)).

### Type of information

On the basis of a (information) security risk assessment must become clear if it concerns the following type of information:
Secret:

- share price sensitive financial information;
- information on fraud management;
- information on Lawful Intercept.

Confidential:

- other financial information;
- information related to a person;
- information on {{companys}} infrastructure;
- information on {{companys}} security vulnerabilities;
- information on {{companys}} intellectual property;
- information on competitiveness (strategic plans, M&A, etc.).

### Confidential information

Information must be classified as 'confidential' when unintentional disclosure can have negative impact and/or when the information is related to a person.

When information is classified as 'confidential', certain requirements are applicable to protect the information from being unintentionally disclosed in the public domain.

Personal data of {{companys}} employees as well as customers must by classified 'confidential' as set in the privacy regulation.

Disclosure of network and (functional) architecture drawings causes several demonstrable risks. Therefore these designs must also be classified as 'confidential'.

### Secret information

In certain special circumstances information must be classified as secret. These circumstances are when {{company}} is legally bound to handle information secretly and when unintentional disclosure can have extreme negative impact on {{company}}. Special procedures must be implemented to handle secret information.

When unintentional disclosure of information could lead to negative impact, information must be classified as confidential. This means additional measures are taken to protect the information. However, in certain special cases even stronger measures must be taken. These situations are rare within {{company}} and the majority of {{companys}} employees will never handle secret information. For those situations where secret information is handled, specific procedures must be implemented.

Information on mergers and acquisitions, information that might influence {{companys}} share price.

### Information for Internal use

Information must be classified “for internal use” when it may be broadly communicated to {{companys}} employees and when compromising this information will not cause any harm to {{company}}.

When information is classified for internal use, it must be distributed considering to protect the information from being unintentionally disclosed in the public domain.

### Public information

Information which is meant for public use without any constraints. Documents containing public information must not be labeled. All documents including public information must be approved by Corporate communications before being distributed outside the {{company}}.

### Labelling confidential information

Documents containing confidential information must contain the word “Confidential” on each page.

### Manage critical assets

Identify assets that are critical in providing service capability and take steps to maximize their reliability and availability to support business needs.
1. Define criticality levels and identify asset criticality in an asset register.
2. Enforce information security requirements on assets.

### Manage the asset life cycle

Manage assets from procurement to disposal to ensure that assets are utilised as effectively and efficiently as possible and are accounted for and physically protected.
1. Identify and communicate the risk for information security non-compliance related to the asset life cycle.
2. Ensure that information security measures and requirements are met throughout the life cycle

### Manage licences

Manage software licences so that the optimal number of licences is maintained to support business requirements and the number of licences owned is sufficient to cover the installed software in use.
1. Establish a procedure for control of software installations and other IT assets.
2. Perform regular network checks for unwanted software

### Identify and record current assets

Maintain an up-to-date and accurate record of all IT and TI assets required to deliver services and ensure alignment with configuration management and financial management.
1. Identify dependencies between assets.
2. Identify information security requirements for current assets and take into account the dependencies.
3. Address information security for IT assets, data and forms, etc.

### Information Security for Surveys

Surveys process in almost all cases, confidential information (personal data). These should therefore be set up carefully.

How to handle the information security aspects that are relevant to the implementation and execution of surveys? Context for surveys these days is an electronic way of presenting them (portals), but the essence of the requirements is not limited to this.

1. The information within a survey must be classified as confidential.

2. Because of the classification of the information, it must have a designated owner (in person).

3. Before any communication about the survey occurs, the survey must be reviewed with a {{companys}} Privacy Officer and the interviewer / pollster needs to obtain his/her approval.

4. The (electronic) communication about the survey must originate from within a {{companys}} domain. The authenticity and correctness of messages must be verifiable by recipients. This holds for all forms of communication. If messages are replyable, the replies must go to the originating {{companys}} domain.
    Articles, explanations etc. should be posted on the {{companys}} intranet; e-mail communication only from (and reply-able to) an {{company_email_adress}} mail address.

  Link targets in for example (but not limited to) e-mail messages or {{companys}} postings must be hosted within- or routed/redirected via {{companys}} domain. A direct link to an outside resource is not allowed. In general sense, e-mail communication about a survey must comply with the relevant requirements from the policy 'Securing e-mail' .

5. A call for participation cannot just “pop up” all of a sudden – the population must be informed about the survey at an earlier moment in time.
    This eliminates extra traffic to the helpdesk “is this a phishing mail” and similar questions.

6. The web portal that presents the survey must be protected against unauthorized access.
    There are multiple ways of achieving this:

    * Username + password + brute force lock out at the portal

    * Single sign on via grip (but be careful with surveys that claim anonymity).

    * A “random” string of characters in for example the URL within the personal invitation to participate. The string must be long, not enumerable and the portal must have a brute force lock out facility. 

      A URL example:
      randomsurveyexample.com/surveys/6be4c40b2d4db3b714bf9e932aeee196a4586c33fe57242ced9c01b5e251fd3f
      in which the part in red type is obtained by feeding a user-ID and a salt through an acceptable hash function (sha256 in this case). The resulting long URL must be distributed as-is (and not be fed through a URL-shortener).

7. With all involved external parties, a data processor agreement must be signed. In this agreement, a detailed limitative description of the transferred data objects as well as the purpose of data processing must be included.
    If, with a particular 3rd party, an existing data processor agreement is already in place it must be reviewed and possibly modified to obtain compliance with this document.
    Depending on the contract value with a 3rd party, the establishment of a Data processor agreement is taken care of via Corporate Procurement Office, or one can compile the basis of an agreement document by using the materials found in the Legal & Regulatory DIY portal. In both cases the final result before signing requires the approval of a {{companys}} Compliance Officer.

8. If desired the survey results must, after processing, be archived according to Storing confidential information.
    When the survey implementation and/or execution involves a 3rd party that processes {{companys}} data, it must be established and agreed upon that this party will destroy all PII and other (including raw) data after aggregation and reporting.

9. In the case {{company}} will develop and implement a web portal and will host this as well. This must be regarded as an Innovation and Development activity and should be treated according to Security measures in innovation and development.

10. In the case {{company}} contracts an external party to build and/or implement the survey. The resulting web portal (for example) can be hosted within or outside the {{companys}} domain.

    With each external party a Security Annex need to be established and agreed upon.

### Data minimization

Only strictly necessary information may be collected and only for the purposes for which they are processed.

During the development of new services and products must be considered what personal data are needed to provide the service or product to realize data minimization.

### Anonymization

All (in)directly identifiable information must be removed.

Personal data must be processed in such a way, that they are no longer usable to identify a natural person. This means that the processing should be irreversible.


### Virtual desktop restrictions

When connecting to a virtual desktop environment, direct file exchange between the local (in possession of the employee working from a remote location) and virtual environment is forbidden. This is applicable to local and removable media.

### {{companys}} Data Center

The confidentiality, integrity and availability security requirements for data used for the continuous delivery of Critical or Vital services, information on {{companys}} vulnerabilities and for data classified as Secret only allow it to be stored on an infrastructure that is exclusively used by  {{company}} , owned by  {{company}}  and installed on  {{companys}}  premise.
Compliance with internal policies ({{companys}}  security measures) is required.

### Perform an (information) security risk assessment

Prior to purchasing or using cloud services an (information) security risk assessment must be performed, which takes into account:
the type, classification and importance of information that may be handled in the cloud (e.g., commercial information, financial information, intellectual property (IP), legal, regulatory and privileged information (LRP), logistical information, management information or personally identifiable information (PII)).

## Media handling

### Cleaning of storage media

Storage media are cleaned to prevent information on recycled or discarded media to be restored and thus to be accessible to unauthorized persons.

### Destroying secret information

Secret information must be personally destroyed as soon as the information is no longer needed.

Digital secret information must be permanently deleted, not merely wiped or formatted. When digital secret information cannot be permanently deleted, the media containing the digital secret information must be physically destroyed according to a certified process.. Hardcopy secret information must be destroyed using a paper shredder. Secret documents must not be disposed in the supplied containers for confidential documents.

Desktop PC’s, laptops, mobile data carriers and other hardware containing secret information which is no longer required must be removed in consultation with the SSM for destroying.

### Printing confidential information

When printing confidential information on shared (multifunctional) printers the “Secure Printing” option must be used. Documents containing confidential information must not be left unattended on printers or in the printer area.

### Sending confidential information

Digital confidential information send to e-mail addresses outside of the {{company}}  must be encrypted before sending out.

The sender must inform the recipient that the information is confidential.

The sender must verify that the recipient’s address is correct.

Passwords must be communicated through a different communication channel (e.g. by phone or text message).

The user of the {{companys}} mailbox itself judges if information may be shared and/ or sent.

Hardcopy confidential information must be sent in closed envelopes.

Envelopes must not contain the word “Confidential”.

Before confidential information is sent to third parties, permission of the information owner must be obtained.

### Transporting company assets

1. Company assets* that are being transported out of the building by employees must be accompanied by a so-called pass document.
2. Security loges employees are allowed to check whether the pass document is present when company assets are transported out of the building.

**This is applicable for all company assets except for laptops and smartphones used for work by employees.*

### Disposal of SSDs, flash storage media (USB Sticks), tablet, telephone, or domotica

To dispose of data on a SSD or flash storage media the following methods are approved:

* Write a file the size of the disk volume to the disk.

* If the SSD support the Secure Erase feature then this can be used.

* Shredding of the storage medium.

* Using {{company}}-compliant encryption for full disk encryption and afterwards overwriting the encryption key with random data.

When a tablet, telephone, or (home) domotica is received indefinitely (not for repair cases), data must be wiped by first decoupling the device from the Apple iCloud, associated Google account or other cloud service. After this obligatory step, the device must be factory reset.

### Disposal of magnetic storage medium

To dispose of data on a magnetic storage medium, including tape, the following methods are approved:
- Zeroing all data from the first addressable byte until the last byte of the disk.
- Degaussing of the disk.
- Shredding of the storage medium.
- Using {{company}}-compliant encryption for full disk encryption and afterwards overwriting the encryption key with random data.

### Media cleaning

All media carrying information must be completely and irrecoverably cleaned or destroyed before re-use or disposal.

To prevent information on re-used or disposed media being recovered and becoming exposed to unauthorized parties. Depending on costs and dependability of a cleaning solution the choice for either cleaning or re-use can be made.

There is a large scale of potential information carrying media. They include but are not limited to:

- System media (hard drives, solid state disks, memory chips);
- Disposable media (memory sticks, CDs, DVDs, etc.);
- End user devices (phones, smartphones, tablets);

It might not be possible, or too expensive, to irretrievably remove information. In such cases we might opt for destruction of the media or device instead.

### Destruction of old equipment

Hard disks, external storage incl. USB sticks, or memory of old equipment must be wiped or destroyed by a certified party before disposal or resale.

### Disposal of magnetic disks assembled before 2001

Any hard disk assembled before 2001 must either be shredded or degaussed. Any other method is not allowed.