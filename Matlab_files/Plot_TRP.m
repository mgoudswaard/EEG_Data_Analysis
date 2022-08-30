% Function to plit a spider diagram of TRP values, requires the package 
% https://github.com/NewGuy012/spider_plot, spider_plot_R2019b.m must be 
% in matlab path. Labels can be adjusted accordingly. Label order is in
% order of columns in input TRP vectors.
% 

function Plot_TRP(TRP1, TRP2)

    P = [TRP1; TRP2];

    labels = {'Fz', 'F4', 'F8', 'C4',...
          'T8', 'P4', 'P8', 'O2',...
          'O1', 'P7', 'P3', 'T7',...
          'C3', 'F7', 'F3', 'Fpz'};

    axes_limits = zeros(2,16);
    axes_limits(1,:) = min(P,[],'all') - 0.1;
    axes_limits(2,:) = max(P, [], 'all') + 0.1;
    
    axes_shaded_limits = 0.9 * axes_limits;
    
    spider_plot_R2019b(P, 'AxesLimits', axes_limits, 'AxesShadedLimits', axes_shaded_limits, 'AxesLabels', labels);
        