
import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()

pytrend.build_payload(kw_list=['Taylor Swift'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)