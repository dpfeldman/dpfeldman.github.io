function dS = F(t,S)
% 
% this is the function for the right hand side of the 
% schrodinger equation for the infinite square well
% note that beta is an input to the function in addition
% to S1 and 

% **************************************************
% Energy of the particle 
% You will need to experiment with this as "shoot"
E = 2.000;  % energy in eV
% **************************************************

m = 2*511000; % mass of the particle in eV
a = 0.4; % width of the well in nm
hc = 1240; %hc = 1240 eV.nm
% NOTE:  this is for a well that goes from 0 to a
beta = sqrt( 8*pi*pi*m*E/(hc)^2);

S1=S(1);
S2=S(2);
dS1 = S2;
dS2 = -beta*beta*S1;
% collect the derivatives into a column vector
dS = [dS1;dS2];

