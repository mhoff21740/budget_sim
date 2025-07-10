# budget_sim
A simple, functional programming-based personal budgeting app written in Python.


# Functional Personal Budget Simulator

  A simple, functional programming-based personal budgeting app written in Python.
  This project helps users simulate monthly income, expenses, savings, and forecasts.
  While reinforcing key functional programming (FP) concepts like pure functions,
  immutability, map/filter/reduce, and composability.

---

## Purpose

  This project is a learning tool and a useful budgeting utility. It was created to:
  
  - Practice functional programming patterns in Python
  - Reinforce concepts like pure functions, state immutability, and statelessness
    transformations
  - Explore real-world value through a personal budgeting use case

---

## Project Structure
  personal_budget/
  │
  ├── main.py # Entry point / CLI loop
  ├── budget_state.py # Core state and pure functions
  ├── calculations.py # Totals, filters, forecasts
  ├── categories.py # Category filtering and logic
  ├── recurring.py # Generator functions for recurring expenses
  ├── examples.py # Sample test run and scenarios
  └── tests.py # Basic test functions



---

## Functional Programming Concepts Used
  
  - **Pure functions**  
    Functions that do not modify state always return the same output for a given input.
  
  - **Immutability**  
    The budget "state" is never modified directly; instead, a new copy is returned after
    each update.
  
  - **Map / Filter / Reduce**  
    Used for expense summaries, filtering by category, and computing totals.
  
  - **Generator functions**  
    Used to simulate recurring expenses like rent or subscriptions.
  
  - **Composability**  
    Category filters and state transforms can be composed together for complex behavior.

---

## Getting Started

  1. Clone the repository:
  
     ```bash
     git clone https://github.com/your-username/personal_budget.git
     cd personal_budget
  
  2. Run python main.py


## Core Features

  *Add income and expenses.
  
  *Calculate total expenses and savings
  
  *Categorize and filter expenses.
  
  *Maintain immutable state after each update
  
  *Recurring expense support via generators

## Planned Features

  *Monthly budget forecasting
  
  *CLI or TUI interface
  
  *Export budget summaries
  
  *Save/load budgets from JSON
  
  *Unit test coverage for all functions

