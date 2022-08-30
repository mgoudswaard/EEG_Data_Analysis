% Function to plit a spider diagram of TRP values, requires the package 
% https://github.com/NewGuy012/spider_plot, spider_plot_R2019b.m must be 
% in matlab path. Labels can be adjusted accordingly. Label order is in
% order of columns in input TRP vectors.
% 

function Plot_TRP(TRP1, TRP2, varargin)

    defaultName1 = '';
    defaultName2 = '';

    p = inputParser;
    addRequired(p,'TRP1');
    addRequired(p,'TRP2');
    addOptional(p,'Name1', defaultName1, @isstring);
    addOptional(p,'Name2', defaultName2, @isstring);

    parse(p,TRP1,TRP2,varargin{:})


    TRP_Vec = [p.Results.TRP1; p.Results.TRP2];
    Label1 = p.Results.Name1;
    Label2 = p.Results.Name2;

    labels = {'Fz', 'F4', 'F8', 'C4',...
          'T8', 'P4', 'P8', 'O2',...
          'O1', 'P7', 'P3', 'T7',...
          'C3', 'F7', 'F3', 'Fpz'};

    axes_limits = zeros(2,16);
    axes_limits(1,:) = min(TRP_Vec,[],'all') - 0.1;
    axes_limits(2,:) = max(TRP_Vec, [], 'all') + 0.1;
    
    axes_shaded_limits = 0.9 * axes_limits;
    
    spider_plot_R2019b(TRP_Vec, 'AxesLimits', axes_limits, 'AxesShadedLimits', axes_shaded_limits, 'AxesLabels', labels);
    
    if ~isempty(Label1) | ~isempty(Label2)
        legend(Label1, Label2, 'Location', 'southoutside');
    end
    
        
