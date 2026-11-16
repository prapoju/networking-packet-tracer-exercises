# Introduction

You're **Jax**, 24 years old. You live in Harbor Hill, a fishing town of about 9,000 people. You rent a one-bedroom apartment over a bakery. The heater only works on the lowest setting, and the landlord hasn't called back about it.

<p align="center">
  <img src="img/jax-harbor-hill.svg" width="450" alt="Drawing of Jax in an orange hoodie, standing on the Harbor Hill boardwalk with the harbor and lighthouse behind him">
  <br><em>You, on the boardwalk in Harbor Hill.</em>
</p>

After high school, you applied to six places. The Coastline Telecom call center called back first, and it paid 15 corins an hour. For three years you answered internet complaints from a script: *"Have you tried turning your router off and on again?"* Most calls ended there. The rest went to a technician, and you never heard how they turned out.

<p align="center">
  <img src="img/call-center.svg" width="450" alt="Drawing of Jax at a call center desk, wearing a headset, next to a screen showing the router script">
  <br><em>Your old desk at Coastline Telecom. Call 47 of 80.</em>
</p>

Then, one Thursday afternoon, a manager from head office called all 42 of you into the break room. He read from a printed page: the Harbor Hill center would close in two weeks, and the calls would be answered overseas. Nobody asked questions. On your last day, you packed your desk into a printer-paper box: a mug, a phone charger, a dead plant. How long does it take to clear out three years? About ten minutes.

<p align="center">
  <img src="img/last-day.svg" width="450" alt="Drawing of Jax carrying a printer-paper box out of the closed Coastline Telecom building, past a FOR LEASE sign">
  <br><em>Your last day at Coastline Telecom.</em>
</p>

Since then, you've applied to 14 jobs and heard back from one, which went to someone else. Neighbors still ask you about their Wi-Fi, so you printed 50 flyers at the library: **"Network problems? I come to you. Jax, 555-0147"**. Rent is 650 corins, due on the 1st. You have 410 in the bank.

<p align="center">
  <img src="img/flyer-board.svg" width="450" alt="Drawing of Jax holding a stack of flyers next to his flyer on the Marlow's Coffee community board, with one phone tab torn off">
  <br><em>Your flyer at Marlow's Coffee. Someone already took one of the tabs.</em>
</p>

Three weeks after the flyers went up, your phone rang. It was Rosa, who had pulled a tab off your flyer at Marlow's Coffee. Her twins, Leo and Mia, have one computer each, and since the spring the two computers can't find each other. She offered 25 corins to come by on Saturday morning. You're still 240 short of rent.

<p align="center">
  <img src="img/phone-call.svg" width="450" alt="Split drawing: Jax on the phone at his kitchen table, and Rosa on the phone in her apartment at night">
  <br><em>Yesterday evening.</em>
</p>

# Context

<p align="center">
  <img src="img/characters.svg" width="700" alt="Mosaic of the four characters: Jax, Rosa, Leo and Mia, each with their name and role">
  <br><em>The people in this story.</em>
</p>

Rosa rents a two-bedroom apartment with Leo and Mia, who are 11. The twins share the smaller bedroom. Their two computers sit on two desks, side by side, about a meter apart.

<p align="center">
  <img src="img/room-today.svg" width="420" alt="Deployment diagram of Rosa's apartment today: Leo's computer and Mia's computer in Leo and Mia's room, not connected">
  <br><em>Leo and Mia's room today.</em>
</p>

<p align="center">
  <img src="img/uc-devices.svg" width="600" alt="Mosaic of two use case diagrams: Leo's computer (host a Tank Rally match, type school reports) and Mia's computer (join a Tank Rally match, type school reports)">
  <br><em>What each device is for.</em>
</p>

# The problem

## Problem 1: Leo's computer and Mia's computer can't find each other

Until the spring, both computers were plugged into the Coastline Telecom router in the hallway, and the twins played Tank Rally against each other. Then Rosa cancelled the internet to save 45 corins a month, and the router went back to Coastline. Since then, Tank Rally shows "No players found" on both computers. Two computers, a meter apart, and neither knows the other one exists. Now the twins take turns: one plays alone against the computer, and the other waits on the bed.

<p align="center">
  <img src="img/twins-play.svg" width="460" alt="Flow diagram with lanes for Leo, Leo's computer and Mia: Leo opens Tank Rally and looks for a match; Leo's computer shows No players found; Leo plays alone; Mia waits for her turn, then plays alone">
  <br><em>How Leo and Mia play Tank Rally today.</em>
</p>

## Constraints

Rosa bought network cables at the hardware store, and that's everything she has. You can use any of them. She won't buy anything else, and she won't pay for the internet again.

## What Rosa wants

- From Leo's computer, Mia's computer answers.
- From Mia's computer, Leo's computer answers.

# Your task

* Make Leo's computer and Mia's computer find each other again in Cisco Packet Tracer, using `PC-PT` for both.
* Prove it. Packet Tracer can't run Tank Rally, so the two computers answering each other is enough. Rosa won't pay 25 corins for "I think it's fine now."

# What to deliver

- `solution.pkt`, your Packet Tracer file, with the two computers working
- `SOLUTION.md`, where you
    1. Justify the decisions you took to solve the problem and build the network.
    2. (Optional) Show the things that caught your attention in Packet Tracer, along with their explanation.
    3. (Optional) Write about your experiments.

# Useful material

- [Packet Tracer help: logical workspace](https://tutorials.ptnetacad.net/help/default/workspace_logical.htm)
- [Packet Tracer help: connections and links](https://tutorials.ptnetacad.net/help/default/connectionsLinks.htm)
- [Packet Tracer help: simulation mode](https://tutorials.ptnetacad.net/help/default/mode_simulation.htm)
- *The TCP/IP Guide* (Charles M. Kozierok): OSI Reference Model chapters
- [Cloudflare: What is an IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)
