import mechanicalsoup

# Create a Browser object
browser = mechanicalsoup.Browser()

# URL of the login page
url = "https://www.geeksforgeeks.org/"

# Open the login page
login_page = browser.get(url)

# Locate the login form (you may need to inspect the HTML to find the correct form fields)
login_form = login_page.soup.select_one("#your-login-form-id")

# Fill in the username and password
login_form.select("#username-field")[0]['value'] = 'zeus'
login_form.select("#password-field")[0]['value'] = 'ThunderDude'

# Submit the form
response = browser.submit(login_form, login_page.url)

# Check if login was successful (you may need to inspect the HTML of the logged-in page)
if 'Welcome, Zeus!' in response.text:
    print("Login successful!")
else:
    print("Login failed.")
