<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">Data Structures & Algorithms in Python</h1>

  <p align="center">
    A comprehensive learning project featuring implementations of fundamental data structures and algorithms with practical applications and simulations.
    <br />
    <br />
    <a href="#about-the-project">View Project Details</a>
    &middot;
    <a href="#project-structure">Browse Structure</a>
    &middot;
    <a href="#features">See Features</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage Examples</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a comprehensive **Data Structures and Algorithms (DSA)** learning project implemented in Python. It demonstrates fundamental concepts used in computer science and software engineering, including core abstract data types, algorithms, and practical applications. All implementations are done locally for educational purposes, and the resources are available for learning and reference.

**Key Focus Areas:**
- Foundational Abstract Data Types (ADTs)
- Practical algorithm implementations
- Real-world applications of data structures
- Problem-solving techniques

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROJECT STRUCTURE -->
## Project Structure

```
DSA/
├── Stack/                    # Stack ADT implementation
│   ├── stack.py             # Core stack class
│   ├── Stack Questions.py    # Stack problem solutions
│   ├── decimal_to_binary.py  # Number system conversion using stack
│   ├── decimal_to_hex.py     # Decimal to hexadecimal conversion
│   ├── decimal_to_octal.py   # Decimal to octal conversion
│   ├── undoredo.py           # Undo/redo functionality implementation
│   ├── vector_converter.py   # Vector conversion utilities
│   └── auto_data_converter.py # Automatic data type converter
│
├── Queue/                    # Queue ADT implementation
│   └── queue.py             # Core queue class with capacity management
│
├── Dequeu/                   # Double-ended Queue implementation
│   ├── deque.py             # Core deque class
│   ├── deque_test.py        # Unit tests for deque
│   ├── palindrome_checker.py # Palindrome validation using deque
│   ├── browser_logic.py      # Browser history simulation
│   ├── browser.py            # Browser navigation implementation
│   └── dequeu.py            # Alternative deque implementation
│
├── Linkedlst/               # Linked List implementation
│   ├── Linkedlist.py        # Core linked list class
│   ├── node_class.py        # Node structure definition
│   └── Node_Solid.py        # Alternative solid node implementation
│
├── Node Class/              # Node class utilities
│   └── node_class.py        # Node class base implementation
│
├── searching/               # Search algorithms
│   └── binary_search.py     # Binary search implementation
│
├── Simulations/             # Data structure simulations
│   ├── Data_Structure_Learning_project.py  # Main learning project
│   ├── playground.py        # Experimentation space
│   └── Sequence 1/          # Sequential learning modules
│
├── practice/                # Practice problems and questions
│   ├── Q5.py
│   ├── Q8.py
│   ├── question1.py
│   ├── Stack_class.py
│   └── question/
│
├── CH4/                     # Chapter 4 implementations
│   └── main.py
│
└── README.md               # Project documentation
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features

### Core Data Structures Implemented

- **Node Class**: Fundamental building block for linked structures
- **Stack (LIFO)**: 
  - Array-based implementation
  - Node-based implementation
  - Applications: undo/redo, expression evaluation, number conversions
  
- **Queue (FIFO)**:
  - Capacity management
  - Overflow handling
  - Standard queue operations

- **Deque (Double-Ended Queue)**:
  - Insert/remove from both ends
  - Palindrome validation
  - Browser navigation history simulation

- **Linked Lists**:
  - Singly linked lists
  - Node-based traversal
  - Dynamic memory allocation

### Algorithm Implementations

- **Binary Search**: Efficient searching in sorted arrays
- **Number System Conversions**: 
  - Decimal to Binary
  - Decimal to Hexadecimal
  - Decimal to Octal
  
- **Pattern Recognition**: Palindrome checking using deques

### Practical Applications

- Browser navigation with forward/back functionality
- Undo/redo system implementation
- Data type conversion utilities
- Vector operations

### Testing & Validation

- Unit tests for deque operations
- Palindrome checker validation
- Browser simulation testing

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Python 3.6 or higher
- Basic understanding of data structures and algorithms

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/DSA.git
   cd DSA
   ```

2. No external dependencies required - all implementations use Python standard library

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage Examples

### Stack Usage

```python
from Stack.stack import stack

# Create a new stack
s = stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Pop elements
print(s.pop())  # Output: 30

# Check if empty
print(s.is_empty())  # Output: False

# Peek top element
print(s.peek())  # Output: 20
```

### Queue Usage

```python
from Queue.queue import queue

# Create a queue with capacity
q = queue(5)

# Enqueue elements
q.enqueue(10)
q.enqueue(20)

# Check if empty
print(q.is_empty())  # Output: False
```

### Deque Usage

```python
from Dequeu.deque import deque
from Dequeu.palindrome_checker import palindrome_checker

# Check palindrome
result = palindrome_checker("racecar")
print(result)  # Output: True
```

### Number Conversion

```python
from Stack.decimal_to_binary import convert_to_binary
from Stack.decimal_to_hex import convert_to_hex
from Stack.decimal_to_octal import convert_to_octal

# Convert decimal to binary
binary = convert_to_binary(10)  # "1010"

# Convert to hexadecimal
hex_value = convert_to_hex(255)  # "FF"

# Convert to octal
octal_value = convert_to_octal(64)  # "100"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LEARNING OUTCOMES -->
## Learning Outcomes

By exploring this project, you will understand:

1. **Abstract Data Types**: How to design and implement fundamental ADTs
2. **Memory Management**: Stack vs. heap allocation, dynamic memory
3. **Algorithm Complexity**: Time and space complexity considerations
4. **Real-World Applications**: Practical uses of each data structure
5. **Problem-Solving**: How to approach and solve DSA problems
6. **Code Organization**: Best practices for structuring data structure code

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project demonstrates fundamental computer science concepts and serves as an educational resource for understanding data structures and algorithms in Python.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
