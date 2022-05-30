# Odyssee_Sensorielle

Running order : 
* timestamps_to_df.ipynb # organize timestamps in one easily indexable dataframe
* raw_to_da.ipynb # put data in one xarray by participant, easily indexable
* preproc.ipynb # preprocess the data = down sample + clean + cut data and put in one xarray for every participants, easily indexable
* data_to_metrcs.ipynb # read signals and make metrics ready for statistics
* stats.ipynb # make statistics and plots with room as a predictor, and metrics as outcomes


Notes : 

* Participants 4,5,6,9,13,18 have problems of room duration in one or several rooms (duration too short for metrics)
* Participant 14 have curious problem : " data = np.loadtxt(input_file).T : ValueError: Wrong number of columns at line 869012 "
* Participant 3 and 12 have mismatch between data recording duration and timestamps (recording duration is shorter than timestamp of last room)

Visual inspection of quality / usability: 0 = Unusable, 1 = Medium , 2 = Ok
cf df
ECG = more usable, 
EDA and EEG = difficult ...
PPG = bad ++





