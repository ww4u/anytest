
from mrq.sinanju import Sinanju 
import sys 
import win_unicode_console
import math 

# loop a-b-a
# dotB = (t,x,y,z)
# asure cuurent at dotA
def testSample( logFile, robo, dotA, dotB, loopCnt ):

    dataSets = list()
    dataSets.append( dotA )
    dataSets.append( dotB )

    dotC = list()
    dotC.append( dotB[0] * 2 )
    dotC.extend( dotA[1:4] )
    dataSets.append( tuple( dotC) )

    fileName = sys.path[0] + "/local_datasets.mrp"
    robo.writeDataset( fileName, "t,x,y,z", dataSets )

    robo.program( 0,0, fileName )
    robo.waitEnd( 0,0 )

    logFile.write( "\"{}\"\n".format( dotA[1:4] ) )

    distSum = 0
    distMax = -math.inf 
    distMin = math.inf 

    for i in range( loopCnt ):
        robo.call( 0,0 )
        robo.waitIdle( 0,0 )
        posNow = robo.pose()
        dist = robo.eulaDistance( dotA[1:4], posNow  )
        logFile.write( "%d, \"%s\",%g,\n" % ( i, "{}".format(posNow), dist ) )
        # print( "%d, \"%s\",%g,\n" % ( i, "{}".format(posNow), dist ) )    

        distSum += dist 
        distMax = max( distMax, dist )
        distMin = min( distMin, dist )   

    return ( distMax - distMin, distSum / loopCnt, distMax, distMin )                 

def buildTDot( robo, dotA, dotB, v=100.0 ):
    dist = robo.eulaDistance( dotA, dotB )
    t = int((dist / v + 0.49)/0.5) * 0.5

    a = list()
    b = list()

    a.append( 0 )
    a.extend( dotA )

    b.append( t )
    b.extend( dotB )

    return ( tuple(a), tuple(b) )

def testProc( logFile, dot  ):
    
    robo = Sinanju("MRX-T4")

    testOrigin = (250,0,512)
    # testDots = ( (100,100,600), )    
    testDots = ( dot, )
    loopCnt = 500

    for subDot in testDots:
        robo.center()
        robo.waitIdle()

        robo.routeTo( subDot )
        robo.waitIdle( )

        dataSets = buildTDot( robo, subDot, testOrigin )

        ret = testSample( logFile, robo, dataSets[0], dataSets[1], loopCnt )  

        print( ret )

