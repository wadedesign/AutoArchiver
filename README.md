# AutoArchiver

## Introduction

**AutoArchiver** is a powerful Python script designed to help developers declutter their development folders by automatically archiving old projects. It seamlessly runs in the background, monitoring your specified directories and moving projects that haven't been modified in a specified period to an archive location. With upcoming features like colorful logging and version tracking, you'll have a clear view of its operation and the assurance that your workspace remains organized without manual intervention.

## Features

- **Automatic Archiving**: Configure once and forget as it takes care of old projects cluttering your workspace.
- **Customizable Settings**: Easily set your base and archive directories, and define the archiving threshold.
- **Background Operation**: Designed to run silently in the background, ensuring your workspace is always organized.
- **Startup Automation**: With simple setup, ensure AutoArchiver starts with your PC, keeping your environment clean every day.
- **Upcoming Logging Feature**: Visual feedback through colorful logging in the terminal, tracking archiving actions, runtime duration, and more.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `shutil`, `os`, `time`, `dotenv`, and `logging` libraries (included in standard Python installations)
- `colorama` library for colorful logging (coming soon)

### Installation

1. Clone the repository or download the script to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` (This step will be necessary once the `colorama` library is integrated).

### Configuration

1. Use the `.env` file to configure your base and archive directories, along with the archiving threshold.
2. Adjust the `VERSION` variable within the script as needed to track the version of your AutoArchiver tool.

### Usage

1. Run the `autoarch.py` script directly using Python:

    ```bash
    python autoarch.py
    ```

#### Setting Up Auto Start with Batch Script

To ensure AutoArchiver runs continuously, especially after system reboots, use the following batch script and place it in the startup folder:

```batch
:: This batch file is used to run the AutoArchiver script in a loop
:: It is used to keep the AutoArchiver running in the background
:: Make sure to change the path to the autoarch.py file to the correct path on your system

@echo off
:loop
python "C:\Development\Python Projects\AutoArchiver\autoarch.py"
goto loop
```

### Placing the Batch Script in the Startup Folder:

Save the above script as run_autoarch.bat.
Press ``Win + R``, type ``shell:startup``, and press ``Enter`` to open the Startup folder.
Move the ``run_autoarch.bat`` file to the Startup folder. This ensures that the 
script runs automatically every time the computer starts up.

## Contributing
We welcome contributions of all kinds from bug fixes to feature enhancements. Please feel free to create issues or pull requests on our repository.

# AutoArchiver To-Do List

## Functionality Enhancements

- [ ] **Implement Colorful Logging**
  - Integrate the `colorama` library for colorful console output, making logs more readable and engaging.

- [ ] **Expand File Selection Criteria**
  - Add functionality to include or exclude specific file types or directories from being archived.

- [ ] **Configuration via Command Line**
  - Enable users to configure archive settings directly through command-line arguments.

- [ ] **Logging to File and Console**
  - Ensure logs are written to both a file for record-keeping and the console for real-time feedback.

- [ ] **Error Handling and Notifications**
  - Improve error handling to manage permissions issues, missing directories, etc.
  - Implement desktop notifications for critical actions or errors.

## User Experience Improvements

- [ ] **Interactive Setup Process**
  - Create an interactive setup script that guides users through configuring the `.env` file and other settings.

- [ ] **Real-Time Progress Feedback**
  - Provide real-time feedback on the archiving process, including the number of files processed and time elapsed.

- [ ] **Version Update Notification**
  - Check for script updates on startup and notify the user of new versions available for download.

## Performance and Efficiency

- [ ] **Optimize Directory Scanning**
  - Implement more efficient directory scanning algorithms to handle large datasets.

- [ ] **Scheduled Archiving**
  - Instead of constant running, allow scheduling archive operations at less frequent intervals or specific times.

## Security and Reliability

- [x] **Secure Configuration Storage**
  - Encrypt sensitive information in the `.env` file, such as paths to critical directories.

- [ ] **Backup Before Archiving**
  - Offer an option to back up files before moving them to the archive, ensuring no data loss.

## Documentation and Community

- [ ] **Detailed User Documentation**
  - Create comprehensive user documentation, including setup, usage, and troubleshooting guides.

- [ ] **Community Engagement**
  - Establish a community forum or GitHub discussions for users to share tips, request features, and report bugs.

- [ ] **Contribution Guidelines**
  - Draft clear contribution guidelines to encourage and facilitate community contributions to the project.

