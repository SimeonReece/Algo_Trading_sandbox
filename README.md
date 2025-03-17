
# Installation and Setup

This project requires a few dependencies and specific steps for proper execution. Follow the instructions below:

## Prerequisites

* **Git:** If you don't have Git installed, download and install it from the official [Git website](https://git-scm.com/).
* **Python:** Ensure you have Python installed.

## Installation Steps

1.  **Clone the Repository:**
    * Open your terminal or command prompt.
    * Navigate to the directory where you want to store the project.
    * Run the following command:
        ```bash
        git clone https://github.com/SimeonReece/Algo_Trading_sandbox.git
        ```
    * Navigate into the project directory:
        ```bash
        cd Algo_Trading_sandbox
        ```
2.  **Install Dependencies:**
    * Install `yfinance`:
        ```bash
        pip install yfinance
        ```
    * Install `backtrader`:
        ```bash
        pip install backtrader
        ```
    * **Update pip (if necessary):**
        ```bash
        python -m pip install --upgrade pip
        ```

3.  **Running the Code:**
    * **Open with VS Code (Recommended):**
        * From inside the `Algo_Trading_sandbox` directory, run:
            ```bash
            code .
            ```
        * This will open the project in Visual Studio Code.
    * **Individual File Execution:**
        * It's recommended to run each Python file individually for error checking and better understanding. This will help you isolate and debug any issues that may arise.
        * In your terminal, while in the correct directory, you can run a python file like this:
            ```bash
            python your_file_name.py
            ```
            (Replace `your_file_name.py` with the actual name of the file.)

## Notes

* Ensure you are in the `Algo_Trading_sandbox` directory when running commands.
* Using VS Code will provide a better development experience.
* Running each python file individually is encouraged to understand the code and debug errors.

