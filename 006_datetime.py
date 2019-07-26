import datetime

# help(datetime) -> apos import
# dir(datetime)

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVR nascem em {:%A, %B %d, %Y}"
print(message.format(gvr))
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100) # diferenca de 100 dias
print(mill + dt)


lancamento_data = datetime.date(2017, 3, 30)
lancamento_hora = datetime.time(22, 27, 0)
lancamento_datahora = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(lancamento_data)
print(lancamento_hora)
print(lancamento_datahora)


now = datetime.datetime.today()
print(now)
print(now.microsecond)

pouso_lua = "20/07/1969"
pouso_lua_date = datetime.datetime.strptime(pouso_lua, "%d/%m/%Y")
print(pouso_lua_date)