import numpy as np
import matplotlib.pyplot as plt


space = np.zeros([400,400] )
#space = np.random.randint(0,2,[100, 100])

space[200,199] = 1
space[200,201] = 1
space[199,200] = 1
space[201,200] = 1



def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()

# Fixing random state for reproducibility
np.random.seed(19680801)


fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)


img= plt.imshow(space)
t = space.copy()
for r in range(150):
    
    for i in range(1,398):
        for j in range(1,398):
            s= np.sum(np.int16(space[i-2:i+3,j-2:j+3]>0))
            if space[i,j]== 0 :                
                if s>2 and s<6 :
                    t[i,j]=1
            else:
                if  s >=0 :
                    t[i,j] -= s/25
                if t[i,j] < 0.1:
                    t[i,j] = 0
                    
					
    print(r)    
    space=t.copy()
    
    img.set_data(space)    
    plt.pause(0.9)
    
    
    

input()

