
function [F_even] = even(E) 
% This is the function that corresponds to the equation that
% arises from the EVEN condition when matching wavefunctions.
% F(E) = beta * cosine(alpha*a) - alpha * sine(alpha*a) 
% This is for a finite square well with DEPTH V0 and WIDTH 2A. 
% Mass is expressed in electron masses. 
% Energy is expressed in eV. 
% Distance is expressed in nanometers. 
%  
% Specify parameters: 
a    = 0.3; % in nm
V0   = 10; % in eV
Mass = 511000; % in eVc^2
% Specify constants:
hc = 1240; % in eVnm
% Evaluate the function and return. 
alpha  = sqrt( 8*pi^2*Mass*E./(hc^2) ); 
beta   = sqrt(8*pi^2*Mass*(V0-E)/(hc^2)); 
F_even = beta.*cos(alpha*a) - alpha.*sin(alpha*a); 
