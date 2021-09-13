from datetime import datetime

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.hltv.org"
MATCHES_URL = f"{BASE_URL}/matches"
RESULTS_URL = f"{BASE_URL}/results"
RANKING_URL = f"{BASE_URL}/ranking/teams"


class HLTVClient:
    def _soup_from_url(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup

    def get_matches(self):
        matches = []
        soup = self._soup_from_url(MATCHES_URL)
        matches_html = soup.find("div", {"class": "upcomingMatchesWrapper"}).find_all("div", {"class": "upcomingMatch"})
        for match in matches_html:
            event_el = match.find("div", {"class": "matchEventName"})
            if event_el:
                event = event_el.text.strip()
                teams = [item.text.strip() for item in match.find_all("div", {"class": "matchTeam"})]
                date = datetime.fromtimestamp(int(match["data-zonedgrouping-entry-unix"][0:10])).isoformat()
                match_data = {
                    "event": event,
                    "date": date,
                    "team_1": teams[0],
                    "team_2": teams[1]
                }
                matches.append(match_data)
        return matches


    def get_results(self):
        results = []
        soup = self._soup_from_url(RESULTS_URL)
        matches = soup.find("div", {"class": "allres"}).find_all("div", {"class": "result"})
        for match in matches:
            event = match.find("span", {"class": "event-name"}).text.strip()
            teams = [item.text.strip() for item in match.find_all("div", {"class": "team"})]
            result = [item.text.strip() for item in match.find("td", {"class": "result-score"}).find_all("span")]
            match_data = {
                "event": event,
                "team_1": {
                    "name": teams[0],
                    "result": result[0]
                },
                "team_2": {
                    "name": teams[1],
                    "result": result[1]
                }
            }
            results.append(match_data)
        return results

    def get_ranking(self):
        ranking = []
        soup = self._soup_from_url(RANKING_URL)
        teams = soup.find_all("div", {"class": "ranked-team"})
        for position, team in enumerate(teams, start=1):
            name = team.find("span", {"class": "name"}).text.strip()
            points = team.find("span", {"class": "points"})
            points = int(points.text.strip()[1:-1].split(" ")[0])
            ranking_item = {
                "position": position,
                "name": name,
                "points": points
            }
            ranking.append(ranking_item)
        return ranking


print(
    HLTVClient().get_matches()
)