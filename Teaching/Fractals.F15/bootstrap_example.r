# A linear regression example where bootstrappign is used to estimate errors.
# Based on an "Lab 14" from some USNA course.  
# The syllabus for the course is at: http://www.usna.edu/Users/math/jager/courses/sm439/
# This is not the most efficient or fastest way to bootstrap.
# But I think it's reasonably clear code that illustrates what bootstrapping is.  

# Read in the data from the file 'GPafull.txt'
dat = read.table("./GPAfull.txt",header=TRUE)

# look at the data
plot(dat$SAT,dat$CollGPA,
     xlab="SAT Score", ylab="College GPA")
r = lm(dat$CollGPA ~ dat$SAT)
abline(r)

# let's also make a few histograms:
hist(dat$CollGPA,xlab="College GPA",main="Histogram of College GPAs")

slope = r$coeff[2] # this extracts the slope from the linear model.  

# Set up for bootstraping....
N_B = 2000 #number of bootstrap samples.
slope_bootstraps = rep(NA,N_B) # Empty list that will hold the bootstrape slopes
index = 1:length(dat$CollGPA) # List of integers from 1 to 100.

# Now bootstrap
for (i in 1:N_B){
  bootindex = sample(index,length(dat$SAT),replace=T)
  bootsample = dat[bootindex,] # this is the bootindex_th row of dat
  # i.e., dat[15, ] is the 15th row of dat.
  slope_bootstraps[i] = lm(bootsample$CollGPA~ bootsample$SAT)$coeff[2]
}

cat("The regression slope is: ")
cat(slope)
cat(" (")
cat(slope - 1.96*summary(r)$coeff[2,2])
cat(", ")
cat(slope + 1.96*summary(r)$coeff[2,2])
cat(").\n")
cat("\n\n")

# NOTE that to get a 95% confidence interval we need to do
# +- 1.96 times the standard errors.  The standard error is
# what's given by coeff[2,2] from lm.

hist(slope_bootstraps) #plot histogram

slope_distribution = ecdf(slope_bootstraps) #ecdf is empirical cumulative distribution function
plot(slope_distribution,main="cdf for bootstrapped slopes")


# get quantiles so we can get confidence intervals
lower = quantile(slope_bootstraps, 0.025)
upper = quantile(slope_bootstraps, 0.975)

cat("The bootstrapped slope estimate is: ")
cat(mean(slope_bootstraps))
cat(" ( ")
cat(lower)
cat(", ")
cat(upper)
cat(").\n")


