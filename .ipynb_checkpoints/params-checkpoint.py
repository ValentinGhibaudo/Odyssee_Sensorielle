participants = [
    'P01PPILNI',
 'P03PBABCO', # P03PBABCO WARNING : Recording shorter than timestamping
 # 'P04PROMCH', # 3 secs of baseline and 51 secs only in Canopy, no ppg (data shape = (9, 5101720))
 # 'P05PROZEM', # same data than P04PROMCH
 # 'P06PHERAX', # 79 secs only in Savannah , data shape = (9, 4747434) so no ppg ?
 'P07GHOLE',
 'P08AKKOR',
 # 'P09COUAM', # 1 sec only in Savannah
 'P10LEVVA',
 'P11KERSA',
 'P12BOULI', # P12BOULI WARNING : Recording shorter than timestamping
 # 'P13MORMA', # 74 secs only in Underground
 # 'P14BENLA', # data = np.loadtxt(input_file).T : ValueError: Wrong number of columns at line 869012
 'P15LEPMA',
 'P16MAUAD',
 'P17ETRPA'
 # 'P18BLAMA' # less than 72 secs in Take-Off and bats and Underground
 ]

all_participants = [
    'P01PPILNI',
 'P03PBABCO', # P03PBABCO WARNING : Recording shorter than timestamping
 'P04PROMCH', # 3 secs of baseline and 51 secs only in Canopy, no ppg (data shape = (9, 5101720))
 'P05PROZEM', # same data than P04PROMCH
 'P06PHERAX', # 79 secs only in Savannah , data shape = (9, 4747434) so no ppg ?
 'P07GHOLE',
 'P08AKKOR',
 'P09COUAM', # 1 sec only in Savannah
 'P10LEVVA',
 'P11KERSA',
 'P12BOULI', # P12BOULI WARNING : Recording shorter than timestamping
 'P13MORMA', # 74 secs only in Underground
 'P14BENLA', # data = np.loadtxt(input_file).T : ValueError: Wrong number of columns at line 869012
 'P15LEPMA',
 'P16MAUAD',
 'P17ETRPA',
 'P18BLAMA' # less than 72 secs in Take-Off and bats and Underground
 ]

sessions = ['ses_01','ses_02','ses_03']
rooms = ['Baseline','Take-off','Savannah','Canopy','Bats','Underground','Grassland','Sea','End of the world']
dtypes = ['EEGL','EEGR','ECG','EDA','PPG']
srate = 1000
down_srate = 250
sig_by_room_duration = 90