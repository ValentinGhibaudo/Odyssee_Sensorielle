# Odyssee_Sensorielle

Running order : 
* timestamps_to_df.ipynb # organize timestamps in one easily indexable dataframe
* raw_to_da.ipynb # put data in one xarray by participant, easily indexable
* preproc.ipynb # preprocess the data = down sample + clean + cut data and put in one xarray for every participants, easily indexable
* data_to_metrics.ipynb # read signals and make metrics ready for statistics
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

Mes conclusions : 
- La PPG est inutilisable

Pour l'analyse détaillée par salle:
- L'EEG ne rend pas de différence statistique quelque soit la bande de fréquence
- L'EDA est peu utilisable et ne rend pas de différence statistique
- L'ECG rend des métriques de HRV en U shape = le début/milieu de la visite stimule les participants vs les dernières salles (Sea & End Of The World) relaxent


Pour l'analyse globale première vs dernières 15 minutes:
- EEG : + de gamma en fin qu'en début probablement artefacté par Sea 
- ECG montrent un effet relaxant de la visite (+ de SDNN & RMSSD & pNN50)
- EDA : pas grand car sûrement useless signals




