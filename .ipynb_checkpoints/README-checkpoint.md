# Odyssee_Sensorielle

Pilote 01 du 19 avril 2022 : 

- PERSA a 3801 secondes
- GHIVA a 3463 secondes
- MONLI a 3737 secondes

ECG : 
- Avant preproc, MONLI = ECG parasité par mouvements
- Après preproc, toujours pareil, à voir comment la détection de pics réussit, d'ailleurs les pics vers le bas + onde T vers le bas suggèrent qu'il faudrait inverser les deux électrodes (= noire à gauche et rouge à droite)

PPG :
- Avant prepoc, le contact n'a pas toujours l'air bon. Quand il l'est, le signal sature à +60 d'amplitude, donc il faudrait modifier le gain pour avoir une plage d'amplitude + large et/ou recentrer la zone d'intérêt d'amplitude
- Après preproc, plus le "crénelage", les saturations évidemment toujours présentes mais "hachées" par le preproc, l'amplitude des pulse ne semble pas avoir bougé avec le preproc donc elle est utilisable

EDA :
- Avant preproc, le contact n'a pas toujours l'air bon pour GHIVA... sinon ça a l'air utilisable hormis quelques plages de parasites sur mouvement++ ? 
- Après preproc, pareil mais signal lissé

EEGL :
- Avant prepoc, PERSA bon signal, GHIVA signal bon mais avec pas mal d'artefacts OM, MONLI signal inutilisable (sature ++ à +1000)
- Après preproc, signal similaire ++, notch inefficace ? à voir sur PSD

EEGR :
- Avant prepoc, same pour PERSA et GHIVA, MONLI signal présent mais bruité ++ avant 150 secondes puis inutilisable (sature ++ à +1000)
- Après preproc, signal similaire ++, notch inefficace ? à voir sur PSD




PREPROC : 
- = cleaning de neurokit et pour l'EEG , notch 50 Hz + detrend par high_pass 0.1Hz
- Epoching sur 120 secs de signal par room par participant

STATS :
- Pas assez de sujets pour utiliser des tests statistiques pour le moment (possible si N > 3)
- Visuellement :
    - EEG : Augmentation du gamma et du beta au cours du temps, diminution du delta et theta et alpha au cours du temps (Canopy & Sea ont est profils particuliers ? Savannah aussi)
    - HRV : Moins de variabilité cardiaque au cours du temps, + score sympa et - score vagal, Fréquence cardiaque similaire, Savonny profil parasympathique ? 
    - EDA : + sympa en fin qu'en début ,  Canopy profil particulièrement sympa
    - PPG : amplitude augmente de début vers fin , canopy ++ = para sympa ?
    - 
    
