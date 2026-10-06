# Government Systems & Procedures

An interactive, jurisdiction-neutral command-line course written in Python. It helps learners understand how government organizations work, how administrative procedures are followed, and how departments coordinate, with lessons, practical activities, and quizzes.

> **Disclaimer:** This is a general learning aid, not legal or financial advice. Government structures, laws, procedures, budgets, and programs differ by jurisdiction and change over time. Always confirm details with current official sources.

## Objectives

1. Understand government organizational structure and hierarchy.
2. Learn administrative procedures and protocols followed in government offices.
3. Study government acts, rules, and regulations applicable to your department.
4. Understand budgeting processes and financial management in government.
5. Learn about government schemes and programs relevant to your ministry.
6. Develop understanding of inter-departmental coordination and communication.

## Course Topics

| # | Topic |
|---|-------|
| 1 | Government organization and hierarchy |
| 2 | Administrative procedures and protocols |
| 3 | Acts, rules, and regulations |
| 4 | Budgeting and public financial management |
| 5 | Government schemes and programs |
| 6 | Inter-departmental coordination and communication |

Each topic includes:

- **Lesson sections** with key concepts
- **A practical activity** to apply what you learned to your own department
- **A 3-question multiple-choice quiz** with explanations and a score

## Features

- Interactive text menu (read a lesson, take a quiz, view the study plan, exit)
- Instant quiz feedback with a short explanation for every answer
- Suggested study plan
- Input validation and clean exit on `Ctrl+C` / `Ctrl+D`
- No external dependencies, only the Python standard library

## Requirements

- Python 3.8 or higher

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Run the course
python government_systems.py
```

## Usage

When the program starts you will see the main menu:

```
Main menu
  1. Read a lesson
  2. Take a topic quiz
  3. View the suggested study plan
  4. Exit
```

- **Read a lesson:** pick a topic number to read its sections and practical activity.
- **Take a topic quiz:** answer 3 questions per topic and get your score.
- **Study plan:** a recommended way to work through the course.

## Suggested Study Plan

1. Read one lesson and complete its practical activity.
2. Use your department's current official documents to verify local details.
3. Take the lesson quiz and review any missed concepts.
4. Repeat for each topic, then map how the topics connect in your role.

## Project Structure

```
.
├── government_systems.py   # Course content and interactive program
└── README.md
```

The course content lives in the `COURSE` list at the top of the script. To add or edit a lesson, add a dictionary with `title`, `sections`, `activity`, and `questions`.

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your changes, and open a pull request.

## License

Add a license of your choice (for example, MIT) in a `LICENSE` file.

## Author

**D Sree Chaitanya**
B.Tech CSE, Vignan's Lara Institute of Technology and Science
