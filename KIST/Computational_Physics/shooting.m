% Program to illustrate the shooting method for the infinite
% square well
%
% David Feldman
% 01 February 2012
%

% set the width of the well
a = 0.4;  %if you change this, you will also need to change the
% value of a in the function F.m

% Now we need to write the schrodinger equation as two first-order eqs
% S1' = S2
% S2' = -beta S1
% this is written in vector form: S' = F(S), where S is a vector,
% S = [S1, S2], and F is a vector-valued function of the vector S.
% The function F is defined in the file F.m

% set the limits for x
x0 = 0;
xf = a;

% now we call the ode solver
% note the initial conditions S1(0) = 0 and S2(0) = 1;
[X,S]=ode45('F',[x0,xf],[0,1]);

% this plots the first component of S, which is S1 = psi
% as a function of X
plot(X,S(:,1))

