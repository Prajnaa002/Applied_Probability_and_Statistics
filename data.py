def generate_linear_data(n=100):
    x = np.random.randn(n,2)
    y=(X[:,0] + X[:,1] > 0).astype(int)
    return x,y

# def generate_nonlinear_data(n=100,noise=0,1):
#     radius =  np.random.randn(n)
#     angle = 2 * np.pi * np.random.randn(n)

#     x1 = radius * np.cos(angle)
#     x2 = radius * np.sin(angle)

#     X = np.column_stack((x1,x2))
#     y = (radius > 0.5).astype(int)

#     X += noise * np.random.randn(n,2)
#     return X,y