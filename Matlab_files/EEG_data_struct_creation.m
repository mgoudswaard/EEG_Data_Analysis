clear
clc

% This script will take all of the trimmed EEG data and sort it into a
% struct. The EEG data names must be in the form P1_Dig(Phys)_Des(Fam) or
% P1_Resting. The directory containing all the files does not have to be in
% matlab path, but if not, the full path must be called for 'file'.

%Outputs in the 'Data' struct will be callable in dot notation, ie to
%access the processed Resting data for participant 3, call
%Data.Participant3.Processed_data.Resting . 

%% Creating the structure for the data
% Create cell of participant names
Num_participants = 12;
participant_numbers = 1:1:Num_participants;
Participant_names = cell(1,length(participant_numbers));

for i = 1:Num_participants
    Participant_names{i} = sprintf('Participant%d',participant_numbers(i));
end

file = dir("EEG_Internship_2022/Trimmed_Data/*.csv"); %get all csv files in directory
num_files = length(file);
file_names = sort({file.name});%return file_names list of all csv files


Data = struct; % Create empty dtructure to store data in

for i = 1:Num_participants

    Data.(Participant_names{i}).Raw_data = struct('Resting', [], 'Digital_familiarisation', [], 'Digital_task', [], 'Physical_familiarisation', [], 'Physical_task', []);
    Data.(Participant_names{i}).Processed_data = struct('Resting', [], 'Digital_familiarisation', [], 'Digital_task', [], 'Physical_familiarisation', [], 'Physical_task', []);

end

%% Reading data and parsing file name to decide where to put it


for a = 1:length(file_names)
  
    opts = detectImportOptions(file_names{a},'NumHeaderLines',1); % Options for excluding header from CSV file
    current_table = (readtable(file_names{a},opts));
    current_data = table2array(current_table(:,2:17));

    str = file_names{a};
    current_partip_num = sscanf(str,'P%d');
     
    
        if contains(str, 'Resting')
            Data.(Participant_names{current_partip_num}).Raw_data.Resting = current_data;
        elseif contains(str, 'Dig_Des') 
            Data.(Participant_names{current_partip_num}).Raw_data.Digital_task = current_data;
        elseif contains(str, 'Dig_Fam') 
            Data.(Participant_names{current_partip_num}).Raw_data.Digital_familiarisation = current_data;
        elseif contains(str,'Phys_Fam') 
            Data.(Participant_names{current_partip_num}).Raw_data.Physical_familiarisation = current_data;
        elseif contains(str,'Phys_Des') 
            Data.(Participant_names{current_partip_num}).Raw_data.Physical_task = current_data;
        end
        
end


