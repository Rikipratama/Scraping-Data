!pip install google_play_scraper

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google_play_scraper import Sort, reviews

Hasil_Scrapping = pd.DataFrame(result)
Hasil_Scrapping

Hasil_Scrapping.to_csv('Scrapping_IPOT.csv', index=False)
