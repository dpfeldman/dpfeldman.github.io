function [ ] = euler(f,trange,y0,n)
% this code is based on a program written by Todd Young
% and downloaded from http://www.math.ohiou.edu/courses/matlab/
% modified by David Feldman.  28 December 2011
% for use in the Computational Physics class at KIST.
% This function determine approximate solutions to the 
% differential equation y' = f(t,y) with initial condition y(a) = y0
% on the interval [a,b] using n steps of Euler's method.

% **************** Initialze some Variables ***************
a = trange(1); % a is the starting t value
b = trange(2); % b is the ending t value
Delta_T = (b-a)/n;        % step size
t = a; y = y0;      % t and y are the current variables
T = a; Y = y0';      % T and Y will record all steps
% ***************** Begin Main Euler Loop *****************
for i = 1:n
    y = y + Delta_T*f(t,y); % the main Euler step
    t = a + i*Delta_T; % increase the value of t by Delta_t
    T = [T; t];
    Y = [Y; y'];
end
% plot the solution
plot(T,Y)
title('solution using Euler method')
xlabel('t')
ylabel('y(t)')
% display the numerical values:
% comment the below lines if you do not want to see 
% the numerical values that matlab computed
printf("\nt \t\ty(t)\n")
for i = 1:n+1
    printf("%f\t%f\n",T(i),Y(i))
end

% USAGE
% To use this you will need to specify the function f(y,t).
% Do so via the inline function command.  Let f be the name
% of the function.  Then, type the command:
%               myeuler(f, trange,y0,n)
% trange is the range of t values.  If you wanted the solve the equation
% starting at 3 and ending at 5, trange = [3,5].  
% y0 is the initial value.  It is the value of y(t) when t is the first
% value in trange.  
% n is the number of steps.  matlab then computes the step size delta t.

% OTHER TECHNICAL NOTES
% y must be a column vector and f must produce column vectors
% The dimension of y0 must match that of y and f
% T will be a n+1 column vector contianing the times
% Y will be a (n+1) by d matrix where d is the length of y