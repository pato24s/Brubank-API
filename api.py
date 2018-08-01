import re, urllib2, urllib, json, operator	

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

import diccLanguages
from diccLanguages import diccLangs


app = Flask(__name__)

@app.route("/applicant/<applicant>", methods=['GET'])
def potentialApplicantTeam(applicant):
	url = 'https://api.github.com/users/' + applicant + '/repos'
	response= urllib.urlopen(url)
	responseCode= response.getcode()
	if responseCode==404:
		result = {"mensaje": "El usuario "+applicant+" no tiene cuenta de GitHub"}
	elif responseCode==403:
		result = {"mensaje": "Forbidden. Posible causa: Se excedio el rate limit de la API de GitHub"}
	else:
		data = json.load(response)
	
		numberOfRepos = len(data)

		potentialTeams = {'Backend':0, 'Mobile':0, 'Web':0}

		for repo in xrange(0,numberOfRepos):
			repoLanguage = data[repo]['language']
			languageTeam = diccLangs[repoLanguage]
			potentialTeams[languageTeam] += 1

		bestTeamForApplicant =  max(potentialTeams, key=potentialTeams.get)
	
		result = {"applicant": applicant, "team": bestTeamForApplicant}

	return jsonify(result),responseCode


