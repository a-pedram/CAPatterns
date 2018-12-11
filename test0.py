import numpy as np
import matplotlib.pyplot as plt


space = np.zeros([200,200],dtype=int )
#space = np.random.randint(0,2,[100, 100])

#space[101,100] = 1
space[100,99] = 1
space[99,100] = 1
space[100,101] = 1



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
    
    for i in range(1,199):
        for j in range(1,199):
            s= np.sum(space[i-1:i+2,j-1:j+2])
            if space[i,j]== 0 :                
                if s>2 and s<7 :
                    t[i,j]=1
            else:
                if s >7 :
                    t[i,j] =0
    print(r)    
    space=t.copy()
    
    img.set_data(space)    
    #
    plt.pause(0.8)
    #input()
input()
