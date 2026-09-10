# Secure Diagnostic Laboratory Network

A Cisco Packet Tracer-based network security project designed to secure diagnostic data transmission between a medical laboratory and its partner clinics.

## Project Overview

This project focused on designing and simulating a secure network for AVM Labs, a diagnostic laboratory in Muscat, Oman.

The project addressed the secure transmission of diagnostic and patient-related reports between the laboratory and its associated clinic branches. The proposed network used segmentation, access control, secure management protocols, authentication, and traffic monitoring to improve the security of the environment.

> **Academic Project:** This was completed as a group diploma project. The sections describing individual contributions refer specifically to my work within the team.

## Objectives

The main objectives of the project were to:

- Design a secure and structured network architecture
- Segment network traffic using VLANs
- Restrict unauthorized communication using ACLs
- Secure network-device administration using SSH
- Implement firewall policies
- Provide secure wireless authentication
- Secure web-based diagnostic report transmission
- Monitor and validate network traffic
- Automate basic network connectivity monitoring

## Technologies & Tools

- Cisco Packet Tracer
- VLANs
- Extended ACLs
- Firewall rules
- SSH
- WPA2-Enterprise
- Active Directory Domain Services
- HTTPS / TLS
- Wireshark
- Python
- Network routing and NAT

## Network Security Implementation

### VLAN Segmentation

The network was divided into separate VLANs to isolate different types of traffic and reduce unnecessary communication between network segments.

The simulated environment included dedicated segments for:

- Laboratory systems
- Diagnostic/server systems
- Wireless users
- Network management
- Active Directory services

### Access Control Lists

Extended ACLs were configured to control traffic between network segments and restrict access to sensitive resources.

Access rules were designed to ensure that only authorized clinic and internal network traffic could reach protected diagnostic services.

### Secure Device Management

SSH was configured for secure remote administration of network devices, replacing insecure Telnet-based management.

### Firewall Policies

Firewall rules were implemented at the network perimeter to control inbound and outbound traffic and restrict unauthorized access.

### Wireless Security

WPA2-Enterprise authentication was configured for the wireless environment using centralized authentication services.

### Secure Web Communication

HTTPS/TLS was used to protect diagnostic report transmission and prevent sensitive information from being transmitted in plaintext.

### Network Monitoring

Wireshark was used to inspect and validate network traffic during testing.

A Python-based connectivity monitoring script was also developed to detect when a network node became unreachable.

## My Contribution

**Role: Network Implementer & Simulation Lead**

My primary responsibilities within the group included:

- Designing the network topology with a team member
- Implementing VLAN segmentation
- Configuring extended ACLs
- Configuring firewall rules
- Configuring SSH access
- Assisting with server and network configuration
- Working on security configuration and validation
- Developing a Python connectivity monitoring script
- Troubleshooting network and security configuration issues
- Contributing to project documentation and report preparation

### Security-Focused Work

My main technical focus was on implementing and validating the network security controls.

This included isolating network segments using VLANs, restricting traffic using ACLs, securing device administration through SSH, and testing whether unauthorized communication was properly blocked.

I also developed a Python script from scratch to generate an alert when a monitored clinic node became unreachable.

## Testing & Validation

The simulated network was tested against multiple security and connectivity scenarios.

The project report documented **18 security and functionality test cases**, with all test cases passing.

Testing included:

- VLAN connectivity and isolation
- Inter-VLAN communication
- ACL enforcement
- Unauthorized access prevention
- SSH access control
- Telnet restriction
- Wireless authentication
- Active Directory authentication
- HTTPS/TLS communication
- Firewall traffic filtering
- Python connectivity monitoring
- Broadcast-domain isolation

## Challenges & Lessons Learned

One of the main challenges was configuring ACLs correctly. An initial ACL configuration unintentionally blocked legitimate clinic traffic.

This helped me understand the importance of:

- Wildcard masks
- ACL rule ordering
- Traffic direction
- Testing security rules before deployment

I also encountered trunk configuration and other network connectivity issues during the simulation. Packet Tracer's simulation and troubleshooting tools were used to identify and resolve these problems.

The project strengthened my understanding of practical network security concepts, particularly VLAN segmentation, ACLs, secure network administration, and basic network automation.

## Limitations

This project was implemented and tested in Cisco Packet Tracer, so it represents a simulated network rather than a production deployment.

Some production-level capabilities were outside the scope of the project, including:

- Production-grade VPN infrastructure
- Network redundancy
- Advanced intrusion detection
- Large-scale monitoring
- Dynamic routing optimization

## Future Improvements

Possible improvements to the network include:

- Implementing OSPF
- Establishing VPN tunnels between sites
- Adding advanced network monitoring
- Implementing wireless intrusion detection
- Improving redundancy and fault tolerance
- Expanding automated security monitoring

## Project Files

The repository contains selected project materials, including the Cisco Packet Tracer simulation, network diagrams, screenshots, Python automation, and supporting documentation.

## Disclaimer

This repository contains materials from an academic networking and cybersecurity project. It is intended for educational and portfolio purposes.

The original academic project was completed as a group project, and this repository highlights my individual technical contributions.
