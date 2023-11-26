# ADT-Nicaragua
The github repository of the ADT project in Nicaragua.

**Description**
This is the project folder for the ADT (accessible digital textbooks) initiative in Nicaragua. The project includes an app shell or 'bookshelf' that displays all the available and downloaded ADTs. Each ADT is like a digital book with added functionality for accessibility including, read aloud, sign language video, image descriptions, screen reader support, and accessible navigation. Currently there are two ADTs available.

**Getting Started**
Prerequisites
- Ensure you have Flutter installed on your machine.
- A Windows environment is necessary to run the Windows executable.
- Git for cloning the repository.

**Installation
**Clone the repository:

bash
Copy code
git clone [URL of your Git repository]
cd [repository name]
Check for any Flutter setup issues:

Run flutter doctor to ensure Flutter is correctly installed and no issues are present.

Get Flutter dependencies:

bash
Copy code
flutter pub get
Run the application:

For development purposes, you can run the application using:

bash
Copy code
flutter run -d windows
To build and run the executable:

bash
Copy code
flutter build windows
This will generate an executable in the build\windows\runner\Release directory.

Running the Executable
Navigate to the build\windows\runner\Release directory.
Run the .exe file to start the application.
Known Issues and Troubleshooting
If you encounter any DLL-related issues, ensure that all necessary DLL files are present in the executable directory.
For any issues related to Flutter dependencies, run flutter pub get to fetch the latest versions of the dependencies.
Contributing
[Provide instructions for how others can contribute to your project.]

License
[Specify the license under which your project is released.]

