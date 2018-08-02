from flask import jsonify
from flask_api import FlaskAPI, status
import requests
import json
import diccLanguages
from diccLanguages import diccLangs

app = FlaskAPI(__name__)



@app.route("/applicant/<string:applicant>", methods=['GET'])
def potentialTeamForApplicant(applicant):
	url = 'https://api.github.com/users/' + str(applicant) + '/repos'
	response= requests.get(url=url)
	responseCode= response.status_code

	if responseCode==404:
		result = {"mensaje": "User "+applicant+" is not registered in GitHub"}
	elif responseCode==403:
		result = {"mensaje": "Forbidden. Possible cause: GitHub API rate-limit exceeded"}
	else:
		data = response.json()
		numberOfRepos = len(data)

		potentialTeams = {'Backend':0, 'Mobile':0, 'Web':0}

		for repo in range(0,numberOfRepos):
			repoLanguage = data[repo]['language']
			languageTeam = diccLangs[repoLanguage]
			potentialTeams[languageTeam] += 1

		bestTeamForApplicant =  max(potentialTeams, key=potentialTeams.get)
	
		result = {"applicant": applicant, "team": bestTeamForApplicant}

	return jsonify(result),responseCode

if __name__ == "__main__":
    app.run(debug=True)
