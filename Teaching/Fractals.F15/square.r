# Code for Video in unit 3.3 of Fractals and Scaling
# http://www.complexityexplorer.org/online-courses/26-fractals-and-scaling
# Dave Feldman.  September 13, 2015
# I am not an R expert.  This probabily isn't the most beautiful bit of R,
# but it works.

# Designed to illustrate simple regression 

# Data from box-counting for a square of side 2
s <- c(0.50, 0.25, 0.125) #size of boxes
ls <- log(s)
Ns <- c(16, 62, 273) #N(s), number of boxes
lNs <- log(Ns)
plot(ls,lNs, xlab="log(s)", ylab="log(N(s))", main="N(s) vs. s for square of side 2",
     ylim=c(0,6), xlim=c(-2.5,0), pch=15, cex=2, col="blue",
     cex.lab=2,cex.main=2,cex.axis=1.5)
myline.fit <- lm(lNs~ls) #this is a linear model: lNs 'explained by' ls
# the variable myline.fit is now an object containing all sorts of
# information about the fit.
abline(myline.fit)
# adjust margins so the y-axis label fits
# I don't understand exactly how this works
mar.default <- c(5,4,4,2) + 0.1
par(mar = mar.default + c(0, 4, 0, 0)) 
grid(col = 'darkgray') # make grid
# print summary of linear regression
print(summary(myline.fit))