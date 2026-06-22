# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like a number guessing game with scores and difficulty setting
- List at least two concrete bugs you noticed at the start  
  The hints are backwards
  Enter does not work
  New game does not work
  Attempts is off by one number

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Pressed  Enter is supposed   Nothing             N/A
Enter|    to input the new 
          number
|Entered  Hint is supposed to It shows to go     N/A
20 when   say go higher       lower
guess is 
27| 
|Entered  Hint is supposed to It shows to go     N/A
28 when   say go lower        higher
guess is 
27|
|Press    game restarts      Cannot start       N/A
New Game                      new game
|
|Attempts Attempts state is 6 Only have 5       N/A
is off by                     Chances
one number|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code to assist me during this assignment

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One suggestion that AI showed that was correct was when I was unsure where the difficulty logic was, it pointed out where it was. I had a feeling that while I was debugging the game, the difficulty was off but when it was pointed out to me by Claude, it confirmed my suspicions. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It was suggesting that the comments for the hints being wrong was becasue of the emojis. After I looked into the strings, it was not just the emojis, but the placement of where the strings were supposed to be. I swapped the messages to their correct spots and added my own logic to ensure that it was correct.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided if a bug was really fixed if I was able to not repeat it multiple times doing multiple different tests. I also looked at the refactored code and made some edits if needed to ensure it was up to my standard.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One manual test I did was when a user guessed a number, I would intentionally go lower for the first guess, and higher for the second guess to ensure the hint messages were correct. From there I would guess the right number and then hit new game to ensure everything was reset.
- Did AI help you design or understand any tests? How?
AI helped me understand the design of the code. I made sure that with each interaction, I had it explain the logic of the current code being fixed before edits were made, from there I would see if I could make the edit myself before letting Claude Code go through with the edits.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
