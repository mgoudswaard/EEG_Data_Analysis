%Pow_calc - Adam McClenaghan 16/08/2022
%This function calculates the POW for each electrode in the input date. 
% POW is the log of the mean square voltage across the period of interest.

%INPUTS
%Required: signals, an array of signals, one column per electrode
%Opional : 'Start', Start of period of interes in seconds (default is 1)
%          'End', End of period of interest in seconds (defualt is end of
%          signals.
%          'fs', sampling frequency of data in Hz (default is 125Hz)
%
%OUTPUTS
%           Norm_POW, an array of the POW of each electrode
           


function [norm_POW] = POW_calc(signals,varargin)
    % Parse input 

    defaultStart = 1;
    defaultEnd  = (size(signals,1)) - 1;
    defaultFs = 125;

    p = inputParser;
    validScalarPosNum = @(x) isnumeric(x) && isscalar(x) && (x > 0);
    validEndTime = @(x) isnumeric(x) && isscalar(x) && (x > 0) && (x < defaultEnd) ;
    addRequired(p,'signals');
    addOptional(p, 'fs', defaultFs, validScalarPosNum);
    addOptional(p, 'Start', defaultStart, validScalarPosNum);
    addOptional(p, 'End', defaultEnd, validEndTime);

    parse(p,signals,varargin{:})

    %% Calculation of POW across all electrodes
    
    sample_rate = p.Results.fs;
    
    if p.Results.Start == 1
        trial_secs = (p.Results.End/sample_rate);
    else 
        trial_secs = (p.Results.End/sample_rate - p.Results.Start/sample_rate);
    end

    trial = signals(p.Results.Start : p.Results.End, :);
    
     
    trial_uVs = [];
    for i=1:trial_secs
        jump = (i-1)*sample_rate;
        uVs = sum(trial(1+jump:1+jump+sample_rate,:));
        trial_uVs = [trial_uVs; uVs];
    end
    squared_trial = trial_uVs.^2;
    mean_trial = mean(squared_trial);
    norm_trial = log(mean_trial);
    
    norm_POW = norm_trial;
    
    end