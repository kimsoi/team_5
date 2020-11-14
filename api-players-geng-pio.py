# GEN_pio

import requests

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=GEN_Pio"

header = {
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4YTQyMjg3MC0wN2Y1LTAxMzktMDYxNC02NzFkNzYxMTE5NDUiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjA1MjgyNDg0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImhhZWluIn0.f0BNhdmO8bL-Cb9FIDJ1NZO3q5HL-kaR2vxYDIOqvfU",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
players_pio = r.json()
players_pio

# 'id' - accountId (account.e57c514acd19440bbc8a52233e482d93)
# 'Match ID' - Used to lookup the full match object on the /matches endpoint (많음)

# 두번째 GET의 url과 같음 - https://api.pubg.com/shards/steam/players/{account Id}
# 같은내용 다른 url with playerId - https://api.pubg.com/shards/steam/players/account.e57c514acd19440bbc8a52233e482d93