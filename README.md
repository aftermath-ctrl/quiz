# quiz

Language:Python3.X

problem 1: Web server (with optional secure communication).

         
         ./webserver.py
         
  extension:secure server.To generate key and cert files with OpenSSL use following command:
          
          openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
   run
      
         ./secure-server.py


Problem 2: Re-routing/forwarding communication.

  first spin the server in one terminal window
  
        ./server.py

  then start the client server on another terminal window
        
        ./client.py
     
  extension:single server to multiple client endpoints.
   
          ./multiserver.py


Problem 3: Diction & dictionary scrapping.

        pip install requests
        pip install beautifulsoup4

        ./dictionaries.py



Problem 4: Markdown engine.This command will generate two files: cities.md and cities.html
 
        

        source env/bin/activate
        
        pip install markdown


        ./markdown.py




Problem 5: Fermat near-misses.

         ./fermet.py
