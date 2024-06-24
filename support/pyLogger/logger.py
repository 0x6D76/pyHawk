"""
 * File: logger.py
 * Description: The main file that contains logger class, associated functions and members
 * Functions:
 *           Logger
 *              def Header ()
 *              def Footer ()
 *              def Log ()
 *           
 * Author: 0x6D76
 * Copyright (c) 2024 0x6D76 (0x6D76@proton.me)
"""
from tool import TOOL, VER, TAG
from utilities import (MAG, RST, COLOR_MAP, EXIT, GetCurrentTime)
from returnCodes import GetReturnMessages

LINE = "=" * 80
HALF_LINE = "=" * 40


class Logger :

    def __init__ (self, logFile, verbose = False) :
        """
        Instantiate a new object of Logger class.
        :param logFile: string holding the first of the log file
        :param verbose: bool indicating whether to print all the logs to the user (STDOUT) or not
        """
        self.logFile = logFile
        self.verbose = verbose
        self.message = ""

    def Header (self, identifier = "") :
        """
        Formats header line based on tool.py and logs it.
        :param identifier: string holding the identifier
        :return: None
        """
        first = f"{TOOL}"
        second = ""

        if VER :
            first += f" ({VER})"

        if TAG :
            second = f"{TAG.center (80)}"

        if len (second) <= 0 :
            head = f"{LINE}\n{MAG}{first.center (80)}{RST}\n{LINE}"
        else :
            head = f"{LINE}\n{MAG}{first.center (80)}{RST}\n{second}\n{LINE}"

        print (head)

        with open (self.logFile, 'a') as file :
            file.write (f"{LINE}\n{identifier.center (80)}\n{LINE}\n")

    def Footer (self) :
        """
        Formats footer line and logs it.
        :return: None
        """
        print (f"{LINE}\n{EXIT.center (80)}\n{LINE}")
        with open (self.logFile, 'a') as file :
            file.write (LINE)
            file.write ("\n")

    def Log (self, severity, module, rCode, user = False, optional = "") :
        """
        Formats the log message based on the args given and logs it.
        :param severity: string denoting the severity of the log message
        :param module: string denoting the name of the current module
        :param rCode: integer value denoting the return code of the operation to be logged
        :param user: bool value indicating whether to print the log message to STDOUT or not
        :param optional: string holding the optional message to be logged
        :return: None
        """
        color = COLOR_MAP.get (severity)
        message = GetReturnMessages (rCode)
        fileLog = f"{severity} [{GetCurrentTime ()}] [{module}] {message} {optional}"
        with open (self.logFile, 'a') as file :
            file.write (fileLog)
            file.write ("\n")

        if self.verbose is False and user is False :
            return

        userLog = f"{color}{severity}{RST} [{GetCurrentTime ()}] [{module}] {message} {optional}"
        print (userLog)
