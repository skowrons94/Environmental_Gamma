import numpy as np

class Histogram:
    def __init__( self ):
        self.data = { }
        self.read_histo( "lngs_unshielded"    )
        self.read_histo( "surface_unshielded" )
        self.read_xy(    "lngs_shielded"      )

    
    def read_histo( self, name ):
        with open( "data/" + name + ".txt", "r" ) as f:
            data = [ ]
            Lines = f.readlines( )
            for idx in range( len( Lines ) ):
                l = Lines[idx].split( )
                if( len( l ) > 0 ):
                    data.append( [idx,float(l[0])])
            self.data[name] = np.asarray( data )

    def read_xy( self, name ):
        with open( "data/" + name + ".txt", "r" ) as f:
            data = [ ]
            Lines = f.readlines( )
            for idx in range( len( Lines ) ):
                l = Lines[idx].split( )
                if( len( l ) > 0 ):
                    data.append( [float(l[0]),float(l[1])])
            self.data[name] = np.asarray( data )
