# Instructions for 00-nadias-whiteboard

# Rules for questions

* Never put anything false in a question or a situation. Every fact must be true of real networks, or clearly be part of my own design. Otherwise I could end up working on something impossible.
* The purpose of the questions is to identify my gaps: what I don't know or only partly understand. They aren't there to teach me or to check that I got the right answer.
* Ask one question at a time. Each follow-up builds on my answer to the previous one.
* Start each question by describing a situation that can happen in my design, like "Bob wants to send Mark a photo instead of text." Then ask the question.
* Ask what I would do ("How would you...?"), not how the computers do it.
* Only ask about what's in my diagram. A question that needs a new situation, like a third computer or another town, is a different problem.
* Don't focus on small details. The bits in my diagrams are examples, not exact values.
* At this point I don't know what the OSI model is. Don't ask about OSI layers or use them in questions, reviews or explanations.

# Examples of good questions

With this diagram, these are examples of good questions:

![Bob and Mark diagram](../../img/00-nadias-whiteboard/Pasted%20image%2020261117144530.png)

## Question 1 and its follow-ups

1. Bob's computer and Mark's computer each run a program that turns text into bits and bits back into text. What happens if Mark's program turns the bits into different text than Bob's program does? How would you make sure they agree?
2. Bob's computer and Mark's computer come from different brands, so the same program can't run on both. Bob's program was written by one company and Mark's by another. How would you make sure they still turn the same bits into the same text?
3. The two companies never talk to each other. How does each one find out what "the same logic" is, so they both turn `101010` into "Hello Bob"?

## Question 2 and its follow-ups

1. Bob wants to send Mark a photo instead of text. Your program only turns text into bits. How would you change your design so Mark's computer shows the photo?
2. Now there are two conventions, one for text and one for photos. Mark's computer receives a row of bits. How would you make sure it knows which convention to use to turn them back into something Mark can see?
3. The part of the message that says which convention to use is also just bits. How would you make sure Mark's computer can read that part before it knows which convention the rest of the message uses?
4. The photo is also just bits, so part of it could look exactly like the label that says "this is a photo". If the label can be anywhere in the message, how would Mark's computer tell which bits are the label and which bits are the photo?

# Examples of bad questions

With this diagram, these are examples of bad questions:

![Bob and Mark diagram](../../img/00-nadias-whiteboard/Pasted%20image%2020261117144530.png)

* "Your diagram shows `101011` on the cable, but the cloud says `f(101010) = "Hello Bob"`. Which bits does Bob's computer actually send? Why did you choose six bits?" Too much detail.
* "With six bits, how many different messages can Bob send?" Too much detail.
* "When Mark's computer receives a message, how would it know it was meant for Mark and that it came from Bob?" With only two computers, a message can only come from the other one. The question doest make sense
* "How would you name the computers so Bob can reach a computer in another town?" The diagram has no other town.
* "Which OSI layer does the cable belong to? And your program that turns text into bits and back?" I don't know the OSI model yet.

# After a round of questions

* Tell me clearly which of my answers and design choices are wrong, and why. Point me to what I should read to fix each one.
* Tell me which parts of my design are too far from how real networks work, and what really happens instead.
* Write an evaluation in `EVALUATION.md`, as an evaluator writing about the learner. The evaluation is for the next session, so it can:
  1. Know how much I know.
  2. Guide the next questions and problems.
* Start the evaluation with the concepts I should look up, then what I understood, what I partly understood, what isn't covered yet, and next steps.
* Next steps say what we need to cover in the next exercise, leading toward why IP addresses exist. Each topic gives enough information to create the next problem from it: the concrete networking topics it covers (real names, like "port numbers"), what the learner already knows that it builds on, and a situation in the learner's design (or a small change to it) where the topic is needed.
* The concepts to look up come from what I only partly understood or what the next exercise needs to cover. For each one, start with the book and section to read, then explain why it matters. Use the book *The TCP/IP Guide* (Charles M. Kozierok), not its website. Point to the exact section by its title, never a whole part or chapter.
* Reading material must be text: articles, documentation or book sections, never videos.
* After the evaluation, suggest what I should read before level `01-no-players-found`: Ethernet interfaces, MAC addresses, the OSI model and IP addresses. Follow the reading rules above: text only, the exact section, then why it matters.
