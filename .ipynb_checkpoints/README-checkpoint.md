# Odyssee_Sensorielle

Pilote 01 du 19 avril 2022 : 


- PERSA n'a que 661 secondes de signal 
- GHIVA a 3463 secondes
- MONLI a 3737 secondes

ECG : 
- Avant preproc, PERSA et MONLI ont ECG bien parasité, surtout MONLI, probablement par mouvements
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
