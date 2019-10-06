# Operations security

## Operational procedures and responsibilities

### Change registration

For each change the following must be registered:

- Time (actual time of execution / go-live)
- Details (what was changed)
- Approver

This requirement supports both traceability and accountability as well as providing a means to distinguish unauthorized (and potentially malicious) changes.

### Change management

For each change the security and BCM requirements must be taken into account and steps must be taken to ensure compliance.

While the innovation and development driven change process ensures compliance at the moment of hand-over to operations we must take extra steps to ensure that security and business continuity is not lowered by small operational changes.

### Capacity management

When the (B)IA classification is 'high' or 'critical', the average need of processing capacity must be guaranteed. Regardless faults or peak loads, the multi-year average processing capacity is always available in the busiest hour in a day. In this case, processing capacity relates to transport and service processing capacity as well as to storage, cpu power, cooling, etcetera.

### Specific overload

A platform should have sufficient capacity to maintain its functionality, even if there is overload (both in normal situations and in case of calamities). {{company}} should consider applying assets such as load balancers and load limiters.

### Specific provisioning

The provisioning process must always have sufficient capacity to comply to the demands of processing and delivery. It involves stockpiling before delivery and after delivery. The delivery process may not be disrupted due to a disruption in delivery and / or processing. Where processing capacity is dependent on delivery, then sufficient capacity must be provided.

### Specific limitations

The capacity limit of all elements is known, as well as the influence that the capacity of an element has on the capacity of another element.  Following can be considered as capacity limit: licenses, working memory, processor capacity, etcetera.

### Specific utility

Utility processes have sufficient capacity. The technical infrastructure (TI) may not exceed the capacity of the utility processes. Utility processes are power supplies, air conditioning, floor capacity and building space.

### Specific continuous delivery

The capacity of continuous delivery is not disturbed by providing provisioning and assurance data.

### Adequate IT capacity

IT infrastructure with a (B)IA classification 'high', 'critical', or 'medium', of which the RTO is shorter than a week, must always be performed at two different physical locations, each providing 100% of the required capacity (total of 200%). The infrastructure design for both locations is similar. In practice, a week (7 days of 24 hours = 168 hours) is required for replacing hardware. Because this recovery time is too long for IT infrastructure with the above-mentioned classifications, {{company}} should ensure a second physical location with the required capacity.

## Protection from malware

### Malware protection

An up-to-date and supplier supported protection against malware must be set up on the elements on the system where possible. Malware may create a backdoor for unauthorized access on a system.

### Scan of external files

All data, software, email and other files being downloaded from external sources (including removable media) must be checked automatically with authorized anti-virus software for malicious software and email filtering, even in the case of an authorized source.

### Centralized protection solution

The malware protection measures used by device management parties must be centralized, automated and working without intervention (user-transparent). 

Deactivation or bypassing of the protection against malicious software by the user must be prohibited:

• Ability to disable the antivirus services
• Ability to disable or cancel a scheduled scan
• Ability to disable real time scanning
• Ability to modify scan policies

Attempts must be logged and sent to a central logging entity

### Access protection

The anti-malware solution must, at a minimum, have anti-tamper mechanisms, status/health checks, memory and buffer overflow protection in place. If a health check fails or if deactivation or bypass of these mechanisms is detected this must result in an alarm being logged and sent to the responsible department and {{company}} SOC.

### Automated tools

Automated tools must be deployed to monitor workstations, severs, and mobile devices. This tool must, at a minimum, support signature based, behavioural, heuristic, and script based checks for both file and network traffic.

### Software maintenance

Only software versions supported by the supplier must be used.

Software not supported by the supplier can lead to a continuity problem when changes or updates that are needed on the system are no longer compatible. So security vulnerabilities will not be fixed.

Common off the shelve (COTS) software is often sold with maintenance guarantees. For Freeware or other sofware not managed by a supplier an exception must be approved.

### Updates of anti-malware engine

Besides the daily signature updates, also the anti virus software should be kept up-to-date. If the anti-virus software is updated manually, the vendor’s website should be checked periodically for new updates. After applying an update, automated systems should verify that each system has processed its update.

### Signature updates

Signature auto-update features must be deployed. Checks for updates must be done on a daily basis. After applying an update, automated systems must verify that each system has processed its signature update.

### Anti Virus Software version and library updates

Anti-Virus software libraries- and version updates must immediately be updated after their release by software vendors.

### Full scan

Periodically all files on all workstations and servers must be scanned for malware. For performance reasons, this may be an iterative scan. Scan cycles must be run as frequent as possible.

The interval between two cycles must not be greater than 1 month. For fileshares, dropzones, FTP servers or managed file transfer services the files must be scanned (within the scope of the dropzone) with a scan on-access policy.

### Event management

All malware detection events must be sent to enterprise anti-malware administration tool and event log servers. The alerts must be automatically dispatched to the responsible department and {{company}} SOC.

### Certification for Endpoint Protection

The EPP solution supplier must have passed at least three (3) out of four (4) most recent 'MRG-Effitas 360 degree assessment and certification tests' with a level two (2) certification. Possible exception: upon request, an as-of-yet unspecified solution, can be allowed if it passes two (2) consecutive “MRGEffitas 360 degree assessment and certification tests” with a level two (2) certification. For consistency, the period between those two tests, must be at least three months. Test conditions and final approval must be obtained from {{company}} CISO before go-live.

The MRG-Effitas tests provide an accurate and independent measurement guideline to follow when choosing a supplier for endpoint protection. For reasons of consistency, multiple consecutive test results are taken into account. More information can be found at [MRG-Effitas.com](https://www.mrg-effitas.com/).

### Protection of Mobile Computers and Teleworking Systems

The malware protection software must be automatically updated (with new configuration settings, new libraries and new versions of the software) when these devices are connected to the corporate network directly or remotely.

Mobile computers and teleworking systems that have not connected and been updated for 3 months or longer must first be updated and scanned before a new connection is allowed.

Updates can be limited to maintenance windows or be stopped during calm periods.

### Sharing information

Malware detection must be possible without sharing {{company}}-related data outside of the company. Insignificant data such as Hashes or PE-Files are excluded of this rule but sharing is not preferred.

## Backup

### Maximum accepted data loss (back up and restore)

All systems that contain data, have established the Maximum Accepted Data Loss (MAD).

### Backup and restore

All data necessary  to get the service and / or the continuous delivery operational again in the event of an incident, are in accordance with the agreed RTO and RPO.

There are sufficient recent copies (back-ups) of data and configurations for timely restoration of the service or the process as a whole within its recovery norm (RTO).

Back-ups are (also) saved off-site. In case of an incident in one location the data can be restored with the back up that is saved in another location.

The condition of the back-up location is equal to the production location to prevent degradation in quality of the data

### System Data backup

Back-ups of system and application data must be made periodically and backups must be stored at a different location in accordance with continuity and integrity requirements of the system and application owner. Restore must be tested periodically. Personal data may not be stored longer than its original system or application and in conformity to retention periods.

Data may be lost or corrupted by an hardware failure.

### Database Backup security

The backup of data must be secure with the same or stricter security means as the production environment.

## Logging and monitoring

### Centralized logging

All logs must be forwarded to the central logmanagement platform of {{company}}. Within five minutes after the occurrence of the event log data must reside on the central logmanagement platform.

{{company}} collects the logs of security events in {{companys}} networks and systems in a dedicated central log management platform. Guideline {{company_logging_guidelines}} refers to detailed instruction on setting up a log aggregator, an initial log collector (ILC) and realizing connectivity to the central platform.

### Acting upon log events

Log data must be analyzed structurally, at least daily. If suspicious events are detected from log file analysis, this should be treated as a security incident.

### Retention period central logs

The period for storing centralized logs must be set to 180 days. Unless the type of logs does not allow it. In this case, the owner determines the retention time.

When the log data is needed after 180 days, the logs must be aggregated in such way that they can no longer be traced back to individuals.

### Logging of security events

Networks and systems need to log security events. {{responsible_cert}} may require additional logging due to security incident response and / or investigations.

We distinguish the following types of log sources: application, daemon, OS, network element and hardware. Guideline {{company_logging_guidelines}} refers to detailed instruction regarding the type of security events that should be logged.

### Database auditing

Access to the data stored in a database must be auditable via sufficient logging.

### Connect to Log Monitoring

Networks, systems and applications must be connected to Log Monitoring of the {{companys}} SOC.

### Connect to Intrusion Detection Monitoring

Networks, systems and applications must be connected to Intrusion Detection Monitoring of the {{companys}} SOC.

### Connect to Vulnerability Monitoring

Networks, systems and applications must be connected to Vulnerability Monitoring of the {{companys}} SOC.

### Connect to Anti-DDOS Monitoring

Directly accessible networks, systems and applications must be connected to Anti-DDOS Monitoring of the {{companys}} SOC.

## Control of operational software

### Vulnerability scanning

All {{company}} assets connected to a network, must be scanned for vulnerabilities on a minimum monthly basis. All interfaces, including the logical and external interfaces, must be scanned. The asset owner of the system on which the vulnerabilities have been found must take measures in response to the findings.

Customers' assets that are part of the {{company}} network are not in scope for vulnerability scanning.
Vulnerability management on {{company}} assets with an interface in a black zone, not being Internet or {{allowed_networks}}, may deviate from this rule if other, by CISO approved ways, regular management of vulnerabilities are met.

### Centrally managed vulnerability scanning

Vulnerability scanning must be managed centrally and managed for the entire {{company}} organization.

## Technical vulnerability management

### Vulnerability management

A vulnerability management process must be implemented and followed.

Every system is to be scanned for vulnerabilities on a regular basis. The resulting findings need to be resolved within a pre-defined timeframe depending on the severity.

Vulnerabilities can arise over time and must be solved timely to keep the system sufficient safe for attacks. *i.e. Schedule of vulnerability tests for systems* 

Isolated systems (without network link and no mobile storage applicable) have no need for vulnerability management.

### Vulnerability mitigation

Identified vulnerabilities (whether found based on the monthly vulnerability scanning, or found though other means) must be fixed according to the following timelines:

| Category | CVSS v2 Base score | Remediation time in case internet facing | Remediation time in case not internet facing |
| -------- | ------------------ | ---------------------------------------- | -------------------------------------------- |
| Low      | 00-3,9             | Best effort                              | Best effort                                  |
| Medium   | 4,0-6,9            | 1 month                                  | 2 months                                     |
| High     | 7,0-10             | 2 weeks                                  | 1 month                                      |

If a vulnerability cannot be fixed, mitigating measures must be implemented according to the timeframe.

Portal authority findings of CVSS 4.0 or higher need to be solved before go Live. (Portal authority base scores on CVSS v3)

**Common Vulnerability Scoring System (CVSS) Score. Several vendors have their own definition of Low/Medium/High. To not be tied to a specific product or vendor, the categories are based on CVSS v2 Base scores. CVSS v3 in development.* 

### Mitigation of non-hardened residual risk

When certain aspects of a system can’t be hardened, the requirements in the related documents must be consulted to see how to handle mitigation, if possible based on the CVSS score of a non-hardened topic.

### System hardening

Systems must be subjected to a hardening process to conform to the requirements mentioned in this chapter as well as in *Access Control*, *Communications security* and *System acquisition, development and maintenance* chapters to minimize the risk of an attack.

Not necessary features must be closed and protection mechanisms must be used to make the attack surface as little as possible.
Close unnecessary features and ports of operating systems.

### End user device hardening

End user devices must be hardened with respect to user privileges, patching and updates, necessary functionality adequate firewall and up-to-date antivirus/ malware controls.

### Updates

Security updates must be installed per the timelines set in Vulnerability mitigation on all {{company}} assets. This must be verified regularly. Deviations must be resolved as quickly as possible.

## Information systems audit considerations


