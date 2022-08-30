function TRP =  TRP_calc(Data, Participant_names, Participant_number, Task_one, Task_two)

%Parse input
p = inputParser;
validStrings = {'Resting', 'Digital_task', 'Digital_familiarisation', 'Physical_task', 'Physical_familiarisation'};
validScalarPosNum = @(x) isnumeric(x) && isscalar(x) && (x > 0);
validTask = @(x) any(validatestring(x,validStrings)); % EXTEND SO THAT INPUT MUST BE ONE OF A SET OF VALID TASK NAMES
% validNames = ; % EXTENND TO INCLUDE MUST BE CELL ARRAY
addRequired(p,'Data');
addRequired(p, 'Participant_names')
addRequired(p,'Participant_number', validScalarPosNum);
addRequired(p,'Task_one', validTask);
addRequired(p,'Task_two', validTask);

parse(p,Data,Participant_names, Participant_number, Task_one, Task_two)

%% Calculate TRP

partip_num = p.Results.Participant_number;
partip_names = p.Results.Participant_names;

Data = p.Results.Data;
Task_name_1 = p.Results.Task_one;
Task_name_2 = p.Results.Task_two;

TRP_1 = POW_calc(Data.(partip_names{partip_num}).Raw_data.(Task_name_1));
TRP_2 = POW_calc(Data.(partip_names{partip_num}).Raw_data.(Task_name_2));

TRP = TRP_1 - TRP_2;


