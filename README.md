# 6882demos
6.882 Spring 2016 demos

For the stick-breaking demo, you can run it in the following way:
`python stick_break.py 1 1`
The first argument is alpha, and  the second argument is the number of seconds between displaying another stick break:
`python stick_break.py [alpha] [sec_wait]`

For the DPMM demo, you can run it in the following way:
`python demo.py 1 100 1 0.05`
The first argument is alpha. The second argument is the variance of the base distribution (centered at (0,0), cov is sigma1*I). The third argument is the variance of each component distribution (centered at mu sampled from H, cov is sigma2*I). The last argument is the seconds between new data points.
`python demo.py [alpha] [sigma1] [sigma2] [sec_wait]`
