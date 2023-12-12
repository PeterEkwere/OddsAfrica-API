#!/usr/bin/python
"""
    This Module will contain a bookie class for sportybet
    Author: Peter Ekwere
"""
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup 


class SportyBet:
    """
        This Class will handle scraping and parsing for the SportyBet site
    """
    def __init__(self, *args, **kwargs):
        """initializes SportyBet"""
        pass
    
    
    def GetTodayGames(self, sport, market):
        """ This method scrapes and returns todays games
            On Sportybet based on the league and market

        Args:
            sport (str): This is the required league
            market (str): This is the required market
        """
        # Create a new instance of the Chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        
        # Get the current working directory
        market_filename = market.replace("/", "_").replace(" ","_")
        filename = f"sportybet_{sport}_{market_filename}.csv"
        
        
        if sport == "basketball":
            # Check the Markets
            if market == ' 3 Way ':
                # locate the specified sport and market
                self.locate(sport, market, driver)

                # handle market with 2 outcomes
                self.Scrape3WayMarket(filename, market, driver)
            elif market in ['Draw No Bet', ' 2 Way O/U ']:
                # locate the specified sport and market
                self.locate(sport, market, driver)

                # handle normal 2 way market
                self.Scrape2WayMarket(filename, market, driver)
            elif market == 'Over/Under':
                market = ' 2 Way O/U '
                # locate the OVER/Under market
                self.locate(sport, market, driver)

                # Handle the OVER/Under market
                self.scrape_over_under_market(market, filename, driver)
            else:
                print(f"{market} not supported for Sportybet Class")
        elif sport == 'tennis':
             # check the markets
            if market in [' 2 Way O/U ']:
                # locate the specified sport and market
                self.locate(sport, market, driver)  
                # handle market with 2 outcomes
                self.Scrape2WayMarket(filename, market, driver)
            elif market == 'Over/Under':
                market = ' 2 Way O/U '
                # locate the OVER/Under market
                self.locate(sport, market, driver)

                # Handle the OVER/Under market
                self.scrape_over_under_market(market, filename, driver)
            else:
                print(f"{market} not supported for Sportybet Class")
        elif sport == 'iceHockey':
             # check the markets
            if market in ['Odd/Even']:
                # locate the specified sport and market
                self.locate(sport, market, driver)  
                # handle market with 2 outcomes
                self.Scrape2WayMarket(filename, market, driver)
            elif market in ['3 Way & O/U ', 'Double Chance']:
                # locate the specified league and market
                self.locate(sport, market, driver)
                # handle market with 3 outcomes
                self.Scrape3WayMarket(filename, market, driver)
            elif market == 'Over/Under':
                market = ' 3 Way & O/U '
                # locate the OVER/Under market
                self.locate(sport, market, driver)

                # Handle the OVER/Under market
                self.scrape_over_under_market(market, filename, driver)
            else:
                print(f"{market} not supported for Sportybet Class")
        elif sport == 'football':
            # check the markets
            if market in ['Draw No Bet', 'GG/NG']:
                # locate the specified sport and market
                self.locate(sport, market, driver)  
                # handle market with 2 outcomes
                self.Scrape2WayMarket(filename, market, driver)
            elif market in ['3 Way & O/U ', 'Double Chance']:
                # locate the specified league and market
                self.locate(sport, market, driver)
                # handle market with 3 outcomes
                self.Scrape3WayMarket(filename, market, driver)
            elif market == 'Over/Under':
                market = ' 3 Way & O/U '
                # locate the OVER/Under market
                self.locate(sport, market, driver)

                # Handle the OVER/Under market
                self.scrape_over_under_market(market, filename, driver)
            else:
                print(f"{market} not supported for Sportybet Class")
        else:
            print(f"{sport} not supported for Sportybet Class")
        
        
    def Scrape2WayMarket(self, filename, market, driver):
        """ This Method handle Scraping of games with 3 Outcomes

        Args:
            filename (str): name of file to be created
            market (str): type of market to Scrape
            driver (obj): automation tool
        """
        # Create a CSV file to save the data
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([f"THIS IS TODAYS GAMES FOR  {market} ===============>"])
            csv_writer.writerow(["Bookie", " | " "Home Team", " | ", "Away Team", " | ", "Home Odds",  " | ", "Away Odds"])
            
            page_number = 1
            while True:
                # Wait for the page to load
                time.sleep(5)
                
                # Get the page source after it has loaded
                print("Preparing to Scrape the games====================>")
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Wait for the importMatch div to be present
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "importMatch")))
                
                # Find the relevant section of the HTML containing the fixtures
                fixtures_section = soup.find("div", {"id": "importMatch"})
            
                # Find all the rows that contain the game information
                game_rows = fixtures_section.find_all("div", class_="m-table-row m-content-row match-row")
            
            
                # Iterate through each game row and extract the required information
                for game_row in game_rows:
                    home_team = game_row.find("div", class_="home-team").text.strip()
                    away_team = game_row.find("div", class_="away-team").text.strip()
                
                    # Get Odds for game
                    market_element = game_row.find("div", class_="m-market market")
                    odds_elements = market_element.find_all("span", class_="m-outcome-odds")

                    # Extract the home, away odds
                    if (len(odds_elements) == 2):
                        home_odds = odds_elements[0].text.strip()
                        away_odds = odds_elements[1].text.strip()
                        # Write the data to the CSV file
                        csv_writer.writerow(["SportyBet", " | ", home_team, " | ", away_team, " | ", home_odds, " | ", away_odds])
                        print(f"Home Odds: {home_odds}, Away Odds: {away_odds}\n")
                    else:
                        home_odds = "N/A"
                        away_odds = "N/A"
                # Check if there is a next page
                try:
                    next_button = driver.find_element(By.CLASS_NAME, "icon-next")
                    if "icon-disabled" in next_button.get_attribute("class"):
                        break  # Break the loop if there is no next page
                    else:
                        # Click the next button to go to the next page
                        next_button.click()
                        page_number += 1
                except NoSuchElementException:
                    break  # Break the loop if the next button is not found
        # Close the CSV file
        csv_file.close()
        driver.quit()
        print(f"Data has been scraped and saved to {filename}")
        
    def Scrape3WayMarket(self, filename, market, driver):
        """ This Method handle Scraping of games with 3 Outcomes

        Args:
            filename (str): name of file to be created
            market (str): type of market to Scrape
            driver (obj): automation tool
        """
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([f"THIS IS TODAYS GAMES FOR  {market} ===============>"])
            csv_writer.writerow(["Bookie", " | " "Home Team", " | ", "Away Team", " | ", "Home Odds", "Draw odds", " | ", "Away Odds"])
            
            page_number = 1
            
            while True:
                # Wait for the page to load
                time.sleep(5)
                
                # Get the page source after it has loaded
                print("Preparing to Scrape the games====================>")
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Wait for the importMatch div to be present
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "importMatch")))
                
                # Find the relevant section of the HTML containing the fixtures
                fixtures_section = soup.find("div", {"id": "importMatch"})
            
                # Find all the rows that contain the game information
                game_rows = fixtures_section.find_all("div", class_="m-table-row m-content-row match-row")
            
            
                # Iterate through each game row and extract the required information
                for game_row in game_rows:
                    home_team = game_row.find("div", class_="home-team").text.strip()
                    away_team = game_row.find("div", class_="away-team").text.strip()
                
                    # Get Odds for game
                    market_element = game_row.find("div", class_="m-market market")
                    odds_elements = market_element.find_all("span", class_="m-outcome-odds")

                    # Extract the home, draw, and away odds
                    if (len(odds_elements) == 3):
                        home_odds = odds_elements[0].text.strip()
                        draw_odds = odds_elements[1].text.strip()
                        away_odds = odds_elements[2].text.strip()
                        # Write the data to the CSV file
                        csv_writer.writerow(["SportyBet", " | ", home_team, " | ", away_team, " | ", home_odds, " | ", draw_odds, " | ", away_odds])
                        print(f"Home Odds: {home_odds}, Draw odds {draw_odds}, Away Odds: {away_odds}\n")
                    else:
                        home_odds = "N/A"
                        away_odds = "N/A"
                # Check if there is a next page
                try:
                    next_button = driver.find_element(By.CLASS_NAME, "icon-next")
                    if "icon-disabled" in next_button.get_attribute("class"):
                        break  # Break the loop if there is no next page
                    else:
                        # Click the next button to go to the next page
                        next_button.click()
                        page_number += 1
                except NoSuchElementException:
                    break  # Break the loop if the next button is not found
        # Close the CSV file
        csv_file.close()
        driver.quit()
        print(f"Data has been scraped and saved to {filename}")

 
    def scrape_over_under_market(self, market, filename, driver):
        """This method handles scraping of games with over/under markets.

        Args:
            filename (str): Name of the file to be created.
            driver (obj): Automation tool.
        """
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([f"THIS IS TODAYS GAMES FOR {market} MARKET===============>"])
            csv_writer.writerow(["Bookie", " | " "Home Team", " | ", "Away Team", " | ", "Over Option", " | ", "Under Option", " | ", "Over Odds", " | ", "Under Odds"])

            page_number = 1

            while True:
                # Wait for the page to load
                time.sleep(5)

                # Get the page source after it has loaded
                print("Preparing to Scrape the games====================>")
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, "html.parser")

                # Wait for the importMatch div to be present
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "importMatch")))

                # Find the relevant section of the HTML containing the fixtures
                fixtures_section = soup.find("div", {"id": "importMatch"})

                # Find all the rows that contain the game information
                game_rows = fixtures_section.find_all("div", class_="m-table-row m-content-row match-row")

                # Iterate through each game row and extract the required information
                for game_row in game_rows:
                    home_team = game_row.find("div", class_="home-team").text.strip()
                    away_team = game_row.find("div", class_="away-team").text.strip()
                    
                    
                    # locate dropdown button
                    #dropdownXpath = f'//*[@id="importMatch"]/div[2]/div/div[4]/div[{game_rows.index(game_row) + 2}]/div[2]/div[2]/div[1]/div/div/span[1]'
                    #dropdown_filter_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdownXpath)))
                    # Scroll to dropdown and click button
                    #actions = ActionChains(driver)
                    #actions.move_to_element(dropdown_filter_element).click().perform()
                    # Wait for the options to be visible
                    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'af-select-title')))
                    # Retrieve available options but firt Wait for the options to be present
                    #try:
                        #options_xpath = f'//*[@id="importMatch"]/div[2]/div/div[4]/div[{game_rows.index(game_row) + 2}]/div[2]/div[2]/div[1]/div/div/span[1]'
                        #options = WebDriverWait(driver, 10).until(
                            #EC.presence_of_all_elements_located((By.XPATH, options_xpath))
                        #)
                    #except Exception as e:
                        #print(f"Error waiting for options: {e}")
                        #continue
                    
                    # Locate the div with class 'm-market market'
                    game_market = game_row.find_all("div", class_="m-market market")[1]
                    print(f"gamemarket is =============>\n {game_market}")
                    # Locate the div with class 'm-outcome specifiers-select'
                    specifiers_select_div = game_market.find("div", class_="m-outcome specifiers-select")
                    print(f"specifiers_select_div is =============>\n {specifiers_select_div}")
                    # Locate the dropdown button within the specifiers_select_div
                    dropdown_filter_element = specifiers_select_div.find_element(By.CLASS_NAME, 'af-select-title')
                    # Scroll to dropdown and click button
                    actions = ActionChains(driver)
                    actions.move_to_element(dropdown_filter_element).click().perform()
    
                    # Wait for the options to be visible
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'af-select-list')))

                    # Simulate pressing the ARROW_DOWN key to iterate through options
                    dropdown_filter_element.send_keys(Keys.ARROW_DOWN)
                    
                    # Extract and print the current option
                    current_option = driver.execute_script(
                        'return document.querySelector(".af-select-item.active").innerText;'
                        )
                    print(f"For {home_team} vs {away_team} we have: {current_option}") 
                    
                    #print("Option\tOver Odds\tUnder Odds")

                    # Find and extract odds
                    #odds_elements = game_row.find_all("span", class_="m-outcome-odds")
                    #odds = [element.text.strip() for element in odds_elements[-2:]]

                    #print(f"{over_under_option}\t {odds[0]}\t{odds[1]}")
                    
                    
                    # Iterate through options
                    #for option in options:
                        #over_under_option = option.text
                        
                        # Click the specified option 
                        # option.click()
                        # driver.execute_script("arguments[0].click();", option)
                        # Execute JavaScript to get options
                        #options_script = """
                        #const dropdown = document.querySelector('.af-select-title');
                        #dropdown.click(); // Ensure the dropdown is open
                        #dropdown.querySelectorAll('.af-select-item').forEach(option => {
                            #console.log(option.innerText);
                            #});
                        #"""
                        #driver.execute_script(options_script) 

                        # Find and extract odds
                        #odds_elements = game_row.find_all("span", class_="m-outcome-odds")
                        #odds = [element.text.strip() for element in odds_elements[-2:]]

                        #print(f"{over_under_option}\t {odds[0]}\t{odds[1]}")
                        # Store the data in a dictionary
                        #data = {'Over/Under Option': over_under_option, 'Odds': odds}
                        #csv_writer.writerow(["SportyBet", " | ", home_team, " | ", away_team, " | ", data['Over/Under Option'], " | ", data['Odds'][0], " | ", data['Odds'][1]])
                        # Close Drop Down for the Current game row
                        #actions.move_to_element(dropdown_filter_element).click().perform()
                # Check if there is a next page
                try:
                    next_button = driver.find_element(By.CLASS_NAME, "icon-next")
                    if "icon-disabled" in next_button.get_attribute("class"):
                        break  # Break the loop if there is no next page
                    else:
                        # Click the next button to go to the next page
                        next_button.click()
                        page_number += 1
                except NoSuchElementException:
                    break  # Break the loop if the next button is not found

        # Close the CSV file
        csv_file.close()
        driver.quit()
        print(f"Data has been scraped and saved to {filename}")

        
        
    def locate(self, sport, market, driver):
        """ This method Sets the time frame for odds for the next 24 hours and locates the needed market on the betsite

        Args:
            sport (str): This is the needed league
            market (str): This is the needed market
            driver (obj): automation tool
        """
        url = f"https://www.sportybet.com/ng/sport/{sport}/today"
        driver.get(url)
        time.sleep(5)
         # Find and click on the "24h" time filter using JavaScript
        time_filter_xpath = '//*[@id="sportList"]/div[2]/div[2]/div/ul/li[4]'
        time_filter_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, time_filter_xpath)))
        # Scroll to desired button
        actions = ActionChains(driver)
        actions.move_to_element(time_filter_element).click().perform()
        # Wait for 5 seconds
        time.sleep(5)
        # Find the market buttons and click the one matching the provided market
        print(f"Finding all {market} games playing today===============>")
        # CSS selector for finding elements with either "market-item" or "market-item active" class
        selector = ".market-item"

        market_buttons = driver.find_elements(By.CSS_SELECTOR, selector)
        for button in market_buttons:
            if market.lower() in button.text.lower():
                button.click()