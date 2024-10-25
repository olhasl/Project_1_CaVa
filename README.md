## Project 1
# Challenge "Openspace classifier"
## Project 1
# Challenge: Openspace Organizer

## The Team: Olha, Andrii

**Repository:** openspace-organizer  
**Challenge Type:** Consolidation  
**Duration:** 2 days  
**Deadline:** 25/10/24 at 5 PM  
**Team Challenge:** Yes  

## Table of Contents
1. [Project Description](#project-description)
2. [Learning Objectives](#learning-objectives)
3. [Mission](#mission)
4. [Features](#features)
5. [Code Style](#code-style)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Deliverables](#deliverables)

## Project Description
Our company recently relocated to a new open-space office that features 6 tables with 4 seats each, providing a total of 24 seats. To help team members connect and interact more, we developed a daily program that assigns everyone to a new seat at random. This Python-based program takes a list of colleagues from an Excel file, randomly allocates them to available seats, and displays the seating plan, giving everyone the opportunity to work with different colleagues each day.

## Learning Objectives
The project is designed to:
- Utilize object-oriented programming (OOP) concepts effectively
- Create clean, reusable code by applying good OOP principles
- Organize code with imports and project structure
- Load and handle data from Excel files
- Use version control with Git and collaborative tools like Trello, especially if working in a team

## Mission
Develop an algorithm that assigns seats randomly in the open-space area, refreshing the arrangement each day. The program will load a list of colleagues from an Excel file, place them randomly at available tables, and keep track of any remaining open seats. It should also manage cases where there are either too many colleagues or not enough seats.

## Features
### Must-Have
1. Load a list of colleagues from an Excel file.
2. Randomly assign colleagues to 24 seats across 6 tables.
3. Display the seating arrangement and note the number of unoccupied seats.
4. Handle situations where there are more colleagues than seats.

# Project Directory Structure

```plaintext
openspace-organizer/
├── README.md                # Project overview and instructions
├── main.py                  # Entry point to run the seating organizer
├── config.yaml              # Configuration file to specify the Excel file path
└── utils/
    ├── file_utils.py        # Handles file operations like reading the Excel file
    ├── table.py             # Defines the Table and Seat classes
    ├── openspace.py         # Defines the Openspace class, managing tables and assignments
```


# Installation
## Clone the repository (bash):

git clone https://github.com/yourusername/openspace-organizer.git

## Install required dependencies (bash):

pip install -r requirements.txt

## Modify config.yaml to specify the path to your Excel file containing colleague names (yaml):

filepath: "./bouman_8/bouman_8.xlsx"

## Usage

To start the program, run main.py:

python main.py

Output: The seating arrangement will display in the console, indicating which colleagues have been assigned to each table and any remaining unoccupied seats.

## Deliverables
**Source Code**: Complete, functional Python code, organized according to the project structure.
**README**: A detailed README.md with installation and usage instructions, clear objectives, and a project summary.
**Branching Strategy**: The main branch contains only essential features. Additional features or updates are on separate branches and merged via pull requests.

## Optional (Team-Specific)

Use Git for collaboration with a Kanban board on Trello.
Break down the functionalities into individual tasks, assign tasks, and track progress.
Develop each feature on its own branch and merge using PRs.

## Contributors
List your team members here if it's a collaborative project.

## Timeline
This project is designed to be completed within two days.
