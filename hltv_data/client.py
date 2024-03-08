from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.hltv.org"
MATCHES_URL = f"{BASE_URL}/matches"
RESULTS_URL = f"{BASE_URL}/results"
RANKING_URL = f"{BASE_URL}/ranking/teams/2024/march/5"


class HLTVClient:
    def __init__(self):
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

    def _get_page_source(self, url):
        try:
            self.driver.get(url)
            return self.driver.page_source
        except Exception as e:
            print(f"Error occurred while fetching URL: {url}")
            print(f"Error details: {e}")
            return None

    def _get_star_rating(self, event_el):
        return len(event_el.find_elements(By.CSS_SELECTOR, "i.fa.fa-star"))

    def get_ranking(self):
        ranking = []
        page_source = self._get_page_source(RANKING_URL)
        if page_source:
            soup = BeautifulSoup(page_source, "html.parser")
            teams = soup.find_all("div", {"class": "ranked-team"})
            for team in teams:
                position = team.find("span", {"class": "position"}).text.strip()[1:]
                name = (
                    team.find("div", {"class": "teamLine"})
                    .find("span", {"class": "name"})
                    .text.strip()
                )
                points = (
                    team.find("div", {"class": "teamLine"})
                    .find("span", {"class": "points"})
                    .text.strip()[1:-1]
                    .split(" ")[0]
                )
                ranking_item = {
                    "position": int(position),
                    "name": name,
                    "points": int(points),
                }
                ranking.append(ranking_item)
        return ranking

    def get_matches(self):
        matches = []
        self._get_page_source(MATCHES_URL)
        page_source = self.driver.find_elements(
            By.CSS_SELECTOR, "div.upcomingMatchesWrapper div.upcomingMatchesSection"
        )
        for match in page_source:
            event_el = match.find_element(By.CSS_SELECTOR, "div.upcomingMatch")
            if event_el:
                try:
                    event = event_el.text.strip()
                    teams = [
                        item.text.strip()
                        for item in match.find_elements(
                            By.CSS_SELECTOR, "div.matchTeam"
                        )
                    ]
                    if not teams:
                        continue
                    date = datetime.fromtimestamp(
                        int(
                            match.find_element(
                                By.CSS_SELECTOR, "div.matchTime"
                            ).get_attribute("data-unix")[0:10]
                        )
                    ).isoformat()
                    match_data = {
                        "event": event,
                        "date": date,
                        "team_1": teams[0],
                        "team_2": teams[1],
                        "star_rating": self._get_star_rating(match),
                    }
                except:
                    import pdb

                    pdb.set_trace()
                matches.append(match_data)
        return matches

    def get_results(self):
        results = []
        page_source = self._get_page_source(RESULTS_URL)
        matches = self.driver.find_elements(By.CSS_SELECTOR, "div.allres div.result")
        for match in matches:
            event = match.find_element(By.CSS_SELECTOR, "span.event-name").text.strip()
            teams = [
                item.text.strip()
                for item in match.find_elements(By.CSS_SELECTOR, "div.team")
            ]
            result = [
                int(item.text.strip())
                for item in match.find_element(
                    By.CSS_SELECTOR, "td.result-score"
                ).find_elements(By.CSS_SELECTOR, "span")
            ]
            match_data = {
                "event": event,
                "team_1": {"name": teams[0], "result": result[0]},
                "team_2": {"name": teams[1], "result": result[1]},
            }
            results.append(match_data)
        return results

    def close(self):
        self.driver.quit()
