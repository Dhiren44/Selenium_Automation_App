import openpyxl
import requests
from bs4 import BeautifulSoup
from  selenium import webdriver

brwoser = webdriver.Chrome()

# brwoser.get("https://github.com/")

cookies = {
    '_octo': 'GH1.1.364052313.1707414369',
    'preferred_color_mode': 'dark',
    'tz': 'Europe%2FLondon',
    '_device_id': '9ab629f90d8e97f52d2a6be92e96aed3',
    'tz': 'Europe%2FLondon',
    'color_mode': '%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'saved_user_sessions': '60827831%3AVk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW',
    'user_session': 'Vk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW',
    '__Host-user_session_same_site': 'Vk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW',
    'logged_in': 'yes',
    'dotcom_user': 'Monika39-maker',
    'has_recent_activity': '1',
    '_gh_sess': 'oL%2Fo1r1G4Vk5I4zRD5EexEh%2F46%2BoA25NOknTLNxUzOYKF133fMIAKmZNRH%2FqEaH%2FcyxbugbfhIzx7UTBWMFLIffcSby6rFbRfNTuHPa3JPPMks19jS2VuxN5VJOUDvJ3R1pBM5SVSZ%2FCP3KEUVVvgf3EMNqxwpzv%2FRUOgiVxQrtRzyxvoB6Hdt3yKgYY7r0JJPN8TELc77P2w7rsDN3QbmVDD%2FIQu%2BJ1vxcZsNAFQZv6qR3AUBui4ybHhcYob8dPyAFQI0khIr41yKVXc%2FHlsh6l4fgMjVllHcicHVFLXif3IhFYmO9HXzGRtgUImCxpEZVR1%2FgDyFaQE10W41kFuicLNLcHArQWL91lUhlg0eO6PaLiUQqhv8FbrRBFTecvnP6vEQGvQu1Kkqmtep2ex4bBhiH8VAHxXZHf1ZoVi8TIlqTv6nJfBTTnnmIOulPLrcoWreyW6NQWtNWGXAXtRAeGhOxI%2Fdjadf4pFYpNvBrnYUR%2BKIyZJaCTQpv%2FQE1W6XqZ%2FMaFGjm8GbXNulwmpwrXzrkWv83zaykDYNPjl%2BisSRH%2BXXZkyXBsgn66dxBYha5drQZMnMWU2gqd7YPj5SDV0iBrEa3ujdh3uoHWQBgFKaCT5yvqLkDhkSxwLm%2FSTKA57a774CwDXDIoSOdhcwYUVH7xoUTZ%2F%2BlY80wE9m8c7jRcF724HPFryhjBhasJaDc0qX%2FrPynJ6J3e%2FNDpyi8qrpDWsEgbGN%2FZaaOb6IH%2BZY6C%2Fo008p98WQvHgMTKK2H1qKPzABq62%2B%2BRcjbJXlPwN5ASIlAo3EYpwdOJDydcQyMrnmG6a4katEcLgKrB36TX5hbEWk3X8IlEqP6IXSHQ4Tto0Q44LHxfTil0bhw2uNh8OhxTJylQSsNSJWGWOAYSHpEAjDtYutegXH%2BR3VR1Fr%2BsMAircEHDdsjHpj8x1L6y5a5EuArvlC4nhvT0aIisvGywOSaE8Eil--%2FaEk42ifPHUU9qqf--z33bW97%2FOlh%2BGV9wWgdNvA%3D%3D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_octo=GH1.1.364052313.1707414369; preferred_color_mode=dark; tz=Europe%2FLondon; _device_id=9ab629f90d8e97f52d2a6be92e96aed3; tz=Europe%2FLondon; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; saved_user_sessions=60827831%3AVk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW; user_session=Vk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW; __Host-user_session_same_site=Vk7I5Ztlt_zpr-OF2014FTwOSPL5cXYlNy_B7SPd_2qmNYbW; logged_in=yes; dotcom_user=Monika39-maker; has_recent_activity=1; _gh_sess=oL%2Fo1r1G4Vk5I4zRD5EexEh%2F46%2BoA25NOknTLNxUzOYKF133fMIAKmZNRH%2FqEaH%2FcyxbugbfhIzx7UTBWMFLIffcSby6rFbRfNTuHPa3JPPMks19jS2VuxN5VJOUDvJ3R1pBM5SVSZ%2FCP3KEUVVvgf3EMNqxwpzv%2FRUOgiVxQrtRzyxvoB6Hdt3yKgYY7r0JJPN8TELc77P2w7rsDN3QbmVDD%2FIQu%2BJ1vxcZsNAFQZv6qR3AUBui4ybHhcYob8dPyAFQI0khIr41yKVXc%2FHlsh6l4fgMjVllHcicHVFLXif3IhFYmO9HXzGRtgUImCxpEZVR1%2FgDyFaQE10W41kFuicLNLcHArQWL91lUhlg0eO6PaLiUQqhv8FbrRBFTecvnP6vEQGvQu1Kkqmtep2ex4bBhiH8VAHxXZHf1ZoVi8TIlqTv6nJfBTTnnmIOulPLrcoWreyW6NQWtNWGXAXtRAeGhOxI%2Fdjadf4pFYpNvBrnYUR%2BKIyZJaCTQpv%2FQE1W6XqZ%2FMaFGjm8GbXNulwmpwrXzrkWv83zaykDYNPjl%2BisSRH%2BXXZkyXBsgn66dxBYha5drQZMnMWU2gqd7YPj5SDV0iBrEa3ujdh3uoHWQBgFKaCT5yvqLkDhkSxwLm%2FSTKA57a774CwDXDIoSOdhcwYUVH7xoUTZ%2F%2BlY80wE9m8c7jRcF724HPFryhjBhasJaDc0qX%2FrPynJ6J3e%2FNDpyi8qrpDWsEgbGN%2FZaaOb6IH%2BZY6C%2Fo008p98WQvHgMTKK2H1qKPzABq62%2B%2BRcjbJXlPwN5ASIlAo3EYpwdOJDydcQyMrnmG6a4katEcLgKrB36TX5hbEWk3X8IlEqP6IXSHQ4Tto0Q44LHxfTil0bhw2uNh8OhxTJylQSsNSJWGWOAYSHpEAjDtYutegXH%2BR3VR1Fr%2BsMAircEHDdsjHpj8x1L6y5a5EuArvlC4nhvT0aIisvGywOSaE8Eil--%2FaEk42ifPHUU9qqf--z33bW97%2FOlh%2BGV9wWgdNvA%3D%3D',
    'pragma': 'no-cache',
    'referer': 'https://github.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'tab': 'repositories',
}

response = requests.get('https://github.com/Monika39-maker?tab=repositories', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text)
print(soup)




# Load the workbook
wb = openpyxl.load_workbook('data_file.xlsx')

# Select the active worksheet
working_sheet = wb.active

# Create a new workbook to store the updated data
new_wb = openpyxl.Workbook()
new_working_sheet = new_wb.active

# Copy headers from original worksheet to new worksheet
for col in range(1, working_sheet.max_column + 1):
    new_working_sheet.cell(row=1, column=col, value=working_sheet.cell(row=1, column=col).value)

# Iterate through column A and fill column B accordingly in the new worksheet
for row in working_sheet.iter_rows(min_row=2, max_col=1, max_row=working_sheet.max_row):
    name = row[0].value
    if name.startswith(('A', 'S', 'R')):
        new_working_sheet.append([name, 'Yes'])
    else:
        new_working_sheet.append([name, 'No'])


repo_search_input = brwoser.find_element_by_id("dashboard-repos-filter-left")
repo_search_input.send_keys("mairacagri/tv-show-dom-project")

repo_search_input.submit()
   

# Save the new workbook
# new_wb.save('updated_data_file.xlsx')

