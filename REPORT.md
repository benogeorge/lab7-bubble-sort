# Bubble Sort Visualization - REPORT

# First Impressions - Initial Take on the Project Assignment
This lab started as a basic Bubble Sort scaffold and grew into a visualization project. The main challenge was not the algorithm itself, but keeping the code organized so the sorting logic stayed separate from the rendering code.

## Initial Thoughts
I assumed the best approach was to make Bubble Sort emit steps that a renderer could consume. That made it possible to build both a terminal animation and a Pygame visualization without duplicating the algorithm.

## Assumptions Made
I assumed the animation should show comparisons and swaps, not just the final sorted result. I also assumed the visualization should keep running until the user quits, and that pause/resume would make it easier to study the sort.

## Points Needing Clarification
The lab suggested several possible directions, including terminal redraws and a 2D graphical view. The only real decision was how far to take the visualization, so I implemented both a terminal renderer and a Pygame renderer.

# Key Learnings
## Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered

## Computer Science Concepts and Technical Skills
Bubble Sort is much easier to visualize when the algorithm produces step objects instead of printing directly inside the sort loop. That separation made the project easier to test and let the UI stay focused on presentation.

## Insights about Using CoPilot Effectively
CoPilot worked best when I gave it a narrow, testable request, like adding pause control or highlighting swapped values in different colors. It was less reliable when the request was too broad, so I had to keep steering it back to specific behavior.

## New Concepts or Tools Encountered
I used Pygame for the graphics layer and pytest for validation. I also had to account for Python version differences on Windows, because Pygame installed cleanly with Python 3.12 but not with the default Python 3.14 environment.

## Acknowledgements
Thanks to the course materials, the lab instructions, and the contributors whose examples helped shape the final structure of this project. The implementation was easier to finish once the feedback was narrowed into specific, testable steps.

# Report on CoPilot Prompting Experience
## Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.

### Types of prompts that worked well
Prompts with concrete constraints worked well, such as "use two different colors for the values being swapped" and "keep the window open until q or Esc." Those prompts translated directly into code changes.

### Types of prompts that did not work well or failed
Very broad prompts like "do it all" were only useful after I broke the work into smaller parts. PDF extraction was also unreliable in the sandbox, so I had to work from the visible instructions and the actual repo instead of expecting the document to be machine-readable.
Another unhelpful pattern was asking for a full solution without naming the exact file or behavior. That usually led to extra back-and-forth, while direct prompts like "update the report section" or "add a pause control" moved much faster.

# Limitations, Hallucinations and Failures
## In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
## For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
## Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions
One failure mode was trying to treat the PDF as extractable text when the environment could not reliably read it. Another was an early copy of the project that nested the tests folder incorrectly, which needed a quick cleanup.

## Analysis of Why These Issues Occurred
The PDF issue came from sandbox/tooling limits, not from the lab itself. The folder issue came from copying a scaffold into the real repo and then reconciling it with the actual layout.

## Impact on the Project
The main impact was extra cleanup time. Once the structure was corrected, the implementation and documentation work were straightforward.

# AI Trust
## When did I trust the AI?
I trusted it most when it suggested small, verifiable changes such as pure functions, step generators, or UI behavior that I could test immediately.

## When did I stop trusting it?
I stopped trusting it when the request was too vague or when the output risked drifting away from the lab constraints.

## What signals or situations or patterns indicated low reliability?
Missing constraints, over-general advice, and suggestions that ignored the current repo structure were the main warning signs.

# What I Learned
## What did you learn about software development?
Small pure functions plus a step-based renderer make visual algorithms much easier to maintain. Separating the logic from the UI kept the project flexible.

## What did you learn about using AI tools?
AI is best used as a fast collaborator, not as a replacement for understanding. It helped a lot once I kept the prompts narrow and checked the results.

## When should you trust AI? When should you double-check it?
Trust AI for focused scaffolding and implementation ideas. Double-check anything that changes architecture, dependencies, file layout, or environment setup.

## What I would do differently next time
I would split the work into smaller deliverables earlier, keep the documentation updated as I go, and verify each step before moving on. That would make the final push much smoother.

# Reflection
## Did AI make you faster? Why or why not?
Yes, mostly because it sped up the boilerplate and helped with repeated structure. It slowed down when I let the scope stay too broad.

## Did you feel in control of the code?
Yes. I felt in control when the code was split into logic, terminal rendering, and Pygame rendering, and when I kept the algorithm in one place.

## Would you use AI the same way next time? What would you change?
I would split the project into smaller pieces sooner and keep the prompts narrower from the beginning. That would avoid some of the backtracking and cleanup.

# Final Notes
This project now has a working Bubble Sort visualization, a reusable sort generator, automated tests, and written reflections on the development process. The main lesson was that a small, well-structured codebase is easier to finish than a large, loosely defined one.
