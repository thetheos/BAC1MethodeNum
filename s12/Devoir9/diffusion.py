from numpy import *
 
def diffusion(T,beta,nt):
    for i in range(nt):
        short_T = T[1:-1,1:-1]
        T_ip1 = T[2:,1:-1]
        T_im1 = T[0:-2,1:-1]
        T_jp1 = T[1:-1,2:]
        T_jm1 = T[1:-1,:-2]
        T[1:-1,1:-1] = short_T + beta * (T_ip1 + T_im1 + T_jp1 + T_jm1 - 4* short_T)
    return T
 
# =========================================================================
 
 
def diffusionSmart(T,beta,nt):
    l,c = T.shape
    T_jm1 = empty((l-2,c-1))
    for i in range(nt):
        short_T = T[1:-1,:-1]
        T_ip1 = T[2:,:-1]
        T_im1 = T[0:-2,:-1]
        T_jp1 = T[1:-1,1:]
        T_jm1[:,1:] = T[1:-1,:-2]  #On utilise la symetry tq: T_jm1[0] = T_jm1[2]
        T_jm1[:,0] = T_jm1[:,2]
        T[1:-1,:-1] = short_T + beta * (T_ip1 + T_im1 + T_jp1 + T_jm1 - 4* short_T)
    return T