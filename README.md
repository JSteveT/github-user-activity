# GitHub Activity CLI Project

## Overview

This project is a simple command-line interface (CLI) tool that allows you to fetch and display the recent GitHub activity of any user. By providing a GitHub username, the CLI fetches and displays the user's recent events using GitHub's public API. This project serves as an exercise in API interaction, JSON data handling, and CLI application development.

## Features

- Accepts a GitHub username as a command-line argument.
- Fetches the user's recent activity from the GitHub API.
- Displays the fetched activity in the terminal.
- Handles errors gracefully, such as invalid usernames or API request failures.

## Requirements

- The application should run from the command line.
- You can use any programming language, but do not use external libraries for fetching the API data.
- API endpoint for fetching user activity:

<https://roadmap.sh/projects/github-user-activity>

## How to Use

**Install**: Clone this repository to your local machine.

  ```bash
  git clone <repo-url>
  ```

**Run**: Use the command below to fetch the activity for a GitHub user.

  ```bash
  github-activity <username>
  ```

## Error Handling

- If an invalid GitHub username is provided, the CLI will display a user-friendly error message.
- In case of API failures (e.g., rate limits, server issues), appropriate error messages will be shown.

## Future Enhancements

- Filter events by event type (e.g., commits, issues).
- Cache results to avoid unnecessary API calls.
- Fetch additional user information or repository details from other GitHub API endpoints.

## GitHub API Documentation

- Learn more about the GitHub API: [GitHub API Documentation](https://docs.github.com/en/rest)

---

Happy coding! Let me know if you encounter any issues while using this tool.
