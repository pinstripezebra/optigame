# import the requests library
import requests

# specify your custom User Agent
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

urls = ['https://www.amazon.com/CATAN-Board-Game-Discovery-Civilization/dp/B00U26V4VQ/ref=zg_bs_g_166225011_d_sccl_22/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Hasbro-Gaming-Kingdom-Adventures-Exclusive/dp/B00000DMF5/ref=zg_bs_g_166225011_d_sccl_2/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Amerous-Inches-Magnetic-Wooden-Chess/dp/B07N5ZS5QP/ref=zg_bs_g_166225011_d_sccl_33/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Days-Wonder-DO7201-Ticket-Ride/dp/0975277324/ref=zg_bs_g_166225011_d_sccl_2/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Stonemaier-Games-STM910-Wingspan-Multi-colored/dp/B07YQ641NQ/ref=zg_bs_g_166225011_d_sccl_28/130-7568529-7373803?psc=1',
        'https://www.amazon.com/USAopoly-Telestrations-After-Dark-Board/dp/B00V42YPKO/ref=zg_bs_g_166225011_d_sccl_81/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Bezier-Games-ONUWBEZ-Ultimate-Werewolf/dp/B00HS7GG5G/ref=zg_bs_g_166225011_d_sccl_89/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Monopoly-Magical-Adventure-Hogwarts-Players/dp/B0CS7VH7HM/ref=zg_bs_g_166225011_d_sccl_1/130-7568529-7373803?psc=1',
        'https://www.amazon.com/Classic-Operation-Skill-Amazon-Exclusive/dp/B00000DMFM/ref=zg_bs_g_166225011_d_sccl_43/130-7568529-7373803?psc=1']

# specify the target URL
target_url = (
    "https://www.amazon.com/Portable-Mechanical-Keyboard-MageGee-Backlit/dp/B098LG3N6R/"
)

# set an https proxy for http and https connection types
proxies = {
    "http": "http://47.90.205.231:33333",
    "https": "http://47.90.205.231:33333",
}

output = []
# send a get request to the target url with a custom User Agent and a proxy
for url in urls:
    target_url = url
    response = requests.get(target_url, headers=custom_headers, proxies=proxies)

    # check if the response status code is not 200 (ok)
    if response.status_code != 200:
        # print an error message with the status code
        print(f"An error occurred with status {response.status_code}")
    else:
        # get the page html content
        html_content = response.text
        # print the html content
        output.append(html_content)
