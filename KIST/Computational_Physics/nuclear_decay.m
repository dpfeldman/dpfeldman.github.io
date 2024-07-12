% This program simulates nuclear decay
% David Feldman.  9 February 2012
%
lambda = 0.167; %decay rate
N_new = 8; %initial number of particles
N_old = N_new; % during each timestep we start with N_old particles.
% At the end of the timestep, we have N_new particles left

N = N_new; % N is vector that stores N for each timestep
T = 0; % vector that holds the times

% loop for many time steps
for t = 1:10
    %check each particle to see if it decays during this timestep
    %every particle has a probability lambda of decaying each step
  for n = 1:N_old
    if(rand()<lambda)
      N_new = N_new - 1; % particle decays, so number decreases
    end
  end
  T = [T; t]; % add current time to list of times
  N = [N; N_new]; % add current N to list of Ns
  N_old = N_new;  %set the old N equal to the new N
end

plot(T,N)

