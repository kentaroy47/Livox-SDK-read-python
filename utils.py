import struct
import numpy as np
import math
import pptk
import os
import time

def LivoxFileRead(ReadFileName):
    # Input: Read File Name
    # Output: [y,z,x,distance(r),Lidar ID]
    
    Idx = 28
    rf = open(ReadFileName, 'rb')
    d = rf.read()
    #print(d[0:16].decode())
    FSIZE = len(d)
    DeviceCount = d[Idx]
    Idx += 1
    #print("LidarSN", d[Idx:Idx+16].decode())
    
    Idx = Idx + 59 * DeviceCount
    list1 = []
    
    #print("Device", DeviceCount)
    
    #print("Fsize", FSIZE)
    end = 0
    
    while (Idx < FSIZE) :

        nxt = int.from_bytes(d[Idx+8:(Idx+16)],'little')
               
        Idx = Idx + 24
        
        while Idx < nxt:            
            # print("Idx", Idx)
            #print("ID:", d[Idx+3])
            dtype = d[Idx+10]
            # print("data type:", d[Idx+10])
            #time.sleep(1)
            Idx = Idx + 19
            
            if dtype==6:
                Idx = Idx + 24
            elif dtype==2:
                for i in range(96):
                    
                    B2D_X = int.from_bytes(d[Idx:Idx+4],'little', signed=True)
                    B2D_Y = int.from_bytes(d[Idx+4:Idx+8],'little', signed=True)
                    B2D_Z = int.from_bytes(d[Idx+8:Idx+12],'little', signed=True)
                    # print(B2D_X)
                    list_tmp = ([B2D_Y, 
                                 B2D_Z,
                                 B2D_X,
                                 d[Idx+12]
                                 ])
                    if not B2D_X+B2D_Y+B2D_Z==0 and B2D_X+B2D_Y+B2D_Z<1e6:
                        list1.append(list_tmp)
                    Idx = Idx + 14
            else:
                print("dtype",dtype)
                
    rf.close
    OutData = np.array(list1)
    return OutData