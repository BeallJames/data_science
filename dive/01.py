def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return(location)

import matplotlib.pyplot as plt
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
xs2 = [.1,2]
ys2 = [ball_trajectory(.2),0]
xs3 = [.2,2]
ys3 = [ball_trajectory(.3),0]
xs4 = [.3,2]
ys4 = [ball_trajectory(.4),0]
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4)
plt.title('Ball Trajectory')
plt.xlabel('x label')
plt.ylabel('vert')
plt.axhline(y=0)
plt.show()