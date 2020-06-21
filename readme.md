# ugh
Ultimate Glitch History for the CHOP On-call team.

### local setup
```console
> python -m venv venv
> source venv/bin/activate
> pip install -r ./app/requirements.txt
> export REDCAP_TOKEN_UGH="<token goes here>"
> python ./app/main.py
```

Then go to http://localhost:5000/ to see the site.


### docker setup
```console
> sudo docker build -t ugh-image .
> sudo docker run --rm -d --name ugh-container -p 5000:80 -e REDCAP_TOKEN_UGH=<token goes here> ugh-image
```