function [F_odd] = odd(E) 
% This is the function that corresponds to the equation that
% arises from the EVEN condition when matching wavefunctions.
% F(E) = beta * cosine(alpha*a) - alpha * sine(alpha*a) 
% This is for a finite square well with DEPTH V0 and WIDTH 2A. 
% Mass is expressed in electron masses. 
% Energy is expressed in eV. 
% Distance is expressed in nanometers. 
%  
% Written by David Feldman.  21 Dec 2011
% for Computational Physics class at KIST
%
% Specify constants: 
a    = 0.3; % in nm
V0   = 20; % in eV
Mass = 511000; % in eVc^2
%
hc = 1240; % in eVnm
% Evaluate the function and return. 
alpha  = sqrt(8*pi^2*Mass*E./(hc^2)); 
beta   = sqrt(8*pi^2*Mass*(V0-E)/(hc^2)); 
F_odd  = beta.*sin(alpha*a) + alpha.*sin(alpha*a); 
