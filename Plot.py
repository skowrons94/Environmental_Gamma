import numpy as np
import matplotlib.pyplot as plt

backRange = 20

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

def calculate_background( idx, data, fLow ):
    back = 0
    for i in range( backRange ):
        if( fLow ):
            back += data[idx-i]
        else:
            back += data[idx+i]
    return back / backRange

def create_background( data, intMin, intMax ):
    try:
        ax = plt.gca()
        ax.lines[2].remove( )
        ax.lines[1].remove( )
    except:
        pass
    idxMin = np.abs(data[:,0] - intMin).argmin()
    idxMax = np.abs(data[:,0] - intMax).argmin()
    backMin = calculate_background( idxMin, data[:,1], True )
    backMax = calculate_background( idxMax, data[:,1], False )
    m = (backMin - backMax)/(data[idxMin][0] - data[idxMax][0])
    q = backMin - m*data[idxMin][0]
    line = [ ]
    for idx in range( idxMax - idxMin ):
        back = m*data[idxMin+idx][0] + q
        line.append( [data[idxMin+idx][0],back])
    line = np.asarray( line )
    plt.plot( line[:,0], line[:,1], color='tab:red' )
    integral = 0
    for idx in range( idxMin, idxMax ):
        integral += data[idx][1]
    back = (m*data[idxMin][0] + q + m*data[idxMax][0] + q)*(data[idxMax][0] - data[idxMin][0])/2
    counts = integral - back
    return counts, integral

def create_roi( data, intMin, intMax ):
    idxMin = np.abs(data[:,0] - intMin).argmin()
    idxMax = np.abs(data[:,0] - intMax).argmin()
    plt.step( data[idxMin:idxMax,0], data[idxMin:idxMax,1], color='tab:green' )

def create_plot( data, scale, intMin, intMax ):

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)

    line, = ax.step( data[:,0], data[:,1], linewidth=2, color='tab:blue', label="Istogramma" )

    if( scale == 'Logaritmica' ):
        ax.set_yscale('log')
    else:
        ax.set_yscale('linear')
        plt.gca().set_ylim(bottom=0)

    ax.set_xlim( [0,7500] )

    plt.xlabel('Energia del raggio gamma', fontsize=20)
    plt.ylabel("Conteggi all'ora",     fontsize=20)

    plt.tight_layout( )
    plt.show( )