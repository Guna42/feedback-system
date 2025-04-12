 # Feedback Submission and Management System

A web application for LearnSphere, an online learning platform, to collect and manage student feedback efficiently. Built for the CLA-2 web development assignment, due April 15, 2025.

## Overview
This project provides a user-friendly feedback form for students and a secure admin dashboard to review and manage feedback. It includes a success message after submission, spam protection, and a simple admin login for security.

## Features
- **Feedback Form**: Students can submit feedback with optional name and email, a category (Bug, Suggestion, Complaint, Other), and a message (max 500 characters).
- **Success Message**: Displays a green alert after successful submission.
- **Spam Protection**: A "not a robot" checkbox prevents automated submissions.
- **Admin Login**: Secure access to the dashboard with username `admin` and password `password123`.
- **Admin Dashboard**: View all feedback in a table, update status (Open, In Progress, Done), and log out.
- **Database**: Stores feedback in SQLite (`feedback.db`, created automatically).
- **Responsive Design**: Uses Bootstrap for a clean, mobile-friendly interface.

## Setup Instructions
To run the application locally, follow these steps:

1. **Install Python 3**:
   - Download and install from [python.org](https://www.python.org/downloads/).
   - Verify: `python --version` (should show Python 3.x.x).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/Guna42/feedback-system.git
   cd feedback-system