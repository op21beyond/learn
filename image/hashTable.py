import numpy as np
import scipy.ndimage.filters as filters

def hashTable(patch,Qangle,Qstrenth,Qcoherence):
    [gx,gy] = np.gradient(patch)
    
    W = np.zeros((9,9))
    W[4,4]=1.0    
    W = filters.gaussian_filter(W,sigma=1.0)
    gx = np.multiply(W,gx)
    gy = np.multiply(W,gy)
    
    G = np.matrix((gx.ravel(),gy.ravel())).T   
    x = np.matmul(G.T,G)
    [eigenvalues,eigenvectors] = np.linalg.eig(x)
    #print (eigenvalues)
    
    maxarg = np.argmax(eigenvalues)
    
    #For angle
    if (eigenvectors[0,0]==0.0):
        angle = 0.0
    else:
        angle = np.math.atan2(eigenvectors[maxarg,1],eigenvectors[maxarg,0])
        if angle<0:        
           angle += np.pi
    angle /= np.pi
    
    #For strength
    #strength = eigenvalues.max()/(eigenvalues.sum()+0.0001)
    #strength = np.tanh(eigenvalues.max())
    if (eigenvalues.max()==0.0):
        strength = 0.0
    else:
        strength = np.tanh(np.log(eigenvalues.max())/16.0)
    if (strength<0.0):
        strength = 0.0
    
    #For coherence
    lamda1 = np.math.sqrt(eigenvalues.max())
    lamda2 = np.math.sqrt(eigenvalues.min())
    if (lamda1==0.0 and lamda2==0.0):
        coherence = 0.0
    elif (lamda2==0.0):
        coherence = 0.9999
    else:
        coherence = np.abs((lamda1-lamda2)/(lamda1+lamda2))
    
    #Before Quantization
    pre_angle = angle
    pre_strength = strength
    pre_coherence = coherence
    
    #Quantization
    angle = np.floor(pre_angle*Qangle)
    strength = np.floor(pre_strength*Qstrenth)
    coherence = np.floor(pre_coherence*Qcoherence)
    
    return pre_angle, pre_strength, pre_coherence#, int(angle),int(strength),int(coherence)