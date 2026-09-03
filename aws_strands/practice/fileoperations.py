from strands import Agent
import os
from strands_tools import file_read,file_write,editor


FILE_SYSTEM_PROMPT="""You are a file operations specialist. You help users read, 
write, search, and modify files. Focus on providing clear information about file 
operations and always confirm when files have been modified.

Key Capabilities:
1. Read files with various options (full content, line ranges, search)
2. Create and write to files
3. Edit existing files with precision
4. Report file information and statistics

Always specify the full file path in your responses for clarity.
"""

file_agent=Agent(
    system_prompt=FILE_SYSTEM_PROMPT,
    tools=[file_read,file_write,editor],
)

if __name__=="__main__":
     print("\n📁 File Operations Strands Agent 📁\n")
     print("This agent helps with file operations using Strands Agents.")
     print("Type your request below or 'exit' to quit:\n")

     test_file=os.path.join(os.path.expanduser("~"),"strands_test_file.txt")
     if not os.path.exists(test_file):
           with open(test_file, "w") as f:
            f.write("This is a test file created by Strands File Operations example.\n")
            f.write("You can read, edit, or modify this file using the agent.\n")
            f.write("Try commands like:\n")
            f.write("1. Read this file\n")
            f.write("2. Add a new line to this file\n")
            f.write("3. Replace 'test' with 'sample' in this file\n")
            print(f"Created a test file at: {test_file}")
     while True:
         try:
             user_input=input("\n> ")
             if user_input.lower()=='exit':
                  print("\nGoodbye! 👋")
                  break
             file_agent(user_input)
         except KeyboardInterrupt:
              print("\n\nExecution interrupted. Exiting...")
              break
         except Exception as e:
              print(f"\nAn error occurred: {str(e)}")
              print("Please try a different request.")


    
     

