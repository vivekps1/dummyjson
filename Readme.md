
*** 
In order to create a virtual environments, the following packages needs to be installed 

* First python needs to be installed. To install a python, the following code needs to be run on the terminal 

` sudo apt install python3` 

* Also pip needs to be install on the terminal 

`sudo apt install pip`  

* After installing the python and pip, then the package for virtual environment needs to be installed. 

`sudo apt install python3-venv` 

* After installing the required packages, the user can directly create a virtual environment on desired location. To create the virtual environment, the following code needs to be run on the terminal 

`python3 -m venv virtual_env_name` 

* The user can then activate the environment by entering the code on the terminal 

`source virtual_env_name/bin/activate` 

* If the user wants to deactivate the virtual environment then user only needs to enter `deactivate` on the terminal 
***

If the user wants to check whether the package installed correctly, then just enter the package name on the terminal. After that `the command not found package_name` is appeared, then it likely the package is not installed
***
### Installing packages required to automation testing 

To install the requirements for automation testing including api, UI ...etc the user needs to first download the -------[requirement.txt](./requirement.txt "requirement.txt")

After downloading the file, the user should be run the following command on terminal to install all the packages listed on the requirement file 
`pip freeze > requirement.txt` 


### Creating and Saving important details on the environment files 

The user can create an .env file on the root of the project and store the **important variables** on the file. Remember when we are uploading our project to a github account, the env file will be ignored due to the security reasons. So only the informations like credentials...etc should be stored on the file. 

### Running the TestCases 

After setting up the project, now you can run the test files by opening up the terminal and typ the command  `pytest` 

Two markers are added in the test files. So if the user wants to run only the negative test cases then use the commands `pytest -m negative` same goes for the positive test cases also 

If the user wants a report then run the command `pytes --html=report.html` It will generate a report file in the root of the project. The user can give any name to the report


