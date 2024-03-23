import requests

# make api call and store response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store api response in a variable
response_dict = r.json()
print(f"total repos: {response_dict['total_count']}")

# explore info about the repos
repo_dicts = response_dict["items"]
print(f"repos returned: {len(repo_dicts)}")

# examine first repo
repo_dict = repo_dicts[0]

print("\nselected info about repo[0]")
print(f"name: {repo_dict['name']}")
print(f"owner login: {repo_dict['owner']['login']}")
print(f"stars: {repo_dict['stargazers_count']}")
print(f"repo url: {repo_dict['html_url']}")
print(f"created: {repo_dict['created_at']}")
print(f"updated: {repo_dict['updated_at']}")
print(f"description: {repo_dict['description']}")
