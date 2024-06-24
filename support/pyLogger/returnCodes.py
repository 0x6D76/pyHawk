"""
 * File: returnCodes.py
 * Description: This file contains macros, return message dictionary and functions associated with log messages
 * Functions:
 *           def GetReturnMessages ()
 *           
 * Author: 0x6D76
 * Copyright (c) 2024 0x6D76 (0x6D76@proton.me)
"""
UNKNOWN = "Ran into an unknown error"

RETURN_MSGS = {
    -1 : "Keyboard interrupt received. Exiting the tool. ",
     1 : "Initialization successful.",
}


def GetReturnMessages (rCode):
    """
    Returns the message mapped to the given return code.
    :param rCode: integer denoting the return code
    :return: string holding the return message
             if rCode is found in RETURN_MSGS, returns the mapped message
             if rCode is not found in RETURN_MSGS, returns UNKNOWN
    """
    return RETURN_MSGS.get (rCode, UNKNOWN)
