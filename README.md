# BookBot

A command-line tool that analyzes text files (such as books from Project Gutenberg) to generate word and character statistics using core Python programming concepts.

## Key Features

- **Word Count**: Calculates the total number of words in a text file  
- **Character Frequency**: Tallies how often each alphabetic character appears, sorted from most to least frequent  
- **Lowercase Normalization**: All characters are converted to lowercase to avoid duplication  
- **Command-Line Arguments**: File path is provided at runtime via command-line interface  
- **Input Validation**: Graceful handling of missing or incorrect file path arguments  

## Technical Stack

- Python 3  
- Dictionary data structures for efficient counting  
- Lambda functions and `.sort()` for sorting logic  
- File I/O for reading `.txt` files  
- `sys.argv` for command-line argument parsing  

## Skills Demonstrated

- **Core Python**: Functions, conditionals, loops, string manipulation, dictionaries  
- **Data Handling**: Text parsing, data aggregation, filtering  
- **Command-Line Interfaces**: Argument handling and error messaging  
- **Code Organization**: Separation of logic across `main.py` and `stats.py`  
- **Testing and Debugging**: Manual testing with real book files and CLI input  

