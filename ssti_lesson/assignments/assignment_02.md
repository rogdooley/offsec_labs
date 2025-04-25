# Assignment 2 - Advanced Payloads and Bypassing Filters

## Goal
Deepen your SSTI exploitation skills by crafting more advanced payloads and bypassing potential input filters.

## Instructions

1. Try to access server internals:
   - Dump classes or environment variables.
   - Explore the object hierarchy using payloads like:

     ```
     {{''.__class__.__mro__[1].__subclasses__()}}
     ```

2. Locate useful classes:
   - Identify the class responsible for executing commands, such as `subprocess.Popen`.

3. Craft an execution payload:
   - Find a chain to execute system commands.

4. Bypass naive filters:
   - If you imagine the developer tries to block `{{` or `}}`, think about encoding, splitting, or other bypass techniques.

## Deliverables

- Successful payloads for object access and command execution
- Bypass techniques you attempted or discovered
