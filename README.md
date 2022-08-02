# Python-LP-Project-Lotto
Learning Path Python - TomorrowDevs Exercise


## Requirements
<strong>LP1: First part of the project about Italian Lotto Game</strong>
<br/>Reference: https://www.sisal.it/lotto/come-si-gioca

- The project must be OOP so that it can be extended in the next learning path.
- The software should ask the user how many bills he wants to generate (min: 1, max: 5, 0: exit).
- For each bill the software should ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill)
and the "city" (aka "ruota") of the bill: Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte (for the project purpose completely ignore "ruota nazionale" and the "estratto determinato" play type).
- Numbers will be randomly generated in the range 1-90 (inclusive).
- Generate the ticket with nice ascii art table decoration (https://ozh.github.io/ascii-tables/).


<strong>LP2: Second part of the project about Italian Lotto Game</strong>
<br/>Reference: https://www.servizitelevideo.rai.it/televideo/pub/pagina.jsp?p=786&s=0&r=Nazionale&idmenumain=0

- Add lotto number extraction.
- Check if some of the tickets generated result winners.


<strong>LP3: Third part of the project about Italian Lotto Game</strong>
<br/>Reference: https://www.servizitelevideo.rai.it/televideo/pub/pagina.jsp?p=786&s=0&r=Nazionale&idmenumain=0

- When asking for tickets to generate you have also to ask the amount of money to put for each ticket
- If a particular ticket won you have to calculate and show the prizes, both gross and net. see: https://www.estrazionedellotto.it/prontuario-vincite-lotto)


## How to start 

Launch the command:<br/><br/>
<strong>python3 main.py</strong><br/><br/>
Then, for each ticket, the application will ask you how many numbers to extract (1 to 10), the type of bill and the cities.

