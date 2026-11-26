# Evaluation

Evaluator's notes from the quiz on 2026-11-26. They're for the next session, so it can know how much the learner knows and guide the next questions and problems. The quiz was one question at a time. The learner stopped after question 3, so question 4 has no answer.

## Concepts to look up

### Counting the bits in a mask

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), "IP Subnet Masks, Notation and Subnet Calculations"
* **Why:** the solution says the last 1 in Theo's mask is the 27th bit. The learner's own table shows 26 ones, and the `/26` in the script's output says the same. Counting the 1s is the whole point of a mask, so it has to be exact.

### Direct and indirect delivery

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), "IP Datagram Direct Delivery and Indirect Delivery (Routing)"
* **Why:** the solution says Theo's computer "can't send packets to IPs that don't belong to his network". That's only true because there is no router and no default gateway. This section explains what a computer really does with an address outside its network. It leads straight into the next level.

### ICMP echo messages

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), "ICMPv4 Echo (Request) and Echo Reply Messages"
* **Why:** the learner knows type 8 and type 0 from their notes, but called them "request" and "reply" only after checking. The section gives the real names and shows what each message carries.

## What the learner got wrong

* **"The last 1 in Theo's subnet mask is the 27th bit."** Wrong. 255.255.255.192 is 26 ones, so the last 1 is the 26th bit. The learner's own claim that "the 26th bit is different in Theo's IP and Ivy's IP" was correct, because bit 26 is inside the network part. While fixing the first line, the learner first changed the second one to 27 as well. After seeing the bits numbered, they corrected both to 26.
* **Question 2: "only the mask… probably the IP address already belongs to Ivy's network."** The answer is right, but it was a guess. The learner said they didn't want to do the conversion. Their own "Seen from Ivy's computer" table already shows that Theo's IP shares its first 24 bits with Ivy's network, so the evidence was in their solution.
* **Question 3 was left half answered.** The learner named the type 8 request from Ivy to Theo and the type 0 reply from Theo to Ivy. They didn't say that the reply never left Theo's computer, although the solution says so.
* **Question 4 was not answered.** Ivy with 10.20.30.20 and mask 255.255.255.192 is in network 10.20.30.0/26, which covers 10.20.30.0 to 10.20.30.63. Theo's 10.20.30.70 is outside it. So Ivy's computer would refuse to send the request at all, and now neither direction works. The same check that failed on Theo's side would fail on Ivy's side.

## Too far from reality

* **"Theo can't send packets to IPs that don't belong to his network."** In a real network, a computer sends packets for other networks to its default gateway, a router. Theo's computer gave up only because it has no gateway configured, and there's no router in the shop. The rule the learner found is really "a computer delivers directly only inside its own network".
* **"Theo refused to respond."** The computers don't refuse or argue. Theo's computer received the request and tried to answer. Before sending, it checked whether Ivy's address is in its own network. It isn't, and with no gateway there was nowhere else to send the reply, so it was dropped.
* **The fix itself is realistic.** In real life the two computers on one cable must use the same network and the same mask. Moving Ivy into Theo's network, with a free address like 10.20.30.65, is what a technician would do. Moving Theo to Ivy's mask would work just as well.

## Understood

* **What a subnet mask does.** The learner can AND an IP address with its mask, get the network address, and explain that the mask keeps the network part and zeroes the host part.
* **Why a computer stores the mask and not the network address.** In their own words: the network address alone doesn't say where the network part ends.
* **Two computers can disagree about the same address.** The solution shows that Ivy sees Theo as local and Theo doesn't see Ivy as local. The binary tables show why.
* **Either side can be changed.** In question 1, the learner saw that the opposite fix, changing Theo's settings, works too.
* **Network and broadcast addresses can't be given to a computer.** The script excludes them, and Theo's address, from the list of free addresses.
* **CIDR notation.** The learner knows that `/26` is the prefix length.
* **Using Python to check the work.** The learner wrote a script with the `ipaddress` library to print the addresses in binary and list the free addresses.

## Partly understood

* **Counting bits.** The learner can write addresses in binary but miscounted the mask (27 instead of 26), and avoids converting when not forced to.
* **ICMP echo.** The learner knows the type numbers and directions from notes, but not yet what happens to the reply when the sender can't deliver it.
* **The check happens on the sending side.** The learner saw it on Theo's side but didn't get to apply it to a new setup (question 4).

## Not covered yet

* The default gateway and routers. Never introduced.
* ARP's place in the solution. A computer only uses ARP for addresses in its own network, but it wasn't quizzed.
* OSI layers for ICMP, IP and the mask check. Not asked in this round.

## Next steps

We need to cover these things in the next exercises, in this order:

### 1. Default gateway

* **Topics:**
  * Default gateway
  * Router
  * Indirect delivery
* **Builds on:** the learner knows that a computer checks whether a destination is in its own network, and that without help it drops packets for other networks.
* **Situation:** two computers that must stay in different networks, for example because each network was set up by someone else and can't be renumbered, with a router between them. The learner has to find out what each computer needs so its packets for the other network go to the router.

### 2. Switch with several devices

* **Topics:**
  * Switch
  * Several computers in one network
* **Builds on:** subnet masks and same-network delivery.
* **Situation:** a shop adds a third and fourth computer, and one cable between two computers is no longer enough.

## Reading before the next level

* *The TCP/IP Guide*, "IP Datagram Direct Delivery and Indirect Delivery (Routing)".
* *The TCP/IP Guide*, "IP Addressing Categories (Classful, Subnetted and Classless) and IP Address Adjuncts (Subnet Mask and Default Gateway)", only the part about the default gateway.
