participants = [
    'P01PPILNI',
 # 'P03PBABCO', # P03PBABCO WARNING : Recording shorter than timestamping
 # 'P04PROMCH', # 3 secs of baseline and 51 secs only in Canopy, no ppg (data shape = (9, 5101720))
 'P05PROZEM', 
 # 'P06PHERAX', # 79 secs only in Savannah , data shape = (9, 4747434) so no ppg ?
 'P07GHOLE',
 'P08AKKOR',
 # 'P09COUAM', # 1 sec only in Savannah
 'P10LEVVA',
 'P11KERSA',
 'P12BOULI', 
 # 'P13MORMA', # 74 secs only in Underground
 'P14BENLA', 
 'P15LEPMA',
 'P16MAUAD',
 'P17ETRPA',
#  'P18BLAMA', # less than 72 secs in Take-Off and bats and Underground
 'P19MONAL', 
    'P20POUAX', 
    'P21LIYAT',
    'P22DALPI',
   #  'P23VIVBA', # room too short
   #  'P24BELCL', # no timestamps
    'P25PEIAN',
    # 'P26BOUHE', # no txt
    'P27OSTMA',
    'P28JUDGU',
   #  'P29FICMA' # room too short
    'P30BATDI'
 ]

participants_for_visit_effect = [
    'P01PPILNI',
 'P03PBABCO', # P03PBABCO WARNING : Recording shorter than timestamping
 # 'P04PROMCH', # 3 secs of baseline and 51 secs only in Canopy, no ppg (data shape = (9, 5101720))
 'P05PROZEM', 
 # 'P06PHERAX', # 79 secs only in Savannah , data shape = (9, 4747434) so no ppg ?
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
 'P18BLAMA', # less than 72 secs in Take-Off and bats and Underground
 'P19MONAL', 
    'P20POUAX', 
    'P21LIYAT',
    'P22DALPI',
    'P23VIVBA', # room too short
    'P24BELCL', # no timestamps
    'P25PEIAN',
    # 'P26BOUHE', # no txt
    'P27OSTMA',
    'P28JUDGU',
    'P29FICMA', # room too short
    'P30BATDI'
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
 'P18BLAMA', # less than 72 secs in Take-Off and bats and Underground
     'P19MONAL',
    'P20POUAX',
    'P21LIYAT',
    'P22DALPI',
    'P23VIVBA', # 37 sec in savannah
    'P24BELCL',
    'P25PEIAN',
    'P26BOUHE', # no txt
    'P27OSTMA',
    'P28JUDGU',
    'P29FICMA', # 1 sec in sea
    'P30BATDI'
 ]

sessions = ['ses_01','ses_02','ses_03']
rooms = ['Baseline','Take-off','Savannah','Canopy','Bats','Underground','Grassland','Sea','End of the world']
dtypes = ['EEGL','EEGR','ECG','EDA','PPG']
biosigs = ['EEG','ECG','EDA','PPG']
srate = 1000
down_srate = 250
sig_by_room_duration = 90

# encoding of ecg peak : 1 if ecg has to be reversed, 0 if not
ecg_reverse = { 
       'P01PPILNI':1,
 'P03PBABCO':1, 
 'P04PROMCH':0, 
 'P05PROZEM':1,
 'P06PHERAX':0,
 'P07GHOLE':0,
 'P08AKKOR':1,
 'P09COUAM':0, 
 'P10LEVVA':0,
 'P11KERSA':1,
 'P12BOULI':0, 
 'P13MORMA':0, 
 'P14BENLA':1, 
 'P15LEPMA':1,
 'P16MAUAD':1,
 'P17ETRPA':0,
 'P18BLAMA':0, 
     'P19MONAL':1,
    'P20POUAX':1,
    'P21LIYAT':0,
    'P22DALPI':1,
    'P23VIVBA':0,
    'P24BELCL':0,
    'P25PEIAN':0,
    'P26BOUHE':0,
    'P27OSTMA':0,
    'P28JUDGU':1,
    'P29FICMA':0,
    'P30BATDI':0
}