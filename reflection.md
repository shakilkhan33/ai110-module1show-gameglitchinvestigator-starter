# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").


  a. I noticed that there was either higher or lower gussing number but it showed wrong hints, Too high , Too low problems.
  b.When The secret number and the guessing number is correct , the game doest not give me play again. a new game will not show up.
  c. There was a history delay.
  d.Incorrect attempt : The is not reduce properly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I am using Copilot, and it helps me to correct the problems that I chose in guessing number. It is supposed to give me "Too High" or "Too Low" hints, but it gives me the opposite. However, AI also gives me the wrong answer. As I tried to re-start the game, it didn't let me play a new game. While I tried to fix it, the random import was missing, and I fixed it manually.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I play the game again that help me to understand the code was really fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I used pytest, It showed me green line that was changed and I read the code to see if it is wrong or not.

- Did AI help you design or understand any tests? How?

First of all, when I find the bugs, AI helps me to fix them as a mentor line by line, but I have to make sure to give AI the right selection parts; otherwise, it gives me the wrong answer. Let’s say I try to fix a bug in one chat box; it gives me a mixed answer based on previous code that I didn’t want. I have learned something new: if I use AI, I have to guide it properly; otherwise, it gives me the wrong answer.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I used Streamlit for the first time and it helped me to learn how webpages work and whenever I click a button or change something, the entire app code runs again from top to bottom. While I changed the code or found any bugs, I fixed the main code and saw the Streamlit changes such as when I fixed the new game to play again, it worked perfectly. It's different from regular web apps where you have to manage state manually with databases or cookies.

---


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I have learned something new such as Git and GitHub usage and how to fix bugs, identify bugs, and efficiently fix errors. I believe these habits can help me in future debugging with me and ChatGPT together.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I might try to fix the problems first, then ask ChatGPT to help with the issues. This approach could help me build self-confidence while also improving the AI's suggestions, making the code more efficient.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
The project changed my whole perspective. I used to think AI was something you could use blindly and that machines would not give wrong answers, but I learned that we need to guide it properly; otherwise, it sometimes gives incorrect answers.