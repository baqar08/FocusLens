# FocusLens
<div align="center">
   

**FocusLens is a productivity tracking application designed to provide insights into your work sessions. It allows users to log their focus sessions, track energy levels, and analyze performance patterns to optimize productivity.**

</div>

## Features

*   **Session Management:**
    *   **Log Work:** Record session details including date, time period, duration, and task type.
    *   **Energy Tracking:** Monitor your energy levels for each session to understand your peak productivity times.
    *   **History:** View a comprehensive log of all past sessions.
*   **Analytics & Insights:**
    *   **Performance Metrics:** Analyze how different factors contribute to your workflow.
    *   **Visual Data:** (Coming Soon) Interactive charts to visualize productivity trends over time.
    *   **Optimization:** Identify the best times of day and task types for maximum efficiency.
*   **User Interface:**
    *   **Clean Dashboard:** A streamlined interface for effortless data entry and review.
    *   **Responsive Design:** Accessible on various devices.

## Technologies Used

*   **Backend:** Python, Flask
*   **Database:** SQLite
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Templating:** Jinja2

## Demo Video

A showcase of the application features and workflow.

<!-- 🎥 [DEMO VIDEO](link_to_video) -->
*Demo video coming soon.*

## Local Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)

### 2. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/baqar08/FocusLens.git
cd FocusLens
```

### 3. Create a Virtual Environment

It is highly recommended to create a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python libraries using `pip`.

```bash
pip install -r requirements.txt
```
*Note: If a requirements file is not present, you can install the necessary packages manually:*
```bash
pip install flask
```

### 5. Configuration

This project uses a local SQLite database which is initialized automatically.

1.  **Database:** The `focuslens.db` file will be created in the root directory upon the first run.

### 6. Run the Application

Once the setup is complete, you can start the Flask development server:

```bash
python app.py
```

Now, open your web browser and navigate to the following address:

```
http://localhost:5000/
```

You should see the **FocusLens** dashboard running!

## How to Use

1.  **Access the Dashboard:** Open the application in your browser.
2.  **Log a Session:** Use the submission form to enter your session date, time, duration, energy level, and task type.
3.  **Review Data:** Check the dashboard list to see your logged sessions.
4.  **Analyze Trends:** Use the insights section to understand your productivity habits.
5.  **Manage Entries:** Delete incorrect or old entries as needed.

## Author

-   Name: Baqar Mustafa
-   Email: baqarmustafa84@gmail.com
-   GitHub: baqar08
