# Evaluation

Evaluator's notes from the quiz on 2026-11-18. They're for the next session, so it can know how much the learner knows and guide the next questions and problems. The quiz was one question at a time.

## Concepts to look up

### Subnet mask

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), IP Addressing Concepts and Issues: "IP Basic Address Structure and Main Components: Network ID and Host ID", then "IP Addressing Categories (Classful, Subnetted and Classless) and IP Address Adjuncts (Subnet Mask and Default Gateway)"
* **Why:** the learner said the mask "doesn't matter for now". Then Packet Tracer refused to ping 192.168.2.20 from 192.168.1.10 because it was "not in the same subnet". The mask is what decides that.

### Ethernet covers two layers

* **Read:** Wikipedia, "Ethernet over twisted pair", the sections on cabling and on Auto-MDIX.
* **Why:** the learner thinks the cable is a separate standard from Ethernet. The article shows that the Ethernet standard also defines how bits travel over the cable. It also explains cross-over cables and why real computers rarely need them now.

### Wi-Fi frames

* **Read:** Wikipedia, "802.11 frame types", the section on the frame format.
* **Why:** the learner said Wi-Fi uses the same Ethernet II frame. It doesn't. Comparing the two frame layouts shows what they share (MAC addresses) and what's different.

### TCP/IP layers and OSI layers

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), TCP/IP Protocol Suite and Architecture: "TCP/IP Architecture and the TCP/IP Model"
* **Why:** the learner asked whether Ethernet II is part of the TCP/IP stack. This section shows where TCP/IP's own protocols stop and where Ethernet takes over.

## What the learner got wrong

* **"The cable is a separate standard from Ethernet."** Partly wrong. The cable itself (its category and how its connectors are wired) comes from a separate cabling standard, TIA/EIA-568. But the Ethernet standard, IEEE 802.3, defines how bits are sent over that cable (for example 100BASE-TX). So Ethernet is not only a layer 2 protocol. It covers layer 1 and layer 2.
* **"Wi-Fi uses the same DIX or Ethernet II standard."** Wrong. Wi-Fi is IEEE 802.11 and has its own frame format, with up to four addresses. Both use the same kind of 48-bit MAC address, and a Wi-Fi access point translates frames to Ethernet II when it passes them to a cable.
* **"The subnet mask doesn't matter for now."** Wrong. The mask decides whether the other computer is in the same network. If it is, the computer sends directly and uses ARP. If it isn't, the computer sends the packet to its default gateway. With no gateway, the packet is dropped. That's exactly the error Packet Tracer showed.
* **"Ethernet is a standard to send packets."** A small terminology slip. At layer 2, the unit is a frame. The IP packet travels inside the Ethernet frame.

## Too far from reality

* **Cross-over cables.** In Packet Tracer, two `PC-PT` computers need a cross-over cable. Most real network cards made in the last 15 years have Auto-MDIX: they detect the cable and swap send and receive themselves. In Rosa's real apartment, a straight-through cable would almost certainly work too. The solution's reasoning ("same type of device, so cross-over") is right for Packet Tracer and for old hardware.

## Understood

* **The cable has to fit the devices in Packet Tracer.** The learner saw that a straight-through cable between two PCs leaves the port down, and knew that the cross-over cable is the one for connecting two PCs.
* **Ethernet II is a layer 2 frame format with MAC addresses.** After reading about it, the learner described it in their own words.
* **The cable is at layer 1.**
* **ARP, the ARP cache and NDP.** The solution explains why ARP appears before the first ping and not before the second, and that IPv6 uses Neighbor Discovery instead. These weren't quizzed.

## Partly understood

* **Where Ethernet sits.** The learner knows the layer 2 part, but not that Ethernet also defines layer 1. They also asked whether Ethernet II belongs to the TCP/IP stack, so the line between TCP/IP's protocols and the technology below them isn't clear yet.
* **IP addresses.** The learner gave both computers addresses that work, but didn't say why they chose those values.

## Not covered yet

* What the subnet mask decides, and what "same subnet" means.
* The default gateway. The learner said they don't know what it is. It only matters once there's a router, so it should come after subnet masks.
* Cable wiring details. The learner doesn't want them, so leave them out.
* ARP and NDP in the quiz. They're in the solution but weren't asked about.

## Next steps

We need to cover these things in the next exercises, in this order:

### 1. Subnet masks

* **Topics:**
  * Subnet mask
  * Network part and host part of an IP address
  * Same subnet or not
* **Builds on:** the learner already gives two computers IP addresses and pings between them, and has seen the "not in the same subnet" error.
* **Situation:** two computers on one cable, and one of them has an address that someone else set up in a different network. The ping fails, and the client won't let the learner change that computer's address. The learner has to find out what makes the two addresses "the same network" and fix it from the other side.

### 2. Default gateway

* **Topics:**
  * Default gateway
  * Router
  * Sending to another network
* **Builds on:** subnet masks from exercise 1. The learner will know when the other computer is in a different network.
* **Situation:** two small networks that need to reach each other, with a router between them.

### 3. Ethernet and Wi-Fi

* **Topics:**
  * IEEE 802.3 and IEEE 802.11
  * Ethernet II frames and 802.11 frames
  * Access points
* **Builds on:** the learner knows Ethernet II at layer 2 and asked about Wi-Fi.
* **Situation:** a laptop on Wi-Fi needs to reach a computer on a cable. The problem asks what the frame looks like on each side.

## Reading before the next level

* Ethernet interfaces and MAC addresses: Wikipedia, "MAC address", the sections on the address format and on universal and local addresses.
* The OSI model: *The TCP/IP Guide*, "OSI Reference Model Layer Summary".
* IP addresses and the subnet mask: the two *TCP/IP Guide* sections under "Subnet mask" above.
