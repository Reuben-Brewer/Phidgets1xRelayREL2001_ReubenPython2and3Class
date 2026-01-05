########################

Phidgets1xRelayREL2001_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) to control Phidgets 1-relay controller REL2001 (VINT).
Under the hood, the REL2001 (as well as other relay Phidgets) are simply controlling Phidget's DigitalOutput() objects,
so this same code can control other single-DigitalOutput Phidget devices like the
Power Plug Phidget (ID: PSU1000_0, https://www.phidgets.com/?tier=3&catid=46&pcid=39&prodid=1142).

From Phidgets' website:
"The REL2002 is a simple, easy to use, mechanical relay.
This Phidget connects to your computer through a VINT Hub.
Rated for 210W of DC power or 1750 VA of AC power.
DC applications - switch a circuit of up to 30V at 7A.
AC applications - switch up to 12A or 277V AC, as long as the total power doesn't exceed 1750 VA.
Isolation - A voltage spike on the load side of the relay will not damage the control side."

Relay Phidget

ID: REL2001_0

https://phidgets.com/?tier=3&catid=46&pcid=39&prodid=722

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision I, 01/02/2026

Verified working on:

Python 3.11/12.

Windows 10/11 64-bit

Raspberry Pi Bookworm

(no Mac testing yet)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

########################  

######################## Python module installation instructions, all OS's

Phidgets1xRelayREL2001_ReubenPython2and3Class, ListOfModuleDependencies: ['Phidget22', 'ReubenGithubCodeModulePaths']

Phidgets1xRelayREL2001_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPrint_ReubenPython2and3Class', 'ReubenGithubCodeModulePaths']

Phidgets1xRelayREL2001_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: []

Phidgets1xRelayREL2001_ReubenPython2and3Class, ListOfModuleDependencies_All:['MyPrint_ReubenPython2and3Class', 'Phidget22', 'ReubenGithubCodeModulePaths']

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:

pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -

sudo apt-get install -y libphidget22
 
###########################
