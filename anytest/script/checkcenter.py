from mrq.MRQ import MRQ 
from mrq.sinanju import Sinanju
import sys 

# import testcommon
from testcommon import *

# test config
_testOrigin = (200,100,400)
_dutOrigin = (250,0,512)
_err = 50

def dutZero( robo ):
    """
    test the dut zero
    """
    dstPt = _testOrigin
    robo.routeTo( dstPt )
    robo.waitIdle( )

    # check pos
    nowPos = robo.pose( )
    dist = robo.eulaDistance( dstPt, nowPos )
    if ( dist > _err ):
        print( "fail", "dst:{}".format(dstPt), "now:{}".format( nowPos) )
        failTest()

    # center
    robo.center( )        
    robo.waitIdle()

    nowPos = robo.pose( )
    dist = robo.eulaDistance( _dutOrigin, nowPos )
    if ( dist > _err ):
        print( "fail" )
        failTest()

def jointZero( robo, dev, jId ):
    
    robo.routeTo( _testOrigin )
    robo.waitIdle( )
    robo.assertPos( _testOrigin, err = _err )

    # for the joint 
    robo.jCenter( jId = jId )
    # robo.waitIdle()
    dev.waitIdle( jId )

    # check the angle
    zAngle = dev.zeroAngle( jId )

    nAngle = dev.absAngle( jId )

    print( "zero:%g,now:%g" % (zAngle, nAngle) )
    if ( abs( zAngle - nAngle ) > 1 ):
        failTest()       

# dutZero
# jId
if __name__=="__main__":
    # print( sys.argv[1] )    # cmd 
    # print( sys.argv )
        
    # create the robo
    robo = Sinanju('MRX-T4')
    dev = MRQ("device1")
    print( "@enter\n" )
    if ( len(sys.argv) == 1 ):
        dutZero( robo ) 
    elif ( len(sys.argv) == 2 ):
        jointZero( robo, dev, int( sys.argv[1] )  )          
    else:
        failTest()            

    print( "@completed\n" )        

    # dutZero( robo )

    # for i in range( 4 ):
    #     jointZero( robo, dev, i )