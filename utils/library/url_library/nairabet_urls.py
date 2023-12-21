#!/usr/bin/python
"""
    This module contains all the nairabet league code to be used for querying
    Author: Peter Ekwere
"""
SOCCER =  {
  "Angola": [
    "ANGOLA_GIRABOLA"
  ],
  "Argentina": [
    "ARGENTINA_CUP",
    "ARGENTINA_PRIMERA_DIVISION",
    "ARGENTINA_TORNEO_REGIONAL_FEDERAL_AMATEUR",
    "ARGENTINA_RESERVE_LEAGUE"
  ],
  "Asia": [
    "AFC_CHAMPIONS_LEAGUE",
    "INTERNATIONAL_AFC_CUP"
  ],
  "Australia": [
    "AUSTRALIA_A-LEAGUE",
    "AUSTRALIA_WOMEN_W-LEAGUE"
  ],
  "Azerbaijan": [
    "AZERBAIJAN_FIRST_DIVISION",
    "AZERBAIJAN_PREMIER_LEAGUE"
  ],
  "Chile": [
    "COPA_CHILE"
  ],
  "Colombia": [
    "COLOMBIA_PRIMERA_A"
  ],
  "Croatia": [
    "CROATIA_1_HNL"
  ],
  "Czech Republic": [
    "CZECH_REPUBLIC_DIVISION_1"
  ],
  "Denmark": [
    "DENMARK_CHAMPIONSHIP__W"
  ],
  "England": [
    "EN_FA",
    "EN_PR",
    "EN_D1",
    "EN_LC",
    "ENGLAND_WOMENS_SUPER_LEAGUE",
    "EN_D3",
    "EN_D2",
    "ENGLAND_NATIONAL_LEAGUE_SOUTH",
    "ENGLAND_NATIONAL_LEAGUE",
    "SOUTHERN_FOOTBALL_LEAGUE",
    "ENGLAND_NATIONAL_LEAGUE_NORTH"
  ],
  "Europe": [
    "EU_UC",
    "EU_CL",
    "UEFA_WOMENS_CHAMPIONS_LEAGUE",
    "UEFA_YOUTH_LEAGUE",
  ],
  "France": [
    "FRANCE_LIGUE_2",
    "FR_L1",
    "FRANCE_NATIONAL_1"
  ],
  "Germany": [
    "GERMANY_BUNDESLIGA_2",
    "DE_BL",
    "GERMANY_3_LIGA",
    "GERMANY_REGIONALLIGA_NORTH",
    "GERMANY_REGIONAL_LIGA_NORDOST",
    "GERMANY_REGIONAL_LIGA_WEST",
    "GERMANY_REGIONALLIGA_SUDWEST"
  ],
  "India": [
    "INDIA_I-LEAGUE",
    "INDIA_SUPER_LEAGUE"
  ],
  "Indonesia": [
    "INDONESIA_LIGA_2"
  ],
  "Ireland": [
    "NORTHERN_IRELAND_PREMIER_LEAGUE"
  ],
  "Israel": [
    "ISRAEL_LIGA_ALEF_-_SOUTH",
    "ISRAEL_STATE_CUP",
    "ISRAEL_U19_LEAGUE",
  ],
  "Italy": [
    "IT_SA",
    "ITALY_SERIE_B",
    "ITALY_SERIE_C"
  ],
  "Japan": [
    "JAPAN_UNIVERSITY_CHAMPIONSHIP",
    "JAPAN_WE_LEAGUE_WOMEN"
  ],
  "Jordan": [
    "JORDAN_PROFESSIONAL_LEAGUE",
    "JORDAN_1ST_DIVISION"
  ],
  "Kenya": [
    "KENYA_PREMIER_LEAGUE"
  ],
  "Malta": [
    "MALTA_FA_TROPHY"
  ],
  "Morocco": [
    "MOROCCO_BOTOLA_PRO"
  ],
  "Netherlands": [
    "NETHERLANDS_EREDIVISIE",
    "NETHERLANDS_EREDIVISIE_WOMEN",
    "NETHERLANDS_EERSTE_DIVISIE"
  ],
  "Nigeria": [
    "NIGERIA_PREMIER_LEAGUE"
  ],
  "Poland ": [
    "POLAND_1_LIGA",
    "POLAND_EKSTRAKLASA",
    "POLAND_2_LIGA"
  ],
  "Portugal": [
    "PORTUGAL_PRIMEIRA_LIGA",
    "PORTUGAL_SEGUNDA_LIGA"
  ],
  "Qatar": [
    "QATAR_-_STARS_LEAGUE"
  ],
  "Romania": [
    "ROMANIA_LIGA_I"
  ],
  "Rwanda": [
    "RWANDA_NATIONAL_LEAGUE"
  ],
  "Saudi Arabia": [
    "SAUDI_PRO_LEAGUE",
    "SAUDI_ARABIA_DIVISION_1"
  ],
  "Scotland ": [
    "LD_SP",
    "SCOTLAND_LEAGUE_CUP",
    "SCOTLAND_LEAGUE_TWO",
    "SCOTLAND_LEAGUE_ONE",
    "SCOTLAND_CHAMPIONSHIP",
  ],
  "Slovakia": [
    "SLOVAKIA_SUPER_LIGA"
  ],
  "Slovenia": [
    "SLOVENIA_PREMIER_LEAGUE"
  ],
  "South Africa": [
    "SOUTH_AFRICA_PREMIER_LEAGUE",
    "SOUTH_AFRICA_LEAGUE_CUP"
  ],
  "Spain ": [
    "ES_PL",
    "SPAIN_SEGUNDA_DIVISION",
    "SPAIN_PRIMERA_DIVISION_W",
    "SPAIN_YOUTH_CHAMPIONSHIP",
  ],
  "Switzerland": [
    "SWITZERLAND_SUPER_LEAGUE",
    "SWITZERLAND_CHALLENGE_LEAGUE"
  ],
  "Thailand": [
    "THAILAND_THAI_LEAGUE_1"
  ],
  "Tunisia": [
    "TUNISIA_LIGUE_1"
  ],
  "Uganda": [
    "UGANDA_UGANDA_PREMIER_LEAGUE"
  ],
  "Uruguay": [
    "URUGUAY_PRIMERA_DIVISION"
  ],
  "Wales": [
    "WALES_FA_CUP",
    "Welsh Premier League"
  ],
}


BASKETBALL = {
  "Argentina": [
    "ARGENTINA_LNB",
    "LA_LIGA_ARGENTINA"
  ],
  "Australia": [
    "AUSTRALIA_NBL",
    "AUSTRALIA_WNBL"
  ],
  "Brazil": [
    "BRAZIL_NBB"
  ],
  "China": [
    "CHINA_CBA"
  ],
  "Croatia": [
    "CROATIA_A1_LIGA"
  ],
  "Czech Republic": [
    "CZECH_REPUBLIC_NBL"
  ],
  "Denmark": [
    "DENMARK_BASKETLIGAEN"
  ],
  "Europe": [
    "EUROLEAGUE",
    "EUROCUP_(M)",
    "EUROPECUP_(M)",
    "FIBA_BASKETBALL_CHAMPIONS_LEAGUE",
    "EUROLEAGUE_(W)"
  ],
  "Finland": [
    "FINLAND_KORISLIIGA"
  ],
  "Germany": [
    "GERMANY_BBL",
  ],
  "Greece": [
    "GREECE_A1_ETHNIKI"
  ],
  "Iceland": [
    "ICELAND_PREMIER_LEAGUE_WOMEN"
  ],
  "Israel": [
    "ISRAEL_LIGAT_HAAL"
  ],
  "Japan": [
    "JAPAN_B_LEAGUE"
  ],
  "Korea, Republic of": [
    "KOREA_WKBL"
  ],
  "Latvia": [
    "LATVIA_-_ESTONIAN_BASKETBALL_LEAGUE"
  ],
  "Mexico": [
    "MEXICO_LNBP"
  ],
  "Norway": [
    "NORWAY_BLNO"
  ],
  "Poland ": [
    "POLAND_1_LIGA_MEZCZYZN",
    "POLAND_PBL"
  ],
  "Qatar": [
    "QATAR_BASKETBALL_LEAGUE"
  ],
  "Serbia": [
    "SERBIA_KLS"
  ],
  "Slovenia": [
    "SLOVENIA_SKL_WOMEN"
  ],
  "Spain ": [
    "SPAIN_ACB",
  ],
  "Sweden ": [
    "SWEDEN_LIGAN"
  ],
  "Turkey": [
    "TURKEY_SUPER_LIGI"
  ],
  "United Kingdom": [
    "GREAT_BRITAIN_BBL"
  ],
  "United States": [
    "US_NBA",
    "NCAA",
  ],
  "Uruguay": [
    "URUGUAY_LIGA_CAPITAL"
  ]
}

VOLLEYBALL = {
  "Europe": [
    "INTERNATIONAL_CEV_CUP",
    "INTERNATIONAL_CEV_CHALLENGE_CUP",
    "INTERNATIONAL_CEV_CHAMPIONS_LEAGUE",
  ],
  "Germany": [
    "BUNDESLIGA_WOMEN_OUTRIGHT",
  ],
  "Italy": [
    "ITALY_SERIE_A1_WOMEN",
  ],
  "Poland ": [
    "POLAND_TAURON_LIGA_WOMEN"
  ],
}


ICE_HOCKEY = {
  "Australia": [
    "AHL"
  ],
  "Austria": [
    "AUSTRIA_OEL",
  ],
  "Czech Republic": [
    "CZECH_REPUBLIC_EXTRALIGA",
  ],
  "Denmark": [
    "DANISH_METAL_LIGAEN"
  ],
  "Europe": [
    "INTERNATIONAL_CHAMPIONS_LEAGUE",
    "EUROPEAN_CHAMPIONS_HOCKEY_LEAGUE",
    "EURO_HOCKEY_TOUR",
  ],
  "Finland": [
    "FINLAND_MESTIS",
  ],
  "Germany": [
    "GERMANY_DEL",
  ],
  "Kazakhstan": [
    "KAZAKHSTAN_CHAMPIONSHIP"
  ],
  "Norway": [
    "NORWAY_1ST_DIVISION",
  ],
  "Sweden ": [
    "SWEDEN_ALLSVENSKAN",
    "SWEDEN_SHL",
  ],
  "Switzerland": [
  ],
  "United States": [
    "US_NHL",
  ],
}


TENNIS = {
  "France": [
    "WTA_-_FRENCH_OPEN_WOMEN_SINGLES",
    "ATP_-_FRENCH_OPEN_MEN_SINGLES",
    "WTA_125K_-_WTA_125K_LIMOGES"
  ],
  "Tunisia": [
    "ITF_WOMEN_-_ITF_TUNISIA_52A"
  ]
}

DARTS = {
  "World": [
    "PDC_WORLD_DARTS_CHAMPIONSHIP",
    "MODUS_SUPER_SERIES"
  ]
}