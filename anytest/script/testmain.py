import time 
import sys
import os
import math 

import win_unicode_console

import t4accuracy 

if __name__=="__main__":
    # file 
    logPath = sys.path[0] + "/data"

    # filename
    fileName = time.strftime('%Y-%m-%d %H-%M-%S.csv',time.localtime(time.time()))
    logFileName = logPath + "/" + fileName
    if os.path.exists(logPath):
        pass 
    else:
        os.mkdir(logPath)

    logFile = open( logFileName, "w" )

    # remote 
    if ( len(sys.argv ) > 1 ):
        pass 
    else:
        # comment = input( "please input the comment:")
        comment = "\"{}\"".format( sys.argv )
        logFile.write( comment + "\n" )
       
    print("@enter\n")            
    # iqcProc( logFile )

    # roboProc( logFile )

    # accuracy
    # x,y,z
    if ( sys.argv[1] == 'accuracy' ):
        print( sys.argv )
        dot = ( float(sys.argv[2]),float( sys.argv[3] ), float( sys.argv[4] ) )
        t4accuracy.testProc( logFile, dot )

    print("@completed\n")            

    logFile.write( "completed\n" )

    logFile.close()

    print( "File save at", logFileName )