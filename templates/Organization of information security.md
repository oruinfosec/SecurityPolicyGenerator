# Organization of information security

## Internal organization

### Reference to responsible disclosure page

A reference to the responsible disclosure page on [company webpage]({{link_to_the_company_webpage}}) must be included. This reference should be no more than one click away from the main page.

English:
[Disclosure page]({{link_to_the_resonsible_disclosure_page}})

## Mobile devices and teleworking

### Mobile Device Management (MDM) software

Centrally provided Mobile Device Management (MDM) software must be installed, that provides remote:

* lock-out of the device.
* monitoring of device (BYOD) activity (in the event evidence is required for forensic analysis).
* deletion (often referred to as ‘remote wipe’) by securely destroying all {{company}} information stored on the device (BYOD) and any attached storage.

### Device (BYOD) lock-out

Device (BYOD) lock-out must be forced following multiple failed authentication attempts (after 10 incorrect passwords/PIN codes in succession).

No connection to corporate infrastructure is possible anymore until it is determined that the device (BYOD) still is in possession of the registered owner.

### Device (BYOD) change or employment termination

When an employee with a device registered for use in the BYOD program changes to a new device or leaves the company:
a) access to the corporate infrastructures must be revoked for the registered device(s) owned by the employee;
b) the {{company}} data on the registered device must be wiped within 48 hours by using the de-registration script by the owner. The employee sends a confirmation email of this action to the {{company}} Security Helpdesk.

### Use of wireless keyboards

All forms of wireless use of a keyboard is not allowed.

An exception is possible when the Bluetooth Passkey Entry is used to authenticate the keyboard with the host using a random PIN per pairing sequence. The exception is void when used for vital infrastructure maintenance.