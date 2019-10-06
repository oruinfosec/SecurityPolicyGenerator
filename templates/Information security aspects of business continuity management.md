# Information security aspects of business continuity management

## Information security continuity

### Impact on continuity

In the creation, adaptation or elimination of a case (such as a process, product, service, application, semi-finished product, infrastructure, building, etcetera) it must be determined whether continuity plans must be written or adjusted.
Before the creation, adaptation or elimination is taken into production or transferred to management, it must be demonstrated by a test of the continuity plan that the related continuity standards are being met.

All {{companys}} business activities are directly or indirectly connected to each other. That is why it is important that every change is prepared and tested in such a way that it demonstrably has no adverse effect on the continuity of related matters.

### Data: complete and correct

Data required for the continuous provision of services and the management of calamities are up-to-date, correct and accurate.

### Data availability

Data is available and accessible at the right time, in the right location and for the right people when necessary for answering continuity questions (including incident management).

### IT infrastructure and data availability

The availability of the IT infrastructure is always in accordance with the stated RTO and RPO.
The availability of IT data (production data) is in accordance with RTO and RPO.
IT infrastructure and IT data can be restored within the RTO.

### Presence of an exit strategy on cloud services

A data and service exit strategy must be in place before operating with a Cloud Service Provider (CSP).

### Avoidance of (temporary) cloud service destruction

Financial control must be in place to avoid the (temporary) destruction of a cloud service, due to not paying in time. Reinstating the service as-is must not be assumed.

### Determine scope

For each Service, Service Component or Application must the scope (for which the risks must be evaluated) be determined in accordance with {{document_scoping_bcm}} ‘Scope Document’. The results must be delivered to CISO.

### Determine BCM planning and process

A BCM process and planning is necessary to identify continuity risks and measures to be taken. In order to achieve a similar impact classification and risk assessment, a uniform process is used within {{company}}.

| RASCI MATRIX |                                                              | Top management | CISO | Risk Management | Product Owner | Product Manager | Asset Owners(buildings and applications) | Employees |
| :----------: | ------------------------------------------------------------ | -------------- | ---- | --------------- | ------------- | --------------- | ---------------------------------------- | --------- |
|      P1      | BCM policy requirements in KSP                               | A              | R    | C               | I             | I               | I                                        | I         |
|      P2      | BCM process development                                      | A              | R    | C               | I             | I               | I                                        | I         |
|      P3      | Define information security objectives and KPIs              | A              | R    |                 |               |                 |                                          |           |
|      P4      | Business Continuity awareness and communication              | A              | R    | R               | R             | R               | R                                        | I         |
|      D1      | Determine Risk Appetite Business Continuity                  | A              | R    | I               |               |                 |                                          |           |
|      D2      | Determine Risk Analysis and define Risk Treatment Plan (including quarterly RTP update) |                | S/I  | C               | A             | R               | A/R                                      |           |
|      D3      | Create, maintain and test Continuity Plans (including evaluation report) |                | S/I  | C               | A             | R               | A/R                                      |           |
|      D4      | Create, maintain and test Continuity Plans(including evaluation report) |                | S/I  | C               | A             | R               | A/R                                      |           |
|      C1      | Verify BCM process compliance / status                       | I              | A/R  |                 | I             | I               | I                                        |           |
|      C2      | Quality Assurance for analyses of {{company}} critical components and Random Quality Check for non-critical components and Test Reports | I              | A/R  |                 | I             | I               | I                                        |           |
|      C3      | ISO Audit BCM Analyses and Continuity Plans (only for ISO Certification) | A              |      | R               |               |                 |                                          |           |
|      C5      | Revision of lists of {{country}} vital services, {{company}} critical services, critical service components, critical buildings and critical applications | A              | R    | I               | I             | I               | I                                        |           |
|      A1      | Implement recommendations of Quality Assurance and Random Quality Check |                | S/I  | C               | A             | R               | A/R                                      |           |
|      A2      | Risk mitigation                                              | A/R*           | I    |                 | R*            | R*              | R*                                       |           |

**Depending on the risk (Procuration Matrix)*

P=Plan
D=Do
C=Check
A=Act

A=Accountable
R=Responsible
C=Consulted
S=Support
I=Informed

| Role            | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| Top Management  | Board of Directors. Mostly done via OLT for the COO organization and the CCLT for the CCO organization |
| CISO            | Chief Information Security Officer. Delegated to employees of the Chief Information Security Office |
| Risk Management | Coordinator for ISO Certifications. To support that the {{company}} Security Policy does not conflict with the ISO requirements. To perform audits. |
| Product Owner   | The Product Owner owns the service or service component and does the review of the BCM components. |
| Product Manager | The Product Manager manages the service or service component and defines and maintains the BCM components. |
| Asset Owner     | The Asset Owner owns and manages the building or application and defines and maintains the BCM components |
| Employees       | All persons employed by the {{company}}                      |

### Exercise Business Continuity Plans

All continuity plans (SCPs/BCPs/CRPs/TRPs) and all technical solutions that are created to mitigate continuity risks must be exercised at least once a year or when major changes in the service, service component, application or building occur.

Exercises must be prepared and evaluated in an exercise report. Recommendations must be decided on succession and implemented within the timeline as stated in the report.

### Business Continuity Management Governance

Responsibilities for Business Continuity Management must be defined.

Without a clear understanding of roles and responsibilities it will be practically impossible to implement regulatory, customer and {{companys}} business requirements for business continuity in a consistent manner.

### BCM Planning

On a yearly basis, a BCM plan on segment and department level (each unit delivering a monthly Management Letter) must be drafted.

Insight must be provided into the following activities:
• Yearly cycle of the BCM Process;
• Yearly review of existing BCM documentation;
• By {{companys}} management approved Risk appetite;
• By {{companys}} management approved budget and required staff needed for the realization of th BCM plan;
• Timelines;
• Commitment from stakeholders of the delivered services outside the unit.

### BCM Process

A Business Continuity Management process must be implemented for services, service components, buildings and applications that will identify continuity risks and determine, implement and check, the mitigating measures where regulations require action or continuity risks exceed risk appetite.

To have insight in the BCM risks of services, service components, buildings and applications. This enables the organization to realize a comprehensive framework of mitigating measures to prevent situations that threaten the continuity of the organization and minimize the resulting harm as much as possible in the case that a calamity happens

### Business Continuity Framework reporting

On a quarterly basis the Business Continuity status of continuous delivery for all approved critical services, service components and critical applications must be reported by the service owner or application owner to {{companys}} CISO. All reporting units must use the same Business Continuity Framework.

To compile an corporate BCM status overview for {{company}}, and in order to report both internally and externally in a consistent manner, it is mandatory that all reporting units (that deliver a monthly Management Letter) use the same methodology and reporting methods, as prescribed by the CISO. The framework will encompass as well regulatory and {{companys}} requirements.

The BCM status of continuous delivery for all approved critical services, critical service components and critical applications must be reported quarterly to CISO, including BCM BIA or IA ((Business) Impact Analysis) status, BCM RT (Risk Tool) status, status of the risk mitigating measures and the Continuity Plan test execution and results status.

### Evaluation of and defining requirements to Critical Services (pitat Tonia)

On a yearly basis, the business critical services must be defined and evaluated. To accomplish this the {{companys}} impact classification of all services must be defined by means of the BCM Business Impact Assessment (BCM BIA) and reported to CISO. CISO uses this information to complete the proposal Critical Services overview in Q4 which must be approved by executive management in OLT and CCLT.

The selection criteria for {{companys}} Critical Services are based on the impact that a severe disruption of service may cause (as mentioned in the BCM BIA):

• Financial impact: loss of sales ≥ €6M and/or cost of recovery ≥ €6M;

• Reputation damage: great loss of (potential) customers;

• Major social disruption (1-1-2 unreachability always highest impact).

The requirements regarding to the maximum impact a failure may have on the service are the following:

• Max. 100.000 affected connections* caused by the failure;

• ≤ 4 hours outage for more than 10.000 affected connections*;*

• Regional impact (max 100.000 connections*) for fixed and mobile services;

• Max. 1 regional incident per year (no repeating failures for the same customers).

*connections: for business customers the number of total connections affected are counted
Contractual agreement scan overrule above requirements.

For critical services, each three years a table-top chain exercise must be held to check the correct and timely interoperability of continuity plans and crisis management in all involved parts of the organization. A real incident invoking these plans and crisis management process may also fulfil this requirement when the underlying evidence and evaluation report are adequate. This is judged by the CISO.

Applying focus to the services with major impact because of financial, reputational or social importance.

### Business Impact Analysis (BIA)

Yearly, or in case of newly developed (innovation) or significantly changed functionality, must be determined what the impact of prolonged unavailability is due to a worst case scenario of a Service, Service Component, Application or a Building from a customer, society as well as {{companys}} point of view.

The classification of a Service must be done with BIA, the classification of a Service Component, an Application or a Building using {{bcm_ia_guideline}}. 

The tools must be filled in by the responsible Product Manager of the Service or Service Component or the owner of the Application or Building, and be approved by the responsible manager. Hereafter the completed tool must be send to CISO.

### Risk Assessment

For Services, Service Components and Applications, High or Critical (Medium if Telecom Law relevant), and for critical or high classified Buildings according to BIA/IA output, yearly a Risk Assessment must be performed to have an actual overview of risks, identified Single Points of Failure (SPoFs) and environmental risks.

As inventory of BCM risks is the use of the threats in {{bcm_threats_list}} - BCM Threats list for Risk Assessment mandatory.

The identified risks must be evaluated by the responsible Asset owner or Manager to define whether the risks have to be mitigated by taking measures or by accepting risks according to the Procuration Matrix (Shared Service Organisation).

### Invoke continuity plans

Continuity plans must be invoked in case of events/incidents impacting the availability of {{companys}} services.

Continuity Plans are created, maintained and exercised yearly to make sure that the organization is prepared when a major incident occurs. When serious incidents occur, the prepared continuity plans, if available, must be used to mitigate the impact. 

Documents such as: Business Continuity Plan (BCP), Service Continuity Plan (SCP), IT Chain Recovery Plan (CRP), Technical Recovery Plan (TRP) should be delivered to CISO.

### BCM Risk Acceptance

Risks may only be accepted by the responsible manager who, according to the procuration matrix, is allowed to sign for the amount of money of the worst case impact of the risk, together with an mandatory argumentation for the reason of accepting the risk.

### Corporate Crisis Management

For crisis situations threatening the company as a whole, or as directed by the government, the executive management must be able to manage these situations, and must be trained yearly.

Severe crisis may be of great danger for the continuity of {{company}} as a whole. Besides that {{company}} must, because of law and regulation, be prepared for crisis situations issued and directed by government.

### BCM Risk Mitigation

Identified risks to be mitigated must be supplied with mitigating measures.

The implementation of mitigating measures must be justified by the responsible Manager based on a business case.

The implementation status of the mitigating measures must be actual and available.

Mitigation measures must be approved by the responsible Manager to the level according to the Procuration Matrix.

### Business Continuity Plans

Continuity plans must be created and stored in a central repository, and must at all times be accessible even if {{companys}} internal (office) infrastructure is malfunctioning.

Continuity plans must be reviewed, exercised and tested at least annually or after a major change and updated if needed. Exercise and test planning and results must be reported to CISO.

The title (not the plan itself) and exercise and test dates and results of Continuity plans of MSPs must be delivered to CISO.

### Business Continuity Requirement Management

Yearly, or in case of newly developed or significantly changed functionality, the services, service components and applications and their continuity requirements must be reviewed or determined by the service, service component or application owner. Business Continuity requirements must reflect customer, contractual, regulatory, internal quality requirements and social demands.

The requirements for (critical) services, service components and applications regarding availability and maximum impact of severe incidents must be set by {{companys}} executive management. These requirements can be: maximum impacted customers from one failure, maximum unavailability, maximum dataloss, regional or nationwide impact.

### Testing system and application

The continuity requirements of systems and applications (for both IT and TI) must be demonstrably tested at least annually.

 Systems and applications are demonstrably tested to ensure that they have the required capacity and performance to meet the defined continuity requirements.

### Robustness tests

In case of TI equipment implementations, immediately demonstrable robustness tests are performed with regard to all continuity measures.

### Continuity Incident Reporting

Major incidents  with severe continuity impact (Code Orange or Code Red) must be reported to authority.

### Responsible employee

{{companys}} CISO is responsible to manage that BCM policies are defined and that reporting units are working up to, and reporting the level of compliancy to these policies.

### Continuity Plan

{{company}} must create and maintain a Continuity Plan.

{{company}} should take appropriate technical and organizational measures to appropriately manage the risks to the safety and integrity of their networks and services.

## Redundancies

### Cables and trenches separation in the Core and Backhaul infrastructure

There are always at least two trench separated cable routes between two network locations. The service should not malfunction by one calamity in the Core and/or Backhaul network in which one or more cables are involved.

### Cables and trenches separation in the Core and Backhaul infrastructure (specific)
The cable network is constructed in such a way that Core and Backhaul connections can be routed via redundant cable routes.

Core sites are routed through two physically separate distributors.

Infrastructure for core infrastructural connections is build redundantly.

The number of manipulation points (distributors) should be restricted to a minimum.

Core cables are not used for welding backhaul and access connections.

### Redundant within the set RTO
Service platforms, network platforms and transportation networks and administration infrastructure should be redundant to the level dat they comply within the shortest set RTO.

### Geographic redundancy

Technical buildings with the highest security rating and data centers with platforms of which the RTO is less than 168 hours (one calendar week), account must be taken of geographical redundancy and redundancy in utilities (power supply, air conditioning and internal cabling).

The distance between two georedundant locations is about 50 km in relation to regional infrastructures such as electricity, water and regional effects of, for example, an earthquake and storm.

### Redundancy related to a building

Critical services, critical service components and critical applications need to be resilient for the failure of a building and should be able to operate within the defined BCM norms (e.g. RTO, RPO).

A service, service component or application can be defined as critical based on the BIA / IA outcome. Hardware elements of such service, service component and / or application are located in a building. Failure of that building may not lead to exceeding the defined BCM norms of the critical service, service component or application.

### Redundancy of a building related to the climate

Mitigating measures must be taken against failure of a building to floodings.

When new buildings are used, it must be checked what the water level above ground level is (can be checked at the local communal office) and measure must be according to this water level. This is also because of effects of climate change (e.g. heavy rain).

### Redundancy testing of building amenities

The redundancy of building amenities should be tested before use and when in use, tested annually.
- When a hot standby is used, the technique should be tested annually.
- When a warm/cold standby is used, the technique and the business processes should be tested annually.

### Redundancy of cables and trenches
Applied redundancy must also be guaranteed in underlying layers of the infrastructure.


Cable infrastructure that has been laid out redundant must be laid in separate cable channels and separate cable ducts within a building

### Redundancy management

Redundancy management must be set up in such a way that, in case of a site failure, management is still possible and able to carry out mitigation actions.

### Diverting to another location

The processes for diverting to another loation and the return to normal after a diversion, should be determined in procedures.

The diversion to another location must be restored as soon as possible to recover redundancy.


### Network availability
The design of a network must ensure the required level of availability. Due to the function of a network component (handling traffic), different data streams for different services are transported. The highest availability requirement of the data streams prescribes the measures that must be taken for a network infrastructure.

If a service must be “always on”, robust components must be used and deviceor location redundancy must be implemented.

The service description of the network enables the end user to be aware of possible continuity interruptions and the duration and extent of this. It is up to the end user to take suitable measures.