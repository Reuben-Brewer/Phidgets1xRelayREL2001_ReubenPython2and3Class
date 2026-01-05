# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com,
www.reubotics.com

Apache 2 License
Software Revision I, 01/02/2026

Verified working on: Python 3.12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#########################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
#########################################################

#########################################################
from MyPrint_ReubenPython2and3Class import *
from Phidgets1xRelayREL2001_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import traceback
import math
import keyboard
import collections
#########################################################

#########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global Phidgets1xRelayREL2001_Object
    global Phidgets1xRelayREL2001_OPEN_FLAG
    global SHOW_IN_GUI_Phidgets1xRelayREL2001_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:

        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if Phidgets1xRelayREL2001_OPEN_FLAG == 1 and SHOW_IN_GUI_Phidgets1xRelayREL2001_FLAG == 1:
                Phidgets1xRelayREL2001_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global Phidgets1xRelayREL2001_Object
    global Phidgets1xRelayREL2001_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_Phidgets1xRelayREL2001_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_Phidgets1xRelayREL2001
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_Phidgets1xRelayREL2001 = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_Phidgets1xRelayREL2001, text='   RELAY   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_Phidgets1xRelayREL2001 = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    if Phidgets1xRelayREL2001_OPEN_FLAG == 1:
        Phidgets1xRelayREL2001_Object.CreateGUIobjects(TkinterParent=Tab_Phidgets1xRelayREL2001)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    #################################################
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_Phidgets1xRelayREL2001_FLAG
    USE_Phidgets1xRelayREL2001_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1

    global USE_CycleThroughRelayStatesForTesting_FLAG
    USE_CycleThroughRelayStatesForTesting_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_Phidgets1xRelayREL2001_FLAG
    SHOW_IN_GUI_Phidgets1xRelayREL2001_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_Phidgets1xRelayREL2001
    global GUI_COLUMN_Phidgets1xRelayREL2001
    global GUI_PADX_Phidgets1xRelayREL2001
    global GUI_PADY_Phidgets1xRelayREL2001
    global GUI_ROWSPAN_Phidgets1xRelayREL2001
    global GUI_COLUMNSPAN_Phidgets1xRelayREL2001
    GUI_ROW_Phidgets1xRelayREL2001 = 1

    GUI_COLUMN_Phidgets1xRelayREL2001 = 0
    GUI_PADX_Phidgets1xRelayREL2001 = 1
    GUI_PADY_Phidgets1xRelayREL2001 = 1
    GUI_ROWSPAN_Phidgets1xRelayREL2001 = 1
    GUI_COLUMNSPAN_Phidgets1xRelayREL2001 = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_Phidgets1xRelayREL2001
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global CycleThroughRelayStatesForTesting_TimeBetweenStateFlips
    CycleThroughRelayStatesForTesting_TimeBetweenStateFlips = 1.0

    global CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread
    CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread = -11111.0

    global CycleThroughRelayStatesForTesting_RelayStateToBeSet
    CycleThroughRelayStatesForTesting_RelayStateToBeSet = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global Phidgets1xRelayREL2001_Object

    global Phidgets1xRelayREL2001_OPEN_FLAG
    Phidgets1xRelayREL2001_OPEN_FLAG = -1

    global Phidgets1xRelayREL2001_MostRecentDict
    Phidgets1xRelayREL2001_MostRecentDict = dict()

    global Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_State
    Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_State = [-1]*1

    global Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag
    Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag = [-1]*1

    global Phidgets1xRelayREL2001_MostRecentDict_Time
    Phidgets1xRelayREL2001_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global Phidgets1xRelayREL2001_GUIparametersDict
    Phidgets1xRelayREL2001_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_Phidgets1xRelayREL2001_FLAG),
                                                    ("EnableInternal_MyPrint_Flag", 0),
                                                    ("NumberOfPrintLines", 10),
                                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                                    ("GUI_ROW", GUI_ROW_Phidgets1xRelayREL2001),
                                                    ("GUI_COLUMN", GUI_COLUMN_Phidgets1xRelayREL2001),
                                                    ("GUI_PADX", GUI_PADX_Phidgets1xRelayREL2001),
                                                    ("GUI_PADY", GUI_PADY_Phidgets1xRelayREL2001),
                                                    ("GUI_ROWSPAN", GUI_ROWSPAN_Phidgets1xRelayREL2001),
                                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_Phidgets1xRelayREL2001)])

    global Phidgets1xRelayREL2001_SetupDict
    Phidgets1xRelayREL2001_SetupDict = dict([("GUIparametersDict", Phidgets1xRelayREL2001_GUIparametersDict),
                                               ("VINT_DesiredSerialNumber", -1), #-1 MEANS ANY SN, CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                               ("VINT_DesiredPortNumber", 0), #CHANGE THIS TO MATCH YOUR UNIQUE VINT
                                               ("DesiredDeviceID", 96),
                                               ("WaitForAttached_TimeoutDuration_Milliseconds", 5000),
                                               ("NameToDisplay_UserSet", "Reuben's Test 1xRelay REL2001_0"),
                                               ("UsePhidgetsLoggingInternalToThisClassObjectFlag", 1),
                                               ("MainThread_TimeToSleepEachLoop", 0.002)])

    if USE_Phidgets1xRelayREL2001_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            Phidgets1xRelayREL2001_Object = Phidgets1xRelayREL2001_ReubenPython2and3Class(Phidgets1xRelayREL2001_SetupDict)
            Phidgets1xRelayREL2001_OPEN_FLAG = Phidgets1xRelayREL2001_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("Phidgets1xRelayREL2001_Object __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################
    
    #################################################
    #################################################
    if USE_Phidgets1xRelayREL2001_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if Phidgets1xRelayREL2001_OPEN_FLAG != 1:
                print("Failed to open Phidgets1xRelayREL2001_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_GUIparametersDict
    MyPrint_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_SetupDict
    MyPrint_SetupDict = dict([("NumberOfPrintLines", 10),
                            ("WidthOfPrintingLabel", 200),
                            ("PrintToConsoleFlag", 1),
                            ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                            ("GUIparametersDict", MyPrint_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_Phidgets1xRelayREL2001 = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    print("Starting main loop 'test_program_for_Phidgets1xRelayREL2001_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        #################################################
        #################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        #################################################

        ################################################# GET's
        #################################################
        if Phidgets1xRelayREL2001_OPEN_FLAG == 1:

            Phidgets1xRelayREL2001_MostRecentDict = Phidgets1xRelayREL2001_Object.GetMostRecentDataDict()

            if "Time" in Phidgets1xRelayREL2001_MostRecentDict:
                Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_State = Phidgets1xRelayREL2001_MostRecentDict["DigitalOutputsList_State"]
                Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_ErrorCallbackFiredFlag = Phidgets1xRelayREL2001_MostRecentDict["DigitalOutputsList_ErrorCallbackFiredFlag"]
                Phidgets1xRelayREL2001_MostRecentDict_Time = Phidgets1xRelayREL2001_MostRecentDict["Time"]

                #print("Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_State: " + str(Phidgets1xRelayREL2001_MostRecentDict_DigitalOutputsList_State))
        #################################################
        #################################################

        ################################################# SET's
        #################################################
        if Phidgets1xRelayREL2001_OPEN_FLAG == 1:

            if USE_CycleThroughRelayStatesForTesting_FLAG == 1:

                if CurrentTime_MainLoopThread - CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread >= CycleThroughRelayStatesForTesting_TimeBetweenStateFlips:

                    Phidgets1xRelayREL2001_Object.SetRelayState(CycleThroughRelayStatesForTesting_RelayStateToBeSet)
                    CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread = CurrentTime_MainLoopThread
                    #print("CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread: " + str(CycleThroughRelayStatesForTesting_LastTimeOfStateFlip_MainLoopThread))

                    if CycleThroughRelayStatesForTesting_RelayStateToBeSet == 0:
                        CycleThroughRelayStatesForTesting_RelayStateToBeSet = 1

                    else:
                        CycleThroughRelayStatesForTesting_RelayStateToBeSet = 0

        #################################################
        #################################################

        time.sleep(0.002)

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################

    print("Exiting main program 'test_program_for_Phidgets1xRelayREL2001_ReubenPython2and3Class.")

    #################################################
    if Phidgets1xRelayREL2001_OPEN_FLAG == 1:
        Phidgets1xRelayREL2001_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################