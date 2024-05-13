from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2),'OSL'))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3),'BLR'))

print(data_oslo,data_oslo.tzname())
print(data_sao_paulo)