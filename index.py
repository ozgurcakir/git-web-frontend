from flask import Flask, render_template
from git import Repo
#from time import gmtime

app = Flask(__name__)

@app.route("/")
@app.route("/<repository>")
def index(repository=None):
    try:
        # create git repository object
        repo = Repo(repository)
        # fetch latest 20 commits
        commits = list(repo.iter_commits("master", max_count=20))
    except:
        commits = False
    # display results
    return render_template('index.html', commits=commits)

#run application in debug mode 	
if __name__ == '__main__':
    app.run(debug=True)	

