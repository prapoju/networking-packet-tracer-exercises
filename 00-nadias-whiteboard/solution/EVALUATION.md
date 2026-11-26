# Evaluation

Evaluator's notes from the quiz on 2026-11-17. They're for the next session, so it can know how much the learner knows and guide the next questions and problems. The quiz followed `INSTRUCTIONS.md`: one question at a time

## Concepts to look up

### Network protocol

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), Fundamental Network Characteristics: "Protocols: What Are They, Anyway?"
* **Why:** it's the real name for the shared convention the learner described.

### Message header

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), Key OSI Reference Model Concepts: "Data Encapsulation, Protocol Data Units (PDUs) and Service Data Units (SDUs)"
* **Why:** a header is the real name for the "convention of conventions": the fixed part of a message that says how to read the rest. The section sits in the OSI chapters, which the learner hasn't covered yet, so skip the parts about layers.

### IP address

* **Read:** *The TCP/IP Guide* (Charles M. Kozierok), IP Addressing Concepts and Issues: "IP Addressing Overview and Fundamentals"
* **Why:** the next exercise asks the learner to give each computer an IP address, so a game on one computer can find the other.

## Understood

* **Messages travel as bits.** The learner designed two computers that turn text into bits, send the bits through a cable, and turn them back into text.
* **Both sides must follow the same convention.** The learner went from "install the same program" to "the programs can be different if the logic is the same" to "there must be a convention for writing these programs". This is the idea behind a protocol and a standard. The learner doesn't know those words yet.
* **Different kinds of data need different conventions.** The learner said that sending a photo instead of text needs another convention.
* **A message must say which convention it uses.** The learner said the convention should be written in the message.
* **The label needs a fixed place.** The learner first said the label could go anywhere in the message. After seeing that photo bits could look like the label, they said there must be "a convention of conventions". This is the idea behind a header. The learner doesn't know that word yet.
* **A message can be meant for one program.** When Mark's computer runs a chat and a game, the learner said the message needs an identifier for the program it's meant for.

## Partly understood

* **"Convention of conventions" is still vague.** The learner hasn't said exactly what that rule decides: where the label goes, how long it is, and what comes after it.
* **Agreeing on the program identifier.** The learner didn't answer how Bob's computer and Mark's computer would agree on which identifier means "the game". It's the shared convention again, applied to identifiers.

## Not covered yet

* Which computer a message is for. Level `01-no-players-found` covers it through IP addresses.
* Port numbers. They need IP addresses first, so they come later.
* The OSI model.
* What physically travels through the cable, where one message ends and the next starts, flipped bits, and both computers sending at once.

## Next steps

We need to cover these things in the next exercises, in this order:

### 1. IP addresses

* **Topics:**
  * IP addresses
  * How a program on one computer names the other computer
* **Builds on:** the learner already sends messages between two computers through one cable.
* **Situation:** Leo's computer and Mia's computer can't find each other to play Tank Rally. This is level `01-no-players-found`, done in Packet Tracer.

### 2. Agreeing on which number means which program

* **Topics:**
  * Port numbers
  * Well-known ports
  * Who assigns port numbers
* **Builds on:** IP addresses from exercise 1, and the learner's idea that a message needs an identifier for the program it's meant for.
* **Situation:** two programs from companies that never talk to each other use the same number on Mark's computer, so the second one can't start. This is question 3c, which is still open.

### 3. What the "convention of conventions" decides

* **Topics:**
  * Message headers
  * Header fields
  * Encapsulation
* **Builds on:** the learner said a message needs a fixed rule about where the label goes.
* **Situation:** Bob's computer sends a photo for Mark's photo viewer and a text for Mark's chat. The problem asks the learner to draw one message and mark exactly which bits give the addresses, the program number and where the data starts.
