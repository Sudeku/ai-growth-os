# AI Workflow Design

## Goal

Turn a repeated task into a clear AI-assisted workflow.

## Process

### 1. Define the task

Bad:
"Help with marketing."

Good:
"Audit this landing page and create 10 specific improvements ranked by impact."

### 2. Define inputs

- business context
- audience
- goal
- constraints
- examples
- current data
- preferred output format

### 3. Define output

The AI should produce something usable:

- checklist
- brief
- table
- report
- plan
- script
- dashboard structure

### 4. Add quality rules

Examples:

- separate facts from assumptions
- do not invent numbers
- prioritize actions
- write for a non-technical user
- include risks
- include next step

### 5. Test

Run the prompt with 2-3 real examples.

### 6. Improve

Remove vague instructions.
Add missing context.
Make output stricter.

## Template

```markdown
You are [role].

Task:
[task]

Context:
[context]

Inputs:
[data]

Constraints:
[constraints]

Output format:
[format]

Quality rules:
[rules]
```
