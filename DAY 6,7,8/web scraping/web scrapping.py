from bs4 import BeautifulSoup
import pandas as pd

# Example HTML (replace this with your real full HTML content)
html_content = """
<html>
<head><title>Example Table</title></head>
<body>
  <table border="1">
    <tr>
      <th rowspan="2">Salt Concentration (%)</th>
      <th colspan="5">Light Transmittance (%)</th>
    </tr>
    <tr>
      <th>400 nm</th><th>450 nm</th><th>500 nm</th><th>550 nm</th><th>600 nm</th>
    </tr>
    <tr>
      <td>0</td><td>90</td><td>88</td><td>85</td><td>80</td><td>75</td>
    </tr>
    <tr>
      <td>5</td><td>85</td><td>83</td><td>80</td><td>76</td><td>72</td>
    </tr>
  </table>
</body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the table
table = soup.find("table")
if not table:
    raise ValueError("No <table> tag found in the HTML content")

# Extract header rows
header_rows = table.find_all("tr")[0:2]
if len(header_rows) < 2:
    raise ValueError("Expected at least two rows in the table header")

# First header cell
headers = [header_rows[0].find('th').text.strip()]

# Second row contains actual column headers
second_header_cells = header_rows[1].find_all('th')
headers += [cell.text.strip() for cell in second_header_cells]

# Extract data
data = []
for row in table.find_all("tr")[2:]:
    cells = row.find_all('td')
    values = [cell.text.strip() for cell in cells]
    if values:
        data.append(values)

# Create DataFrame
df = pd.DataFrame(data, columns=headers)

# Output
print(df)
df.to_csv("salt_transmittance_data.csv", index=False)
